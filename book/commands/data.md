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

(data)=
# data
Deprecated. Old way of streaming inn and out data to SHOP when running as an executable.

|   |   |
|---|---|
|Options|nan|
|License|SHOP_STREAMING|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Streaming of data
Data can be streamed through SHOP. The following commands are used to start and stop data streaming, respectively:
```
DATA
/DATA
```

Using these commands, data input can be streamed to SHOP, and the result series are streamed from SHOP, with the –silent option suppressing other output.



