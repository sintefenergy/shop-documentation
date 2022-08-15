---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: 'Python 3'
  name: python3
---

(set_time_delay_unit)=
# set time_delay_unit
Set the time unit used to specify the time delay of discharge from gates, plants, etc. Can be either "HOUR", "MINUTE", or "TIME_STEP_LENGTH", where the last option is default and uses the time unit of the optimization run

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

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



