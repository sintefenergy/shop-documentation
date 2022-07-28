---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: 'Python 3'
  language: python
  name: python3
---

+++ {"Collapsed": "false"}

# Individual water values in SHOP

The model setup for the three examples are available in the following formats:

- pyshop
    - [ind_wv.py](ind-wv-py)
- YAML
    - [model.yaml](ind-wv-model-yaml)
    - [constant_energy_value.yaml](constant-energy-values-yaml)
    - [constant_mixed_values.yaml](constant-mixed-values-yaml)
    - [water_value_tables.yaml](water-value-tables-yaml)
- ASCII
    - [model.ascii](ind-wv-model-ascii)
    - [constant_energy_values.ascii](constant-energy-values-ascii)
    - [constant_mixed_values.ascii](constant-mixed-values-ascii)
    - [water_value_tables.ascii](water-value-tables-ascii)
      

The examples show how to use constant water values (in €/Mm$^3$ and €/MWh) and water value tables to specify the end value of the end reservoir contents in SHOP. A simple case with three reservoirs and two plants is used to illustrate some of the relevant input and output for individual water values.

```{code-cell} ipython3
:Collapsed: 'false'

#Necessary imports used in all examples
import pandas as pd
import cufflinks as cf
import plotly.offline as py
import plotly.graph_objs as go
cf.go_offline()
py.offline.init_notebook_mode(connected=True)
from pyshop import ShopSession

#Functions used in this example for building a tunnel model, adding a gate to a tunnel and running the optimization
from ind_wv import build_model, run_model
```

+++ {"Collapsed": "false"}

## Constant water values in €/MWh
The first example will use water (or energy) values specified in €/MWh for all of the three reservoirs (see figure below). The values are set with the attribute called **energy_value_input** in the API.

```{code-cell} ipython3
:Collapsed: 'false'

#Create a standard ShopSession
shop=ShopSession()
#Build a simple model with three reservoirs and two plants.
build_model(shop)
#Display topology to the screen
display(shop.model.build_connection_tree())

#The three reservoir objects
rsv1 = shop.model.reservoir.Reservoir1
rsv2 = shop.model.reservoir.Reservoir2
rsv3 = shop.model.reservoir.Reservoir3

#In the first run we define the end value of the water in terms of €/MWh with the energy_value_input attribute
rsv1.energy_value_input.set(31.0)
rsv2.energy_value_input.set(30.0)
rsv3.energy_value_input.set(20.0)

#Optimize model by calling "run_model"
run_model(shop)
```

+++ {"Collapsed": "false"}

The energy_value_input must be converted from €/MWh to €/Mm$^3$ by SHOP before it can be added to the objective function. This requires reservoir specific conversion factors that depend on the best point operation of the downstream plant. Note that energy_value_input is a local value relative to the downstream plant, which means that the *global* water value for each reservoir must be calculated after the conversion factors have been found. The global water value is calculated by summing up the local water values (in €/Mm$^3$) from the bottom of the watercourse and up. The calculated reservoir output attributes **energy_conversion_factor** and **calc_global_water_value** that SHOP has used can be inspected after the first iteration of the otimization:

```{code-cell} ipython3
:Collapsed: 'false'

#Print out the energy conversion factors for all reservoirs used in the conversion from €/MWh -> €/Mm3
for rsv in shop.model.reservoir:
    print(f"{rsv.get_name()} has an energy conversion factor of {rsv.energy_conversion_factor.get():.3f} MWh/Mm3")
print("")

#Print out the calculated global water value for all reservoirs.
for rsv in shop.model.reservoir:
    print(f"{rsv.get_name()} has a calculated global water value of {rsv.calc_global_water_value.get():.2f} €/Mm3")
print("")

#Optimization results for the total reservoir end values
for rsv in shop.model.reservoir:
    end_val = -rsv.end_value.get()[-1]
    end_vol = rsv.storage.get()[-1]
    avrg_wv = end_val/(end_vol+10**(-10))

    print(f"{rsv.get_name()} has a total value of {end_val:.2f} € at {end_vol:.2f} Mm3 and an average water value of {avrg_wv:.2f} €/Mm3")
print("")
```

