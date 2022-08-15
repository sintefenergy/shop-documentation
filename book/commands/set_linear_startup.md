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

(set_linear_startup)=
# set linear_startup
Toggle the building of liner startup and shutdown costs for generators and pumps on or off when MIP is not active. Default option "/not_set" uses the linear_startup_flag on each plant to decide if startup and shutdown costs should be used

|   |   |
|---|---|
|Options|/on, /off, /not_set|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

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



