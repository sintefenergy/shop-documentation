---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"Collapsed": "false"}

<style>
th {
  font-size: 14px
}
td {
  font-size: 14px
}
</style>

+++ {"Collapsed": "false"}

# Basic pump example

This example is available in the following formats:

- pyshop
    - [basic_pump.py](#basic_pump.py)
- YAML
    - [basic_pump.yaml](#basic_pump.yaml)
- ASCII
    - [basic_pump.ascii](#basic_pump.ascii)

+++

## Introduction

+++

This example imports a basic model and adds a simple binary pump. By varying the sale price in the market, we see that the watercourse pumps water to the upper reservoir when the price is lower than its water value.

+++

## Imports

```{code-cell} ipython3
:Collapsed: 'false'

#Necessary imports used in all examples
import pandas as pd
import cufflinks as cf
from cufflinks import tools
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

from pyshop import ShopSession

#Functions used in this example for building a basic SHOP model and running it
from basic_pump import build_model, run_model
```

## Create a SHOP session and import basic model from file function

```{code-cell} ipython3
:Collapsed: 'false'

#Create a standard ShopSession
shop=ShopSession()
#Build a basic SHOP model
build_model(shop)
#Display topology to the screen
display(shop.model.build_connection_tree())
```

## Add pumping capabilites

+++

Pumps can be added as pump objects, and need to be connected to a plant. We then apply attributes to the pump object. Whereas you in the old ASCII format don't need to specify a maximum and minimum production for a binary pump, you need to explicitly add those attributes in addition to the nominal production in pyshop.

```{code-cell} ipython3
p1p1=shop.model.pump.add_object("P1P1")
p1p1.connect_to(shop.model.plant.Plant1)
p1p1.penstock.set(1)
p1p1.p_nom.set(40)
p1p1.p_min.set(40)
p1p1.p_max.set(40)
p1p1.startcost.set(500)
p1p1.gen_eff_curve.set(pd.Series([100,100], index=[0,50]))
p1p1.turb_eff_curves.set([pd.Series([87],index=[80],name=40),pd.Series([86],index=[70],name=50),pd.Series([85],index=[60],name=60)])
```

## Run SHOP

```{code-cell} ipython3
run_model(shop)
```

## Plots and results

+++

We observe that the pump is used in the first six hours of the period, where the market price is lower than the water value in the upper reservoir. 

```{code-cell} ipython3
# Plot market price and water value of reservoirs
spot_price=shop.model.market.Day_Ahead.sale_price.get()
end_water_value=shop.model.reservoir.Reservoir1.energy_value_input.get()
water_value=pd.Series(dtype=object,index=spot_price.index)
water_value=water_value.fillna(end_water_value)


fig = go.Figure()
colorscale = px.colors.sequential.RdBu_r
color = 1
fig.add_trace(go.Scatter(x=spot_price.index, marker_color = colorscale[color], y=spot_price.values, name="Market price"))

for rsv in shop.model.reservoir:
    color+=1
    end_water_value=rsv.energy_value_input.get()
    water_value=pd.Series(dtype=object,index=spot_price.index)
    water_value=water_value.fillna(end_water_value)
    curve_name="Water value of "+rsv.get_name()
    fig.add_trace(go.Scatter(x=water_value.index, y=water_value.values, marker_color = colorscale[color], name=curve_name, line=dict(dash="dot")))
    
fig.update_layout(title="<b>Market price and water value of reservoirs</b>", xaxis_title="<b>Time</b> (Hour)", yaxis_title="<b>Price</b> (€/MWh)")

fig.show()
```

```{code-cell} ipython3
# Plotting pump consumption and generator production
p1p1_consumption=shop.model.pump.P1P1.consumption.get()
p1g1_production=shop.model.generator.P1G1.production.get()
fig = go.Figure()
colorscale = px.colors.sequential.Magenta
fig.add_trace(go.Bar(x=p1p1_consumption.index, y=p1p1_consumption.values, name="Pump consumption", marker_color=colorscale[1]))
fig.add_trace(go.Bar(x=p1g1_production.index, y=p1g1_production.values, name="Generator production", marker_color=colorscale[6]))
fig.update_layout(title="<b>Pump consumption and generator production</b>", xaxis_title="<b>Time</b> (Hour)", yaxis_title="<b>Production/Consumption</b> (MW)")
```

```{code-cell} ipython3
# Plotting reservoir trajectories
water_storage_rsv1=shop.model.reservoir.Reservoir1.storage.get()
water_storage_rsv2=shop.model.reservoir.Reservoir2.storage.get()
fig = go.Figure()
colorscale = px.colors.sequential.RdBu_r
fig.add_trace(go.Scatter(x=water_storage_rsv1.index, y=water_storage_rsv1.values, name="Reservoir1 storage", marker_color=colorscale[1],fill='tozeroy'))
fig.add_trace(go.Scatter(x=water_storage_rsv2.index, y=water_storage_rsv2.values, name="Reservoir2 storage", marker_color=colorscale[2],fill='tozeroy'))
fig.update_layout(title="<b>Reservoir trajectories </b>", xaxis_title="<b>Time</b> (Hour)", yaxis_title="<b>Volume</b> (Mm<sup>3</sup>)")
fig.show()
```

+++ {"Collapsed": "false"}

# File contents

+++ {"Collapsed": "false"}

## basic_pump.py <a name="tunnel_model.py"></a>

```{code-cell} ipython3
:Collapsed: 'false'

%pycat basic_pump.py
```

+++ {"Collapsed": "false"}

## basic_pump.yaml <a name="tunnel_model.yaml"></a>

```{code-cell} ipython3
:Collapsed: 'false'

shop.dump_yaml(file_path='basic_pump.yaml',input_only=True)
%pycat basic_pump.yaml
```

+++ {"Collapsed": "false"}

## basic_pump.ascii <a name="tunnel_model.ascii"></a>

```{code-cell} ipython3
:Collapsed: 'false'

%pycat basic_pump.ascii
```

```{code-cell} ipython3

```
