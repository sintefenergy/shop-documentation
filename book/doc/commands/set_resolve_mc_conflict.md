## Resolve conflicting restrictions
Conflicting restrictions can also be handled when printing marginal cost curves before running SHOP. The command below should be set before the command [](print_mc_curves).
```
set resolve_mc_conflict /<option>
```

|<option>|Comment|
|---|---|
|on|Conflicting restrictions will be resolved|
|off|No testing for possible conflicts between given restrictions|

If command not set: No testing for possible conflicts between given restrictions will be done