+++ {"Collapsed": "false"}

The energy_conversion_factor for Reservoir1 and Reservoir2 are identical since they are referred to the same downstream plant. Since there are no reservoirs below Reservoir3, the calc_global_water_value attribute is simply the product of the energy_value_input and energy_conversion_factor. Since the energy_value_input is relative to the downstream *plant* and not the first downstream reservoir, the global water value for both Reservoir1 and Reservoir2 is found by adding their respective local water values (energy_value_input$\cdot$energy_conversion_factor) to the global water value of Reservoir3.

The average water value, calculated by dividing the optimized end reservoir value by the end volume of each reservoir, gives the same result as the calculated global water value - as it should in a constant water value case!

The storage volume, global output water value (**water_value_global_result**), and local output energy value (**energy_value_local_result**) from the optimization results are shown in the plots below. The water_value_global_result is the dual value of the reservoir balance constraints, and are directly extracted from the optimization problem. These values are usually negative due to the way the constraints are modelled in SHOP. The energy_value_local_result attribute is found by first calculating the local output water value of the reservoir relative to the reservoir below the plant, and then converting it to €/MWh with the energy_conversion_factor. 

These output time series are strongly related to the water value input given to SHOP. A good consistency check is to look at the (negative of the) final values of the water_value_global_result and energy_value_local_results time series. These should be identical to the global water value and energy_value_input, respectively. This identity may not hold if penalties are present in the SHOP run since the dual values of the problem are influenced by penalty values.

```{code-cell} ipython3
:Collapsed: 'false'

pd.DataFrame([rsv.storage.get().rename(rsv.get_name()) for rsv in shop.model.reservoir]).transpose().iplot(title="Reservoir storage")
pd.DataFrame([-rsv.water_value_global_result.get().rename(rsv.get_name()) for rsv in shop.model.reservoir]).transpose().iplot(title="Reservoir global water value")
pd.DataFrame([-rsv.energy_value_local_result.get().rename(rsv.get_name()) for rsv in shop.model.reservoir]).transpose().iplot(title="Reservoir local energy value")
```

+++ {"Collapsed": "false"}

## Mix of constant water values in €/MWh and €/Mm$^3$
It is possible to define constant water values in €/MWh for some reservoirs and €/Mm$^3$ for the rest. Constant water values in €/Mm$^3$ are used directly by SHOP since they are assumed to be *global*. The example below is identical to the previous one except that the enrgy_value_input of Reservoir3 has been changed to a constant global water value with the **water_value_input** attribute. 

Caution is advised when having both definitions in the system, as it is possible to create cases where the global water value is not increasing upwards in the system. In our example, setting a high water_value_input for Reservoir2 could make it higher than the calculated global water value of Reservoir1. This can happen because the energy_value_input is a local value relative to the reservoir below the downstream plant, and so the global water value of Reservoir2 is skipped when converting the energy_value_input into a global water value for Reservoir1.

