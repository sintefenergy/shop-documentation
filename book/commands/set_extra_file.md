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

(set_extra_file)=
# set extra_file
Specify the name of the extra ascii model file that is used when running SHOP through the SIM interface.

|   |   |
|---|---|
|Options|nan|
|License|SHOP_EXTRA_DATA|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Changing the name of the extra_data file
To change the name of the extra_data file, use the command:
```
set extra_file <filename.ascii>
```

The default filename is "extra_data.ascii".

The command must be given before simulation starts.



