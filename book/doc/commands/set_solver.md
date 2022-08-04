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