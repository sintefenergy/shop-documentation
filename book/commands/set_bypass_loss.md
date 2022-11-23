(set_bypass_loss)=
# set bypass_loss
Turn on or off (default) the addition of the flow in bypass gates when calculating tailrace loss for plants if tailrace_loss_from_bypass_flag is not used

|   |   |
|---|---|
|Options|/on, /off|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Include bypass in tailrace loss
The tailrace head loss due to water transported in bypass gates can be included by giving the command:
```
set bypass_loss /<option>
```

|<option>|Comment|
|---|---|
|on|Include bypass loss|
|off|Don’t include bypass loss|

If command not set: Don't include bypass loss.



