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

(simple-tunnel)=
# Simple tunnel example

This example is available in the following formats.

- pyshop
    - [tunnel_model.py](tunnel-model-py)
    - [tunnel_gate.py](tunnel-gate-py)
- YAML
    - [tunnel_model.yaml](tunnel-model-yaml)
    - [tunnel_gate.yaml](tunnel-gate-yaml)
- ASCII
    - [tunnel_model.ascii](tunnel-model-ascii)
    - [tunnel_gate.ascii](tunnel-gate-ascii)

```{code-cell} ipython3
:Collapsed: 'false'

#Necessary imports used in all examples
import pandas as pd
import cufflinks as cf
import plotly.offline as py
import plotly.express as px
cf.go_offline()
py.offline.init_notebook_mode(connected=True)
from pyshop import ShopSession

#Functions used in this example for building a tunnel model, adding a gate to a tunnel and running the optimization
from tunnel_model import build_model, add_gate, run_model
```

+++ {"Collapsed": "false"}

We create a system with three reservoirs, three tunnels and one plant. In the first model, **shop_default**, there are no gates to optimize, and the flow simply follows the physical laws of the tunnel system. Both the start level and the inflow in Reservoir3, the closest reservoir to the plant, is higher than in the other reservoirs. This means, that some of this extra water in Reservoir3 will naturally flow into the other reservoirs.

```{code-cell} ipython3
:Collapsed: 'false'

#Create a standard ShopSession
shop_default=ShopSession()
#Build a simple tunnel model without tunnel gates by calling function "build_model" in tunnel_model.py
build_model(shop_default)
#Optimize model by calling "run_model" in tunnel_model.py
run_model(shop_default)
#Display topology to the screen
display(shop_default.model.build_connection_tree())
#Display results for reservoir levels
pd.concat([obj.head.get().rename(obj.get_name()) for obj in shop_default.model.reservoir], axis=1).iplot(title="Reservoir level")
#Display results for tunnel flows
pd.concat([obj.flow.get().rename(obj.get_name()) for obj in shop_default.model.tunnel], axis=1).iplot(title="Tunnel flow")
```

+++ {"Collapsed": "false"}

The second model is allowed to adjust the gate opening in the tunnel between Reservoir2 and Reservoir3. As we see in the results, SHOP is able to keep more water in Reservoir3, and thus get more energy from the plant, by closing this gate for most of the period. Only at the end of the period it is partially opened to prevent spillage from Reservoir3.

```{code-cell} ipython3
:Collapsed: 'false'

#Create a standard ShopSession
shop_optimized=ShopSession()
#Build a simple tunnel model without gates by calling function "build_model" in tunnel_model.py
build_model(shop_optimized)
#Add a gate between Reservoir2 and Reservoir3 by calling function "add_gate" in tunnel_model.py
add_gate(shop_optimized)
#Optimize model by calling "run_model" in tunnel_model.py
run_model(shop_optimized)
#Display results for reservoir levels
pd.concat([obj.head.get().rename(obj.get_name()) for obj in shop_optimized.model.reservoir], axis=1).iplot(title="Reservoir level")
#Display results for tunnel flows
pd.concat([obj.flow.get().rename(obj.get_name()) for obj in shop_optimized.model.tunnel], axis=1).iplot(title="Tunnel flow")
#Display results for tunnel opening
pd.concat([obj.gate_opening.get().rename(obj.get_name()) for obj in shop_optimized.model.tunnel], axis=1).iplot(title="Gate opening")

#Compare objective functions to see improvement in result from optimizing the gate
default_objective=shop_default.model.objective["average_objective"].grand_total.get()
optimized_objective=shop_optimized.model.objective["average_objective"].grand_total.get()
print(f"Optimization of the gate in Tunnel2 improved the objective with {-(optimized_objective-default_objective):.2f}€")
```

+++ {"Collapsed": "false"}

# File contents

+++ {"Collapsed": "false"}

(tunnel-model-py)=
## tunnel_model.py <a name="tunnel_model.py"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('tunnel_model.py', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(tunnel-gate-py)=
## tunnel_gate.py

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('tunnel_gate.py', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(tunnel-model-yaml)=
## tunnel_model.yaml <a name="tunnel_model.yaml"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('tunnel_model.yaml', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(tunnel-gate-yaml)=
## tunnel_gate.yaml <a name="tunnel_gate.yaml"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('tunnel_gate.yaml', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(tunnel-model-ascii)=
## tunnel_model.ascii <a name="tunnel_model.ascii"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('tunnel_model.ascii', 'r') as f:
    print(f.read())
```

+++ {"Collapsed": "false"}

(tunnel-gate-ascii)=
## tunnel_gate.ascii <a name="tunnel_gate.ascii"></a>

```{code-cell} ipython3
:Collapsed: 'false'
:tags: ['remove-input']

with open('tunnel_gate.ascii', 'r') as f:
    print(f.read())
```
