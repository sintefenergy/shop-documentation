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

(multiple-price-bid-matrix)=
# Multiple price bid matrix example

The model setup is available in the following formats:

- pyshop
    - [multi_price_bid_matrix_model.py](multi-price-bid-matrix-model-py)

+++ {"Collapsed": "false"}

In this example we show how to import a spreadsheet containing multiple prices (up to 52 time series) into a dataframe. This price input will be used to create the same amount of scenarios which we in turn feed to SHOP. The output of this multiple price input run from SHOP will result into a joint bid matrix which consider all the stochastic price inputs to SHOP with all its price data intact, ready to make use of in a marked bidding situation with uncertainty regarding the price forecasts.

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
cf.go_offline()
from cufflinks import tools
import plotly.offline as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from pyshop import ShopSession
```

+++ {"Collapsed": "false"}

Additionally, we import basic SHOP functions and data from a predefined demo dataset, see <a href="https://shop.sintef.energy/documentation/examples/example-data-sets-and-functions/" target="_blank">this</a> section of the documentation:

```{code-cell} ipython3
:Collapsed: 'false'

from multi_price_bid_matrix_model import build_model, run_model
```

+++ {"Collapsed": "false"}

## Instancing SHOP and building the model

+++ {"Collapsed": "false"}

In order to have SHOP receive our inputs, run the model we create and give us results, we need to instance a running SHOP session. You may create multiple SHOP sessions simultaneously if needed.

```{code-cell} ipython3
:Collapsed: 'false'

#Create a standard ShopSession
shop = ShopSession()
```

+++ {"Collapsed": "false"}

We then build our model using the existing function imported from bp.py

```{code-cell} ipython3
:Collapsed: 'false'

#Build a simple model with one plant with two equal generators and a second plant with one large and three small generators 
#by calling function "build_model" in bp.py
build_model(shop)
```

+++ {"Collapsed": "false"}

The imported model can now be visualized:

```{code-cell} ipython3
:Collapsed: 'false'

#Display topology to the screen
display(shop.model.build_connection_tree())
```

+++ {"Collapsed": "false"}

## Data preperation

+++ {"Collapsed": "false"}

Since we we need to work a bit with time horizons given that we will consider part of a period with stochastic information, we retrive the start time from the imported data

```{code-cell} ipython3
:Collapsed: 'false'

# Retrieve the start time for adding stochastic time series later
timeres=shop.get_time_resolution()
shop.get_time_resolution()
```

+++ {"Collapsed": "false"}

### Importing prices from spreadsheet

+++ {"Collapsed": "false"}

After the model data has been imported and read, we move on to the prices we want to consider. 
We first define the number of prices we want to import

```{code-cell} ipython3
:Collapsed: 'false'

# Import number of prices
n_prices = 10
```

+++ {"Collapsed": "false"}

which will be equal to the scenarios we will create later on. 
We then define for how long of a period we want to consider the stochastic price input. This can not be a larger period than what you have data for in your price forecasts.

```{code-cell} ipython3
:Collapsed: 'false'

# Set the hours to import stochastic price
stochastic_prices_start = timeres['starttime']
# In this example, we choose 24 hours
stochastic_prices_end = stochastic_prices_start + pd.Timedelta(hours=23)
```

+++ {"Collapsed": "false"}

Next we import the stochastic prices accordingly into a dataframe

```{code-cell} ipython3
:Collapsed: 'false'

# Use pandas read_excel function to import n_prices to a dataframe, starting from the first column to the left in the spreadsheet
stochastic_prices_from_file = pd.read_excel ('52_hourly_prices_random.xls', header=None,usecols=list(range(0,n_prices)))

# Optionally, select which scenarios you want relative to the columns in your spreadsheet. They must then be equal to n_prices;
#stoch_price_from_file = pd.read_excel (r'20200123_scens_edit.xlsx', usecols=[1,2,5,7,9])

stochastic_prices_from_file
```

+++ {"Collapsed": "false"}

In order to later combine the stochastic prices with a deterministic price into the future, we make sure the dataframe has the correct timestamp indexing

```{code-cell} ipython3
:Collapsed: 'false'

