## Reserve group slack cost
The reserve group slack cost can be changed with the command:
```
set reserve_slack_cost <value>
```

If command not set: The slack cost will be set to 1.0e-6 NOK/MWh.

This slack cost is applied if there is too much reserve power allocated, and so the default cost is not set very high. A much harsher penalty cost is used if there is too little reserve power present.  