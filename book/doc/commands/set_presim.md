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