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

(production_group)=
# production_group
Represents a group of hydropower plants that must abide by the sum production constraints defined in the production_group 

|   |   |
|---|---|
|Input connections|<a href="plant.html">plant</a>|
|Output connections|<a href="plant.html">plant</a>|
|License|SHOP_OPEN|
|Release version|14.0.0.1|

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
object_attributes = table[table["Object type"] == "production_group"].reset_index().iloc[:, 1:]
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

(production_group:energy_target)=
### energy_target
Sum energy production target for time steps with energy_target_period_flag set to 1. (xUnit: MWH, yUnit: MWH)


(production_group:energy_penalty_cost_up)=
### energy_penalty_cost_up
Penalty cost for producing more energy than the target amount. (xUnit: NOK/MWH, yUnit: NOK/MWH)


(production_group:energy_penalty_cost_down)=
### energy_penalty_cost_down
Penalty cost for producing less energy than the target amount. (xUnit: NOK/MWH, yUnit: NOK/MWH)


(production_group:energy_target_period_flag)=
### energy_target_period_flag
Flag defining which time steps are part of the target energy production constraint (xUnit: NO_UNIT, yUnit: MWH)


(production_group:max_p_limit)=
### max_p_limit
The maximal power production limit for the sum of plants in the group. (xUnit: NO_UNIT, yUnit: MW)


(production_group:min_p_limit)=
### min_p_limit
The minimal power production limit for the sum of plants in the group. (xUnit: NO_UNIT, yUnit: MW)


(production_group:max_p_penalty_cost)=
### max_p_penalty_cost
The penalty cost for breaking the maximum power production limit constraint. The default penalty cost is specified by the power_limit_penalty_cost on the global_settings object. (xUnit: NO_UNIT, yUnit: NOK/MW)


(production_group:min_p_penalty_cost)=
### min_p_penalty_cost
The penalty cost for breaking the minimum power production limit constraint. The default penalty cost is specified by the power_limit_penalty_cost on the global_settings object. (xUnit: NO_UNIT, yUnit: NOK/MW)


(production_group:sum_production)=
### sum_production
The sum power production of all the plants connected to the group. (xUnit: NO_UNIT, yUnit: MW)


(production_group:min_p_penalty)=
### min_p_penalty
The incurred penalty for breaking the minimum power production constraint. (xUnit: NO_UNIT, yUnit: NOK)


(production_group:max_p_penalty)=
### max_p_penalty
The incurred penalty for breaking the maximum power production constraint. (xUnit: NO_UNIT, yUnit: NOK)


(production_group:energy_penalty_up)=
### energy_penalty_up
The total penalty incurred when breaking the target energy constraint by generating more energy than the target. (xUnit: NOK, yUnit: NOK)


(production_group:energy_penalty_down)=
### energy_penalty_down
The total penalty incurred when breaking the target energy constraint by generating less energy than the target. (xUnit: NOK, yUnit: NOK)


