(save_optbasis)=
# save optbasis
Specify the name of the file containing a saved input basis for the optimization problem. If no name is given, no input basis will be loaded

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Using optimal basis
If subsequent fairly equal models are solved, it is advantageous to reuse information from the previous optimal solution. This can be done by storing the optimal basis from the previous solution and loading it into SHOP and using it when calculating optimal solution to the existing case.

The same method can be used between iterations, but the improvement is not big enough to justify the use of the commands in this case. Such use is not recommended.

### Writing optimal basis to file
```
save optbasis <filename.ascii>
```

The basis is saved after the next time the model is solved. If we want the optimal basis from later iterations, we need to re-enter the command (The feature is in probably useful for the first full iteration only).

### Loading optimal basis from file
```
read optbasis <filename.ascii>
```

A filename to a valid basis file must be applied. The basis is read next time the model is solved. If we want to read start basis for later iteration we need to re-enter the command. (The feature is probably useful for the first full iteration only)

### Control the use of optimal basis
A heuristic for choosing which variables to build a start basis from is also provided. This is done with the command:
```
set optbasis /<option>
```



