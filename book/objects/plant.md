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

(plant)=
# plant
A hydropower plant which houses up to several hydropower generators and pumps

|   |   |
|---|---|
|Input connections|<a href="reservoir.html">reservoir</a>, <a href="generator.html">generator</a>, <a href="pump.html">pump</a>, <a href="junction.html">junction</a>, <a href="junction_gate.html">junction_gate</a>, <a href="creek_intake.html">creek_intake</a>, <a href="discharge_group.html">discharge_group</a>, <a href="production_group.html">production_group</a>, <a href="bid_group.html">bid_group</a>, <a href="tunnel.html">tunnel</a>, <a href="plant_reserve_capability.html">plant_reserve_capability</a>|
|Output connections|<a href="river.html">river</a>, <a href="reservoir.html">reservoir</a>, <a href="tunnel.html">tunnel</a>, <a href="junction.html">junction</a>, <a href="discharge_group.html">discharge_group</a>, <a href="production_group.html">production_group</a>, <a href="bid_group.html">bid_group</a>, <a href="generator.html">generator</a>, <a href="pump.html">pump</a>, <a href="plant_reserve_capability.html">plant_reserve_capability</a>|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```



## Examples
  - [](best-profit)
  - [](best-profit-basic-example)
  - [](maintenance-example)
  - [](ramping)
  

## References
  - An overview on formulations and optimization methods for the unit-based short-term hydro scheduling problem {cite}`Kong2020`
  - Dynamic incorporation of nonlinearity into MILP formulation for short-term hydro scheduling {cite}`Skjelbred2020`
  - A comparison of linear interpolation and spline interpolation for turbine efficiency curves in short-term hydropower scheduling problems {cite}`Zhang2019`
  - Calculation of power compensation for a pumped storage hydropower plant with hydraulic short-circuit operation {cite}`Skjelbred2017b`
  - Combining start-up costs with non-linear head optimization of hydro storage {cite}`Skjelbred2013`
  

## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "plant"].reset_index().iloc[:, 1:]
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

(plant:num_gen)=
### num_gen
Number of generators in the plant (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:num_pump)=
### num_pump
Number of pumps in the plant (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:less_distribution_eps)=
### less_distribution_eps
The tolerance level for heuristically distributing discharge on generators (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:latitude)=
### latitude
Reserved for future use (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:longitude)=
### longitude
Reserved for future use (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:ownership)=
### ownership
Percentage of ownership of plant in case of shared ownership. Used to scale generator efficiency curves accordingly. (xUnit: %, yUnit: %)


(plant:prod_area)=
### prod_area
Production from this plant will be sold in markets connected to the given production area (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:prod_area_flag)=
### prod_area_flag
Flag determining whether production area connection should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:prod_factor)=
### prod_factor
Optional fixed production factor for the plant in KWh/m3, which is used to convert between NOK/MWh and NOK/Mm3. If this is not specified (value of 0.0), SHOP will calculate a production factor for the plant based on best point operation given the initial plant head. (xUnit: KWH/MM3, yUnit: KWH/MM3)


(plant:outlet_line)=
### outlet_line
The level (meter above sea level) of the outlet tunnel from the plant (xUnit: METER, yUnit: METER)


(plant:intake_line)=
### intake_line
Minimum upper level used to calculate the height the pump must lift water to. The upper reservoir water level is used if it is above the value of intake_line (xUnit: NO_UNIT, yUnit: METER)


(plant:main_loss)=
### main_loss
The loss factor for the main tunnel of the plant (xUnit: S2/M5, yUnit: S2/M5)


(plant:penstock_loss)=
### penstock_loss
The list of loss factors for the penstocks of the plant (xUnit: S2/M5, yUnit: S2/M5)


(plant:tailrace_loss)=
### tailrace_loss
The head loss curve for the tailrace of the plant which can be modelled as an additional head loss related to the discharge of the plant (and bypass) (xUnit: M3/S, yUnit: METER)


(plant:tailrace_loss_from_bypass_flag)=
### tailrace_loss_from_bypass_flag
Flag determining whether the bypass discharge should be included in the calculation of tailrace loss (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:intake_loss)=
### intake_loss
The head loss curve for the intake of the plant which can be modelled as an additional head loss related to the discharge of the plant (and bypass) (xUnit: M3/S, yUnit: METER)


(plant:intake_loss_from_bypass_flag)=
### intake_loss_from_bypass_flag
Flag determining whether the bypass discharge should be included in the calculation of intake loss (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:tides)=
### tides
The change of plant head related to tides (xUnit: NO_UNIT, yUnit: DELTA_METER)


(plant:time_delay)=
### time_delay
The delay between the water leaving the plant and until it ends up in the downstream reservoir (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:shape_discharge)=
### shape_discharge
Describes the shape of the delayed discharge as a wave function of ratios per time step (xUnit: HOUR, yUnit: NO_UNIT)


(plant:discharge_fee)=
### discharge_fee
Extra cost for plant discharge referring to the time when it was discharged by the plant (xUnit: NO_UNIT, yUnit: NOK/MM3)


(plant:discharge_fee_flag)=
### discharge_fee_flag
Flag determining whether the discharge fee should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:discharge_cost_curve)=
### discharge_cost_curve
Extra cost depending on the discharge of the plant (xUnit: M3/S, yUnit: NOK/H/M3/S)


(plant:feeding_fee)=
### feeding_fee
Extra cost for feeding electricity into the grid. The feeding fee is added as an extra production cost in the objective function. (xUnit: NO_UNIT, yUnit: NOK/MWH)


(plant:feeding_fee_flag)=
### feeding_fee_flag
Flag determining whether the feed-in fee should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:production_fee)=
### production_fee
Fee that is used to reduce the sale price for energy delivered by this plant (xUnit: NO_UNIT, yUnit: NOK/MWH)


(plant:production_fee_flag)=
### production_fee_flag
Flag determining whether the production fee should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:consumption_fee)=
### consumption_fee
Fee that is used to increase the buy price for energy consumed by this plant (xUnit: NO_UNIT, yUnit: NOK/MWH)


(plant:consumption_fee_flag)=
### consumption_fee_flag
Flag determining whether the consumption fee should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:linear_startup_flag)=
### linear_startup_flag
Flag determining whether the plant should have linear startup costs when MIP is not active (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:maintenance_flag)=
### maintenance_flag
Flag determining whether the plant is out for maintenance or not (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:mip_flag)=
### mip_flag
Flag determining for which time steps to use binary variables to model generator startup and min production (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:mip_length)=
### mip_length
Set the binary variable length to another value other than the default length of one time step (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:mip_length_flag)=
### mip_length_flag
Flag determining whether the mip_length should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:gen_priority)=
### gen_priority
Prioritization for startup order of generators. If no generators have TXY priority, use this static generator priority (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:n_seg_down)=
### n_seg_down
The number of segments below the best efficiency point of the unit in the building of original PQ curve in incremental mode (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:n_seg_up)=
### n_seg_up
The number of segments above the best efficiency point of the unit in the building of original PQ curve in incremental mode (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:n_mip_seg_down)=
### n_mip_seg_down
The number of segments below the best efficiency point of the unit in the building of original PQ curve in full mode (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:n_mip_seg_up)=
### n_mip_seg_up
The number of segments below the best efficiency point of the unit in the building of original PQ curve in full mode (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:dyn_pq_seg_flag)=
### dyn_pq_seg_flag
Flag determining whether dynamically define the segments in the building of the original PQ curve for all the units in this plant in incremental mode (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:dyn_mip_pq_seg_flag)=
### dyn_mip_pq_seg_flag
Flag determining whether dynamically define the segments in the building of the original PQ curve for all the units in this plant in full mode (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:build_original_pq_curves_by_turb_eff)=
### build_original_pq_curves_by_turb_eff
Flag determining whether the original PQ curve should be built by the turbine efficiecny curves of the unit or all the operating limits (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:min_p_constr)=
### min_p_constr
Time-dependent minimum production limit for the plant (xUnit: NO_UNIT, yUnit: MW)


(plant:min_p_constr_flag)=
### min_p_constr_flag
Flag determining whether the time-dependent minimum production limit for the plant should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:min_p_penalty_flag)=
### min_p_penalty_flag
Flag determining whether the time-dependent minimum production limit for the plant should be a hard or soft constraint: 0 = hard; 1 = soft (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:min_p_penalty_cost)=
### min_p_penalty_cost
Given penalty cost for violating the time-dependent minimum production limit for the plant (if min_p_penalty_flag is set as 1) (xUnit: NO_UNIT, yUnit: NOK/MWH)


(plant:min_p_penalty_cost_flag)=
### min_p_penalty_cost_flag
Flag determining whether the cost for violating the minimum production constraint should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:max_p_constr)=
### max_p_constr
Time-dependent maximum production limit for the plant (xUnit: NO_UNIT, yUnit: MW)


(plant:max_p_constr_flag)=
### max_p_constr_flag
Flag determining whether the time-dependent maximum production limit for the plant should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:max_p_penalty_flag)=
### max_p_penalty_flag
Flag determining whether the time-dependent maximum production limit for the plant should be a hard or soft constraint: 0 = hard; 1 = soft (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:max_p_penalty_cost)=
### max_p_penalty_cost
Given penalty cost for violating the time-dependent maximum production limit for the plant (if max_p_penalty_flag is set as 1) (xUnit: NO_UNIT, yUnit: NOK/MWH)


(plant:max_p_penalty_cost_flag)=
### max_p_penalty_cost_flag
Flag determining whether the cost for violating the maximum production constraint should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:min_q_constr)=
### min_q_constr
Time-dependent minimum discharge limit for the plant (xUnit: NO_UNIT, yUnit: M3/S)


(plant:min_q_constr_flag)=
### min_q_constr_flag
Flag determining whether the time-dependent minimum discharge limit for the plant should be included in the optimization (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:min_q_penalty_flag)=
### min_q_penalty_flag
Flag determining whether the time-dependent minimum discharge limit for the plant should be a hard or soft constraint: 0 = hard; 1 = soft (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:min_q_penalty_cost)=
### min_q_penalty_cost
Given penalty cost for violating the time-dependent minimum discharge limit for the plant (if min_q_penalty_flag is set as 1) (xUnit: NO_UNIT, yUnit: NOK/MM3)


(plant:min_q_penalty_cost_flag)=
### min_q_penalty_cost_flag
Flag determining whether the cost for violating the minimum discharge constraint should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:max_q_constr)=
### max_q_constr
Time-dependent maximum discharge limit for the plant (xUnit: NO_UNIT, yUnit: M3/S)


(plant:max_q_constr_flag)=
### max_q_constr_flag
Flag determining whether the time-dependent maximum discharge limit for the plant should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:max_q_penalty_flag)=
### max_q_penalty_flag
Flag determining whether the time-dependent maximum discharge limit for the plant should be a hard or soft constraint: 0 = hard; 1 = soft (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:max_q_penalty_cost)=
### max_q_penalty_cost
Given penalty cost for violating the time-dependent maximum discharge limit for the plant by (if max_q_penalty_flag is set as 1) (xUnit: NO_UNIT, yUnit: NOK/MM3)


(plant:max_q_penalty_cost_flag)=
### max_q_penalty_cost_flag
Flag determining whether the cost for violating the maximum discharge constraint should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:max_q_limit_rsv_up)=
### max_q_limit_rsv_up
Maximum plant discharge limit (m3/s) and upstream reservoir water level (meter above sea level) relation (xUnit: METER, yUnit: M3/S)


(plant:max_q_limit_rsv_down)=
### max_q_limit_rsv_down
Maximum plant discharge limit (m3/s) and downstream reservoir water level (meter above sea level) relation (xUnit: METER, yUnit: M3/S)


(plant:production_schedule)=
### production_schedule
Plant production schedule (xUnit: NO_UNIT, yUnit: MW)


(plant:production_schedule_flag)=
### production_schedule_flag
Flag determining whether the plant production schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:discharge_schedule)=
### discharge_schedule
Discharge schedule (xUnit: NO_UNIT, yUnit: M3/S)


(plant:discharge_schedule_flag)=
### discharge_schedule_flag
Flag determining whether the plant discharge schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:consumption_schedule)=
### consumption_schedule
Plant consumption schedule (xUnit: NO_UNIT, yUnit: MW)


(plant:consumption_schedule_flag)=
### consumption_schedule_flag
Flag determining whether the plant consumption schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:upflow_schedule)=
### upflow_schedule
Plant upflow schedule (xUnit: NO_UNIT, yUnit: M3/S)


(plant:upflow_schedule_flag)=
### upflow_schedule_flag
Flag determining whether the plant upflow schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:sched_penalty_cost_down)=
### sched_penalty_cost_down
Given penalty cost for deviating below the plant schedule (xUnit: NOK, yUnit: NOK)


(plant:sched_penalty_cost_up)=
### sched_penalty_cost_up
Given penalty cost for deviating above the plant schedule (xUnit: NOK, yUnit: NOK)


(plant:power_ramping_up)=
### power_ramping_up
Maximum limit for increase in plant production per hour (xUnit: NO_UNIT, yUnit: MW_HOUR)


(plant:power_ramping_down)=
### power_ramping_down
Maximum limit for decrease in plant production per hour (xUnit: NO_UNIT, yUnit: MW_HOUR)


(plant:discharge_ramping_up)=
### discharge_ramping_up
Maximum limit for increase in plant discharge per hour (xUnit: NO_UNIT, yUnit: M3SEC_HOUR)


(plant:discharge_ramping_down)=
### discharge_ramping_down
Maximum limit for decrease in plant discharge per hour (xUnit: NO_UNIT, yUnit: M3SEC_HOUR)


(plant:block_merge_tolerance)=
### block_merge_tolerance
Maximum deviation in production between two time steps that allows SHOP to force these hours to have the same production in later iterations (xUnit: NO_UNIT, yUnit: MW)


(plant:block_generation_mwh)=
### block_generation_mwh
Gives a constant production for the plant in one or more blocks of time steps (xUnit: NO_UNIT, yUnit: HOUR)


(plant:block_generation_m3s)=
### block_generation_m3s
Gives a constant discharge for the plant in one or more blocks of time steps (xUnit: NO_UNIT, yUnit: HOUR)


(plant:frr_up_min)=
### frr_up_min
Minimum FRR_UP delivery for the plant (xUnit: NO_UNIT, yUnit: MW)


(plant:frr_up_max)=
### frr_up_max
Maximum FRR_UP delivery for the plant (xUnit: NO_UNIT, yUnit: MW)


(plant:frr_down_min)=
### frr_down_min
Minimum FRR_DOWN delivery for the plant (xUnit: NO_UNIT, yUnit: MW)


(plant:frr_down_max)=
### frr_down_max
Maximum FRR_DOWN delivery for the plant (xUnit: NO_UNIT, yUnit: MW)


(plant:rr_up_min)=
### rr_up_min
Minimum RR_UP delivery for the plant (xUnit: NO_UNIT, yUnit: MW)


(plant:frr_symmetric_flag)=
### frr_symmetric_flag
Flag determining whether all the generators in the plant should deliver both FRR_UP and FRR_DOWN as long as they are assigned for the FRR reserve (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:bp_dyn_wv_flag)=
### bp_dyn_wv_flag
Flag determining whether water values in the best profit calculation should be based on dynamic results per time step from the optimization or the static end value description (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:ref_prod)=
### ref_prod
Production of the plant indicating the planned operating point as starting point for the best profit calculation (xUnit: NO_UNIT, yUnit: MW)


(plant:plant_unbalance_recommit)=
### plant_unbalance_recommit
Flag determining whether the generators in the plant should be recommitted when the optimization model changes from full mode to incremental mode and the resulting plant discharge is smaller than the optimal discharge from solver (xUnit: NO_UNIT, yUnit: NO_UNIT)


(plant:spinning_reserve_up_max)=
### spinning_reserve_up_max
Sets a maximum limit for the sum of spinning reserves delivered in the upward direction for the plant. The sum ranges over reserves delivered on all generators and pumps in the plant (xUnit: NO_UNIT, yUnit: MW)


(plant:spinning_reserve_down_max)=
### spinning_reserve_down_max
Sets a maximum limit for the sum of spinning reserves delivered in the downward direction for the plant. The sum ranges over reserves delivered on all generators and pumps in the plant (xUnit: NO_UNIT, yUnit: MW)


(plant:production)=
### production
Resulting plant production, i.e. sum of resulting generator production (xUnit: NO_UNIT, yUnit: MW)


(plant:solver_production)=
### solver_production
Preliminary result for the sum of generator production that is returned by the linearized optimization problem (xUnit: NO_UNIT, yUnit: MW)


(plant:sim_production)=
### sim_production
Simulated plant production (xUnit: NO_UNIT, yUnit: MW)


(plant:prod_unbalance)=
### prod_unbalance
Difference between the result of the non-linear post-calculation (production) and the production determined by the linear optimization problem (solver_production) (xUnit: NO_UNIT, yUnit: MW)


(plant:consumption)=
### consumption
Resulting plant consumption, i.e. sum of resulting pump consumption (xUnit: NO_UNIT, yUnit: MW)


(plant:sim_consumption)=
### sim_consumption
Simulated plant consumption, i.e. sum of resulting pump consumption (xUnit: NO_UNIT, yUnit: MW)


(plant:solver_consumption)=
### solver_consumption
Preliminary result for the sum of pump consumption that is returned by the linearized optimization problem (xUnit: NO_UNIT, yUnit: MW)


(plant:cons_unbalance)=
### cons_unbalance
Difference between the result of the non-linear post-calculation (consumption) and the consumption determined by the linear optimization problem (solver_consumption) (xUnit: NO_UNIT, yUnit: MW)


(plant:discharge)=
### discharge
Resulting plant discharge, i.e. sum of resulting generator discharge (xUnit: NO_UNIT, yUnit: M3/S)


(plant:solver_discharge)=
### solver_discharge
Preliminary result for the sum of generator discharge that is returned by the linearized optimization problem (xUnit: NO_UNIT, yUnit: M3/S)


(plant:sim_discharge)=
### sim_discharge
Simulated plant discharge (xUnit: NO_UNIT, yUnit: M3/S)


(plant:upflow)=
### upflow
Resulting plant upflow, i.e. sum of resulting pump upflow (xUnit: NO_UNIT, yUnit: M3/S)


(plant:sim_upflow)=
### sim_upflow
Simulated plant upflow, i.e. sum of resulting pump upflow (xUnit: NO_UNIT, yUnit: M3/S)


(plant:solver_upflow)=
### solver_upflow
Preliminary result for the sum of pump upflow that is returned by the linearized optimization problem (xUnit: NO_UNIT, yUnit: M3/S)


(plant:gross_head)=
### gross_head
Plant gross head, i.e. the difference between upstream reservoir water level and MAX(plant outlet_line, downstream reservoir water level) (xUnit: NO_UNIT, yUnit: METER)


(plant:eff_head)=
### eff_head
Resulting plant effective head. If overall generating, effective plant head is defined as the lowest eff_head of the generators. If overall pumping, effective plant head is defined as the highest eff_head of the pumps. (xUnit: NO_UNIT, yUnit: METER)


(plant:head_loss)=
### head_loss
Plant head loss, i.e. the plant gross head minus the lowest effective head of the unit in the plant. If overall generating, plant head loss is positive. If overall pumping, plant head loss is negative. (xUnit: NO_UNIT, yUnit: METER)


(plant:min_p_penalty)=
### min_p_penalty
Resulting penalty when the time-dependent maximum production limit for the plant is violated (xUnit: NO_UNIT, yUnit: MW)


(plant:max_p_penalty)=
### max_p_penalty
Resulting penalty when the time-dependent maximum production limit for the plant is violated (xUnit: NO_UNIT, yUnit: MW)


(plant:min_q_penalty)=
### min_q_penalty
Resulting penalty when the time-dependent minimum discharge limit for the plant is violated (xUnit: NO_UNIT, yUnit: MM3)


(plant:max_q_penalty)=
### max_q_penalty
Resulting penalty when the time-dependent maximum discharge limit for the plant is violated (xUnit: NO_UNIT, yUnit: MM3)


(plant:p_constr_penalty)=
### p_constr_penalty
Resulting penalty cost when the time-dependent maximum or minimum production limit for the plant is violated (xUnit: NO_UNIT, yUnit: NOK)


(plant:q_constr_penalty)=
### q_constr_penalty
Resulting penalty cost when the time-dependent maximum or minimum discharge limit for the plant is violated (xUnit: NO_UNIT, yUnit: NOK)


(plant:schedule_up_penalty)=
### schedule_up_penalty
Resulting penalty when deviating above the plant schedule (xUnit: NO_UNIT, yUnit: NOK)


(plant:schedule_down_penalty)=
### schedule_down_penalty
Resulting penalty when deviating below the plant schedule (xUnit: NO_UNIT, yUnit: NOK)


(plant:schedule_penalty)=
### schedule_penalty
Resulting penalty cost for violation of the plant schedule (xUnit: NO_UNIT, yUnit: NOK)


(plant:best_profit_q)=
### best_profit_q
Plant discharge after changing the production of the plant from the current operating point to a new point in the best profit curve of the plant (xUnit: MW, yUnit: M3/S)


(plant:best_profit_mc)=
### best_profit_mc
Marginal production cost after changing the production of the plant from the current operating point to a new point in the best profit curve of the plant (xUnit: MW, yUnit: NOK/MW)


(plant:best_profit_ac)=
### best_profit_ac
Average production cost after changing the production of the plant from the current operating point to a new point in the best profit curve of the plant (xUnit: MW, yUnit: NOK/MW)


(plant:best_profit_commitment_cost)=
### best_profit_commitment_cost
Sum of startup costs or shutdown costs after changing the production of the plant from the current operating point to a new point in the best profit curve of the plant (xUnit: MW, yUnit: NOK)


(plant:best_profit_bid_matrix)=
### best_profit_bid_matrix
A plant bid matrix created by reducing the best_profit_mc curves when the command 'print bp_bid_matrix' is called. The maximum number of price columns in the bid matrix is set by the attribute bp_bid_matrix_points on the global_settings object. (xUnit: MW, yUnit: NOK/MW)


(plant:times_of_wrong_pq_uploading)=
### times_of_wrong_pq_uploading
How many times the unit PQ segments are wrongly uploaded, i.e. the latter segments are fulfilled first. (xUnit: NO_UNIT, yUnit: NO_UNIT)


