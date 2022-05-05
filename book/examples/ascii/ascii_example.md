---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"Collapsed": "false"}

# ASCII example

+++ {"Collapsed": "false"}

The model setup for this example is available in the following formats:

- ASCII
    - [ascii_model.ascii](#ascii_model.ascii)
    - [ascii_data.ascii](#ascii_data.ascii)
    - [ascii_time.ascii](#ascii_time.ascii)
    - [ascii_commands.ascii](#ascii_commands.ascii)
      

This example models the exact same model found in the basic example and runs the same optimization. However, in this script the model is defined in ASCII files and optimized by running a command file. PyShop provides methods for reading models from ASCII files and executing commands in command files. ASCII files have historically been the main method for defining Shop models, and command files have been used for executing commands on such ASCII models. In PyShop it is possible to combine the older approach with the newer python-based one.

+++ {"Collapsed": "false"}

## Imports and settings

+++ {"Collapsed": "false"}

The first thing we do is to import the needed packages. You can import whichever packages you like, however we use the following ones for this example:

* Pandas for structuring our data into dataframes
* Cufflinks and Plotly for dynamic graph plotting
* Pyshop in order to create a SHOP session

```{code-cell} ipython3
:Collapsed: 'false'

import pandas as pd
import cufflinks as cf
from cufflinks import tools
import plotly.offline as py
import plotly.graph_objs as go
from pyshop import ShopSession
```

+++ {"Collapsed": "false"}

Additionally, we set Cufflinks and Plotly to an offline state, only usable in this notebook/environment:

```{code-cell} ipython3
:Collapsed: 'false'

cf.go_offline()
py.offline.init_notebook_mode(connected=True)
```

+++ {"Collapsed": "false"}

## Instancing SHOP

+++ {"Collapsed": "false"}

In order to have SHOP receive our inputs, run the model we create and give us results, we need to declare a running SHOP session, in this example to the instance 'shop'.

You may create multiple SHOP sessions simultaneously if needed.

```{code-cell} ipython3
:Collapsed: 'false'

# Creating a new SHOP session to the instance 'shop'
shop = ShopSession()
```

+++ {"Collapsed": "false"}

We might also want to check the current versions of SHOP and its solvers.

```{code-cell} ipython3
:Collapsed: 'false'

# Writing out the current version of SHOP 
shop.shop_api.GetVersionString()
```

+++ {"Collapsed": "false"}

## Reading ASCII files as input data

+++ {"Collapsed": "false"}

We make use of the read_ascii_file function to save data from file into the shop instance we created in the previous cell. 
Note that it is important to import files in the correct order, meaning you cannot import something that relies on data that you have not imported from before. 

The example of importing files below show best practice by
- First importing the data structure and indexing such as the time horizon and time period(s) of the model, and thus its data
- Furthermore importing the model topology and parameters
- Lastly populating the model with data and time series

Also note that the file(s) must be present in the same working directory/folder as the script/notebook that you are executing, if not using (absolute) paths.

+++ {"Collapsed": "false"}

### Reading and verifying time units

+++ {"Collapsed": "false"}

We start by importing the time period and time resolution from the file test_time.ascii.

```{code-cell} ipython3
:Collapsed: 'false'

# Importing the time period and time resolution
shop.read_ascii_file('ascii_time.ascii')
```

+++ {"Collapsed": "false"}

We then verify which time data has been read into the shop instance.

```{code-cell} ipython3
:Collapsed: 'false'

# Listing time resolution data from the model instance
shop.get_time_resolution()
```

+++ {"Collapsed": "false"}

### Reading and verifying the topology and parameters

+++ {"Collapsed": "false"}

After the time structure has been correctly imported, we move on to importing the watercourse topology and its static parameters from the file test_model.ascii

```{code-cell} ipython3
:Collapsed: 'false'

# Importing the model's topology and assosiated parameters
shop.read_ascii_file('ascii_model.ascii')
```

+++ {"Collapsed": "false"}

We can then verify what has been read into the *shop* instance by quering data using different get functions.

+++ {"Collapsed": "false"}

### List reservoirs and reservoir parameters in current model

+++ {"Collapsed": "false"}

In order to retrieve the current reservoir names in the model on the current *shop* instance, we can use

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the reservoirs in the current model
shop.model.reservoir.get_object_names()
```

+++ {"Collapsed": "false"}

Once we have verified the names, we can make use of them for more detailed queries, such as volume/head relations (stage-storage curves)

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the volume/head relation in Reservoir1
shop.model.reservoir.Reservoir1.vol_head.get()
```

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the volume/head relation in Reservoir2
shop.model.reservoir.Reservoir2.vol_head.get()
```

+++ {"Collapsed": "false"}

The flow descriptions

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the overflow description in Reservoir1
shop.model.reservoir.Reservoir1.flow_descr.get()
```

+++ {"Collapsed": "false"}

Attributes like HRL and LRL, can just as easily be retrieved 

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the highest regulated level (HRL) in Reservoir1
shop.model.reservoir.Reservoir1.hrl.get()
```

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the lowest regulated level (LRL) in Reservoir1
shop.model.reservoir.Reservoir1.lrl.get()
```

+++ {"Collapsed": "false"}

### List plants and plant parameters in current model

+++ {"Collapsed": "false"}

The same process is applicable for all other object types, such as plants. We can retrieve the current plant names

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the plants in the current model
shop.model.plant.get_object_names()
```

+++ {"Collapsed": "false"}

And then verify what has been read into the model by querying attributes from the objects using the get functions

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the number of generators on Plant1
shop.model.plant.Plant1.num_gen.get()
```

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the penstock loss on Plant1
shop.model.plant.Plant1.penstock_loss.get()
```

+++ {"Collapsed": "false"}

### List generators and generator parameters in current model

+++ {"Collapsed": "false"}

And again, if we want to verify the generators and its parameters, we can do use the same approach as above

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the generators in the current model
shop.model.generator.get_object_names()
```

```{code-cell} ipython3
:Collapsed: 'false'

# Listing the number of generators on Plant1
shop.model.generator.Plant1_G1.turb_eff_curves.get()
```

+++ {"Collapsed": "false"}

Since the ascii file also included the connections between reservoirs, plants and generators, we can then verify if the topology is correctly set up, by graphing out the topology tree.

```{code-cell} ipython3
:Collapsed: 'false'

# Print out the topology
dot = shop.model.build_connection_tree()
display(dot)
```

+++ {"Collapsed": "false"}

### Reading and verifying the input data

+++ {"Collapsed": "false"}

After the topology and model structure has been set up correctly, we can populate additional data needed for SHOP to run, such as initial reservoir levels, endpoint descriptions (water values), market(s), inflow and other time dependent data, i.e. time series

```{code-cell} ipython3
:Collapsed: 'false'

# Importing other input data to the model
shop.read_ascii_file('ascii_data.ascii')
```

+++ {"Collapsed": "false"}

### List initial input data and time series

+++ {"Collapsed": "false"}

We can retrieve the newly imported static data out for inspection like before;

```{code-cell} ipython3
:Collapsed: 'false'

# Retrieve the start volume of Reservoir1
shop.model.reservoir.Reservoir1.start_vol.get()
```

```{code-cell} ipython3
:Collapsed: 'false'

# Retrieve the endpoint description (water value) of Reservoir1

shop.model.reservoir.Reservoir1.energy_value_input.get()
```

+++ {"Collapsed": "false"}

But now we are also introduced to time dependent data in time series

```{code-cell} ipython3
:Collapsed: 'false'

# Retrieve the inflow to Reservoir1
shop.model.reservoir.Reservoir1.inflow.get()
```

+++ {"Collapsed": "false"}

Which in many cases also can be useful to plot

```{code-cell} ipython3
:Collapsed: 'false'

# Plotting the inflow to Reservoir 1
shop.model.reservoir.Reservoir1.inflow.get().iplot(title="Inflow to Reservoir 1",xaxis_title="Time", yaxis_title="m3/s")
```

+++ {"Collapsed": "true"}

For a complete overview of all objects and attributes you can query data from, see the [SHOP reference manual](https://sintefshop.no/documentation/reference/)'s [attribute section](https://sintefshop.no/documentation/reference/attributes/), or use a Language Server Protocol (LSP) in your IDE (which is included in the [Lab](https://sintefshop.no/lab/)) as illustrated below for an even easier and dynamic workflow.

+++ {"Collapsed": "false"}

![LSP.PNG](attachment:LSP.PNG)

+++ {"Collapsed": "false"}

## Running SHOP optimizations and commands from file

+++ {"Collapsed": "false"}

Once the model is fully imported and verified, we can then call for the optimizer. Since we now control all commands from a separate command file, this file needs to be inspected (and optinally altered and saved) before running the file in pyshop by using the *run_command_file* command.


```{code-cell} ipython3
:Collapsed: 'false'

# Running the command file and executing SHOP based on the imported input
shop.run_command_file('.', 'ascii_commands.txt')
```

+++ {"Collapsed": "false"}

In this example, we chose CPLEX as the solver, enabled universal MIP and ran three full and three incremental iterations before we wrote the results to files.

For a full overview of the possible commands you can use when running SHOP, see the [SHOP reference manual](https://sintefshop.no/documentation/reference/)'s [command section](https://sintefshop.no/documentation/reference/commands/).

+++ {"Collapsed": "false"}

## Plotting the results

+++ {"Collapsed": "false"}

Finally, we can review the result from SHOP by plotting the graphs we want. 

```{code-cell} ipython3
:Collapsed: 'false'

# Defining a plot dataframe to combine multiple time series in the same dataframe for plotting purposes (NB: they need to have the same time index)
plot = pd.DataFrame()

# Retrieving the reservoir trajectories adding them to the plot dataframe
plot["Reservoir1"]=shop.model.reservoir.Reservoir1.storage.get()
plot["Reservoir2"]=shop.model.reservoir.Reservoir2.storage.get()

# Plotting the figure
plot.iplot(title="Reservoir trajectories",xaxis_title="Time",yaxis_title="Mm3")
```

+++ {"Collapsed": "false"}

# Files

+++ {"Collapsed": "false"}

## ascii_model.ascii

```{code-cell} ipython3
:Collapsed: 'false'

%pycat ascii_model.ascii
```

+++ {"Collapsed": "false"}

## ascii_data.ascii

```{code-cell} ipython3
:Collapsed: 'false'

%pycat ascii_data.ascii
```

+++ {"Collapsed": "false"}

## ascii_time.ascii

```{code-cell} ipython3
:Collapsed: 'false'

%pycat ascii_time.ascii
```

+++ {"Collapsed": "false"}

## ascii_commands.txt

```{code-cell} ipython3
:Collapsed: 'false'

%pycat ascii_commands.txt
```
