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

(set_presim)=
# set presim
nan

|   |   |
|---|---|
|Options|/on, /off|
|License|SHOP_PRESIM|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Activating presim
In order to get a better estimate of reservoir trajectories for reservoirs connected by deltameter gates and junctions, a pre-optimization calculation can be performed. This calculation uses the reservoir level results from the previous iteration to refine the starting point for the next.
```
set presim /<option>
```

|<option>|Comment|
|---|---|
|on|Turn on presim functionality|
|off|Turn off presim functionality|

If command is not set, no pre-optimization simulation will be done.



