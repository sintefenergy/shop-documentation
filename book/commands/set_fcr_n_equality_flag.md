(set_fcr_n_equality_flag)=
# set fcr_n_equality_flag
Turn on or off (default) the building of constraints to force the fcr_n delivery for all units to by symmetric

|   |   |
|---|---|
|Options|/on, /off|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Equality requirement on FCR_N_UP and FCR_N_DOWN
If one wants to activate the equality requirement on FCR_N_UP and FCR_N_DOWN, the following command should be used:
```
set fcr_n_equality_flag /<option>
```

|<option>|Comment|
|---|---|
|on|Turn on FCR-N equality requirement|
|off|Turn off FCR-N equality requirement|

If command not set: The equality requirement is not activated



