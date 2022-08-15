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

(set_mix_cut_vv)=
# set mix_cut_vv
Deprecated

|   |   |
|---|---|
|Options|nan|
|License|SHOP_MIX_CUT_VV_PROTOTYPE|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Mixing cuts and independent water values
It is possible to allow some reservoirs to have water value defined by cuts and others to be defined by independent water values in the same SHOP run. This can be controlled with the command:
```
set mix_cut_vv /<option>
```

|<option>|Comment|
|---|---|
|on|Allow mixed water value description|
|off|Don’t allow mixed water value description|

If command not set: Don’t allow mixed water value description.



