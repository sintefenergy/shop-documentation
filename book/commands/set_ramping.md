(set_ramping)=
# set ramping
Turn on or off all ramping constraints related to the plant, reservoir, and gate objects. For contract and multi-object ramping constraints, the /request option can be used to only add ramping constraints if they were violated in the previous iteration.

|   |   |
|---|---|
|Options|/request, /on, /off|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

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



