## Marginal cost curve segmentation
The segmentation of the marginal cost curves can be set by the following command:
```
set mc_nseg /<option> <value>
```

|<option>|Comment|
|---|---|
|up|Set the number of points above best point|
|down|Set the number of points below best point|
|all|Set the number of points above and below best point|

If the command is not set: If segmentation has been set for the PQ curves with a TXY table or the "set nseg" command, the same number of points will be used for the mc curves. If not, 3 points are used up and down.