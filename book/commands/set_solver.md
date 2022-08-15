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

(set_solver)=
# set solver
Choose the optimization solver that will be used to solve the SHOP model. The CPLEX solver is the default option for running SHOP.

|   |   |
|---|---|
|Options|/cplex, /gurobi, /osi|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Choosing the LP solver
Changing LP solver used in SHOP is done with the command:
```
set solver /<option>
```

|<option>|Comment|
|---|---|
|cplex|Use CPLEX as solver|
|gurobi|Use GUROBI as solver|
|osi|Use OSI as solver|

If command not set: CPLEX will be used as the LP solver

Changing the LP solver requires that the correct dll file can be found by SHOP.



