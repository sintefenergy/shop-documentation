---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: 'Python 3.7.9 64-bit (''SHOP'': conda)'
  name: python3
---

(discrete-droop)=
# Discretization of droop results

The model setup for the iterative discretization of droop results presented below is available in the following formats:

- pyshop
    - [discrete_droop.py](#discrete_droop.py)
- YAML
    - [model.yaml](#model.yaml)
    - [reserve_obligation.yaml](#reserve_obligation.yaml)
    - [discrete_droop_input.yaml](#discrete_droop_input.yaml)
- ASCII
    - [model.ascii](#model.ascii)
    - [reserve_obligation.ascii](#reserve_obligation.ascii)    
    - [discrete_droop_input.ascii](#discrete_droop_input.ascii)

+++

## Iterative droop discretization
A simple system with 6 generators located on two separate plants will be used to illustrate the basic features of the droop discretization heuristic in SHOP. The droop variable is a continuous variable in SHOP, but there is usually a set of discrete droop values that can be implemented in the real world. The discrete droop functionality in SHOP enables the user to specify a set of discrete legal values that the droop variable in SHOP will be rounded and fixed to in the next iteration(s). This is a heuristic approach to the problem, since the droop variables are not formulated as discrete variables in the optimization problem. This would require the use of extra binary variables that will impact the tractability and calculation time of SHOP. Note that the droop discretization functionality requires the **SHOP_DISCRETE_DROOP** license.

First, we create and run the basic model without any droop discretization:

```{code-cell} ipython3
#Necessary imports used in all examples
import pandas as pd
import cufflinks as cf
import plotly.offline as py
import plotly.graph_objs as go
cf.go_offline()
py.offline.init_notebook_mode(connected=True)
from pyshop import ShopSession

#Functions used in this example for building and solving a simple model with cuts
from discrete_droop import build_model, run_model, get_gen_droop
```

```{code-cell} ipython3
#Create a standard ShopSession
shop=ShopSession()
#Build a simple model with two reservoirs, two plants, and 6 generators.
build_model(shop)
#Display topology to the screen
display(shop.model.build_connection_tree())

#Add FCR_N obligation in both directions where all generators can participate
fcr_group = shop.model.reserve_group.add_object("fcr_group")
fcr_group.fcr_n_up_obligation.set(20)
fcr_group.fcr_n_down_obligation.set(20)    

for gen in shop.model.generator:
    fcr_group.connect_to(gen) 

#Run an optimization without any droop discretization
run_model(shop)
```

The resulting droop values can now be plotted. Note that the plotting below removes the time information form the droop values and plots them for the same x value:

```{code-cell} ipython3
#Display the resulting droop values from the optimization

#Retrieve the generator droop results
gen_droop = get_gen_droop(shop)

gen_names = [gen.get_name() for gen in shop.model.generator]

fig = go.Figure(layout={'title':"Droop values",'xaxis_title':"Generator",'yaxis_title':"Droop [%]"})

#Add dashed lines to show the integer values between 1 and 12
for i in range(1,13):
    fig.add_trace(go.Scatter(showlegend=False,x=gen_names,y=[i]*len(gen_names),mode='lines', line={'color': "black", 'width': 0.5,'dash':"dash"})) 
           
for gen_name, droop in gen_droop.items():
    fig.add_trace(go.Scatter(showlegend=False,x=[gen_name]*len(droop),y=droop,mode='markers')) 

fig.show()
```

The optimized droop values shown above are not necessarily legal or practical to implement in the real world. It is possible to round down and fix the droop values to the closest legal discrete value in SHOP. Each unit can have its own list of legal droop values specified by the double_array attribute **discrete_droop_values**. If no list is defined, the integers are assumed to be the legal values for the unit. The command `set droop_discretization_limit <value>`, or the equivalent double attribute **droop_discretization_limit** on the global_setting object, is used to tell SHOP to round *down* all droop values *below* the specified limit to their closest legal value, and fix the droop varaible to this value in the next iteration. Since the values are always rounded down, the generators are forced to deliver more (or equal) frequency response compared to the optimal solution. This can lead to a more costly solution, but will not cause infeasibility issues. If a unit has no legal discrete values below the given droop_discretization_limit, the droop will not be fixed. The droop variables will also never be fixed to a value outside its upper and lower bounds. These bounds have default values of 1 and 12, respectively, and can be changed by specifying the **droop_min** and **droop_max** TXY unit attributes. If the rounded droop value is outside the defined limits, it is fixed to the boundary instead.

Now we create an identical SHOP model but add specified legal discrete droop values for the generators in Plant2. By gradually increasing the droop_discretization_limit between the incremental iterations, the droop values are iteratively fixed to legal values.

```{code-cell} ipython3
#Create a standard ShopSession
shop=ShopSession()
#Build a simple model with two reservoirs, two plants, and 6 generators.
build_model(shop)

#Add FCR_N obligation in both directions where all generators can participate
fcr_group = shop.model.reserve_group.add_object("fcr_group")
fcr_group.fcr_n_up_obligation.set(20)
fcr_group.fcr_n_down_obligation.set(20)    

for gen in shop.model.generator:
    fcr_group.connect_to(gen) 

#Set specific legal discrete droop values for generators in Plant2 (1,1.5,2,2.5,...,12)
plant2 = shop.model.plant.Plant2
for gen in plant2.generators:
    gen.discrete_droop_values.set([1+0.5*i for i in range(23)])
    
#Run the full iterations and the first incremental iteration without any fixing and discretization
shop.start_sim([], ['3'])
shop.set_code(['incremental'], [])
shop.start_sim([], ['1'])

#Save the droop results before any fixing and discretization
gen_droop = get_gen_droop(shop)
droop_results = [gen_droop]

#Gradually fix droop values for each following iteration
for d in [3,6,9,12]:
    shop.set_droop_discretization_limit([],[d])
    shop.start_sim([], ['1'])
    
    #Save the droop results for each generator after each iteration
    gen_droop = get_gen_droop(shop)        
    droop_results.append(gen_droop)
```

Now we can plot the evolution of the droop results for each generator for the four final incremental iterations:

```{code-cell} ipython3
for desc,gen_droop in zip(["before fixing","fixed below 3","fixed below 6","fixed below 9","fixed below 12"], droop_results):

    fig = go.Figure(layout={'title':f"Droop values {desc}",'xaxis_title':"Generator",'yaxis_title':"Droop [%]"})

    for i in range(1,13):
        fig.add_trace(go.Scatter(showlegend=False,x=gen_names,y=[i]*len(gen_names),mode='lines', line={'color': "black", 'width': 0.5,'dash':"dash"})) 

    for i in range(11):
        fig.add_trace(go.Scatter(showlegend=False,x=["Plant2_G1","Plant2_G4"],y=[1.5+i,1.5+i],mode='lines', line={'color': "red", 'width': 0.5,'dash':"dash"})) 

        
    for gen_name,droop_values in gen_droop.items():
        fig.add_trace(go.Scatter(showlegend=False,x=[gen_name]*len(droop_values),y=droop_values,mode='markers')) 

    fig.show()
```

Since the default upper bound for the droop is 12 in SHOP, all droop values are rounded and fixed when the discretization limit is set to 12 before the final iteration. The droop values of the generators in Plant1 are all fixed to integer values in the end, while the generators in Plant2 are allowed to take values defined earlier with the discrete_droop_values attribute.

+++

## discrete_droop.py <a name="discrete_droop.py"></a>

```{code-cell} ipython3
%pycat discrete_droop.py
```

## model.yaml <a name="model.yaml"></a>

```{code-cell} ipython3
%pycat model.yaml
```

## reserve_obligation.yaml <a name="reserve_obligation.yaml"></a>

```{code-cell} ipython3
%pycat reserve_obligation.yaml
```

## discrete_droop_input.yaml <a name="discrete_droop_input.yaml"></a>

```{code-cell} ipython3
%pycat discrete_droop_input.yaml
```

## model.ascii <a name="model.ascii"></a>

```{code-cell} ipython3
%pycat model.ascii
```

## reserve_obligation.ascii <a name="reserve_obligation.ascii"></a>

```{code-cell} ipython3
%pycat reserve_obligation.ascii
```

## discrete_droop_input.ascii <a name="discrete_droop_input.ascii"></a>

```{code-cell} ipython3
%pycat discrete_droop_input.ascii
```
