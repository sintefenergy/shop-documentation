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

({{ object.Object_type }})=
# {{ object.Object_type }}
{{ object.Description }}

|   |   |
|---|---|
|Input connections|
{%- for connection in inputs -%}
  {%- if loop.index > 1 %}, {% endif -%}
  <a href="{{ connection }}.html">{{ connection }}</a>
{%- endfor -%}
|
|Output connections|
{%- for connection in object.Legal_output_connections -%}
  {%- if loop.index > 1 %}, {% endif -%}
  <a href="{{ connection }}.html">{{ connection }}</a>
{%- endfor -%}
|
|License|{{ object.License }}|
|Release version|{{ object.Version_added }}|

```{contents}
:local:
:depth: 1
```

{{ doc }}

{% if examples is defined -%}
## Examples
  {% for example in examples -%}
  - []({{ example }})
  {% endfor %}
{%- endif %}

{% if references is defined -%}
## References
  {% for reference in references -%}
  - {{ reference.title }} {cite}`{{ reference.ID }}`
  {% endfor %}
{%- endif %}

## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "{{ object.Object_type }}"].reset_index().iloc[:, 1:]
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

{% for attribute in attributes -%}
({{ attribute.Object_type }}:{{ attribute.Attribute_name }})=
### {{ attribute.Attribute_name }}
{{ attribute.Description }}

{{ attribute.doc }}
{% endfor %}