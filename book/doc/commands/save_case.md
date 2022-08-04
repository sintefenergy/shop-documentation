## Saving the case model data
It is possible to make a dump of the user input data to SHOP. This command is convenient for debugging purposes, and also makes it possible for a customer to dump case data for manual editing.
```
save case <filename.ascii>
```

The case file is “;” delimited for use in Excel spreadsheets. If the command is given before start sim, the case will first be saved when the first start sim is entered.