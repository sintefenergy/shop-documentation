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

(gate)=
# gate
A general water rout that is used to move water from an upstream reservoir to the downstream reservoir

|   |   |
|---|---|
|Input connections|<a href="reservoir.html">reservoir</a>, <a href="creek_intake.html">creek_intake</a>, <a href="discharge_group.html">discharge_group</a>|
|Output connections|<a href="reservoir.html">reservoir</a>, <a href="junction.html">junction</a>, <a href="discharge_group.html">discharge_group</a>|
|License|SHOP_OPEN|
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
object_attributes = table[table["Object type"] == "gate"].reset_index().iloc[:, 1:]
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

(gate:time_delay)=
### time_delay
The delay between water leaving the gate and until it ends up in the downstream reservoir (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:add_slack)=
### add_slack
Include slack variables for the corresponding delta meter gate (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:max_discharge)=
### max_discharge
Maximum discharge capacity for the gate (xUnit: M3/S, yUnit: M3/S)


(gate:lin_rel_a)=
### lin_rel_a
Linear approximation to model gate discharge (in Mm3) as a function of upstream reservoir volume: gate_flow = lin_rel_a*up_rsv_volume + lin_rel_b (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:lin_rel_b)=
### lin_rel_b
Linear approximation to model gate discharge (in Mm3) as a function of upstream reservoir volume: gate_flow = lin_rel_a*up_rsv_volume + lin_rel_b (xUnit: MM3, yUnit: MM3)


(gate:shape_discharge)=
### shape_discharge
Describes the wave shape of the delayed discharge for a gate by ratios as a function of time delays (xUnit: HOUR, yUnit: NO_UNIT)


(gate:spill_cost_curve)=
### spill_cost_curve
Describes a piece-wise constant cost curve for the flow in the gate. This is only available for spill gates, and overrides the default overflow penalty in SHOP. (xUnit: M3/S, yUnit: NOK/M3/S)


(gate:peak_flow_cost_curve)=
### peak_flow_cost_curve
Describes the piece-wise constant cost curve for the highest achieved flow rate in the gate over the optimization horizon (xUnit: M3/S, yUnit: NOK/M3/S)


(gate:peak_flow_penalty)=
### peak_flow_penalty
The penalty incurred based on the peak_flow_cost_curve and the highest achieved flow rate in the gate over the optimization horizon (xUnit: NO_UNIT, yUnit: NOK)


(gate:functions_meter_m3s)=
### functions_meter_m3s
The relation between the head and opening of the gate or weir to define the discharge function of the gate (xUnit: METER, yUnit: M3/S)


(gate:functions_deltameter_m3s)=
### functions_deltameter_m3s
Relationship between flow through the gate and water level in upper reservoir and difference in water level between upper and lower reservoir (xUnit: DELTA_METER, yUnit: M3/S)


(gate:min_flow)=
### min_flow
Minimum flow constraint on the gate (xUnit: NO_UNIT, yUnit: M3/S)


(gate:min_flow_flag)=
### min_flow_flag
Flag determining whether the min_flow should be used (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:max_flow)=
### max_flow
Maximum flow constraint on the gate (xUnit: NO_UNIT, yUnit: M3/S)


(gate:max_flow_flag)=
### max_flow_flag
Flag determining whether the max_flow should be used (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:schedule_m3s)=
### schedule_m3s
Gate discharge schedule (xUnit: NO_UNIT, yUnit: M3/S)


(gate:schedule_percent)=
### schedule_percent
Gate schedule in percent opening of the gate (xUnit: NO_UNIT, yUnit: %)


(gate:schedule_flag)=
### schedule_flag
Flag determining how the gate schedule should be used: 0 = no discharge schedule; 1 = discharge schedule; 2 = flow is calculated from reservoir water level and flow function for the gate (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:setting)=
### setting
Predefined position of the gate to be used for determining gate flow together with functions and upstream water level (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:setting_flag)=
### setting_flag
Flag determining whether the gate setting should be used to determine the flow through the gate (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:discharge_fee)=
### discharge_fee
Cost of discharging water through the gate referred to the time of discharge (xUnit: NO_UNIT, yUnit: NOK/MM3)


(gate:discharge_fee_flag)=
### discharge_fee_flag
Flag determining whether discharge_fee should be used in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:block_merge_tolerance)=
### block_merge_tolerance
Maximum deviation in discharge between two time steps that forces these hours to have the same discharge in later iterations (xUnit: NO_UNIT, yUnit: M3/S)


(gate:min_q_penalty_flag)=
### min_q_penalty_flag
A flag enabling the penalty cost for the minimum discharge constraint on the gate (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:max_q_penalty_flag)=
### max_q_penalty_flag
A flag enabling the penalty cost for the maximum discharge constraint on the gate (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:ramping_up)=
### ramping_up
Maximum limit for increase in gate discharge per hour (xUnit: NO_UNIT, yUnit: M3SEC_HOUR)


(gate:ramping_up_flag)=
### ramping_up_flag
A flag for toggling the upper ramping limit constraint on and off for this gate (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:ramping_down)=
### ramping_down
Maximum limit for decrease in gate discharge per hour (xUnit: NO_UNIT, yUnit: M3SEC_HOUR)


(gate:ramping_down_flag)=
### ramping_down_flag
A flag for toggling the lower ramping limit constraint on and off for this gate (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:ramp_penalty_cost)=
### ramp_penalty_cost
The penalty cost for breaking the upper or lower discharge ramping limits for the gate (xUnit: NO_UNIT, yUnit: NOK/M3/S)


(gate:ramp_penalty_cost_flag)=
### ramp_penalty_cost_flag
A flag for toggling the use of the specified ramping penalty cost for this gate on or off (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:max_q_penalty_cost)=
### max_q_penalty_cost
The penalty cost for the gate maximum discharge constraint (xUnit: NO_UNIT, yUnit: NOK/MM3)


(gate:min_q_penalty_cost)=
### min_q_penalty_cost
The penalty cost for the gate minimum discharge constraint (xUnit: NO_UNIT, yUnit: NOK/MM3)


(gate:max_q_penalty_cost_flag)=
### max_q_penalty_cost_flag
Flag determining whether max_q_penalty_cost should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:min_q_penalty_cost_flag)=
### min_q_penalty_cost_flag
Flag determining whether min_q_penalty_cost should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(gate:min_q_penalty)=
### min_q_penalty
Resulting penalty when the gate minimum discharge is violated (xUnit: NO_UNIT, yUnit: NOK)


(gate:max_q_penalty)=
### max_q_penalty
Resulting penalty when the gate maximum discharge is violated (xUnit: NO_UNIT, yUnit: NOK)


(gate:discharge)=
### discharge
Resulting gate discharge (xUnit: NO_UNIT, yUnit: M3/S)


(gate:sim_discharge)=
### sim_discharge
Simulated gate discharge (xUnit: NO_UNIT, yUnit: M3/S)


