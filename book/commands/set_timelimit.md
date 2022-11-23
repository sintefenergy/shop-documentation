(set_timelimit)=
# set timelimit
Set the number of seconds that can be used to solve a single iteration in SHOP. Default is 900 sec.

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Setting time limits on optimization
It is possible to set an upper limit on the time used by CPLEX and OSI by giving the command:
```
set timelimit <value >
```

If command not set: A time limit of 900 s will be used

The value must be an integer and greater than zero. The value applies to most of the functions performed in CPLEX. The time limit does not include functions in SHOP as model building, updating and returning of results. If CPLEX does not find an optimal solution within the time limit for a MIP problem, SHOP will display the resulting MIP gap and continue if the solution is feasible.

The commands associated with starting and running the optimization itself will be covered in this section. Commands for using the simulator is also found here.