# Add correct indexing to the dataframe
stochastic_prices_from_file.index=pd.date_range(stochastic_prices_start,stochastic_prices_end,freq='H')
```

+++ {"Collapsed": "false"}

Then we can plot and review the newly imported prices

```{code-cell} ipython3
:Collapsed: 'false'

# Plot all stochastic prices imported from Excel
stochastic_prices_from_file.iplot(title="Stochastic prices imported from spreadsheet", xaxis_title="Time", yaxis_title="EUR/MWh")
```

+++ {"Collapsed": "false"}

### Creating scenarios

+++ {"Collapsed": "false"}

Now it is time to create scenarios that we can populate with the imported prices. We make sure to create just as many scenarios as we have prices imported.

```{code-cell} ipython3
:Collapsed: 'false'

# Generate as many scenarios as prices
n_scenarios = n_prices
for i in range (1, n_scenarios+1):
    scenario_name='S'+str(i)
    # The first scenario always exists in SHOP and should not be added again
    if i>1:
        scenario = shop.model.scenario.add_object(scenario_name)
    else:
        scenario=shop.model.scenario[scenario_name]
    scenario.scenario_id.set(i)
    
    # Set each scenario equally probable
    scenario.probability.set(1.0/n_scenarios)
    
    # Branch immediately, i.e. at 'starttime'
    scenario.common_scenario.set(pd.Series([i], index=[timeres['starttime']]))
    
    # Optionally set branching to start after given number of hours (all scenarios are set equal to scenario 2 before this) 
    #scen.common_scenario.set(pd.Series([2, i], index=[timeres['starttime'], branching_start_time]))
```

+++ {"Collapsed": "false"}

### Creating the new price array from stochastic and deterministic prices

+++ {"Collapsed": "false"}

Since we have chosen to only consider the first 24 hours as stochastic when it comes to the price, but have longer total time horizon, we need to combine the stochastic and deterministic prices into a joint price dataframe. We have already defined the start and end time for the stochastic price, but need to make sure that we also define when the deterministic price should be valid and thus overlap each other.

```{code-cell} ipython3
:Collapsed: 'false'

# Use first (and only) market as index for setting stochastic data and getting results
name_list = shop.model.market.get_object_names()

# The deterministic model only has one market, so we give stochastic price to that (da is just a name we use to indicate that we regard it to be a day ahead energy market)
day_ahead_market = shop.model.market[name_list[0]]

# Get the deterministic price from ASCII import for correct indexing 
deterministic_price = day_ahead_market.sale_price.get()

# Create a new array for deterministic price with n_prices columns in order to combine it with the stochastic price
deterministic_price_multi_dimension_array = pd.DataFrame(index=deterministic_price.index, columns=list(range(0,n_prices)))

# Define when to use deterministic price
deterministic_price_start = timeres['starttime']+pd.Timedelta(hours=24)
deterministic_price_end = timeres['endtime']-pd.Timedelta(hours=1)
```

+++ {"Collapsed": "false"}

We print out the start and end times to make sure they are correct.

```{code-cell} ipython3
:Collapsed: 'false'

# Print out start and end set point for prices
print("Stochastic price(s) start time",stochastic_prices_start)
print("Stochastic price(s) end time",stochastic_prices_end)
print("Deterministic prices start time",deterministic_price_start)
print("Deterministic prices end time",deterministic_price_end)
```

+++ {"Collapsed": "false"}

Lastly, we need to combine the stochastic and deterministic price inputs. We do this by creating a new dataframe with the right dimensions and indexes, and then populate it according to the start and end times defined above.

```{code-cell} ipython3
:Collapsed: 'false'

# Creating a new price dataframe which will combine both stochastic and deterministic price
combined_price = pd.DataFrame(index=deterministic_price.index, columns=list(range(0,n_prices)))

# Loop over the new price array and assign stochastic and deterministic prices

for j in range(0,n_prices):
    deterministic_price_multi_dimension_array[j]=deterministic_price
for i in pd.date_range(stochastic_prices_start,stochastic_prices_end,freq='H'):
       combined_price.loc[i] = stochastic_prices_from_file.loc[i]
for i in pd.date_range(deterministic_price_start,(deterministic_price_end),freq='H'):
        combined_price.loc[i] = deterministic_price_multi_dimension_array.loc[i]
