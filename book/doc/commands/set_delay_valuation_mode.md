## Water in transition value
When the value of water in transition is calculated, the first point on the water value curve is used. If the water value does not depend on reservoir level, there is only this one point. However, if it is not independent of reservoir level, the first point is the water value when the reservoir is empty. To instead use the middle point on the water value curve, use the command: 
```
set delay_valuation_mode /<option>
```

|<option>|Comment|
|---|---|
|default|Use first water value point to value water in transition|
|middle|Use middle water value point to value water in transition|

If command not set: Use the first point of the water value description to value water in transition