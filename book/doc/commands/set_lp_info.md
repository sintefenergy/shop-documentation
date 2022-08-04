## Reduce size of LP-model for very large cases
This command reduces the size of the LP-model that is sent to the solver. This could reduce memory usage, but normally not calculation time, for very large cases. If the solver detects any problems with the model, the feedback from the solver will contain less useful information when this option is set to "min".
```
set lp_info /<option>
```

|<option>|Comment|
|---|---|
|min|Remove certain information from the LP-model that is sent to the solver.|

If command not set: The LP-problem is transferred with the normal amount of information to the solver.

Results calculated and optimized in SHOP can be saved to file in many different ways. User data and the LP model can also be dumped to file.