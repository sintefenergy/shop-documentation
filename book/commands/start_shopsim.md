(start_shopsim)=
# start shopsim
Start the SHOP simulator 

|   |   |
|---|---|
|Options|/inflow, /gen_mw_schedule, /gen_m3s_schedule, /gen_mw_result, /gen_m3s_result, /plant_mw, /plant_m3s, /optimize|
|License|SHOP_SIMULATION|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Start a simulation
Before starting a simulation, the optimization results that have been saved to file with the save optres_for_shopsim command must be loaded into SHOP with the add model command. A simulation can then be started with the command:
```
start shopsim
```