```{code-cell} ipython3
:Collapsed: 'false'

#Create the same basic model as before
shop=ShopSession()
build_model(shop)

#The three reservoir objects
rsv1 = shop.model.reservoir.Reservoir1
rsv2 = shop.model.reservoir.Reservoir2
rsv3 = shop.model.reservoir.Reservoir3

#We keep the energy_value_input for rsv1 and rsv2 unchanged, but define a global water value of 4000 €/Mm3 for rsv3 which is slightly higher than in the previous example.
rsv1.energy_value_input.set(31.0)
rsv2.energy_value_input.set(30.0)
rsv3.water_value_input.set([pd.Series([5000.0], index=[0], name=0)])

#Optimize model by calling "run_model"
run_model(shop)

#The energy_conversion_factors
for rsv in shop.model.reservoir:
    print(f"{rsv.get_name()} has an energy conversion factor of {rsv.energy_conversion_factor.get():.3f} MWh/Mm3")
print("")

#The calculated global water values
for rsv in shop.model.reservoir:
    print(f"{rsv.get_name()} has a calculated global water value of {rsv.calc_global_water_value.get():.2f} €/Mm3")
print("")

#Optimization results
for rsv in shop.model.reservoir:
    end_val = -rsv.end_value.get()[-1]
    end_vol = rsv.storage.get()[-1]
    avrg_wv = end_val/(end_vol+10**(-10))
    print(f"{rsv.get_name()} has a total value of {end_val:.2f} € at {end_vol:.2f} Mm3 and an average water value of {avrg_wv:.2f} €/Mm3")
print("")
```

+++ {"Collapsed": "false"}

Note that all of the energy conversion factors are identical to the first example since they are not influenced by the water value function of the reservoirs. The calc_global_water_value attribute is not calculated for Reservoir3 since it already has a global water value given in €/Mm$^3$. The calculated global water values of Reservoir1 and Reservoir2 are higher compared to the last example since the water value for Reservoir3 is higher, but their relative difference is the same as before.

The final value of the local energy value time series for Reservoir1 and Reservoir2 are still the same as their energy_value_input, while the water_value_input defined for Reservoir3 is found in the final value of the global output water value time series. 

```{code-cell} ipython3
:Collapsed: 'false'

pd.DataFrame([rsv.storage.get().rename(rsv.get_name()) for rsv in shop.model.reservoir]).transpose().iplot(title="Reservoir storage")
pd.DataFrame([-rsv.water_value_global_result.get().rename(rsv.get_name()) for rsv in shop.model.reservoir]).transpose().iplot(title="Reservoir global water value")
pd.DataFrame([-rsv.energy_value_local_result.get().rename(rsv.get_name()) for rsv in shop.model.reservoir]).transpose().iplot(title="Reservoir local energy value")
```

+++ {"Collapsed": "false"}

## Water value tables
An example of how to specify water values as piece-wise constant functions is shown below. The water value tables are based on the original water values calculated in the first example. The marginal water values in the water value table are spread around the original water value in a uniform way for each volume segment.

It is possible to have reservoirs with constant water values in €/Mm$^3$ and reservoirs with water value tables in the same system, but it is not advisable to mix water value tables and constant end values in €/MWh. This is because the conversion from local energy values to global water values requires a constant water value for all reservoirs of the system. If reservoirs with water value tables and constant local energy values are mixed, the start volume is used to find an approximation of the global water value of the reservoirs with water value tables.

```{code-cell} ipython3
:Collapsed: 'false'


#Create the same basic model as before
shop=ShopSession()
build_model(shop)

#The three reservoir objects
rsv1 = shop.model.reservoir.Reservoir1
rsv2 = shop.model.reservoir.Reservoir2
rsv3 = shop.model.reservoir.Reservoir3

reservoirs = [rsv1,rsv2,rsv3]

#Create a water value table with n segments that has the same total value at vmax as in the first example
wv_orig = [22177.52,21594.52,4104.50] 
n = 10

for wv,rsv in zip(wv_orig,reservoirs):
    vmax = rsv.max_vol.get()
    delta = 0.1*wv
    #The volume segments are vmax/n long, the marginal water value is decreasing from wv+delta to wv-delta from the first to the last segment
    wv_list = [wv+delta*(1-2*i/(n-1)) for i in range(n)]
    vol_list = [i*vmax/n for i in range(n)]
    rsv.water_value_input.set([pd.Series(wv_list, index=vol_list, name=0)])
    
#Plot the water value tables
for i, rsv in enumerate(reservoirs):
    wv_table = rsv.water_value_input.get()[0]
    vols = list(wv_table.index)
    wvs = list(wv_table.values)
        
    dv = vols[1]-vols[0]
    fig = go.Figure(layout={'bargap':0,'title':f"Reservoir{i+1}",'xaxis_title':"End volume",'yaxis_title':"Marginal water value"})
    fig.add_trace(go.Bar(name='Water value table', x0=0.5*dv,dx=dv, y=wvs))
    fig.add_trace(go.Scatter(name="Original water value",x=[0,vols[-1]+dv],y=[wv_orig[i],wv_orig[i]],mode='lines'))    
    fig.update_yaxes(range=[min(wvs)*0.9, max(wvs)*1.1])
    fig.show()
    print("")
    
#Print the water value tables
for rsv in reservoirs:
    wv_table = rsv.water_value_input.get()[0]
    print(f"{rsv.get_name()}:")
    print("Vol WV")
    for vol,wv in wv_table.items():
        print(vol,wv)    
    print("")
```

