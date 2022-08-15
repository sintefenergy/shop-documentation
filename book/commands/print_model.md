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

(print_model)=
# print model
Print out the LP model with the specified name after the next iteration is done

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Printing the optimization model
There is a command for printing the optimization problem passed over to the LP solver. The format of the problem is in a standard LP formulation which can be read into the standalone version of the solver. The option is useful for debugging and for testing other optimization algorithms and parameter options.
```
print model <filename.lp>
```

The command will only print the LP problem solved in the very next iteration, so the command cannot be given after the last start sim command.



