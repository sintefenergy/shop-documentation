(set_mip_nseg)=
# set mip_nseg
Set the number of PQ curve segments to be used above, below, or above and below the last production level in full iterations if plant specific values are not given. Default value is 3 segments up and down.

|   |   |
|---|---|
|Options|/up, /down, /all|
|License|SHOP_EBL_PLANT|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Changing the PQ curve segmentation
The relationship between discharge (Q) and electric power output (P) from a generating unit (or power consumed by a pumping unit) is a nonlinear and nonconvex function. It depends on both the net head and the turbine/generator efficiency. In addition, the turbine efficiency is a nonlinear function of the net head and the water discharge. In SHOP, this function is approximated as a piecewise linear function to incorporate it into the mixed integer linear programming (MILP) framework of the optimization problem. This piecewise linear function is called as PQ curve.

The PQ curve for each unit is default built as default 6 linear pieces (also known as “segment”) with 7 breakpoints: 3 above the old working point, 3 below, and 1 local just around the working point from last iteration (In the first iteration, the best efficiency point is chosen as the middle point). The following commands modify the values used for number of segments above and below the working point.

### Segmentation in the MIP model
```
set mip_nseg /<option> <value>
```

|<option>|Comment|
|---|---|
|up|Set number of points above working point|
|down|Set number of points below working point|
|all|Set number of points above and below working point|

If command is not set: 3 points above and 3 points below working point is used.

### Segmentation in incremental mode
```
set nseg /<option> <value>
```

|<option>|Comment|
|---|---|
|up|Set number of points above working point|
|down|Set number of points below working point|
|all|Set number of points above and below working point|

If command is not set: 3 points above and 3 points below working point is used.

### Dynamic segmentation
The segmentation can also be done dynamically. This means the resolution close to the working point from the previous iteration will be refined. The idea behind this is to save calculation time by not calculating many irrelevant points.
```
set dyn_seg /<option>
```

|<option>|Comment|
|incr|Dynamic segmentation in the incremental mode|
|mip|Dynamic segmentation in the MIP model|
|on|Dynamic segmentation in both the incremental and MIP model|

The dynamic segmentation can also be controlled at plant level by input to SHOP, see [](plant)].



