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

(bid_group)=
# bid_group
Represents a group of hydropower plants that will participate in the optimal bidding problem when running a stochastic SHOP optimization

|   |   |
|---|---|
|Input connections|<a href="plant.html">plant</a>|
|Output connections|<a href="plant.html">plant</a>|
|License|SHOP_SCENARIO_FUNCTIONALITY|
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
object_attributes = table[table["Object type"] == "bid_group"].reset_index().iloc[:, 1:]
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

(bid_group:price_dimension)=
### price_dimension
Number of prices in the resulting bid matrix (xUnit: NO_UNIT, yUnit: NO_UNIT)


(bid_group:time_dimension)=
### time_dimension
Number of time steps in the resulting bid matrix (xUnit: NO_UNIT, yUnit: NO_UNIT)


(bid_group:bid_start_interval)=
### bid_start_interval
Index of the first time step in the bid matrix (xUnit: NO_UNIT, yUnit: NO_UNIT)


(bid_group:bid_end_interval)=
### bid_end_interval
Index of the last time step in the bid matrix (xUnit: NO_UNIT, yUnit: NO_UNIT)


(bid_group:reduction_cost)=
### reduction_cost
The cost of reducing the full bid matrix to the desired number of points (xUnit: NO_UNIT, yUnit: NO_UNIT)


(bid_group:bid_curves)=
### bid_curves
Resulting bid matrix (xUnit: NOK/MWH, yUnit: MWH)


(bid_group:bid_penalty)=
### bid_penalty
The sum of penalty over all scenarios and time steps for violating the requirement of bid volume increasing when price increases in the bid matrix (xUnit: NOK/MWH, yUnit: MWH)


