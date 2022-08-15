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

(busbar)=
# busbar
A node in the electricity grid that production, consumption, market and transmission objects can be connected to

|   |   |
|---|---|
|Input connections|<a href="generator.html">generator</a>, <a href="pump.html">pump</a>, <a href="thermal.html">thermal</a>, <a href="market.html">market</a>, <a href="ac_line.html">ac_line</a>, <a href="dc_line.html">dc_line</a>|
|Output connections|<a href="market.html">market</a>, <a href="generator.html">generator</a>, <a href="pump.html">pump</a>, <a href="thermal.html">thermal</a>, <a href="ac_line.html">ac_line</a>, <a href="dc_line.html">dc_line</a>|
|License|SHOP_OPEN|
|Release version|14.3.4.0|

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
object_attributes = table[table["Object type"] == "busbar"].reset_index().iloc[:, 1:]
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

(busbar:load)=
### load
Load at the busbar (xUnit: NO_UNIT, yUnit: MW)


(busbar:ptdf)=
### ptdf
Power transfer distribution factors describing change in flow for each ac line relative to change in generation at the busbar (xUnit: NO_UNIT, yUnit: NO_UNIT)


(busbar:energy_price)=
### energy_price
Dual value for the energy balance constraint at the busbar (xUnit: NO_UNIT, yUnit: NOK/MWH)


(busbar:power_deficit)=
### power_deficit
Power added to the busbar power balance to cover deficit of energy (xUnit: NO_UNIT, yUnit: MWH)


(busbar:power_excess)=
### power_excess
Power subtracted from the busbar power balance to remove excess of energy (xUnit: NO_UNIT, yUnit: MWH)


