## Merging time steps with similar behaviour
Hours with similar discharge or production can be merged together into blocks in order to save computation time. This is done by the command:
```
Command: set merge /<option>
```

|<option>|Comment|
|---|---|
|on|Merge similar hours into blocks|
|off|Don’t merge similar hours, discard all previously merged blocks|
|stop|Keep previously merged blocks and stop further merging|

If command not set: Don’t merge similar hours.

The tolerance for merging hours can be set by a TXY table, see the block merge functionality documentation.