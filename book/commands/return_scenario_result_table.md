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

(return_scenario_result_table)=
# return scenario_result_table
Write the SHOP results from a stochastic optimization run to the specified file in a text file format

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Save stochastic results (SHARM functionality)
If a stochastic SHOP run is to be saved, use the command:
```
return scenario_result_table <filename.ascii>
```

This saves the system results for all scenarios to the same file. This is only useful to participants in the SHARM project(s), since regular SHOP runs only use one scenario.



