## Save reservoir storage to file
It is possible to save the reservoir storage for the last but one time step for all the reservoirs to a file. The format of the file is such that it can be used as the starting or initial reservoir for a new run.
```
save rsv_storage (<filename.ascii>)
```

If no filename is given by the user, the file will be saved with the default filename "2ndLast_rsv_res_Mm3" without any file extension.