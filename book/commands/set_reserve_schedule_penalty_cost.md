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

(set_reserve_schedule_penalty_cost)=
# set reserve_schedule_penalty_cost
Command to set the penalty cost for breaking the unit reserve schedule constraints. Default value is 10000 NOK/MW

|   |   |
|---|---|
|Options|nan|
|License|SHOP_RESERVE_GROUP|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Reserve group schedule penalty cost
If the reserve group schedule is not fulfilled, a penalty cost will be applied. This cost can be set with the command:
```
set reserve_schedule_penalty_cost <value>
```

If command not set: A penalty cost of 10000 NOK/MWh will be used.



