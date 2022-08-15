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

(penalty_cost)=
# penalty cost
Change various global penalty costs

|   |   |
|---|---|
|Options|/reservoir, /endpoint, /ramping, /load, /overflow, /overflow_time_adjust, /gate, /discharge, /all, /powerlimit, /reserve, /soft_p_penalty, /soft_q_penalty, /plant|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Penalty Costs
The cost of each penalty variable can be changed with the command:
```
penalty cost /<option1> (/<option2>) <value>
```

|<option1>|<option2>|Comment|
|---|---|---|
|all||Set all penalty costs|
|reservoir|||
||ramping|Set reservoir ramping penalty cost|
||endpoint|Set reservoir penalty cost, including endpoint|
|gate|||
||ramping|Set gate ramping penalty cost|
|load||Set load penalty cost|
|powerlimit||Set power limit penalty cost|
|discharge||Set production penalty cost, name confusion due to historical reasons|
|overflow||Set overflow penalty cost|
|overflow_time_adjust||Set overflow time adjustment factor|
|reserve||Set reserve penalty cost|
|soft_p_penalty||Set all plant production penalty costs|
|soft_q_penalty||Set all plant and gate discharge penalty costs|

If command not set: Penalty values according to the table below will be used.

|Penalty|Cost|Unit|
|---|---|---|
|Reservoir ramping penalty|100|NOK/Mm3|
|Reservoir penalty|10000000|NOK/Mm3|
|Gate ramping penalty|360|NOK/(h∙m3/s)|
|Load penalty|5000|NOK/MWh|
|Power limit penalty|10∙load penalty (=50000)|NOK/MWh|
|Production penalty (/discharge)|100|NOK/MWh|
|Overflow penalty|50000|NOK/Mm3|
|Overflow time adjustment|-1.0e-6|NOK/(Mm3∙h)|
|Reserve penalty|1000|NOK/MWh|
|Soft production penalty|100|NOK/MWh|
|Soft discharge penalty|100000|NOK/Mm3|

The default penalty costs can be seen in the table above. The values are referred to as the number of basis units in the currency used in SHOP, not necessarily NOK as listed in the table above. The reservoir endpoint values are also the one used for the reservoirs penalties, if no individual values are given.

The overflow_time_adjust requires a bit more explanation. Its purpose is to give an incentive to delay overflow towards the end of the optimization period. For a given time step, this value is multiplied by the number of hours since the start of optimization and added to the overflow cost. The default value may be too small in some cases, especially if head optimization gives strong incentives to fill up buffer reservoirs.



