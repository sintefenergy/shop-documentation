## Expand window command
Sometimes when using the dependant water value (cut water value description), the windows of valid end reservoir implicit in the cut description turns out to be too small to allow a valid solution to be found. For use in such cases, we have introduced a command that expands the valid end reservoir window to contain the entire reservoir. The command must be given after the water value information is read, otherwise the command results in a warning, and is otherwise ignored.

|Command|Description|
|---|---|
|`expand window /all`|Expand windows for all reservoirs|
|`expand window [<reservoir_names>]`|Expand window for the listed reservoirs|

Note that a missing argument list does not default to /all. The command `expand window [empty]` results in a warning in the log file, but is otherwise ignored. Any unknown reservoir names in the list results in a warning, and is otherwise ignored.