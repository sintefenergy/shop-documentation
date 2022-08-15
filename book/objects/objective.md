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

(objective)=
# objective
An object to hold the information of the objective function after optimization. These objects are automatically created by SHOP, one objective object per scenario is created with the name 'scen_<number>'. In addition, the average objective weighted by the scenario probablities is created in every SHOP run. For a regular deterministic SHOP run, the average_objective and scen_1 objective will be identical.

|   |   |
|---|---|
|Input connections||
|Output connections||
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
object_attributes = table[table["Object type"] == "objective"].reset_index().iloc[:, 1:]
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

(objective:solver_status)=
### solver_status
Description of the latest status from the solver (xUnit: NO_UNIT, yUnit: NO_UNIT)


(objective:times_of_wrong_pq_uploading)=
### times_of_wrong_pq_uploading
How many times the unit PQ segments are wrongly uploaded, i.e. the latter segments are fulfilled first. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(objective:grand_total)=
### grand_total
Objective function equal to the sum of total and sum_penalties (xUnit: NOK, yUnit: NOK)


(objective:sim_grand_total)=
### sim_grand_total
Simulated objective function equal to the sum of total and sum_penalties (xUnit: NOK, yUnit: NOK)


(objective:total)=
### total
Objective function equal to the sum of rsv_end_value, vow_in_transit, market_sale_buy, load_value, reserve_sale_buy, reserve_oblig_value, contract_value, startup_costs, sum_feeding_fee, and sum_discharge_fee (xUnit: NOK, yUnit: NOK)


(objective:sum_penalties)=
### sum_penalties
Penalty cost equal to the sum of minor_penalties and major_penalties (xUnit: NOK, yUnit: NOK)


(objective:minor_penalties)=
### minor_penalties
Penalty cost equal to the sum of rsv_tactical_penalty, plant_p_constr_penalty, plant_q_constr_penalty, plant_schedule_penalty, gen_schedule_penalty, pump_schedule_penalty, gate_q_constr_penalty, gate_discharge_cost, bypass_cost, gate_spill_cost, gate_slack_cost, creek_spill_cost, junction_slack_cost, reserve_violation_penalty, reserve_slack_cost, and reserve_schedule_penalty (xUnit: NOK, yUnit: NOK)


(objective:major_penalties)=
### major_penalties
Penalty cost equal to the sum of rsv_penalty, rsv_end_penalty, load_penalty, group_time_period_penalty, group_time_step_penalty, sum_ramping_penalty, discharge_group_penalty, production_group_energy_penalty, and production_group_power_penalty (xUnit: NOK, yUnit: NOK)


(objective:rsv_end_value)=
### rsv_end_value
Value of water remaining in the reservoirs at the end of the optimization period. If cut description is used, the delayed water on its way to reservoirs is included, while for other end value description this water is valuated in vow_in_transit. (xUnit: NOK, yUnit: NOK)


(objective:sim_rsv_end_value)=
### sim_rsv_end_value
Simulated value of water remaining in the reservoirs at the end of the simulation period. (xUnit: NOK, yUnit: NOK)


(objective:rsv_end_value_relative)=
### rsv_end_value_relative
Change in value of water in the reservoirs between the start and the end of the optimization period (xUnit: NOK, yUnit: NOK)


(objective:vow_in_transit)=
### vow_in_transit
Value of delayed water on its way to reservoirs at the end of the optimization period. If cut description is used the delayed water is valuated as part of the rsv_end_value instead. (xUnit: NOK, yUnit: NOK)


(objective:rsv_spill_vol_end_value)=
### rsv_spill_vol_end_value
End reservoir value lost due to volume over HRL in flood situations. Only appliccapble when running with constant water values. The extra water is evaluated according to the water value of the reservoir downstream of the spill gate. (xUnit: NOK, yUnit: NOK)


(objective:market_sale_buy)=
### market_sale_buy
The sum of the value of power bought from the market minus the value of power sold to the market for all time steps (xUnit: NOK, yUnit: NOK)


(objective:sim_market_sale_buy)=
### sim_market_sale_buy
The sum of the simulated value of power bought from the market minus the value of power sold to the market for all time steps (xUnit: NOK, yUnit: NOK)


(objective:load_value)=
### load_value
The load obligation value by multiplying the load with the market sale price (xUnit: NOK, yUnit: NOK)


