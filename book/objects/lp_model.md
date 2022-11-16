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

(lp_model)=
# lp_model
Represents the optimization model built by SHOP and solved by CPLEX

|   |   |
|---|---|
|Input connections||
|Output connections||
|License|SHOP_OPEN|
|Release version|14.1.0.0|

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
object_attributes = table[table["Object type"] == "lp_model"].reset_index().iloc[:, 1:]
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

(lp_model:sim_mode)=
### sim_mode
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:var_type_names)=
### var_type_names
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:var_type_abbrev)=
### var_type_abbrev
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:var_type_index_type_beg)=
### var_type_index_type_beg
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:var_type_index_type_cnt)=
### var_type_index_type_cnt
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:var_type_index_type_val)=
### var_type_index_type_val
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:row_type_names)=
### row_type_names
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:row_type_index_type_beg)=
### row_type_index_type_beg
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:row_type_index_type_cnt)=
### row_type_index_type_cnt
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:row_type_index_type_val)=
### row_type_index_type_val
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:index_type_names)=
### index_type_names
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:index_type_desc_beg)=
### index_type_desc_beg
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:index_type_desc_cnt)=
### index_type_desc_cnt
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:index_type_desc_val)=
### index_type_desc_val
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:AA)=
### AA
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:Irow)=
### Irow
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:Jcol)=
### Jcol
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:rhs)=
### rhs
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:sense)=
### sense
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:ub)=
### ub
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:lb)=
### lb
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:cc)=
### cc
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:bin)=
### bin
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:x)=
### x
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:dual)=
### dual
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:var_type)=
### var_type
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:var_index_beg)=
### var_index_beg
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:var_index_cnt)=
### var_index_cnt
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:var_index_val)=
### var_index_val
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:row_type)=
### row_type
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:row_index_beg)=
### row_index_beg
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:row_index_cnt)=
### row_index_cnt
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:row_index_val)=
### row_index_val
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_row_type)=
### add_row_type
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_row_index)=
### add_row_index
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_row_variables)=
### add_row_variables
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_row_coeff)=
### add_row_coeff
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_row_rhs)=
### add_row_rhs
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_row_sense)=
### add_row_sense
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_row_last)=
### add_row_last
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_var_type)=
### add_var_type
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_var_index)=
### add_var_index
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_var_ub)=
### add_var_ub
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_var_lb)=
### add_var_lb
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_var_cc)=
### add_var_cc
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_var_bin)=
### add_var_bin
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(lp_model:add_var_last)=
### add_var_last
LP-model data (xUnit: NO_UNIT, yUnit: NO_UNIT)


