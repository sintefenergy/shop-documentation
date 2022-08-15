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

(creek_intake)=
# creek_intake
A creek intake object which represents unregulated inflow entering the tunnel system below a reservoir

|   |   |
|---|---|
|Input connections|<a href="reservoir.html">reservoir</a>, <a href="creek_intake.html">creek_intake</a>|
|Output connections|<a href="plant.html">plant</a>, <a href="gate.html">gate</a>, <a href="junction.html">junction</a>, <a href="creek_intake.html">creek_intake</a>|
|License|SHOP_CREEK_INTAKE|
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
object_attributes = table[table["Object type"] == "creek_intake"].reset_index().iloc[:, 1:]
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

(creek_intake:net_head)=
### net_head
Physical height of the creek intake opening (xUnit: METER, yUnit: METER)


(creek_intake:max_inflow)=
### max_inflow
Static maximum capacity for inflow to this creek intake (xUnit: M3/S, yUnit: M3/S)


(creek_intake:max_inflow_dynamic)=
### max_inflow_dynamic
Time-dependent maxiumu capacity for inflow to this creek intake (xUnit: NO_UNIT, yUnit: M3/S)


(creek_intake:inflow)=
### inflow
Inflow to the creek intake (xUnit: NO_UNIT, yUnit: M3/S)


(creek_intake:sim_inflow)=
### sim_inflow
Resulting inflow to this creek intake after simulation based on observed reservoir level and plant production (xUnit: NO_UNIT, yUnit: M3/S)


(creek_intake:sim_pressure_height)=
### sim_pressure_height
Resulting pressure height of the creek intake after simulation based on observed reservoir level and plant production (xUnit: NO_UNIT, yUnit: METER)


(creek_intake:inflow_percentage)=
### inflow_percentage
Predefined factor to generate inflow to this creek intake based on a percentage of the inflow to the reservoir above (xUnit: NO_UNIT, yUnit: M3/S)


(creek_intake:overflow_cost)=
### overflow_cost
Cost for spillage from this creek intake if a spill gate is connected to it (xUnit: NO_UNIT, yUnit: NOK/MM3)


(creek_intake:non_physical_overflow_flag)=
### non_physical_overflow_flag
Resulting flag series telling if there was non-physical overflow from this creek intake i.e. spilling water with inflow below the maximum capacity (xUnit: NO_UNIT, yUnit: NO_UNIT)