(objective:reserve_sale_buy)=
### reserve_sale_buy
Reserve trade value (xUnit: NOK, yUnit: NOK)


(objective:reserve_oblig_value)=
### reserve_oblig_value
THe reserve obligation value by multiplying the reserve obligation with the market sale price (xUnit: NOK, yUnit: NOK)


(objective:contract_value)=
### contract_value
Contract value (xUnit: NOK, yUnit: NOK)


(objective:startup_costs)=
### startup_costs
The sum of the startup and shutdown costs for all units and time steps. By default this includes costs whenever the commitment status of the unit changes regardless of whether MIP is active or not. (xUnit: NOK, yUnit: NOK)


(objective:sim_startup_costs)=
### sim_startup_costs
The sum of simulated startup and shutdown costs for all units and time steps. By default this includes costs whenever the commitment status of the unit changes regardless of whether MIP is active or not. (xUnit: NOK, yUnit: NOK)


(objective:sum_feeding_fee)=
### sum_feeding_fee
The sum of feed-in fee paid for all plants and time steps. (xUnit: NOK, yUnit: NOK)


(objective:sum_discharge_fee)=
### sum_discharge_fee
The sum of discharge fee paid for all plants and gates and time steps. (xUnit: NOK, yUnit: NOK)


(objective:thermal_cost)=
### thermal_cost
The sum of fuel cost for all thermal units and time steps. (xUnit: NOK, yUnit: NOK)


(objective:reserve_allocation_cost)=
### reserve_allocation_cost
The total cost for allocating reserves on all units in the system. The allocation cost can be specified on each unit for each reserve type, see for instance the 'fcr_n_up_cost' on the generator and pump objects. (xUnit: NOK, yUnit: NOK)


(objective:rsv_tactical_penalty)=
### rsv_tactical_penalty
Resulting total penalty cost when the tactical maximum or minimum volume limits for the reservoirs are violated (xUnit: NOK, yUnit: NOK)


(objective:plant_p_constr_penalty)=
### plant_p_constr_penalty
Resulting total penalty cost when the time-dependent maximum or minimum production limits for the plants are violated (xUnit: NOK, yUnit: NOK)


(objective:plant_q_constr_penalty)=
### plant_q_constr_penalty
Resulting total penalty cost when the time-dependent maximum or minimum discharge limits for the plants are violated (xUnit: NOK, yUnit: NOK)


(objective:plant_schedule_penalty)=
### plant_schedule_penalty
Resulting total penalty cost when the plant schedules are violated (xUnit: NOK, yUnit: NOK)


(objective:plant_rsv_q_limit_penalty)=
### plant_rsv_q_limit_penalty
Resulting total penalty cost when the head dependent maximum discharge limits for the plants are violated. These limits are set by the max_q_limit_rsv_up and max_q_limit_rsv_down attributes on the plant object (xUnit: NOK, yUnit: NOK)


(objective:gen_schedule_penalty)=
### gen_schedule_penalty
Resulting total penalty cost when the generator schedules are violated (xUnit: NOK, yUnit: NOK)


(objective:pump_schedule_penalty)=
### pump_schedule_penalty
Resulting total penalty cost when the pump schedules are violated (xUnit: NOK, yUnit: NOK)


(objective:gate_q_constr_penalty)=
### gate_q_constr_penalty
Resulting total penalty cost when the time-dependent maximum or minimum discharge limits for the gates are violated (xUnit: NOK, yUnit: NOK)


(objective:gate_discharge_cost)=
### gate_discharge_cost
The sum of discharge costs for all gates and time steps (xUnit: NOK, yUnit: NOK)


(objective:bypass_cost)=
### bypass_cost
The sum of bypass discharge costs for all bypass gates and time steps (xUnit: NOK, yUnit: NOK)


(objective:gate_spill_cost)=
### gate_spill_cost
The sum of spill costs for all spill gates and time steps (xUnit: NOK, yUnit: NOK)


(objective:physical_spill_cost)=
### physical_spill_cost
The sum of spill costs for the part of the spill that represents physical spill, i.e. the spill occurs when the water exceeds max_vol of the reservoir. (xUnit: NOK, yUnit: NOK)


(objective:physical_spill_volume)=
### physical_spill_volume
The sum of spill volume for the part of the spill that represents physical spill, i.e. the spill occurs when the water exceeds max_vol of the reservoir. (xUnit: MM3, yUnit: MM3)


