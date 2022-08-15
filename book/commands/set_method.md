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

(set_method)=
# set method
Choose the solution method the LP solver (cplex, gurobi, or osi) will use to solve each non-mip iteration in SHOP

|   |   |
|---|---|
|Options|/primal, /dual, /baropt, /hybbaropt, /netprimal, /netdual, /concurrent_lp|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Defining CPLEX solution method
CPLEX has different solution algorithms that can be used to solve a LP problem. It is possible to choose the algorithm by giving the command:
```
set method /<option>
```

The following options are allowed:
|Option|Comment|
|------|-------|
|primal|Primal simplex method|
|dual|Dual simplex method|
|baropt|Barrier solver|
|hybbaropt|Hybrid barrier solver|
|netprimal|Network primal solver with additional constrains|
|netdual|Network dual solver with additional constrains|

The default solver is **dual simplex**.

When using MIP modelling, a branch and bound algorithm will automatically be used as this is the only valid alternative.



