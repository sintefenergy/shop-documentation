## Using linear start-stop costs
Using linear instead of integer variables to add pump and generator start-stop costs can be done with the command:
```
set linear_startup /<option>
```

|<option>|Comment|
|---|---|
|on|Turn on linear start-stop costs|
|off|Turn off linear start-stop costs|

If command not set: Linear start-stop costs will not be used.

Linear start-stop costs allows a unit to have a fractional start or stop, but may reduce solution time of big problems drastically. The following table shows the outcome of combining the commands [](set_universal_mip) and [](set_linear_startup). In short, if an hour is flagged as a MIP-hour, integer start-stop costs will be built. If the hour is not flagged as MIP, linear start-stop costs will be used if the command `set linear_startup /on` is used. Otherwise, no start-stop costs are built, and SHOP sees no cost of turning the unit on or off.

The table below shows what kind of start- stop costs will be used in SHOP if the commands "set linear_startup" and "set universal_mip" are combined:

||set universal_mip /on|set universal_mip /off|set universal_mip /not_set|
|---|---|---|---|
|set linear_startup /on|Integer start- stop costs used in all hours|Linear start- stop costs used in all hours|Integer start- stop costs used if mip_flag is 1, linear otherwise|
|set linear_startup /off|Integer start- stop costs used in all hours|No start- stop costs used in any hour|Integer start- stop costs used if mip_flag is 1, no start-up costs otherwise|