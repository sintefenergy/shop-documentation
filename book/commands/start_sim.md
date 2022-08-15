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

(start_sim)=
# start sim
Start the specified number of SHOP optimization iterations in the mode given by the "set code" command

|   |   |
|---|---|
|Options|/start, /end, /nosolve|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Starting Optimization
After the preparatory work is done, the optimization procedure is started with the command:
```
start sim <value>
```

The value signifies how many iterations in the current model (full or incremental) should be performed, and must be an integer larger than zero. It is possible to split the iterations between several start sim commands in order to change model parameters between iterations.



