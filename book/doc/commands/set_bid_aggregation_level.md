## Choosing the bid aggregation level in SHARM
One of the requirements for using the bidding functionality in SHARM is to place the plants participating in the bidding into bid groups. This can be done by setting bid_group flags for each plant in the model files, or with the command:
```
set bid_aggregation_level /<option>
```

|<option>|Comment|
|---|---|
|system|Every plant is placed in the same bid group|
|plant|Every plant is placed in its own bid group|
|not_set|The bid_group flags set in the model are used to define the bid groups|

If command not set: The bid_group flags defined in the model files are used to create the bid groups

SHOP currently supports 3 different LP solvers: CPLEX, GUROBI and OSI. CPLEX and GUROBI are commercial solvers that require a license, while OSI is open source. It is possible to change some of the default values in the LP solver through commands in SHOP. CPLEX is the standard solver in SHOP, and most of the commands listed in this section only work with CPLEX.