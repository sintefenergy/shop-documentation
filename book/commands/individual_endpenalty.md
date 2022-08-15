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

(individual_endpenalty)=
# individual endpenalty
Deprecated

|   |   |
|---|---|
|Options|/up, /down|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Individual reservoir penalties
It is also possible to set reservoir penalties and endpoint penalties separately for each reservoir. The values of the different penalty costs are printed in the log file.

The following command is used:
```
individual penalty <reservoir_name> <value>
individual endpenalty <reservoir_name> <value> /<option>
```

|<option>|Comment|
|---|---|
|up|Reservoir end penalty up|
|down|Reservoir end penalty down|

The unit of the endpoint penalty is NOK/Mm3, while the reservoir penalty is given in NOK/MWh.

The end penalty values should usually be the same or lower than the reservoir penalties to ensure that the most logical penalty variables are used. The penalty should usually be much larger than any reasonable price given by that relation.



