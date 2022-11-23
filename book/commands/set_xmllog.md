(set_xmllog)=
# set xmllog
Turn on or off (default) the writing the log in an xml format to the file "shop_log.xml".

|   |   |
|---|---|
|Options|/on, /off|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Changing log file format
To write the log file on xml format, use the command:
```
set xmllog /<option>
```

|<option>|Comment|
|---|---|
|on|Start writing to shop_log.xml|
|off|Stop writing to shop_log.xml, and switch back to shop.log|

Note that start and end xml tags will be written each time the command is given. The `set xmllog /on` command should only be used once. If everything should be written to the xml log, it is not necessary to give the `set xmllog /off` command. Typically the `set xmllog /on` command should be given as the first command in the command file.

The change of log format can also be given as the command line option –xmllog.



