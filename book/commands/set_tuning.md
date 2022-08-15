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

(set_tuning)=
# set tuning
Deprecated

|   |   |
|---|---|
|Options|/on, /off, /weak, /default, /aggressive|
|License|SHOP_MIP_TUNING|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Tuning CPLEX and OSI
CPLEX and OSI do not have automatic MIP tuning, and so several tuning heuristics can be activated with the command below. In practice, OSI is the solver which has the greatest benefit of MIP tuning.
```
set tuning /<option>
```

|<option>|Comment|
|---|---|
|on|Turn on tuning, use “default” tuning heuristic or heuristic last used|
|off|Turn off tuning|
|weak|Turn on tuning, use “weak” tuning heuristic|
|default|Turn on tuning, use “default” tuning heuristic|
|aggressive|Turn on tuning, use “aggressive” tuning heuristic|

If command not set: Tuning is turned off

Turning tuning off and on again does not change the heuristic method used last time. The different heuristics use different values of the parameter ε, which affects the solver tolerance for integer variables. The table below shows the default epsilon values for the different heuristics:

|Heuristic|ε|
|---|---|
|Default|1.0e-5|
|Weak|1.0e-8|
|Aggressive|1.0e-3|

This value of ε can also be set directly with the command [](set_epsilon).

If command not set: Epsilon according to heuristic.

Valid ε values are bounded by: 1.0e-8 ≤ ε ≤ 1.0e-3 .



