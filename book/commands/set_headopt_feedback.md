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

(set_headopt_feedback)=
# set headopt_feedback
Deprecated, old head optimization functionality

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Setting head optimization feedback factor
In the old head optimization model, the heuristic can be tweaked using the command:
```
set headopt_feedback <value>
```

If command not set: The feedback factor will be set to 1.0

We recommend using the new model for head optimization, see [](set_power_head_optimization).



