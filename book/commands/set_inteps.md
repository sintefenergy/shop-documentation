(set_inteps)=
# set inteps
Set the numeric tolerance for accepting a number as an integer in CPLEX. The default value is 0.00001.

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Setting MIP integer tolerance
Sometimes we will get an infeasible or unbounded result from CPLEX even if the MIP model is solvable. This happens when a binary variable has gotten a value close to 0 or 1, and CPLEX has rounded it to the desired integer value. This small change will in some cases render the modified problem infeasible. By default, CPLEX considers a value integer if the absolute value difference is less than 1.0e-5. To change this, use the command:
```
set inteps <value>
```

If command not set: A value of 1.0e-5 will be used

The value set must be between 0 and 0.5.



