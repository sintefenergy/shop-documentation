---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: 'Python 3'
  name: python3
---

(set_bid_aggregation_level)=
# set bid_aggregation_level
Set the bid aggregation level of the SHARM bidding functionality. Add all plants to the same bid group ("/system") or create individual bid groups for each plant ("/plant"). If the default option "/not_set" is used, the plants are placed in bid groups according to the bid_group attribute on the plant

|   |   |
|---|---|
|Options|/system, /plant, /not_set|
|License|SHOP_SCENARIO|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

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



