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

(discharge_group)=
# discharge_group
The sum discharge of the objects connected to a discharge_group is restricted by the constraints defined in the discharge_group

|   |   |
|---|---|
|Input connections|<a href="plant.html">plant</a>, <a href="gate.html">gate</a>, <a href="tunnel.html">tunnel</a>, <a href="river.html">river</a>|
|Output connections|<a href="plant.html">plant</a>, <a href="gate.html">gate</a>, <a href="river.html">river</a>, <a href="tunnel.html">tunnel</a>|
|License|SHOP_DISCHARGE_GROUP_FUNCTIONALITY|
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
object_attributes = table[table["Object type"] == "discharge_group"].reset_index().iloc[:, 1:]
for index, row in object_attributes.iterrows():
  object_attributes.at[index, "Attribute name"] = f"""<a href="{row['Object type']}.html#{row['Attribute name'].replace('_', '-')}">{row['Attribute name']}</a>"""
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

(discharge_group:initial_deviation_mm3)=
### initial_deviation_mm3
The initial volume deviation for the discharge group before the optimization period. The positive value refers to the upward deviation from weighted discharge while the negative value refers to the downward deviation from weighted discharge. (xUnit: MM3, yUnit: MM3)


(discharge_group:max_accumulated_deviation_mm3_up)=
### max_accumulated_deviation_mm3_up
Maximum accumulated upward volume deviation (Mm3) for the discharge group (xUnit: NO_UNIT, yUnit: MM3)


(discharge_group:max_accumulated_deviation_mm3_down)=
### max_accumulated_deviation_mm3_down
Maximum accumulated downward volume deviation (Mm3) for the discharge group (xUnit: NO_UNIT, yUnit: MM3)


(discharge_group:weighted_discharge_m3s)=
### weighted_discharge_m3s
Weighted discharge target for the discharge group (xUnit: NO_UNIT, yUnit: M3/S)


(discharge_group:penalty_cost_up_per_mm3)=
### penalty_cost_up_per_mm3
Given penalty cost for discharging more than the allowed max accumulated deviation for the discharge group (xUnit: NO_UNIT, yUnit: NOK/MM3)


(discharge_group:penalty_cost_down_per_mm3)=
### penalty_cost_down_per_mm3
Given penalty cost for discharging less than the allowed max accumulated deviation for the discharge group (xUnit: NO_UNIT, yUnit: NOK/MM3)


(discharge_group:min_discharge_m3s)=
### min_discharge_m3s
Minimal sum discharge allowed in the discharge group (xUnit: NO_UNIT, yUnit: M3/S)


(discharge_group:max_discharge_m3s)=
### max_discharge_m3s
Maximal sum discharge allowed in the discharge group (xUnit: NO_UNIT, yUnit: M3/S)


(discharge_group:min_discharge_penalty_cost)=
### min_discharge_penalty_cost
Penalty cost for violating the minimum discharge constraint of the discharge group. (xUnit: NO_UNIT, yUnit: NOK/H/M3/S)


(discharge_group:max_discharge_penalty_cost)=
### max_discharge_penalty_cost
Penalty cost for violating the maximum discharge constraint of the discharge group. (xUnit: NO_UNIT, yUnit: NOK/H/M3/S)


(discharge_group:ramping_up_m3s)=
### ramping_up_m3s
Maximal discharge ramping of the total discharge allowed in the upward direction (xUnit: NO_UNIT, yUnit: M3SEC_HOUR)


(discharge_group:ramping_down_m3s)=
### ramping_down_m3s
Maximal discharge ramping of the total discharge allowed in the downward direction (xUnit: NO_UNIT, yUnit: M3SEC_HOUR)


(discharge_group:ramping_up_penalty_cost)=
### ramping_up_penalty_cost
Penalty cost for violating the upward discharge ramping constraint in the discharge group (xUnit: NO_UNIT, yUnit: NOK/H/M3/S)


(discharge_group:ramping_down_penalty_cost)=
### ramping_down_penalty_cost
Penalty cost for violating the downward discharge ramping constraint in the discharge group (xUnit: NO_UNIT, yUnit: NOK/H/M3/S)


(discharge_group:actual_discharge_m3s)=
### actual_discharge_m3s
Resulting discharge for the discharge group (xUnit: NO_UNIT, yUnit: M3/S)


(discharge_group:accumulated_deviation_mm3)=
### accumulated_deviation_mm3
Resulting accumulated volume deviation for the discharge group (xUnit: NO_UNIT, yUnit: MM3)


(discharge_group:upper_penalty_mm3)=
### upper_penalty_mm3
Resulting penalty when the maximum accumulated upward volume deviation for the discharge group is violated (xUnit: NO_UNIT, yUnit: MM3)


(discharge_group:lower_penalty_mm3)=
### lower_penalty_mm3
Resulting penalty when the maximum accumulated downward volume deviation for the discharge group is violated (xUnit: NO_UNIT, yUnit: MM3)


(discharge_group:upper_slack_mm3)=
### upper_slack_mm3
Resulting slack when the maximum accumulated upward volume deviation for the discharge group is not reached (xUnit: NO_UNIT, yUnit: MM3)


(discharge_group:lower_slack_mm3)=
### lower_slack_mm3
Resulting slack when the maximum accumulated downward volume deviation for the discharge group is not reached (xUnit: NO_UNIT, yUnit: MM3)


(discharge_group:min_discharge_penalty)=
### min_discharge_penalty
Resulting penalty when the minimum discharge constraint in the discharge group is violated (xUnit: NO_UNIT, yUnit: NOK)


(discharge_group:max_discharge_penalty)=
### max_discharge_penalty
Resulting penalty when the maximum discharge constraint in the discharge group is violated (xUnit: NO_UNIT, yUnit: NOK)


(discharge_group:ramping_up_penalty)=
### ramping_up_penalty
Resulting penalty when the upward discharge ramping constraint in the discharge group is violated (xUnit: NO_UNIT, yUnit: NOK)


(discharge_group:ramping_down_penalty)=
### ramping_down_penalty
Resulting penalty when the downward discharge ramping constraint in the discharge group is violated (xUnit: NO_UNIT, yUnit: NOK)


