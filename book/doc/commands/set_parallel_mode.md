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