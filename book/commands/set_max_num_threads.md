(set_max_num_threads)=
# set max_num_threads
Set the max number of threads CPLEX can use when solving a MIP problem or using the barrier solver. Default of -1 lets CPLEX use all available threads

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Set maximum number of threads in CPLEX
It is possible to set the maximum number of threads used in CPLEX with the command:
```
set max_num_threads <value>
```

If command not set: Maximum threads available will be used