```

+++ {"Collapsed": "false"}

Then we can plot out the resulting combined price.

```{code-cell} ipython3
:Collapsed: 'false'

# Plot the combined price
combined_price.iplot(title="Combined price input", xaxis_title="Time", yaxis_title="EUR/MWh")
```

+++ {"Collapsed": "false"}

This price is then set as the day ahead market price to consider for all scenarios. We also define a slightly higher buy-back price

```{code-cell} ipython3
:Collapsed: 'false'

day_ahead_market.sale_price.set(combined_price)

# Make sure that the buy price is slightly higher, so no arbitrage occurs

day_ahead_market.buy_price.set(day_ahead_market.sale_price.get()+0.1)
```

+++ {"Collapsed": "false"}

### Create bid groups and configure limits

+++ {"Collapsed": "false"}

Now we need to create a bid group, which is the connection between a set of hydropower plants and their bid matrix. 

```{code-cell} ipython3
:Collapsed: 'false'

# Create a bid group
bg=shop.model.bid_group.add_object('bg')

# Add all plants in the system to the bid group
for plant in shop.model.plant:
    bg.connect_to(plant)

# Defining which periods the bid curve should consider
day_ahead_market.bid_flag.set(pd.Series([1,0],index=[stochastic_prices_start,stochastic_prices_end]))
```

+++ {"Collapsed": "false"}

## Running multi price scenarios in SHOP

+++ {"Collapsed": "false"}

It is time to optimize. We call the predefined function run_model, which calls for five full and three incremental iterations. Since we have defined scenarios in the SHOP instance earlier, all scenarios will be computed and optimized with a single call.

```{code-cell} ipython3
:Collapsed: 'false'

#Optimize model by calling "run_model" bp.py
run_model(shop)
```

+++ {"Collapsed": "false"}

## Creating and plotting the bid matrix

+++ {"Collapsed": "false"}

Once SHOP has finished optimizing all scenarios, we can retrive and start processing the bid matrix the way we want it.

```{code-cell} ipython3
:Collapsed: 'false'

# Get bid matrix as an array
bid_result=bg.bid_curves.get()

# Convert bid matrix to a dataframe structure of choice
bid_matrix=pd.DataFrame(index=bid_result[0].index)
for t in range (0, 23):
    bid_matrix[t]=bid_result[t].values

# Transpose the bid matrix if necessary depending on the viewing needs 
bid_matrix_transposed=bid_matrix.transpose()
```

+++ {"Collapsed": "false"}

When we are satisfied with a data structure that fulfill our needs, we can either print it or plot it to review it 

```{code-cell} ipython3
:Collapsed: 'false'

# Plotting bid matrices with different properties
bid_matrix.iplot(kind='heatmap', colorscale='spectral',title="Bid matrix heatmapped (and inverted compared to normal bid matrix)",xaxis_title ="Market price", yaxis_title="Hours")
```

```{code-cell} ipython3
:Collapsed: 'false'

# Plotting bid matrices with different properties
bid_matrix_transposed.iplot(kind='bar', title="Bid matrix per hour", xaxis_title ="Hour [h]", yaxis_title="Market price")
```

+++ {"Collapsed": "false"}

## Plotting other results

+++ {"Collapsed": "false"}

If we want to see how each scenario suggest to produce, we can of course have a look at that as well

```{code-cell} ipython3
:Collapsed: 'false'

# Get the optimal production value(s)
optimal_production=day_ahead_market.sale.get()
```

```{code-cell} ipython3
:Collapsed: 'false'


# Plot optimal production in different plot types
optimal_production.iplot(kind='bar',title="Bid volumes per stochastic price #", xaxis_title="Time", yaxis_title="Sale/Production [MW]")
```

```{code-cell} ipython3
:Collapsed: 'false'

# Plot optimal production in different plot types
optimal_production.iplot(kind='bar',barmode='stack', bargap=.1,title="Bid volumes per stochastic price #, stacked", xaxis_title="Time", yaxis_title="Sale/Production [MW]")
```

+++ {"Collapsed": "false"}

# Files

+++ {"Collapsed": "false"}

(multi-price-bid-matrix-model-py)=
## multi_price_bid_matrix_model.py

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('multi_price_bid_matrix_model.py', 'r') as f:
    print(f.read())
```
