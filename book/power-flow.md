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

(power-flow-example)=
# Power flow
SHOP implements PTDF-based power flow. The [](busbar), [](ac_line), and [](dc_line) objects are used to specify the model. The following example demonstrates a simple model with power flow and [](thermal) production units.

## Example
Initialize model:

```{code-cell} ipython3
:Collapsed: 'false'

import pandas as pd
import plotly.graph_objs as go
from pyshop import ShopSession

shop = ShopSession()
starttime=pd.Timestamp("2022-02-27T00")
endtime=starttime+pd.DateOffset(hours=1)
shop.set_time_resolution(starttime=starttime, endtime=endtime, timeunit="hour", timeresolution=pd.Series(index=[starttime],data=[1]))
```

Add busbars and set load:
```{code-cell} ipython3
:Collapsed: 'false'

b1=shop.model.busbar.add_object("Busbar1")
b1.load.set(50)
b2=shop.model.busbar.add_object("Busbar2")
b2.load.set(60)
b3=shop.model.busbar.add_object("Busbar3")
b3.load.set(300)
```

Define thermal units and connect to buses:
```{code-cell} ipython3
:Collapsed: 'false'

t1=shop.model.thermal.add_object("Thermal1")
t1.fuel_cost.set(7.5)
t1.n_segments.set(1)
t1.min_prod.set(0)
t1.max_prod.set(140)
t1.connect_to(b1)

t2=shop.model.thermal.add_object("Thermal2")
t2.fuel_cost.set(6.0)
t2.n_segments.set(1)
t2.min_prod.set(0)
t2.max_prod.set(285)
t2.connect_to(b1)

t3=shop.model.thermal.add_object("Thermal3")
t3.fuel_cost.set(14.0)
t3.n_segments.set(1)
t3.min_prod.set(0)
t3.max_prod.set(90)
t3.connect_to(b2)

t4=shop.model.thermal.add_object("Thermal4")
t4.fuel_cost.set(10.0)
t4.n_segments.set(1)
t4.min_prod.set(0)
t4.max_prod.set(85)
t4.connect_to(b3)
```

Create AC lines and connect between buses:
```{code-cell} ipython3
:Collapsed: 'false'

ac1=shop.model.ac_line.add_object("AC_line1")
ac1.max_forward_flow.set(126)
ac1.max_backward_flow.set(126)
b1.connect_to(ac1)
ac1.connect_to(b2)

ac2=shop.model.ac_line.add_object("AC_line2")
ac2.max_forward_flow.set(250)
ac2.max_backward_flow.set(250)
b1.connect_to(ac2)
ac2.connect_to(b3)

ac3=shop.model.ac_line.add_object("AC_line3")
ac3.max_forward_flow.set(130)
ac3.max_backward_flow.set(130)
b2.connect_to(ac3)
ac3.connect_to(b3)
```

Set PTDF factors:
```{code-cell} ipython3
:Collapsed: 'false'

ac_lines=["AC_line1", "AC_line2", "AC_line3"]
b1.ptdf.set(pd.Series(data=[0.2/0.5, (0.2+0.1)/0.5, 0.2/0.5], index=ac_lines))
b2.ptdf.set(pd.Series(data=[-0.1/0.5, 0.1/0.5, (0.2+0.2)/0.5], index=ac_lines))
b3.ptdf.set(pd.Series(data=[0.0, 0.0, 0.0], index=ac_lines))
```

Run model:
```{code-cell} ipython3
:Collapsed: 'false'

shop.start_sim([],["1"])
```

Display outputs:
```{code-cell} ipython3
:Collapsed: 'false'
display(t1.production.get())
display(t2.production.get())
display(t3.production.get())
display(t4.production.get())
display(b1.power_deficit.get())
display(b2.power_deficit.get())
display(b3.power_deficit.get())
display(b1.power_excess.get())
display(b2.power_excess.get())
display(b3.power_excess.get())
display(b1.energy_price.get())
display(b2.energy_price.get())
display(b3.energy_price.get())
display(ac1.flow.get())
display(ac2.flow.get())
display(ac3.flow.get())
```