##Fixing wrong uploading of PQ-segments
This command can be used to automatically fix wrong uploading of pq-segments. If this behaviour has been detected for one or more generators in a given iteration, the pq-curves for this plant will be built with only one segment in all timesteps and all subsequent iterations if this command is set.
```
set simple_pq_recovery /<option>
```

|<option>|Comment|
|---|---|
|on|Use simplified pq-curve if wrong uploading has been detected|

If command not set: Only warning will be given for wrong pq-uploading, no automatic fix is done.