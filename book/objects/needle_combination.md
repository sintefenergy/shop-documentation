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

(needle_combination)=
# needle_combination
A needle combination or isolated production zone of a generator with separate turbine efficiency curves. Can be used to model pelton turbines and other turbines with forbidden production zones

|   |   |
|---|---|
|Input connections|<a href="generator.html">generator</a>, <a href="needle_comb_reserve_capability.html">needle_comb_reserve_capability</a>|
|Output connections|<a href="generator.html">generator</a>, <a href="needle_comb_reserve_capability.html">needle_comb_reserve_capability</a>|
|License|SHOP_PELTON|
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
object_attributes = table[table["Object type"] == "needle_combination"].reset_index().iloc[:, 1:]
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

(needle_combination:p_max)=
### p_max
Static maximum production for the needle combination (xUnit: MW, yUnit: MW)


(needle_combination:p_min)=
### p_min
Static minimum production for the needle combination (xUnit: MW, yUnit: MW)


(needle_combination:p_nom)=
### p_nom
The nominal production that is the rated capacity of the needle combination (xUnit: MW, yUnit: MW)


(needle_combination:turb_eff_curves)=
### turb_eff_curves
The head-dependent turbine efficiency curve(s)for the needle combination (xUnit: M3/S, yUnit: %)


(needle_combination:p_fcr_min)=
### p_fcr_min
Temporary minimum production allowed for the needle combination when delivering FCR (xUnit: NO_UNIT, yUnit: MW)


(needle_combination:p_fcr_max)=
### p_fcr_max
Temporary maximum production allowed for the needle combination when delivering FCR (xUnit: NO_UNIT, yUnit: MW)


(needle_combination:production_cost)=
### production_cost
Production cost depending on the production of the needle combination (xUnit: MW, yUnit: NOK/MW)


(needle_combination:original_pq_curves)=
### original_pq_curves
Original PQ-curve for the needle combination that includes non-convex regions (xUnit: M3/S, yUnit: MW)


(needle_combination:convex_pq_curves)=
### convex_pq_curves
Convexified PQ-curve for the needle combination that includes all the time-dependent operating limits and remove all the nonconcave points of the original PQ curve. The slope of each segment is non-increasing. (xUnit: M3/S, yUnit: MW)


(needle_combination:final_pq_curves)=
### final_pq_curves
Final PQ curve for the needle combination that is the final form included into the MILP optimization problem. The first point of the convex PQ curve is extended to Q=0. (xUnit: M3/S, yUnit: MW)


(needle_combination:max_prod)=
### max_prod
The head dependent maximal production of the needle_combination, most accurate in incremental iterations (xUnit: NO_UNIT, yUnit: MW)


(needle_combination:min_prod)=
### min_prod
The head dependent minimal production of the needle_combination, most accurate in incremental iterations (xUnit: NO_UNIT, yUnit: MW)


