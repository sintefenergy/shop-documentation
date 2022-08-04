## Use plant-based uploading outside MIP-period
This command uses marginal efficiency to predefine an upload sequence for generators at a plant. This sequence is used in timesteps without MIP-flag set on the plant to ensure that generators have different efficiencies. This normally reduces the frequency of production below p_min without MIP.
```
set plant_uploading /<option>
```

|<option>|Comment|
|---|---|
|lp|Use plant-based uploading in the lp (non-MIP) timesteps|

If command not set: No upload sequence is calculated or applied.