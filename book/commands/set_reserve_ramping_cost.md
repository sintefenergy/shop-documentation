(set_reserve_ramping_cost)=
# set reserve_ramping_cost
Set the cost for ramping on the reserve capacity delivered if unit specific costs are not provided. Default value is 0 NOK/MW

|   |   |
|---|---|
|Options|nan|
|License|SHOP_RESERVE_CLUSTERING|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Reserve group ramping cost
A reserve ramping cost implemented in the reserve clustering functionality can be set by the command:
```
set reserve_ramping_cost <value>
```

If command not set: The reserve ramping cost is set to 0.0.

The cost applies to both up and down regulation.



