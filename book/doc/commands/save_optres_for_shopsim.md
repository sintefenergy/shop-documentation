## Saving optimization results for simulation purposes
The simulator in SHOP uses the optimization results as schedule for the simulation. This information is gathered by saving the optimization results to file with the command:
```
save optres_for_shopsim (/m3s) <filename.result>
```

Including the option /m3s will use the discharge results instead of the production results of the generators as schedule in the simulation.