```{code-cell} ipython3
:Collapsed: 'false'

#Optimize model by calling "run_model"
run_model(shop)

for rsv in shop.model.reservoir:
    end_val = -rsv.end_value.get()[-1]
    end_vol = rsv.storage.get()[-1]
    avrg_wv = end_val/(end_vol+10**(-10))

    print(f"{rsv.get_name()} has a total value of {end_val:.2f} € at {end_vol:.2f} Mm3 and an average water value of {avrg_wv:.2f} €/Mm3")
print("")
```

+++ {"Collapsed": "false"}

The results from this SHOP run is not directly comparable to the others even though the water value tables are based on the global water values calulated from the first example. The average water values calculated above are no longer the same as the marginal water values seen in the local water value plot below because of the piece-wise water value definition. The final value of the water_value_global_result are related to the marginal values specified in the water value tables, and it is often equal to the marginal water value in the segment where the final optimized volume lies. However, if the final volume exactly fills a whole number of segments in the table, the marginal value will likely be somewhere between the marginal water value in the last full and first empty segments.

```{code-cell} ipython3
:Collapsed: 'false'

pd.DataFrame([rsv.storage.get().rename(rsv.get_name()) for rsv in shop.model.reservoir]).transpose().iplot(title="Reservoir storage")
pd.DataFrame([-rsv.water_value_global_result.get().rename(rsv.get_name()) for rsv in shop.model.reservoir]).transpose().iplot(title="Reservoir global water value")
pd.DataFrame([-rsv.energy_value_local_result.get().rename(rsv.get_name()) for rsv in shop.model.reservoir]).transpose().iplot(title="Reservoir local energy value")
```

+++ {"Collapsed": "false"}

(ind-wv-py)=
## ind_wv.py <a name="ind_wv.py"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('ind_wv.py', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(ind-wv-model-yaml)=
## model.yaml <a name="model.yaml"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('model.yaml', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(constant-energy-values-yaml)=
## constant_energy_values.yaml <a name="constant_energy_values.yaml"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('constant_energy_values.yaml', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(constant-mixed-values-yaml)=
## constant_mixed_values.yaml <a name="constant_mixed_values.yaml"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('constant_mixed_values.yaml', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(water-value-tables-yaml)=
## water_value_tables.yaml <a name="water_value_tables.yaml"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('water_value_tables.yaml', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(ind-wv-model-ascii)=
## model.ascii <a name="model.ascii"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('model.ascii', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(constant-energy-values-ascii)=
## constant_energy_values.ascii <a name="constant_energy_values.ascii"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('constant_energy_values.ascii', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(constant-mixed-values-ascii)=
## constant_mixed_values.ascii <a name="constant_mixed_values.ascii"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('constant_mixed_values.ascii', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(water-value-tables-ascii)=
## water_value_tables.ascii <a name="water_value_tables.ascii"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('water_value_tables.ascii', 'r') as f:
    print(f.read())
```