(objective:nonphysical_spill_cost)=
### nonphysical_spill_cost
The sum of spill costs for the part of the spill that represents non-physical spill, i.e. the spill occurs when the water does not reach max_vol of the reservoir. (xUnit: NOK, yUnit: NOK)


(objective:nonphysical_spill_volume)=
### nonphysical_spill_volume
The sum of spill volume for the part of the spill that represents non-physical spill, i.e. the spill occurs when the water does not reach max_vol of the reservoir. (xUnit: MM3, yUnit: MM3)


(objective:gate_slack_cost)=
### gate_slack_cost
The sum of costs for the use of slack variables for all deltameter gates and time steps (xUnit: NOK, yUnit: NOK)


(objective:creek_spill_cost)=
### creek_spill_cost
The sum of spill costs for all creek spill gates and time steps (xUnit: NOK, yUnit: NOK)


(objective:creek_physical_spill_cost)=
### creek_physical_spill_cost
The sum of spill costs for the part of the spill that represents physical spill (xUnit: NOK, yUnit: NOK)


(objective:creek_nonphysical_spill_cost)=
### creek_nonphysical_spill_cost
The sum of spill costs for the part of the spill that represents non-physical spill (xUnit: NOK, yUnit: NOK)


(objective:junction_slack_cost)=
### junction_slack_cost
The sum of cost for the use of slack variables for all junctions and time steps (xUnit: NOK, yUnit: NOK)


(objective:reserve_violation_penalty)=
### reserve_violation_penalty
Resulting total penalty cost when the reserve deliveries deviate below the reserve obligations (xUnit: NOK, yUnit: NOK)


(objective:reserve_slack_cost)=
### reserve_slack_cost
Resulting total slack cost when the reserve deliveries deviate above the reserve obligations (xUnit: NOK, yUnit: NOK)


(objective:reserve_schedule_penalty)=
### reserve_schedule_penalty
Resulting total penalty cost when the reserve schedules are violated (xUnit: NOK, yUnit: NOK)


(objective:rsv_peak_volume_penalty)=
### rsv_peak_volume_penalty
Resulting total penalty cost for peak reservoir volumes penalized by the peak_volume_cost_curve on each reservoir (xUnit: NOK, yUnit: NOK)


(objective:gate_peak_flow_penalty)=
### gate_peak_flow_penalty
Resulting total penalty cost for peak gate flows penalized by the peak_flow_cost_curve on each gate (xUnit: NOK, yUnit: NOK)


(objective:rsv_flood_volume_penalty)=
### rsv_flood_volume_penalty
Resulting total penalty cost for the reservoir volumes penalized by the flood_volume_cost_curve (xUnit: NOK, yUnit: NOK)


(objective:river_peak_flow_penalty)=
### river_peak_flow_penalty
Resulting total penalty cost for peak river flows penalized by the peak_flow_cost_curve on each river (xUnit: NOK, yUnit: NOK)


(objective:river_flow_penalty)=
### river_flow_penalty
Resulting total penalty cost for river flows penalized by the flow_cost_curve on each river (xUnit: NOK, yUnit: NOK)


(objective:rsv_penalty)=
### rsv_penalty
Resulting total penalty cost when the maximum or minimum volume limits for all reservoirs during the optimization period are violated (xUnit: NOK, yUnit: NOK)


(objective:rsv_hard_limit_penalty)=
### rsv_hard_limit_penalty
Resulting total penalty cost for breaking the hard min/max constraints on the reservoir volume or level (xUnit: NOK, yUnit: NOK)


(objective:rsv_over_limit_penalty)=
### rsv_over_limit_penalty
Resulting total penalty cost when the volume of reservoirs with an attached flood gate goes over the physical maximum volume limits (xUnit: NOK, yUnit: NOK)


(objective:sim_rsv_penalty)=
### sim_rsv_penalty
Simulated total penalty cost when the maximum or minimum volume limits for all reservoirs during the optimization period are violated (xUnit: NOK, yUnit: NOK)


(objective:rsv_end_penalty)=
### rsv_end_penalty
Resulting total penalty cost when the maximum or minimum volume limits for all reservoirs at the end of the optimization period are violated (xUnit: NOK, yUnit: NOK)


(objective:load_penalty)=
### load_penalty
Resulting total penalty cost when load obligations are violated (xUnit: NOK, yUnit: NOK)


