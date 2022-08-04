## Including ramping constraints
There are several options for adding ramping constraints to the model:
```
set ramping /<option>
```

|<option>|Comment|
|---|---|
|on|Add all ramping constraints|
|off|Ignore all ramping constraints|
|request|Add constraints when violations are detected|

If command not set: Ignore all ramping constraints.

Checking if the ramping constraints are being violated is performed after each iteration, and the result is written to file or to the screen. If ramping constraints are to be activated it must be done in the full mode. Activating ramping and turning on incremental mode usually results in an infeasible optimization problem.