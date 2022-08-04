## Marginal cost curves for Pelton turbines
Pelton turbines can be set to be ignored (treated as on maintenance) in marginal cost calculations with the command:
```
set mc_pelton /<option>
```

|<option>|Comment|
|---|---|
|on|Include Pelton turbines in marginal cost calculations|
|off|Exclude Pelton turbines in marginal cost calculations|

If command not set: All Pelton turbines are included in marginal cost calculations.

Even if the Pelton turbine is included in marginal cost calculations, only the PQ data will be printed out when using print mc_curves. To change this, use command [](set_pelton_mc_print).