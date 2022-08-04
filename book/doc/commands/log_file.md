## Changing the log file names
This command changes the name of the log files. The default name of the program execution log is "shop.log" and contains all run time and diagnose information. The /lp option changes the name of the optimization log file, that is the internal log file in the optimization package. If only the log file command is used, the optimization log file is suppressed.  Maximum length of the log file name is 40 characters.
```
log file <filename.log> (/lp)
```

If command is not set, "shop.log" will be used as the log filename.

The change of log filename can also be given as the command line option –logfile <filename.log>.