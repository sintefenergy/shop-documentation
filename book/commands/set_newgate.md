(set_newgate)=
# set newgate
Deprecated

|   |   |
|---|---|
|Options|/on, /off|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## New gate format
The new gate format can be used if the command set newgate is given. For the command to be in effect, it must be given before the gates are read.
```
set newgate /<option>
```

|<option>|Comment|
|---|---|
|on|Use the new format|
|off|Use the old format|

If command not set: The old gate format will be used.

The command line option -newgate can also be used to set the new gate format.