(objective:group_time_period_penalty)=
### group_time_period_penalty
Resulting total penalty cost when period sum constraints on the old ascii multi-object format are violated. Sum over all constraints (xUnit: NOK, yUnit: NOK)


(objective:group_time_step_penalty)=
### group_time_step_penalty
Resulting total penalty cost when time-dependent constraints on the old ascii multi-object format are violated. Sum over all constraints and time steps (xUnit: NOK, yUnit: NOK)


(objective:sum_ramping_penalty)=
### sum_ramping_penalty
Resulting total penalty cost when ramping sum constraints on the old ascii format are violated. Sum over all constraints and time steps (xUnit: NOK, yUnit: NOK)


(objective:plant_ramping_penalty)=
### plant_ramping_penalty
Resulting total penalty cost when plnat production ramping constraints are violated. Sum over all plants and time steps (xUnit: NOK, yUnit: NOK)


(objective:rsv_ramping_penalty)=
### rsv_ramping_penalty
Resulting total penalty cost when reservoir storage ramping constraints are violated. Sum over all reservoirs and time steps (xUnit: NOK, yUnit: NOK)


(objective:gate_ramping_penalty)=
### gate_ramping_penalty
Resulting total penalty cost when discharge ramping constraints on gates are violated. Sum over all gates and time steps (xUnit: NOK, yUnit: NOK)


(objective:contract_ramping_penalty)=
### contract_ramping_penalty
Resulting total penalty cost when contract ramping constraints are violated. Sum over all contracts and time steps (xUnit: NOK, yUnit: NOK)


(objective:group_ramping_penalty)=
### group_ramping_penalty
Resulting total penalty cost when time-dependent group ramping constraints on the old ascii format are violated. Sum over all constraints and time steps (xUnit: NOK, yUnit: NOK)


(objective:discharge_group_penalty)=
### discharge_group_penalty
Resulting total penalty cost when the allowed deviations for discharge groups are violated. Sum for both upward and downward violation over all discharge groups and time steps (xUnit: NOK, yUnit: NOK)


(objective:discharge_group_ramping_penalty)=
### discharge_group_ramping_penalty
Resulting total penalty cost when the discharge ramping constraints for discharge groups are violated. Sum for both upward and downward violation over all discharge groups and time steps (xUnit: NOK, yUnit: NOK)


(objective:production_group_energy_penalty)=
### production_group_energy_penalty
Resulting total penalty cost when the energy target production constraints on production groups are violated. Sum for both upward and downward violation over all production groups. (xUnit: NOK, yUnit: NOK)


(objective:production_group_power_penalty)=
### production_group_power_penalty
Resulting total penalty cost when the maximum or minimum power limit constraints on production groups are violated. Sum for both upward and downward violation over all production groups and time steps (xUnit: NOK, yUnit: NOK)


(objective:river_min_flow_penalty)=
### river_min_flow_penalty
Resulting total penalty for breaking the min_flow river constraints (xUnit: NOK, yUnit: NOK)


(objective:river_max_flow_penalty)=
### river_max_flow_penalty
Resulting total penalty for breaking the max_flow river constraints (xUnit: NOK, yUnit: NOK)


(objective:river_ramping_penalty)=
### river_ramping_penalty
Resulting total penalty cost when the discharge ramping constraints for rivers are violated. Sum for both upward and downward violation over all rivers and time steps (xUnit: NOK, yUnit: NOK)


(objective:river_flow_schedule_penalty)=
### river_flow_schedule_penalty
Resulting total penalty for breaking the flow_schedule river constraints (xUnit: NOK, yUnit: NOK)


(objective:river_gate_adjustment_penalty)=
### river_gate_adjustment_penalty
Resulting total penalty for adjusting the river gates according to the gate_adjustment_cost of each river (xUnit: NOK, yUnit: NOK)


(objective:common_decision_penalty)=
### common_decision_penalty
Penalty cost for violating common decision period constraints in decomposed multi-scenario optimization problems (xUnit: NOK, yUnit: NOK)


(objective:bidding_penalty)=
### bidding_penalty
Penalty cost for violating constraints for increasing bid volume when price increases in decomposed multi-scenario optimization problems (xUnit: NOK, yUnit: NOK)


(objective:safe_mode_universal_penalty)=
### safe_mode_universal_penalty
Penalty cost for all violated constraints when universal penalty is switched on to investigate infeasibility (xUnit: NOK, yUnit: NOK)


