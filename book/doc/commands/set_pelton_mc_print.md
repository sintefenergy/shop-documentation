## Printing pelton MC curves
```
set pelton_mc_print /<option>
```

|<option>|Comment|
|---|---|
|on|Print all marginal cost data for Pelton turbines|
|off|Only write PQ data for Pelton turbines|

If command not set: Don't print marginal cost data for Pelton turbines

Turning off the use of the user defined reference production for Pelton turbines can be done with [](set_mc_ref_prod).