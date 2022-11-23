(penalty_flag)=
# penalty flag
Choose if specific constraint types should be included or excluded from the optimization model

|   |   |
|---|---|
|Options|/all, /on, /off, /load, /reservoir, /ramping, /endpoint, /discharge, /powerlimit, /plant, /min_p_con, /max_p_con, /min_q_con, /max_q_con, /schedule, /gate|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Penalty Flags
An option to include penalty functions is provided by turning on and off penalty flags with the command:
```
penalty flag /<option1> /<option2> (/<option3>)
```

|<option1>|<option2>|<option3>|Comment|
|---|---|---|---|
|all||||			
||on||Turn on all penalty flags|
||off||Turn off all penalty flags|
|on or /off||||
||reservoir|||
|||ramping|Turn on/off reservoir ramping penalty flag|
|||endpoint|Turn on/off reservoir penalty flag, including endpoint|
||load||Turn on/off load penalty flag|
||powerlimit||Turn on/off power limit penalty flag|
||discharge||Turn on/off discharge penalty flag, used to control power production|
||plant|||
|||min_p_con|Turn on/off min plant production penalty flag|
|||max_p_con|Turn on/off max plant production penalty flag|
|||min_q_con|Turn on/off min plant discharge penalty flag|
|||max_q_con|Turn on/off max plant production penalty flag|
|||schedule|Turn on/off plant schedule penalty flag|
||gate|||
|||min_q_con|Turn on/off min gate discharge penalty flag|
|||max_q_con|Turn on/off max gate production penalty flag|
|||ramping|Turn on/off gate ramping penalty flag|

If command not set: The reservoir, load, power limit and discharge penalty flags will be turned on. The plant schedule penalty flag will be turned off, while the other license protected penalty flags will be ignored.

Note that these flags will be valid for all plants, gates and reservoirs in the system. The penalty flag can also be given as a time series for each constraint. Setting the penalty flag by giving the commands has priority over the time series constraints.



