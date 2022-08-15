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

(set_pump_turn_off_limit)=
# set pump_turn_off_limit
Change the limit for considering that a pump is on or off if binary variables are not used in full mode. If the production is below the specified input fraction (between 0.0 and 1.0) of the pump's minimum production, the unit is considered off in incremental iterations. The default value is 0.5 (50%).

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|14.0.0.9|

```{contents}
:local:
:depth: 1
```





