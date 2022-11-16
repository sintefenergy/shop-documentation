---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: 'Python 3'
  name: python3
---

(contract)=
# contract
Represents a financial market contract which allows for additional buying and selling of power outside the market

|   |   |
|---|---|
|Input connections|<a href="busbar.html">busbar</a>|
|Output connections|<a href="busbar.html">busbar</a>|
|License|SHOP_CONTRACT|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```



## Examples
  - [](ramping)
  



## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "contract"].reset_index().iloc[:, 1:]
for index, row in object_attributes.iterrows():
  object_attributes.at[index, "Attribute name"] = f"""<a href="{row['Object type']}.html#{row['Attribute name'].replace('_', '-')}">{row['Attribute name']}</a>"""
  object_attributes.at[index, "Data type"] = f"""<a href="../datatypes.html#{row['Data type'].replace('_', '-')}">{row['Data type']}</a>"""
itables.show(object_attributes,
  dom='tlip',
  search={'regex': True, "caseInsensitive": True},
  column_filters='header',
  columns=[
    {
      'name': '',
      'className': 'dt-control',
      'orderable': False,
      'data': None,
      'defaultContent': '',
    },
    {
      'name': 'Attribute name',
      'className': 'dt-body-left'
    },
    {
      'name': 'Data type',
      'className': 'dt-body-left'
    },
    {
      'name': 'I/O',
      'className': 'dt-body-left'
    },
    {
      'name': 'License',
      'className': 'dt-body-left'
    },
    {
      'name': 'Version added',
      'className': 'dt-body-left'
    },
    {
      'name': 'Description',
      'visible': False
    }
  ]
)
HTML('''<script>
$('tbody').on('click', 'td.dt-control', function () {
    var tr = $(this).closest('tr');
    var table = $(this).closest('table').DataTable();
    var row = table.row(tr);

    if (row.child.isShown()) {
        // This row is already open - close it
        row.child.hide();
        tr.removeClass('shown');
    } else {
        // Open this row
        row.child("<div align='left'>".concat(row.data()[6], "</div>")).show();
        tr.addClass('shown');
    }
});
</script>''')
```

(contract:initial_trade)=
### initial_trade
The amount of power traded on the contract right before the optimization horizon begins, only used to implement ramping constraints for the first time step. If this value is not specified (default value 1e40), no ramping constraints are built for the first time step (xUnit: MW, yUnit: MW)


(contract:trade_curve)=
### trade_curve
The trade_curve defines the size and price of the sale (negative volume) and buy (positive volume) steps of the financial contract. The X values of each XY table represents a step curve of volumes that can be traded, while the Y values defines the price for each volume step. Each XY table is valid from the specified start time until the start time of a later XY table is reached (xUnit: MW, yUnit: NOK/MWH)


(contract:min_trade)=
### min_trade
The minimum amount of power that must be traded on this contract, can be a negative number (xUnit: NO_UNIT, yUnit: MW)


(contract:max_trade)=
### max_trade
The maximum amount of power that must be traded on this contract, can be a negative number (xUnit: NO_UNIT, yUnit: MW)


(contract:ramping_up)=
### ramping_up
The limit for ramping up the power traded in the contract between time steps. The ramping up constraints are hard limits if ramping_up_penalty_cost is not specified on the contract (xUnit: NO_UNIT, yUnit: MW_HOUR)


(contract:ramping_down)=
### ramping_down
The limit for ramping down the power traded in the contract between time steps. The ramping down constraints are hard limits if ramping_down_penalty_cost is not specified on the contract (xUnit: NO_UNIT, yUnit: MW_HOUR)


(contract:ramping_up_penalty_cost)=
### ramping_up_penalty_cost
The cost of breaking the ramping up constraints (xUnit: NO_UNIT, yUnit: NOK/MW)


(contract:ramping_down_penalty_cost)=
### ramping_down_penalty_cost
The cost of breaking the ramping down constraints (xUnit: NO_UNIT, yUnit: NOK/MW)


(contract:trade)=
### trade
The total amount of power traded on the contract (xUnit: NO_UNIT, yUnit: MW)


(contract:ramping_up_penalty)=
### ramping_up_penalty
The penalty for breaking the upward ramping constraints on the contract (xUnit: NO_UNIT, yUnit: NOK)


(contract:ramping_down_penalty)=
### ramping_down_penalty
The penalty for breaking the downward ramping constraints on the contract (xUnit: NO_UNIT, yUnit: NOK)


