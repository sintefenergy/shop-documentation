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