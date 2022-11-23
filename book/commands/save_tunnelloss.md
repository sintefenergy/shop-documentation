(save_tunnelloss)=
# save tunnelloss
Enables the printing of the junction tunnel head loss to the result files written by the "save series" and "save xmlseries" commands. Default behaviour is to not print the tunnel head loss.

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Printing tunnel loss in results
To save the loss in each tunnel in junctions and junction gates, use the command:
```
save tunnelloss
```

This will write the loss to the result file when results are saved with either the command save series or save xmlseries after an optimization, or save xmlshopsimseries after a simulation.



