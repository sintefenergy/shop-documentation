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

(reserve_group)=
# reserve_group
Represents a group of generators and pumps that collectively serve to fulfill a reserve capacity obligation. SHOP distinguishes between eight different types of reserve capacity products: FCR-N, FCR-D, FRR, and RR in poth upward and downward directions.

|   |   |
|---|---|
|Input connections|<a href="generator.html">generator</a>, <a href="pump.html">pump</a>, <a href="market.html">market</a>|
|Output connections|<a href="generator.html">generator</a>, <a href="pump.html">pump</a>, <a href="market.html">market</a>|
|License|SHOP_RESERVE_GROUP|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```



## Examples
  - [](reserves)
  - [](reserve-example)
  

## References
  - Opportunity-cost-pricing of reserves for a simple hydropower system {cite}`Aasgard2016a`
  - Operational hydropower scheduling with post-spot distribution of reserve obligations {cite}`Kong2017`
  - Accounting for reserve capacity activation when scheduling a hydropower dominated system {cite}`Naversen2020b`
  - Operational use of marginal cost curves for hydropower plants as decision support in real-time balancing markets {cite}`Skjelbred2017a`
  - Coordinated hydropower bidding in the day-ahead and balancing market {cite}`Aasgard2019a`
  - Hydropower bidding in a multi-market setting {cite}`Aasgard2019b`
  - The value of coordinated hydropower bidding in the Nordic day-ahead and balancing market {cite}`Aasgard2022`
  

## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "reserve_group"].reset_index().iloc[:, 1:]
for index, row in object_attributes.iterrows():
  object_attributes.at[index, "Attribute name"] = f"""<a href="{row['Object type'].replace('_', '-')}.html#{row['Attribute name'].replace('_', '-')}">{row['Attribute name']}</a>"""
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

(reserve_group:fcr_n_up_obligation)=
### fcr_n_up_obligation
The obligation of FCR_N_UP that should be fulfilled by the reserve group (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_n_down_obligation)=
### fcr_n_down_obligation
The obligation of FCR_N_DOWN that should be fulfilled by the reserve group (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_d_up_obligation)=
### fcr_d_up_obligation
The obligation of FCR_D_UP that should be fulfilled by the reserve group (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_d_down_obligation)=
### fcr_d_down_obligation
The obligation of FCR_D_DOWN that should be fulfilled by the reserve group (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:frr_up_obligation)=
### frr_up_obligation
The obligation of FRR_UP that should be fulfilled by the reserve group (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:frr_down_obligation)=
### frr_down_obligation
The obligation of FRR_DOWN that should be fulfilled by the reserve group (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:rr_up_obligation)=
### rr_up_obligation
The obligation of RR_UP that should be fulfilled by the reserve group (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:rr_down_obligation)=
### rr_down_obligation
The obligation of RR_DOWN that should be fulfilled by the reserve group (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_n_penalty_cost)=
### fcr_n_penalty_cost
Given penalty cost for deviating below the FCR_N_UP or FCR_N_DOWN obligation for the reserve group (xUnit: NO_UNIT, yUnit: NOK/MW)


(reserve_group:fcr_d_penalty_cost)=
### fcr_d_penalty_cost
Given penalty cost for deviating below the FCR_D_UP obligation for the reserve group (xUnit: NO_UNIT, yUnit: NOK/MW)


(reserve_group:frr_penalty_cost)=
### frr_penalty_cost
Given penalty cost for deviating below the FRR_UP or FRR_DOWN obligation for the reserve group (xUnit: NO_UNIT, yUnit: NOK/MW)


(reserve_group:rr_penalty_cost)=
### rr_penalty_cost
Given penalty cost for deviating below the RR_UP or RR_DOWN obligation for the reserve group (xUnit: NO_UNIT, yUnit: NOK/MW)


(reserve_group:fcr_n_up_slack)=
### fcr_n_up_slack
Resulting slack when deviating above the FCR_N_UP obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_n_down_slack)=
### fcr_n_down_slack
Resulting slack when deviating above the FCR_N_DOWN obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_d_up_slack)=
### fcr_d_up_slack
Resulting slack when deviating above the FCR_D_UP obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_d_down_slack)=
### fcr_d_down_slack
Resulting slack when deviating above the FCR_D_DOWN obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:frr_up_slack)=
### frr_up_slack
Resulting slack when deviating above the FRR_UP obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:frr_down_slack)=
### frr_down_slack
Resulting slack when deviating above the FRR_DOWN obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:rr_up_slack)=
### rr_up_slack
Resulting slack when deviating above the RR_UP obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:rr_down_slack)=
### rr_down_slack
Resulting slack when deviating above the RR_DOWN obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_n_up_violation)=
### fcr_n_up_violation
Resulting penalty when deviating below the FCR_N_UP obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_n_down_violation)=
### fcr_n_down_violation
Resulting penalty when deviating below the FCR_N_DOWN obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_d_up_violation)=
### fcr_d_up_violation
Resulting penalty when deviating below the FCR_D_UP obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:fcr_d_down_violation)=
### fcr_d_down_violation
Resulting penalty when deviating below the FCR_D_DOWN obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:frr_up_violation)=
### frr_up_violation
Resulting penalty when deviating below the FRR_UP obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:frr_down_violation)=
### frr_down_violation
Resulting penalty when deviating below the FRR_DOWN obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:rr_up_violation)=
### rr_up_violation
Resulting penalty when deviating below the RR_UP obligation (xUnit: NO_UNIT, yUnit: MW)


(reserve_group:rr_down_violation)=
### rr_down_violation
Resulting penalty when deviating belown the RR_DOWN obligation (xUnit: NO_UNIT, yUnit: MW)


