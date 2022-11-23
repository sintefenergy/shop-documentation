(print_pqcurves)=
# print pqcurves
Print out the PQ curves constructed by SHOP to the specified file name in xml format. The different options will write either the original PQ curves based on the input data, the PQ curves after convexification, the finalized PQ curves used in the optimization, or all of the mentioned cases. If a file name is not specified, a default file name starting with "pq_curves_" and ending with the current iteration number will be used.

|   |   |
|---|---|
|Options|/all, /original, /convex, /final|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Print PQ curves
The PQ curves can be written on xml format for each unit at each time step for each iteration.
```
print pqcurves /<option> (<filename.xml>)
```

The command will only print the PQ curve in the very next iteration, so the command cannot be given after the last start sim command.

If no filename is given by the user, the file will be saved with the default file "pq_curves_full_mode_iter1.xml" where the mode and the iteration number depend on the very next iteration.

Note that if a unit is under maintenance or committed not to run, it will not be taken into account in the optimization and hence no PQ curve can be printed out. In the incremental mode, only the committed units from full mode will be considered in the optimization and hence only PQ curve for those units will be printed out.

|<option>|Comment|
|---|---|
|all|Print all three types of PQ curves|
|original|Print PQ curves calculated based on given generator- and turbine efficiency curves|
|convex|Print PQ curves after convexification|
|final|Print PQ curves after extending to Q=0|

Three types of PQ curves can be printed out:
- **Original** PQ curve refers to the one calculated based on given generator- and turbine efficiency curves.
- **Convex** PQ curve refers to the one after convexification. That is, nonconcave breakpoints are removed and the slope of each segment  is non-increasing.
- **Final** PQ curve refers to the one that the first point of PQ curve is extended to Q=0. In the full mode, if mip_flag is given, binary variable for each unit is introduced to indicate the on/off status of the unit. The first segment of PQ curve is extended to Q=0. If mip_flag is not given, to avoid mis-uploading of PQ segments we choose the best-efficiency point (the point has the maximum value of ) and extend to the point (0, 0). In the incremental mode, since only the units that are already committed to run will be built, no binary variables are needed. The first segment of PQ curve is extended to Q=0.

Note that how many points of the PQ curves will be printed out relies on how the PQ curves are built. See for details. If the user chooses to build PQ curve including all the limits, i.e. set build_pq_curve /all_limits, and there is production schedule or discharge schedule on the unit, only one point referring to the schedule will be given. Otherwise, the number of points of the PQ curves depend on the number of segments defined by the user and default number is 7.



