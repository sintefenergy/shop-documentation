(read_model)=
# read model
Read in the first ascii model file with the specified name which must include the start time, end time, and time resolution of the optimization run

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Reading the system model
The system model is read from multiple text files. It is possible to store all the information in a single file, but this easily leads to large and disorganized files. It is good practice to organize the system input into several files, as this will make finding mistakes and making changes to the model more manageable. For instance, separating the time varying data, market information and system load from the topology of the system is a good idea. It is a requirement that the system topology is read before the variable data of a water course.

There are two commands used for reading in system data from file. To read in the very first system file, the command:
```
read model <filename.ascii>
```
must be used. It is required that the data structure "OPTIMIZATION time" is defined in this file, which sets the optimization period and time resolution.

Additional data files must be read using the command:
```
add model <filename.ascii>
```



