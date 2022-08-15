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

(save_case)=
# save case
Writes the input of the current SHOP model to an ascii file with the specified name.

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Saving the case model data
It is possible to make a dump of the user input data to SHOP. This command is convenient for debugging purposes, and also makes it possible for a customer to dump case data for manual editing.
```
save case <filename.ascii>
```

The case file is “;” delimited for use in Excel spreadsheets. If the command is given before start sim, the case will first be saved when the first start sim is entered.



