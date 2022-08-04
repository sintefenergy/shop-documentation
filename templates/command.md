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

({{ object.Command }})=
# {{ object.Command }}
{{ object.Description }}

|   |   |
|---|---|
|Options|{{ object.Options }}|
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
