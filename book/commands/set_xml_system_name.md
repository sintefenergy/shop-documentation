(set_xml_system_name)=
# set xml_system_name
Turn on or off (default) the insertion of the system name defined in the extra data files into the result xml file created by the "save xmlseries" command. Only has an effect when running through the SIM interface with extra data files.

|   |   |
|---|---|
|Options|/on, /off|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Adding system name to filename on xml format
To add the system name to the filenames created by save xmlseries, use the command:
```
set xml_system_name /<option>
```

|<option>|Comment|
|---|---|
|on|Add system name on xml format|
|off|Don’t add system name on xml format|

If command not set: Don’t add system name on xml format

This command only works when using extra_data files.



