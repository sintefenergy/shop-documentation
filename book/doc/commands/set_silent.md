## The silent command
The silent command can be used to let the output that usually goes to standard out be written to the file "shop_run.log":
```
set silent /<option>
```

|<option>|Comment|
|---|---|
|on|Output to shop_run.log|
|off|Output to standard out|

If command not set: Output to standard out

It is possible to use the silent command several times in the command file to turn on and turn off messages to screen. The silent command can also be given as the command line option -silent when starting SHOP.