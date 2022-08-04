## Setting time delay unit
The unit for the time delay given in the plant and gate attributes can be set by the command:
```
set time_delay_unit <unit>
```

|<unit>|Comment|
|---|---|
|HOUR|Time delay in hours|
|MINUTE|Time delay in minutes|
|TIME_STEP_LENGTH|Time delay in multiple of interval length|

If command not set: The time delay is interpreted as a multiple of the interval length

The same unit is used for all plants and all gates.