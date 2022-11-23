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

(thermal)=
# thermal
A general thermal power generating unit with a fixed linear or quadratic fuel cost

|   |   |
|---|---|
|Input connections|<a href="busbar.html">busbar</a>|
|Output connections|<a href="busbar.html">busbar</a>|
|License|SHOP_OPEN|
|Release version|14.3.2.0|

```{contents}
:local:
:depth: 1
```



## Examples
  - [](power-flow-example)
  



## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "thermal"].reset_index().iloc[:, 1:]
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

(thermal:fuel_cost)=
### fuel_cost
Cost proportional to the amount of fuel used by the thermal unit (xUnit: NOK/MWH, yUnit: NOK/MWH)


(thermal:quadratic_fuel_cost)=
### quadratic_fuel_cost
Cost proportional to the square of the amount of fuel used by the thermal unit (xUnit: NOK/MWH, yUnit: NOK/MWH)


(thermal:n_segments)=
### n_segments
Number of segments on the production curve of the unit (xUnit: NO_UNIT, yUnit: NO_UNIT)


(thermal:min_prod)=
### min_prod
Minimum production level of the unit (xUnit: MW, yUnit: MW)


(thermal:max_prod)=
### max_prod
Maximum production level of the unit (xUnit: MW, yUnit: MW)


(thermal:startcost)=
### startcost
Cost for starting up the unit (xUnit: NOK, yUnit: NOK)


(thermal:stopcost)=
### stopcost
Cost for shutting down the unit (xUnit: NOK, yUnit: NOK)


(thermal:production)=
### production
Production from the unit (xUnit: MW, yUnit: MW)


