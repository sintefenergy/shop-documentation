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

(river)=
# river
The river object models open channel flow of water in a river streach or channel between reservoirs

|   |   |
|---|---|
|Input connections|<a href="reservoir.html">reservoir</a>, <a href="plant.html">plant</a>, <a href="discharge_group.html">discharge_group</a>, <a href="tunnel.html">tunnel</a>, <a href="river.html">river</a>|
|Output connections|<a href="river.html">river</a>, <a href="reservoir.html">reservoir</a>, <a href="discharge_group.html">discharge_group</a>|
|License|SHOP_OPEN|
|Release version|14.3.1.0|

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
object_attributes = table[table["Object type"] == "river"].reset_index().iloc[:, 1:]
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

(river:length)=
### length
Length of the river segment (xUnit: METER, yUnit: METER)


(river:upstream_elevation)=
### upstream_elevation
The elevation of the river floor upstream (xUnit: METER, yUnit: METER)


(river:downstream_elevation)=
### downstream_elevation
The elevation of the river floor downstream (xUnit: METER, yUnit: METER)


(river:time_delay_const)=
### time_delay_const
The time delay of the water flowing down the river (xUnit: HOUR, yUnit: HOUR)


(river:delayed_water_energy_value)=
### delayed_water_energy_value
Specifies a constant energy value used to evaluate the water in transit at the end of the optimization horizon. The water value of the downstream reservoir will be used if this attribute is not specified. (xUnit: NOK/MWH, yUnit: NOK/MWH)


(river:initial_gate_opening)=
### initial_gate_opening
Specifies the initial opening position of the gate in the river before optimization, which is used when applying gate_adjustment_cost and gate_ramping constraints for the first time step. These constraints will not be applied for t=0 if the initial gate opening is not specified (-1)  (xUnit: NO_UNIT, yUnit: NO_UNIT)


(river:main_river)=
### main_river
Specifies that this river should be considered the main waterway downstream a reservoir, and is only needed if a reservoir has no directly connected downstream power plant and has multiple output rivers. The first connected river is assumed to be the main river if this value has not been set on any of the output rivers. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(river:width_depth_curve)=
### width_depth_curve
The curve describing the shape of the river cross section (xUnit: METER, yUnit: METER)


(river:flow_cost_curve)=
### flow_cost_curve
Describes a piece-wise constant cost curve for the flow in each time step for the river. This convex curve is preferred over the standard flow_cost TXY attribute if both are defined for the river object (xUnit: M3/S, yUnit: NOK/M3/S)


(river:peak_flow_cost_curve)=
### peak_flow_cost_curve
Describes the piece-wise constant cost curve for the highest achieved flow rate in the river over the optimization horizon (xUnit: M3/S, yUnit: NOK/M3/S)


(river:time_delay_curve)=
### time_delay_curve
Function for modelling wave-shaped time delay. X-values are the time since discharge and Y-values are the amount of water arriving at the end of the river at that time. Separate curves can be given in for different reference flows, in this case the time delay will be interpolated between the curves based on the flow in the past SHOP iteration. (xUnit: HOUR, yUnit: M3/S)


(river:past_upstream_flow)=
### past_upstream_flow
Represents the upstream flow in the river before the start of the optimization period, which is considered for rivers with time delay. The X-values represent the number of hours before optimization start, and should be increasing negative numbers. The Y-values are the corresponding flow. (xUnit: HOUR, yUnit: M3/S)


(river:up_head_flow_curve)=
### up_head_flow_curve
Function determining the relationship between water level in the reservoir directly above the river and the flow in the river. The XY flow functions can be given in for multiple gate settings where the gate opening position is the reference value of the XY table (xUnit: METER, yUnit: M3/S)


(river:gate_opening_curve)=
### gate_opening_curve
Function determining the relationship between the user-defined position of the gate (X-value) and the corresponding height in meters above the river bottom (Y-value) (xUnit: NO_UNIT, yUnit: METER)


