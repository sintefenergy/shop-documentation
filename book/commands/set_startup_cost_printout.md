(set_startup_cost_printout)=
# set startup_cost_printout
If the "/optimized" option is given, the startup and shutdown costs printed in the log file will only include the costs seen by the optimization problem in full iterations, which can include the cost of partial startups and shutdowns if MIP is not used. The default option is to print out post-calculated value based on the final unit commitment used in incremental iterations.

|   |   |
|---|---|
|Options|/default, /optimized|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

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



