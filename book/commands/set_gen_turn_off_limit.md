(set_gen_turn_off_limit)=
# set gen_turn_off_limit
Change the limit for considering that a generator is on or off if binary variables are not used in full mode. If the production is below the specified input fraction (between 0.0 and 1.0) of the generators's minimum production, the unit is considered off in incremental iterations. The default value is 0.5 (50%).

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Generator turn off limit
To avoid running generators at low efficiency in the full mode without MIP, a turn-off limit can be set. If any generator operates below this limit, the production will be set to zero after the iteration. This limit is set by the command:
```
set gen_turn_off_limit <value>
```

If command not set: The turn-off limit will be 50% of the minimum operating level of the generator.

The value must be a decimal number between 0 and 1, which signifies how many percent of the minimum operating level of the generator the limit will be set at.  



