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

(market)=
# market
The representation of an electricity market, usually the day-ahead energy market. It is also possible to define a reserve capacity market by connecting the market object to a reserve_group object. Only generators and pumps connected to the reserve_group will participate in the reserve market, and the reserve obligation in the reserve_group serves as market 'load'

|   |   |
|---|---|
|Input connections|<a href="reserve_group.html">reserve_group</a>, <a href="busbar.html">busbar</a>|
|Output connections|<a href="reserve_group.html">reserve_group</a>, <a href="busbar.html">busbar</a>|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```







## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "market"].reset_index().iloc[:, 1:]
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

(market:prod_area)=
### prod_area
Definition of which production area this market belongs to. All the plants with corresponding prod_area will sell their production to markets in this area. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(market:market_type)=
### market_type
String defining the product that is sold in this market. Allowed values are ENERGY, FCR_N_UP, FCR_N_DOWN, FCR_D_UP, FCR_D_DOWN (from version 14.2.0.0), FRR_UP, FRR_DOWN, RR_UP, and RR_DOWN. If this value is not given default market type is ENERGY. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(market:load)=
### load
Fixed demand that must be delivered to this market. This comes in addition to any power sold to the market. (xUnit: NO_UNIT, yUnit: MW)


(market:max_buy)=
### max_buy
The maximum power that can be bought from the market (xUnit: NO_UNIT, yUnit: MW)


(market:max_sale)=
### max_sale
The maximum power that can be sold to the market (xUnit: NO_UNIT, yUnit: MW)


(market:buy_price)=
### buy_price
Price for buying power from this market (xUnit: NO_UNIT, yUnit: NOK/MWH)


(market:sale_price)=
### sale_price
Price for selling power to this market (xUnit: NO_UNIT, yUnit: NOK/MWH)


(market:buy_delta)=
### buy_delta
A (small) amount that will be added to the buy price in this market (xUnit: NO_UNIT, yUnit: NOK/MWH)


(market:sale_delta)=
### sale_delta
A (small) amount that will be subtracted from the sale price in this market (xUnit: NO_UNIT, yUnit: NOK/MWH)


(market:bid_flag)=
### bid_flag
Flag determining the time steps that should be included in the bid matrix (xUnit: NO_UNIT, yUnit: NO_UNIT)


(market:common_scenario)=
### common_scenario
Definition of non-anticipativity constraints for each market. The amount traded in the market must be the same for all scenarios and time steps where common_scenario is equal. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(market:buy)=
### buy
Resulting power bought from this market. (xUnit: NO_UNIT, yUnit: MW)


(market:sale)=
### sale
Resulting power sold to this market. (xUnit: NO_UNIT, yUnit: MW)


(market:sim_sale)=
### sim_sale
Simulated power sold to this market. (xUnit: NO_UNIT, yUnit: MW)


(market:reserve_obligation_penalty)=
### reserve_obligation_penalty
Resulting penalty when the reserve obligation is violated (xUnit: NO_UNIT, yUnit: MW)


(market:load_penalty)=
### load_penalty
Resulting penalty when the load obligation is violated (xUnit: NO_UNIT, yUnit: MW)


