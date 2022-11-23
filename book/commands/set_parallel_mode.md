(set_parallel_mode)=
# set parallel_mode
Choose the parallel mode CPLEX uses when solving a problem in parallel. Default behaviour is to ensure deterministic result behaviour, the opportunistic setting lets CPLEX fully utilize the parallel processing without guaranteed reporoducability, and the automatic setting lets CPLEX decide based on the problem

|   |   |
|---|---|
|Options|/deterministic, /auto, /opportunistic|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Set parallel mode in CPLEX
It is possible to set the parallel mode in CPLEX with the command:
```
set parallel_mode /<option>
```

|<option>|Comment|
|---|---|
|deterministic|Multiple runs will reproduce the same solution|
|opportunistic|Multiple runs may produce different solutions. Less synchronization compared to deterministic|
|auto|CPLEX decides the mode|

If command not set: The deterministic option will be used



