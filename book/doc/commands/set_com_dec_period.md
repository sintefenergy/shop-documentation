## Common decision end time (SHARM functionality)
To force production to be equal in scenarios with different inflow, use the command:
```
set com_dec_period <value>
```

If command not set: No common production decisions will be enforced

The value is the last time step where common production decisions will be enforced. This is only useful to participants in the SHARM project(s), since regular SHOP runs only use one scenario.