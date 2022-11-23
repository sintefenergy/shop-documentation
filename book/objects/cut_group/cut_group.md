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

(cut_group)=
# cut_group
An object to represent the set of linear cut constraints that can be used as end valuation for a watercourse. The constant right-hand side of the cut constraints are stored on this object, while the cut coefficients are found on the connected reservoir and inflow_series objects.

|   |   |
|---|---|
|Input connections|<a href="reservoir.html">reservoir</a>, <a href="inflow_series.html">inflow_series</a>|
|Output connections|<a href="reservoir.html">reservoir</a>, <a href="inflow_series.html">inflow_series</a>|
|License|SHOP_OPEN|
|Release version|14.0.0.3|

```{contents}
:local:
:depth: 1
```





## References
  - Increased Information Flow between Hydropower Scheduling Models through Extended Cut Sharing {cite}`Gjerden2016`
  

## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "cut_group"].reset_index().iloc[:, 1:]
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

(cut_group:rhs)=
### rhs
The right hand side constant for each cut in the cut_group. Represent the future expected income of the system and is usually a positive number. In the case of price dependent cuts, the price level should be the reference value for each xy in the xy_array. (xUnit: NO_UNIT, yUnit: NOK)


(cut_group:end_value)=
### end_value
Future expected income of the system that is part of the cut_group. (xUnit: NO_UNIT, yUnit: NOK)


(cut_group:binding_cut_up)=
### binding_cut_up
The zero-indexed binding cut constraint in the closest price level above the average price in SHOP is saved as the final value in the time series. The value is set to -1 if no cuts have a price above the average price in SHOP. In case of price independent cuts, the value is the binding cut in the cut group. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(cut_group:binding_cut_down)=
### binding_cut_down
The zero-indexed binding cut constraint in the closest price level below the average price in SHOP is saved as the final value in the time series. In case of price independent cuts or if there are no cuts with a price below the average price in SHOP, the value is set to -1. (xUnit: NO_UNIT, yUnit: NO_UNIT)


