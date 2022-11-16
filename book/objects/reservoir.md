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

(reservoir)=
# reservoir
A reservoir that is part of a regulated hydropower watercourse

|   |   |
|---|---|
|Input connections|<a href="plant.html">plant</a>, <a href="gate.html">gate</a>, <a href="junction.html">junction</a>, <a href="volume_constraint.html">volume_constraint</a>, <a href="cut_group.html">cut_group</a>, <a href="inflow_series.html">inflow_series</a>, <a href="tunnel.html">tunnel</a>, <a href="river.html">river</a>|
|Output connections|<a href="plant.html">plant</a>, <a href="river.html">river</a>, <a href="gate.html">gate</a>, <a href="tunnel.html">tunnel</a>, <a href="cut_group.html">cut_group</a>, <a href="inflow_series.html">inflow_series</a>, <a href="junction_gate.html">junction_gate</a>, <a href="junction.html">junction</a>, <a href="creek_intake.html">creek_intake</a>, <a href="volume_constraint.html">volume_constraint</a>|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```



## Examples
  - [](cut-description)
  - [](water-value-descriptions)
  - [](individual-water-values)
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
object_attributes = table[table["Object type"] == "reservoir"].reset_index().iloc[:, 1:]
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

(reservoir:latitude)=
### latitude
Reserved for future use (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:longitude)=
### longitude
Reserved for future use (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:max_vol)=
### max_vol
Maximum volume of the reservoir (xUnit: MM3, yUnit: MM3)


(reservoir:lrl)=
### lrl
Lowest Regulation Level (meter above sea level) of the reservoir (xUnit: METER, yUnit: METER)


(reservoir:hrl)=
### hrl
Highest Regulation Level (meter above sea level) of the reservoir (xUnit: METER, yUnit: METER)


(reservoir:vol_head)=
### vol_head
The volume (Mm3) and water level (meter above sea level) relation of the reservoir (xUnit: MM3, yUnit: METER)


(reservoir:elevation_adjustment)=
### elevation_adjustment
Adjustment for the lowest regulation level (lrl), highest regulation level (hrl), and the volume (Mm3) and water level (meter above sea level) relation of the reservoir (xUnit: NO_UNIT, yUnit: METER)


(reservoir:start_vol)=
### start_vol
Reservoir start volume (xUnit: MM3, yUnit: MM3)


(reservoir:start_head)=
### start_head
Reservoir start water level (meter above sea level) (xUnit: METER, yUnit: METER)


(reservoir:inflow)=
### inflow
Inflow to reservoir (xUnit: NO_UNIT, yUnit: M3/S)


(reservoir:inflow_flag)=
### inflow_flag
Flag determining whether the inflow to a reservoir should be used as input or calculated as output in the simulation: 0 = input; 1 = output (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:sim_inflow_flag)=
### sim_inflow_flag
Flag determining whether inflow should be simulated to reservoir or not (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:flow_descr)=
### flow_descr
The water level (meter above sea level) and overflow (m3/s) relation of the reservoir (xUnit: METER, yUnit: M3/S)


(reservoir:overflow_mip_flag)=
### overflow_mip_flag
Flag determining whether the binary variables should be used to prevent non-physical spill (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:overflow_cost)=
### overflow_cost
Overflow cost for the reservoir (xUnit: NO_UNIT, yUnit: NOK/MM3)


(reservoir:overflow_cost_flag)=
### overflow_cost_flag
Flag determining whether overflow cost for this reservoir should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:min_vol_constr)=
### min_vol_constr
Time-dependent minimum volume limit for the reservoir (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:min_vol_constr_flag)=
### min_vol_constr_flag
Flag determining whether the time-dependent minimum volume limit for the reservoir should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:max_vol_constr)=
### max_vol_constr
Time-dependent maximum volume limit for the reservoir (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:max_vol_constr_flag)=
### max_vol_constr_flag
Flag determining whether the time-dependent maximum volume limit for the reservoir should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:min_head_constr)=
### min_head_constr
Time-dependent minimum water level limit for the reservoir. The min_vol_constr attribute is preferred if it is present for the same reservoir. (xUnit: NO_UNIT, yUnit: METER)


(reservoir:min_head_constr_flag)=
### min_head_constr_flag
Flag determining whether the time-dependent minimum water level limit for the reservoir should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:max_head_constr)=
### max_head_constr
Time-dependent maximum water level limit for the reservoir. The max_vol_constr attribute is preferred if it is present for the same reservoir. (xUnit: NO_UNIT, yUnit: METER)


(reservoir:max_head_constr_flag)=
### max_head_constr_flag
Flag determining whether the time-dependent maximum water level limit for the reservoir should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:tactical_limit_min)=
### tactical_limit_min
Tactical minimum volume limit for the reservoir (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:tactical_limit_min_flag)=
### tactical_limit_min_flag
Flag determining whether the tactical minimum volume limit should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:tactical_cost_min)=
### tactical_cost_min
Given penalty cost for violating the tactical minimum volume limit for the reservoir (xUnit: NO_UNIT, yUnit: NOK/MM3H)


(reservoir:tactical_cost_min_flag)=
### tactical_cost_min_flag
Flag determining whether the penalty cost for violating the tactical minimum volume limit should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:tactical_limit_max)=
### tactical_limit_max
Tactical maximum volume limit for the reservoir (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:tactical_limit_max_flag)=
### tactical_limit_max_flag
Flag determining whether the tactical maximum volume limit should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:tactical_cost_max)=
### tactical_cost_max
Given penalty cost for violating the tactical maximum volume limit for the reservoir (xUnit: NO_UNIT, yUnit: NOK/MM3H)


(reservoir:tactical_cost_max_flag)=
### tactical_cost_max_flag
Flag determining whether the penalty cost for violating the tactical maximum volume limit should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:upper_slack)=
### upper_slack
Value used for expanding end reservoir volume range above maximum reference volume in cuts (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:lower_slack)=
### lower_slack
Value used for expanding end reservoir volume range below minimum reference volume in cuts (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:schedule)=
### schedule
Reservoir volume schedule (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:schedule_flag)=
### schedule_flag
Flag determining whether the reservoir volume schedule should be included in the optimization model: 0 = no schedule; 1 = the endpoint interval upper_slack and lower_slack is valid; 2 = reservoir volume schedule is valid anywhere during the optimization period (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:volume_schedule)=
### volume_schedule
Reservoir volume schedule (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:level_schedule)=
### level_schedule
Reservoir water level schedule (xUnit: NO_UNIT, yUnit: METER)


(reservoir:volume_ramping_up)=
### volume_ramping_up
Maximum limit for increase in reservoir volume per hour (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:volume_ramping_down)=
### volume_ramping_down
Maximum limit for decrease in reservoir volume per hour (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:level_ramping_up)=
### level_ramping_up
Maximum limit for increase in reservoir level per hour (xUnit: NO_UNIT, yUnit: METER)


(reservoir:level_ramping_down)=
### level_ramping_down
Maximum limit for decrease in reservoir level per hour (xUnit: NO_UNIT, yUnit: METER)


(reservoir:water_value_input)=
### water_value_input
The input water value description of water values referred to the sea. Can be a single constant value, a water value table (xy), or cut coefficients for a single or multiple price nodes. In the case of price dependent cut coefficients, the reference value of each xy in the xy_array should be the relevant price level. (xUnit: MM3, yUnit: NOK/MM3)


(reservoir:energy_value_input)=
### energy_value_input
The input local energy value of the reservoir which will be converted to a global water value internally. (xUnit: NOK/MWH, yUnit: NOK/MWH)


(reservoir:peak_volume_cost_curve)=
### peak_volume_cost_curve
A piece-wise constant increasing cost which is applied to the highest reservoir volume reached in the optimization horizon (xUnit: MM3, yUnit: NOK/MM3)


(reservoir:flood_volume_cost_curve)=
### flood_volume_cost_curve
A piece-wise constant increasing cost curve which is used to penalize the reservoir volume level in each hour of the optimzation (xUnit: MM3, yUnit: NOK/MM3)


(reservoir:storage)=
### storage
Resulting reservoir volume (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:sim_storage)=
### sim_storage
Simulated reservoir volume (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:head)=
### head
Resulting reservoir water level (meter above sea level) (xUnit: NO_UNIT, yUnit: METER)


(reservoir:sim_head)=
### sim_head
Simulated reservoir water level (meter above sea level) (xUnit: NO_UNIT, yUnit: METER)


(reservoir:sim_inflow)=
### sim_inflow
Simulated inflow to reservoir (xUnit: NO_UNIT, yUnit: M3/S)


(reservoir:endpoint_penalty)=
### endpoint_penalty
Resulting penalty when the maximum or minimum volume limit for the reservoir at the end of the optimization period is violated (xUnit: MM3, yUnit: MM3)


(reservoir:penalty)=
### penalty
Resulting penalty when the maximum or minimum volume limit for the reservoir during the optimization period is violated (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:tactical_penalty_up)=
### tactical_penalty_up
Resulting penalty when the tactical maximum volume limit for the reservoir is violated (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:tactical_penalty_down)=
### tactical_penalty_down
Resulting penalty when the tactical minimum volume limit for the reservoir is violated (xUnit: NO_UNIT, yUnit: MM3)


(reservoir:end_penalty)=
### end_penalty
Resulting penalty cost when the maximum or minimum volume limit for the reservoir at the end of the optimization period is violated (xUnit: NO_UNIT, yUnit: NOK)


(reservoir:penalty_nok)=
### penalty_nok
Resulting penalty cost when the maximum or minimum volume limit for the reservoir during the optimization period is violated (xUnit: NO_UNIT, yUnit: NOK)


(reservoir:tactical_penalty)=
### tactical_penalty
Resulting penalty cost when the tactical maximum or minimum volume limit for the reservoir is violated (xUnit: NO_UNIT, yUnit: NOK)


(reservoir:water_value_global_result)=
### water_value_global_result
Marginal cost of 1 Mm3 of the water in the reservoir calculated using the sum of the best efficiency point of all cascaded plants below this reservoir (xUnit: NO_UNIT, yUnit: NOK/MM3)


(reservoir:water_value_local_result)=
### water_value_local_result
Marginal cost of 1 Mm3 of the water discharged from the reservoir through the downstream plant (xUnit: NO_UNIT, yUnit: NOK/MM3)


(reservoir:energy_value_local_result)=
### energy_value_local_result
Marginal cost of 1 MWh power that generated from the water in the reservoir through the downstream plant (xUnit: NO_UNIT, yUnit: NOK/MWH)


(reservoir:end_value)=
### end_value
Value of reservoir contents at the end of the optimization period (xUnit: NO_UNIT, yUnit: NOK)


(reservoir:change_in_end_value)=
### change_in_end_value
Relative change in value of reservoir contents between the start and the end of the optimization horizon (xUnit: NO_UNIT, yUnit: NOK)


(reservoir:vow_in_transit)=
### vow_in_transit
Value of delayed water on its way to this reservoir after the end of the optimization period (xUnit: NO_UNIT, yUnit: NOK)


(reservoir:calc_global_water_value)=
### calc_global_water_value
The resulting global water value of the reservoir after the local energy value has been converted internally based on the energy_conversion_factor reservoir attribute. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(reservoir:energy_conversion_factor)=
### energy_conversion_factor
The calculated conversion factor between MWh and Mm3 based on the first plant below the reservoir and initial start head. (xUnit: MWH/MM3, yUnit: MWH/MM3)


(reservoir:water_value_cut_result)=
### water_value_cut_result
The resulting output water value cut coefficients when SHOP is used to create cuts. (xUnit: MM3, yUnit: NOK/MM3)


(reservoir:added_to_network)=
### added_to_network
Flag determining whether the model has determined that this reservoir is part of a tunnel network (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:network_no)=
### network_no
Network identification number set by the model to indicate which tunnel network this reservoir is part of (xUnit: NO_UNIT, yUnit: NO_UNIT)


(reservoir:peak_volume_penalty)=
### peak_volume_penalty
The peak volume penalty incurred for the reservoir, zero in all time steps except for when the reservoir volume peak occurs (xUnit: NO_UNIT, yUnit: NOK)


(reservoir:flood_volume_penalty)=
### flood_volume_penalty
The penalty incurred for the reservoir based on the optimized reservoir volume and the flood_volume_cost_curve (xUnit: NO_UNIT, yUnit: NOK)


