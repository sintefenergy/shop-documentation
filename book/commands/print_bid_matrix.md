(print_bid_matrix)=
# print bid_matrix
Print out the bid matrix for each bid_group in the system when using the SHARM bidding functionality. If the option "/system" or "/plant" is used, the bid matrices on system or plant level will be printed out instead

|   |   |
|---|---|
|Options|/system, /plant|
|License|SHOP_SCENARIO|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## Printing bidding results from SHARM
To save the results from a SHARM run with bidding, the two commands below can be used. See the bidding documentation for further information.

### Printing and reducing the bid matrix
To print out the bid matrices made from a SHARM run, use the command:
```
Command: print bid_matrix (/option) (<value>)
```

|<option>|Comment|
|---|---|
|system|Print out the bid matrix for the sum of all plants to the file "system_bid_matrix.txt"|
|plant|Print out the bid matrix for every plant to the files "<plant_name>_bid_matrix.txt"|

If no option is given, the bid matrix for every bid_group defined in the system will be printed out. Note that one may print out the system or plant bid matrix regardless of the bid_aggregation_level used. The bid matrix may contain several hundred price columns, so a reduction algorithm is applied to reduce the bid matrix down to a smaller size. If either the option /system or /plant is used, the reduction will be carried out on the sum of all bid_groups present in the model. The prices found in this reduction will be used to create the system or plant matrices. If no option is given, each bid_group will be reduced separately. Both the reduced and the original bid matrices will be printed out, where the original bid matrix file name will have the prefix "unreduced_". The optional value is the number of price columns that should be present in the reduced matrix. If no value is given, the default value of 64 is used.

### Printing an interpolated bid matrix
In the "print bid_matrix" command, the price columns present in the reduced bid matrix are chosen based on a reduction algorithm. It is also possible to print out a bid matrix based on user specified prices with the command:
```
interpolate bid_matrix [<values>]
```

The list of values are the prices that will be used as price columns in the bid matrix. The bid values for these prices are calculated by interpolating the bids from the original bid matrix.



