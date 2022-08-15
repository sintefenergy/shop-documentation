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

(save_shopsimseries)=
# save shopsimseries
Save detailed simulation results to the specified text file

|   |   |
|---|---|
|Options|nan|
|License|SHOP_SIMULATION|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Saving detailed simulation results
As for the optimization, detailed simulation results can be saved to either ascii or xml format with the commands:
```
save shopsimseries <filename.ascii>
save xmlshopsimseries <filename.xml>
```

Note that both commands are password protected by the simulation functionality, and saving the results as an xml file is also protected by the xml format functionality.



