(return_shopsimres)=
# return shopsimres
Write simplified SHOP simulation results to the specified file in a text file format, the "/generator" option will only write unit results in the file

|   |   |
|---|---|
|Options|/generator|
|License|SHOP_SIMULATION|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Saving basic simulation results
Simplified simulation results of plants, gates and reservoirs can be saved with the command:
```
return shopsimres (/generator) <filename.result>
```

Only [](plant) information with the power production and discharge for individual units will be printed when using the /generator option.

This command will terminate execution of SHOP:
```
quit
```