(river:delta_head_ref_up_flow_curve)=
### delta_head_ref_up_flow_curve
Set of functions determining the relationship between the difference in water level between the reservoir directly above and below the river (X-value) and the flow in the river (Y-value). The reference for each function is the water level in the upper reservoir. (xUnit: METER, yUnit: M3/S)


(river:delta_head_ref_down_flow_curve)=
### delta_head_ref_down_flow_curve
Set of functions determining the relationship between the difference in water level between the reservoir directly above and below the river (X-value) and the flow in the river (Y-value). The reference for each function is the water level in the lower reservoir. (xUnit: METER, yUnit: M3/S)


(river:inflow)=
### inflow
The upstream natural inflow to the river (xUnit: M3/S, yUnit: M3/S)


(river:min_flow)=
### min_flow
Defines a minimum flow constraint for the river (xUnit: M3/S, yUnit: M3/S)


(river:max_flow)=
### max_flow
Defines a maximum flow constraint for the river (xUnit: M3/S, yUnit: M3/S)


(river:min_flow_penalty_cost)=
### min_flow_penalty_cost
The penalty cost for breaking the min_flow constraint. Overrides the default river_flow_penalty_cost defined on global_settings. (xUnit: NOK/M3/S, yUnit: NOK/M3/S)


(river:max_flow_penalty_cost)=
### max_flow_penalty_cost
The penalty cost for breaking the max_flow constraint. Overrides the default river_flow_penalty_cost defined on global_settings. (xUnit: NOK/M3/S, yUnit: NOK/M3/S)


(river:ramping_up)=
### ramping_up
Defines a maximum upward flow ramping constraint for the river (xUnit: M3SEC_HOUR, yUnit: M3SEC_HOUR)


(river:ramping_down)=
### ramping_down
Defines a maximum downward flow ramping constraint for the river (xUnit: M3SEC_HOUR, yUnit: M3SEC_HOUR)


(river:ramping_up_penalty_cost)=
### ramping_up_penalty_cost
The penalty cost for breaking the ramping_up constraint. Overrides the default gate_ramp_penalty_cost defined on global_settings. (xUnit: NOK/M3/S, yUnit: NOK/M3/S)


(river:ramping_down_penalty_cost)=
### ramping_down_penalty_cost
The penalty cost for breaking the ramping_down constraint. Overrides the default gate_ramp_penalty_cost defined on global_settings. (xUnit: NOK/M3/S, yUnit: NOK/M3/S)


(river:cost_curve_scaling)=
### cost_curve_scaling
The values in this time series will be multiplied with the flow_cost_curve values. This makes it possible to vary the convex flow_cost_curve over the optimization horizon. (xUnit: NOK/M3/S, yUnit: NOK/M3/S)


(river:flow_schedule)=
### flow_schedule
Schedule for flow through the river. If the river has time delay, it is referenced to the start of the river. (xUnit: NO_UNIT, yUnit: M3/S)


(river:flow_schedule_penalty_cost)=
### flow_schedule_penalty_cost
Penalty cost for breaking the flow_schedule for the river. The default penalty cost for all rivers can be set with the river_flow_schedule_penalty_cost attribute on global_settings (xUnit: NO_UNIT, yUnit: NOK/M3/S)


(river:gate_opening_schedule)=
### gate_opening_schedule
Schedule for opening of the gate in the river. The value given here is interpreted as the X-value of the gate_opening_curve. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(river:flow_block_merge_tolerance)=
### flow_block_merge_tolerance
Maximum difference in flow between two timesteps that results in a merged result for these timesteps in the next iteration. This requires merging to be activated in the command file by set merge /on. (xUnit: NO_UNIT, yUnit: M3/S)


(river:gate_ramping)=
### gate_ramping
Maximal allowed change in the gate height per hour in both upward and downward direction. (xUnit: NO_UNIT, yUnit: METER/HOUR)


