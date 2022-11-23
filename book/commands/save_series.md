(save_series)=
# save series
Write the SHOP results to the specified file in a text file format

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Saving detailed optimization results
Detailed optimization results of the system can be saved to either an ascii or xml file using these commands:
```
save series <filename.ascii>
save xmlseries <filename.xml>
```

This is the most common way to save optimization results in SHOP. Note that only the save xmlseries command is password protected by the xml format functionality.

### Related commands
- [](set_xml_system_name)



