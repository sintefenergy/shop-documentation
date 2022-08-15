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

(return_simres)=
# return simres
Write simplified SHOP results to the specified file in a text file format, the "/generator" option will include unit results in the file

|   |   |
|---|---|
|Options|/gen|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Saving basic optimization results
Basic [](reservoir), [](gate), [](plant) and [](market) results from the optimization may be saved to file with the command:
```
return simres (/generator) <filename.result>
```

Only plant information with the power production and discharge for individual units will be printed when using the /generator option.



