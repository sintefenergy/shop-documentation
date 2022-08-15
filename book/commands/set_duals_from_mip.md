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

(set_duals_from_mip)=
# set duals_from_mip
Turning the command on will fix binary variables after solving a MIP iteration and solve the resulting linear problem again to get dual values. Default behaviour  (option "/off") does not re-solve MIP problems to get dual values

|   |   |
|---|---|
|Options|/on, /off|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```





