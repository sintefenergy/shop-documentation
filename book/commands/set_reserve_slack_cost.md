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

(set_reserve_slack_cost)=
# set reserve_slack_cost
The cost for delivering more than the reserve capacity obligations of any reserve type in any reserve group. Default value is 0.000001 NOK/MW

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Reserve group slack cost
The reserve group slack cost can be changed with the command:
```
set reserve_slack_cost <value>
```

If command not set: The slack cost will be set to 1.0e-6 NOK/MWh.

This slack cost is applied if there is too much reserve power allocated, and so the default cost is not set very high. A much harsher penalty cost is used if there is too little reserve power present.  



