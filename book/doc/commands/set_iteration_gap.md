## Setting the iteration gap tolerance
It is possible to stop the remaining iterations set by start sim if the optimal solution of two consecutive iterations has already converged. The solutions are said to converge if either the relative or absolute difference in their objective function values is smaller than a user defined value, which can be set by the command:
```
set iteration_gap /<option> (<value>)
```

|<option>|Comment|
|---|---|
|RELATIVE|Relative iteration gap (value between 0 and 1)|
|ABSOLUTE|Absolute iteration gap (value in currency)|

If no value is given, the gap will be set to 1.0e-6 if the gap is relative and 20 if the gap is absolute. This check of convergence will start from the first iteration in full mode if head optimization is off, and from the third iteration if it is on. In the incremental mode, the check starts from the second iteration independent of head optimization.