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

(scenario)=
# scenario
The scenario object is used to define a scenario tree when running the stochastic version of SHOP (SHARM). A single scenario called 'S1' is always created in SHOP, and only N-1 new scenarios should be created when running SHARM.

|   |   |
|---|---|
|Input connections||
|Output connections||
|License|SHOP_SCENARIO_FUNCTIONALITY|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```



## Examples
  - [](multiple-price-bid-matrix)
  

## References
  - Applying successive linear programming for stochastic short-term hydropower optimization {cite}`Belsnes2016`
  - Progressive hedging for stochastic programs with cross-scenario inequality constraints {cite}`Aasgard2020`
  - Evaluating a stochastic-programming-based bidding model for a multireservoir system {cite}`Aasgard2014`
  - Comparing Bidding Methods for Hydropower {cite}`Aasgard2016b`
  - Hydropower Bidding Using Linearized Start-Ups {cite}`Krohn2017`
  - Value of multi-market trading for a hydropower producer {cite}`Fodstad2017`
  - Optimizing day-ahead bid curves in hydropower production {cite}`Aasgard2018`
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
object_attributes = table[table["Object type"] == "scenario"].reset_index().iloc[:, 1:]
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

(scenario:scenario_id)=
### scenario_id
Scenario ID. Should be numbered consecutively starting from 1 (xUnit: NO_UNIT, yUnit: NO_UNIT)


(scenario:probability)=
### probability
Probability between 0 and 1 for realization of this scenario. The sum of probabilities for all scenarios must be equal to 1. Only the probability for the last time step is used and it will be applied to all time steps to ensure consistency (xUnit: NO_UNIT, yUnit: NO_UNIT)


(scenario:common_scenario)=
### common_scenario
Definition of non-anticipativity constraints for the full model. All decision variables must be the same for all scenarios and time steps where common_scenario is equal. All input time-series with stochastic data must accordingly have the same value for all scenarios and time steps where common_scenario is equal. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(scenario:common_history)=
### common_history
Definition of which scenario that should be used as the source for a branch in the current scenario. Branching from a different scenario than itself allows modelling of continuous short-term uncertainty by re-using existing scenarios. (xUnit: NO_UNIT, yUnit: NO_UNIT)


