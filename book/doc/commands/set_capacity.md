## Setting gate capacity
The capacities of gates, bypasses and spills have default values in SHOP that can be changed with the command:
```
set capacity /<option> <value>
```

|<option>|Comment|
|---|---|
|all|Set capacity of all gate types|
|gate|Set regular gate capacity|
|bypass|Set bypass gate capacity|
|spill|Set spill gate capacity|

If command not set: Default values according to the table below will be used:

|Gate type|Max capacity|Unit|
|---|---|---|
|Regular gates|100|m3/s|
|Bypass gates|30|m3/s|
|pill gates|200|m3/s|