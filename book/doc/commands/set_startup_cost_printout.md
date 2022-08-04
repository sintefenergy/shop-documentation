## Printing out the optimized start-stop costs
The total start-stop costs incurred by SHOP is printed in the log file alongside the other components of the objective function. This is based on how many times the generators and pumps in the system have been turned on and off in the final SHOP solution. To only count starts and stops in hours flagged as MIP, use the command:
```
set startup_cost_printout /<option>
```

|<option>|Comment|
|---|---|
|optimized|Print out the start-stop costs based on MIP-flag|
|default|Print out the start-stop costs based on the total amount of starts and stops|

If command not set: The /default option is used

Note that this command does not take into account running with linear start-stop costs.