(river:gate_ramping_penalty_cost)=
### gate_ramping_penalty_cost
The penalty cost for breaking the gate ramping constraints in either upward or downward direction. (xUnit: NO_UNIT, yUnit: NOK/METER_HOUR)


(river:gate_adjustment_cost)=
### gate_adjustment_cost
The cost for changeing the gate height between two time steps in either upward or downward direction. (xUnit: NO_UNIT, yUnit: NOK/METER)


(river:flow_cost)=
### flow_cost
A linear cost for the flow of water in the river. If a covex flow_cost_curve is defined on the gate, it will be preferred over the flow_cost (xUnit: NO_UNIT, yUnit: NOK/M3/S)


(river:mip_flag)=
### mip_flag
A flag series used to turn on (1) and off (0) the use of binary variables to ensure that the river flow is zero when the reservoir head is below the gate or bottom of the river bed. Non-physical flow may occur if the mip_flag is turned off (xUnit: NO_UNIT, yUnit: NO_UNIT)


(river:flow)=
### flow
The flow in the river, referenced at the upstream enpoint (xUnit: M3/S, yUnit: M3/S)


(river:upstream_flow)=
### upstream_flow
The flow in the river at the upstream enpoint (xUnit: M3/S, yUnit: M3/S)


(river:downstream_flow)=
### downstream_flow
The flow in the river at the downstream enpoint (xUnit: M3/S, yUnit: M3/S)


(river:gate_height)=
### gate_height
The height of the gate in MASL (xUnit: METER, yUnit: METER)


(river:min_flow_penalty)=
### min_flow_penalty
The incurred penalty for breaking the min_flow constraint (xUnit: NOK, yUnit: NOK)


(river:max_flow_penalty)=
### max_flow_penalty
The incurred penalty for breaking the max_flow constraint (xUnit: NOK, yUnit: NOK)


(river:ramping_up_penalty)=
### ramping_up_penalty
The incurred penalty for breaking the ramping_up constraint (xUnit: NOK, yUnit: NOK)


(river:ramping_down_penalty)=
### ramping_down_penalty
The incurred penalty for breaking the ramping_down constraint (xUnit: NOK, yUnit: NOK)


(river:flow_penalty)=
### flow_penalty
The penalty incurred based on the flow_cost_curve and the flow rate in the river over the optimization horizon (xUnit: NO_UNIT, yUnit: NOK)


(river:peak_flow_penalty)=
### peak_flow_penalty
The penalty incurred based on the peak_flow_cost_curve and the highest achieved flow rate in the river over the optimization horizon (xUnit: NO_UNIT, yUnit: NOK)


(river:gate_ramping_penalty)=
### gate_ramping_penalty
The penalty incurred for breaking the gate_ramping constraints according to the gate_ramping_penalty_cost (xUnit: NO_UNIT, yUnit: NOK)


(river:gate_adjustment_penalty)=
### gate_adjustment_penalty
The incurred cost for changeing the gate height between time steps according to the gate_adjustment_cost (xUnit: NO_UNIT, yUnit: NOK)


(river:flow_schedule_penalty)=
### flow_schedule_penalty
The incurred cost for breaking the flow_schedule constraints on the river (xUnit: NO_UNIT, yUnit: NOK)


(river:physical_flow)=
### physical_flow
The physical flow into the top of the river based on the post-calculated reservoir head values. If the river flow is not dependent on the upstream reservoir head, the physical_flow will be identical to the regular flow attribute. (xUnit: NO_UNIT, yUnit: M3/S)


(river:initial_downstream_flow)=
### initial_downstream_flow
The calculated initial flow that will flow out from the end of the river. This is calulated based on the time delay in the river and the past_upstream_flow and distributed_past_upstream_flow attribute. (xUnit: NO_UNIT, yUnit: M3/S)


(river:distributed_past_upstream_flow)=
### distributed_past_upstream_flow
The past upstream flow of upstream river objects that have been distributed down to this river. (xUnit: HOUR, yUnit: M3/S)


