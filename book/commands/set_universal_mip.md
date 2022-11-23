(set_universal_mip)=
# set universal_mip
Turn on or off all binary variables related to unit commitment and reserve capacity procurement. If the default option of not_set is used, the mip_flag on each plant will decide when binary varaible requirements are used

|   |   |
|---|---|
|Options|/on, /off, /not_set|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Turning on and off MIP
The MIP flag set in the model can be overridden with the command:
```
set universal_mip /<option>
```

|<option>|Comment|
|---|---|
|on|Turn on MIP in all hours|
|off|Turn off MIP in all hours|
|not_set|Turn on and off MIP according to MIP flags|

If command not set: MIP will be controlled by the MIP flags set in the model.

Note that the command does not overwrite the MIP flags, so giving the command set universal_mip /not_set will undo the override of the two other command options.



