---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: 'Python 3'
  name: python3
---

(junction)=
# junction
A hydraulic junction coupling two reservoirs to a common output tunnel. Water flows in the junction tunnels according to the pressure and mass balance

|   |   |
|---|---|
|Input connections|<a href="reservoir.html">reservoir</a>, <a href="plant.html">plant</a>, <a href="gate.html">gate</a>, <a href="junction.html">junction</a>, <a href="creek_intake.html">creek_intake</a>|
|Output connections|<a href="plant.html">plant</a>, <a href="junction_gate.html">junction_gate</a>, <a href="junction.html">junction</a>, <a href="reservoir.html">reservoir</a>|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```







## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "junction"].reset_index().iloc[:, 1:]
for index, row in object_attributes.iterrows():
  object_attributes.at[index, "Attribute name"] = f"""<a href="{row['Object type'].replace('_', '-')}.html#{row['Attribute name'].replace('_', '-')}">{row['Attribute name']}</a>"""
  object_attributes.at[index, "Data type"] = f"""<a href="../datatypes.html#{row['Data type'].replace('_', '-')}">{row['Data type']}</a>"""
itables.show(object_attributes,
  dom='tlip',
  search={'regex': True, "caseInsensitive": True},
  column_filters='header',
  columns=[
    {
      'name': '',
      'className': 'dt-control',
      'orderable': False,
      'data': None,
      'defaultContent': '',
    },
    {
      'name': 'Attribute name',
      'className': 'dt-body-left'
    },
    {
      'name': 'Data type',
      'className': 'dt-body-left'
    },
    {
      'name': 'I/O',
      'className': 'dt-body-left'
    },
    {
      'name': 'License',
      'className': 'dt-body-left'
    },
    {
      'name': 'Version added',
      'className': 'dt-body-left'
    },
    {
      'name': 'Description',
      'visible': False
    }
  ]
)
HTML('''<script>
$('tbody').on('click', 'td.dt-control', function () {
    var tr = $(this).closest('tr');
    var table = $(this).closest('table').DataTable();
    var row = table.row(tr);

    if (row.child.isShown()) {
        // This row is already open - close it
        row.child.hide();
        tr.removeClass('shown');
    } else {
        // Open this row
        row.child("<div align='left'>".concat(row.data()[6], "</div>")).show();
        tr.addClass('shown');
    }
});
</script>''')
```

(junction:junc_slack)=
### junc_slack
Flag determining whether slack variables should be added to the mass balance of the junction (xUnit: NO_UNIT, yUnit: NO_UNIT)


(junction:altitude)=
### altitude
Physical height of the connection point between tunnel_1 and tunnel_2 coming into this junction (xUnit: METER, yUnit: METER)


(junction:tunnel_flow_1)=
### tunnel_flow_1
Resulting flow in tunnel_1 (xUnit: NO_UNIT, yUnit: M3/S)


(junction:tunnel_flow_2)=
### tunnel_flow_2
Resulting flow in tunnel_2 (xUnit: NO_UNIT, yUnit: M3/S)


(junction:sim_tunnel_flow_1)=
### sim_tunnel_flow_1
The simulated flow in tunnel_1 of the junction (xUnit: NO_UNIT, yUnit: M3/S)


(junction:sim_tunnel_flow_2)=
### sim_tunnel_flow_2
The simulated flow in tunnel_2 of the junction (xUnit: NO_UNIT, yUnit: M3/S)


(junction:loss_factor_1)=
### loss_factor_1
Friction loss factor for tunnel_1 into this junction multiplied with the square of the flow to get head loss (xUnit: S2/M5, yUnit: S2/M5)


(junction:loss_factor_2)=
### loss_factor_2
Friction loss factor for tunnel_2 into this junction multiplied with the square of the flow to get head loss (xUnit: S2/M5, yUnit: S2/M5)


(junction:min_pressure)=
### min_pressure
Minimum pressure requirement at the connection point of tunnel_1 and tunnel_2 (xUnit: NO_UNIT, yUnit: METER)


(junction:pressure_height)=
### pressure_height
Resulting pressure height from the optimization calculations (xUnit: NO_UNIT, yUnit: METER)


(junction:sim_pressure_height)=
### sim_pressure_height
Resulting pressure height from the simulation (xUnit: NO_UNIT, yUnit: METER)


(junction:incr_cost)=
### incr_cost
Resulting marginal value of water in this junction referred to ocean level accounting for headloss between the tunnel connection point and the plant below (xUnit: NO_UNIT, yUnit: NOK)


(junction:local_incr_cost)=
### local_incr_cost
Resulting marginal value of water  in this junction referred to the next reservoir below accounting for headloss between the tunnel connection point and the plant below (xUnit: NO_UNIT, yUnit: NOK)


