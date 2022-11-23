(set_mipgap)=
# set mipgap
Set the MIP gap that will be used by the solver to decide when a MIP problem is sufficiently close to optimum. An absolute MIP gap is the absolute value difference of the best integer and relaxed solution, while a relative MIP gap is the relative objective value difference and should be a number between 0 and 1

|   |   |
|---|---|
|Options|/absolute, /relative|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Setting MIP gap tolerance
MIP models will under some conditions find a near optimal solution very fast and then spend a lot of time verifying the solution. The condition that defines an acceptable solution is the relative or absolute difference between the best MIP solution and the estimate of the best achievable solution.

To set the size of the gap, use the command:
```
set mipgap /<option> <value>
```

|<option>|Comment|
|---|---|
|ABSOLUTE|MIP gap in absolute value (value in currency)|
|RELATIVE|MIP gap in percent (value between 0 and 1)|

If command not set: MIP gap in percent with a value of 1.0e-4 will be used.

Adjusting the MIP gap can result in faster solutions in some cases, but may give an unnecessarily poor integer solution in others. This functionality is only available when using CPLEX and OSI, and OSI only handles absolute MIP gaps.



