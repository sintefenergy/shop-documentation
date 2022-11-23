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

(plant_reserve_capability)=
# plant_reserve_capability
An object describing different types of reserve delivery capabilities for the sum of the units in a hydropower plant.

|   |   |
|---|---|
|Input connections|<a href="plant.html">plant</a>|
|Output connections|<a href="plant.html">plant</a>|
|License|SHOP_RESERVE_GROUP|
|Release version|14.4.0.0|

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
object_attributes = table[table["Object type"] == "plant_reserve_capability"].reset_index().iloc[:, 1:]
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

(plant_reserve_capability:reserve_type_name)=
### reserve_type_name
The reserve product this reserve capability definition is valid for. Can be either FCR_N_UP/DOWN, FCR_D_UP/DOWN, FRR_UP/DOWN, or RR_UP/DOWN   (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant_reserve_capability:p_gen_extended)=
### p_gen_extended
 (xUnit: NO_UNIT, yUnit: MW)


(plant_reserve_capability:p_pump_extended)=
### p_pump_extended
 (xUnit: NO_UNIT, yUnit: MW)


(plant_reserve_capability:schedule)=
### schedule
A schedule for how much reserve capacity of the specified type that must be delivered for all generators and pumps in the plant (xUnit: NO_UNIT, yUnit: MW)


