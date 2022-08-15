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

(set_plant_uploading)=
# set plant_uploading
Deprecated

|   |   |
|---|---|
|Options|/lp|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Use plant-based uploading outside MIP-period
This command uses marginal efficiency to predefine an upload sequence for generators at a plant. This sequence is used in timesteps without MIP-flag set on the plant to ensure that generators have different efficiencies. This normally reduces the frequency of production below p_min without MIP.
```
set plant_uploading /<option>
```

|<option>|Comment|
|---|---|
|lp|Use plant-based uploading in the lp (non-MIP) timesteps|

If command not set: No upload sequence is calculated or applied.



