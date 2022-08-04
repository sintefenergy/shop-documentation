## Reserve group penalty cost
To set the general penalty cost for all reserve types found in the reserve group functionality, use the command:
```
set reserve_penalty_cost <value>
```

If command not set: The default value of 10000.0 will be used.

Note that it is possible to set time dependent penalty costs for each reserve type in each reserve group, and that doing so will override the general penalty cost set by this command for that specific reserve type and group.