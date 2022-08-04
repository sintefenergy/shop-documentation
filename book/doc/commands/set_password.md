## Setting passwords
SHOP environment variables for password protected functionalities can be set in the command file by giving the following command:
```
set password ["<Env1>=<Password1>"]
```

Please note that the environment variable and password must be enclosed by quotation marks. The password is set when the command is read, so if the password is for input data, this command must be given before the input data is read. There is no limit on the number of passwords that can be read on one line. The set password command can also be given several times in the command file, and can be used to both activate and deactivate an environment variable. The environment variable is deactivated if an incorrect password is given.

A summary of SHOP environment variables will be printed in the log file. Note that setting SHOP environment variables in the command file will only have effect on the current SHOP run.