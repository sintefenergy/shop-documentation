(set_dyn_flex_mip)=
# set dyn_flex_mip
Set the number of time steps used for dynamic flexible MIP, which aggregates unit commitment decisions in neighbouring time intervals. Default value of -1 turns off the dynamic flexible MIP functionality

|   |   |
|---|---|
|Options|nan|
|License|SHOP_DYN_FLEX|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Activating dynamic flexible MIP
In order to save computation time, start/stop binary variables in plants can cover more than one time step. The timespan of a MIP interval can be set dynamically in SHOP, meaning that SHOP decides where the intervals should be placed based on previous results. This is done by giving the command:
```
set dyn_flex_mip <value>
```

If command is not set, dynamic MIP intervals will not be used.

The value given by the user is the number of extra time steps that will be included at the start and end of the interval. This is done in order to leave some flexibility for later iterations.



