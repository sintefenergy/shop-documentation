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

(attribute-table)=
# Attributes

```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
import pandas as pd
from IPython.core.display import HTML

init_notebook_mode(all_interactive=True, connected=True)
table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv').reset_index()
for index, row in table.iterrows():
  table.at[index, "Object type"] = f"""<a href="objects/{row['Object type'].replace('_', '-')}.html">{row['Object type']}</a>"""
  table.at[index, "Attribute name"] = f"""<a href="objects/{row['Object type'].replace('_', '-')}.html#{row['Attribute name'].replace('_', '-')}">{row['Attribute name']}</a>"""
  table.at[index, "Data type"] = f"""<a href="datatypes.html#{row['Data type'].replace('_', '-')}">{row['Data type']}</a>"""
itables.show(
  table,
  dom='tlip',
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
      'name': 'Object type',
      'className': 'dt-body-left'
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
        row.child("<div align='left'>".concat(row.data()[7], "</div>")).show();
        tr.addClass('shown');
    }
});
</script>''')
```
