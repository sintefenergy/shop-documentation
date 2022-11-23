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

(dc_line)=
# dc_line
A power line where the flow is decided by the optimization.

|   |   |
|---|---|
|Input connections|<a href="busbar.html">busbar</a>|
|Output connections|<a href="busbar.html">busbar</a>|
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
object_attributes = table[table["Object type"] == "dc_line"].reset_index().iloc[:, 1:]
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

(dc_line:max_forward_flow)=
### max_forward_flow
Maximum transfer capacity in forward direction (xUnit: NO_UNIT, yUnit: MW)


(dc_line:max_backward_flow)=
### max_backward_flow
Maximum transfer capacity in backward direction (xUnit: NO_UNIT, yUnit: MW)


(dc_line:n_loss_segments)=
### n_loss_segments
Number of segments for linearization of quadratic loss (xUnit: NO_UNIT, yUnit: NO_UNIT)


(dc_line:loss_constant)=
### loss_constant
Constant power loss in DC line terminals, independent of power flow (xUnit: NO_UNIT, yUnit: NO_UNIT)


(dc_line:loss_factor_linear)=
### loss_factor_linear
Loss factor multiplied with absolute value of the flow in the line (xUnit: NO_UNIT, yUnit: NO_UNIT)


(dc_line:loss_factor_quadratic)=
### loss_factor_quadratic
Loss factor multiplied with the square of the flow in the line. The calcualtion is linearized with the number of steps defined by n_loss_segments (xUnit: NO_UNIT, yUnit: NO_UNIT)


(dc_line:flow)=
### flow
Flow through the line (xUnit: NO_UNIT, yUnit: MW)


(dc_line:forward_loss)=
### forward_loss
Transmission loss for flow in forward direction of the line (xUnit: NO_UNIT, yUnit: MW)


(dc_line:backward_loss)=
### backward_loss
Transmission loss for flow in backward direction of the line (xUnit: NO_UNIT, yUnit: MW)


