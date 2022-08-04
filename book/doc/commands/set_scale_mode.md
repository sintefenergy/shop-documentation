## Set scale mode in CPLEX
It is possible to change the scale mode in CPLEX for the sake of better feasibility of poorly conditioned problems (when minor changes in input data result in major changes in solutions):
```
set scale_mode /<option>
```

|<option>|Comment|
|---|---|
|aggressive|Aggressive scaling|
|default|Equilibration scaling|
|no_scale|No scaling|

If command not set: Equilibration scaling will be used