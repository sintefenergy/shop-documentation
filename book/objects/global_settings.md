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

(global_settings)=
# global_settings
A singleton object that contains global settings such as penalty cost values. A single global_settings object with the name 'global_settings' is automatically created when SHOP is initialized

|   |   |
|---|---|
|Input connections||
|Output connections||
|License|SHOP_OPEN|
|Release version|14.0.0.1|

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
object_attributes = table[table["Object type"] == "global_settings"].reset_index().iloc[:, 1:]
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

(global_settings:load_penalty_flag)=
### load_penalty_flag
Turn on (1, default) or off (0) the creation of load penalty variables to add to the load balance constraint. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:rsv_penalty_flag)=
### rsv_penalty_flag
Turn on (1, default) or off (0) the addition of reservoir storage penalty variables. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:volume_ramp_penalty_flag)=
### volume_ramp_penalty_flag
Turn on (1, default) or off (0) the addition of penalty variables for volume ramping on reservoir. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:level_ramp_penalty_flag)=
### level_ramp_penalty_flag
Turn on (1, default) or off (0) the addition of penalty variables for level ramping on reservoir. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:production_ramp_penalty_flag)=
### production_ramp_penalty_flag
Turn on (1, default) or off (0) the addition of penalty variables for power ramping on plant production. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:plant_min_q_penalty_flag)=
### plant_min_q_penalty_flag
Turn on (1) or off (0) the addition of penalty variables to the min discharge restrictions on all plants. Default value -1 uses the min_q_penalty_flag specified on each plant to decide if the penalty variables should be added. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:plant_min_p_penalty_flag)=
### plant_min_p_penalty_flag
Turn on (1) or off (0) the addition of penalty variables to the min power restrictions on all plants. Default value -1 uses the min_p_penalty_flag specified on each plant to decide if the penalty variables should be added. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:plant_max_q_penalty_flag)=
### plant_max_q_penalty_flag
Turn on (1) or off (0) the addition of penalty variables to the max discharge restrictions on all plants. Default value -1 uses the max_q_penalty_flag specified on each plant to decide if the penalty variables should be added. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:plant_max_p_penalty_flag)=
### plant_max_p_penalty_flag
Turn on (1) or off (0) the addition of penalty variables to the max power restrictions on all plants. Default value -1 uses the max_p_penalty_flag specified on each plant to decide if the penalty variables should be added. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:gate_min_q_penalty_flag)=
### gate_min_q_penalty_flag
Turn on (1) or off (0) the addition of penalty variables to the min discharge restrictions on all gates. Default value -1 uses the min_q_penalty_flag specified on each gate to decide if the penalty variables should be added. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:gate_max_q_penalty_flag)=
### gate_max_q_penalty_flag
Turn on (1) or off (0) the addition of penalty variables to the max discharge restrictions on all gates. Default value -1 uses the max_q_penalty_flag specified on each gate to decide if the penalty variables should be added. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:gate_ramp_penalty_flag)=
### gate_ramp_penalty_flag
Turn on (1, default) or off (0) the addition of penalty variables to the gate ramping restrictions. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:plant_schedule_penalty_flag)=
### plant_schedule_penalty_flag
Turn on (1, default) or off (0) the addition of penalty variables to allow breaking the plant production or discharge schedule. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:gen_discharge_schedule_penalty_flag)=
### gen_discharge_schedule_penalty_flag
Turn on (1, default) or off (0) the addition of penalty variables to allow breaking the generator discharge schedule. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:pump_schedule_penalty_flag)=
### pump_schedule_penalty_flag
Turn on (1, default) or off (0) the addition of penalty variables to allow breaking the pump consumption or upflow schedule. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:power_limit_penalty_flag)=
### power_limit_penalty_flag
Turn on (1, default) or off (0) the addition of penalty variables to allow breaking the sum power limits for a group of plants. Can also be set with the command 'penalty flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:power_limit_penalty_cost)=
### power_limit_penalty_cost
The penalty cost for breaking the constraints limiting the sum power output for a group of plants. Default value is 50000 NOK/MWh. Can also be set with the command 'penalty cost'. (xUnit: NOK/MWH, yUnit: NOK/MWH)


(global_settings:load_penalty_cost)=
### load_penalty_cost
The penalty cost for not fulfilling the load obligation. Default value is 5000 NOK/MWh. Can also be set with the command 'penalty cost'. (xUnit: NOK/MWH, yUnit: NOK/MWH)


(global_settings:rsv_penalty_cost)=
### rsv_penalty_cost
The penalty cost for breaking the reservoir water balance constraints. Default value is 10,000,000 NOK/Mm3. Can also be set with the command 'penalty cost'. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:rsv_hard_limit_penalty_cost)=
### rsv_hard_limit_penalty_cost
The penalty cost for breaking the hard min/max volume or head limit constraints on all reservoirs. Default value is 9,000,000 NOK/Mm3. Can also be set with the command 'set rsv_hard_limit_penalty_cost'. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:volume_ramp_penalty_cost)=
### volume_ramp_penalty_cost
The penalty cost for breaking the reservoir volume ramping constraints. Default value is 100 NOK/MM3. Can also be set with the command 'penalty cost'. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:level_ramp_penalty_cost)=
### level_ramp_penalty_cost
The penalty cost for breaking the reservoir level ramping constraints. Default value is 100 NOK/METER (xUnit: NOK/METER, yUnit: NOK/METER)


(global_settings:production_ramp_penalty_cost)=
### production_ramp_penalty_cost
The penalty cost for breaking the plant power production ramping constraints. Default value is 100 NOK/MWh. Can also be set with the command 'penalty cost'. (xUnit: NOK/MWH, yUnit: NOK/MWH)


(global_settings:plant_soft_p_penalty)=
### plant_soft_p_penalty
The penalty cost for breaking max and min power production constraints on plant level if max_p_penalty_cost and min_p_penalty_cost are not set for the plant. Default value is 100 NOK/MWh. Can also be set with the command 'penalty cost'. (xUnit: NOK/MWH, yUnit: NOK/MWH)


(global_settings:plant_soft_q_penalty)=
### plant_soft_q_penalty
The penalty cost for breaking max and min discharge constraints on plant level if max_q_penalty_cost and min_q_penalty_cost are not set for the plant. Default value is 100000 NOK/Mm3. Can also be set with the command 'penalty cost'. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:plant_sched_penalty_cost_up)=
### plant_sched_penalty_cost_up
The penalty cost for breaking the plant production or discharge schedules in upward direction. Default value is 1000000 NOK/MWh or 1000000 NOK/Mm3. (xUnit: NOK, yUnit: NOK)


(global_settings:plant_sched_penalty_cost_down)=
### plant_sched_penalty_cost_down
The penalty cost for breaking the plant production or discharge schedules in downward direction. Default value is 1000000 NOK/MWh or 1000000 NOK/Mm3. (xUnit: NOK, yUnit: NOK)


(global_settings:gen_discharge_sched_penalty_cost_up)=
### gen_discharge_sched_penalty_cost_up
The penalty cost for breaking the generator discharge schedule in upward direction. Default value is 1000000 NOK/Mm3. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:gen_discharge_sched_penalty_cost_down)=
### gen_discharge_sched_penalty_cost_down
The penalty cost for breaking the generator discharge schedules in downward direction. Default value is 1000000 NOK/Mm3. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:pump_sched_penalty_cost_up)=
### pump_sched_penalty_cost_up
The penalty cost for breaking the pump production or discharge schedules in upward direction. Default value is 1000000 NOK/MWh or 1000000 NOK/Mm3. (xUnit: NOK, yUnit: NOK)


(global_settings:pump_sched_penalty_cost_down)=
### pump_sched_penalty_cost_down
The penalty cost for breaking the pump production or discharge schedules in downward direction. Default value is 1000000 NOK/MWh or 1000000 NOK/Mm3. (xUnit: NOK, yUnit: NOK)


(global_settings:gate_ramp_penalty_cost)=
### gate_ramp_penalty_cost
The penalty cost for breaking the gate discharge ramping constraints. Default value is 360 NOK/(m3/s). Can also be set with the command 'penalty cost'. (xUnit: NOK/M3/S, yUnit: NOK/M3/S)


(global_settings:discharge_group_penalty_cost)=
### discharge_group_penalty_cost
The penalty cost for breaking the discharge group constraints. Default value is 1000000 NOK/Mm3. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:reserve_schedule_penalty_cost)=
### reserve_schedule_penalty_cost
The penalty cost for breaking the unit reserve schedule constraints. Default value is 10000 NOK/MW. Can also be set with the command 'set reserve_schedule_penalty_cost'. (xUnit: NOK/MW, yUnit: NOK/MW)


(global_settings:reserve_group_penalty_cost)=
### reserve_group_penalty_cost
The penalty cost for delivering less than the reserve obligations of any reserve type in any reserve group. Default value is 10000 NOK/MW. Can also be set with the command 'set reserve_penalty_cost'. (xUnit: NOK/MW, yUnit: NOK/MW)


(global_settings:bypass_cost)=
### bypass_cost
The cost of discharging water in bypass gates. Default value is 0.01 NOK/Mm3. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:gate_cost)=
### gate_cost
The cost of discharging water in regular gates. Default value is 0 NOK/Mm3. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:overflow_cost)=
### overflow_cost
The cost of discharging water in spill gates. Default value is 50000 NOK/Mm3. Can also be set with the command 'penalty cost'. (xUnit: NOK/MM3, yUnit: NOK/MM3)


(global_settings:overflow_cost_time_factor)=
### overflow_cost_time_factor
A small negative cost element added to the spillage cost to avoid all flooding to occur at the end of the optimization period. Default value is -0.000001 NOK/Mm3/h. Can also be set with the command 'penalty cost'. (xUnit: NOK/MM3H, yUnit: NOK/MM3H)


(global_settings:gen_reserve_ramping_cost)=
### gen_reserve_ramping_cost
The cost for ramping on the reserves delivered by the generators if unit specific costs are not provided. Default value is 0 NOK/MW. Can also be set with the command 'set reserve_ramping_cost'. (xUnit: NOK/MW, yUnit: NOK/MW)


(global_settings:pump_reserve_ramping_cost)=
### pump_reserve_ramping_cost
The cost for ramping on the reserves delivered by the pumps if unit specific costs are not provided. Default value is 0 NOK/MW. Can also be set with the command 'set reserve_ramping_cost'. (xUnit: NOK/MW, yUnit: NOK/MW)


(global_settings:reserve_contribution_cost)=
### reserve_contribution_cost
The cost for a unit participating in the reserve delivery. Default value is 0 NOK/MW. Can also be set with the command 'set reserve_contribution_cost'. (xUnit: NOK, yUnit: NOK)


(global_settings:gate_ramp_cost)=
### gate_ramp_cost
The cost of ramping on gate discharge. Default value is 0 NOK/(m3/s). (xUnit: NOK/M3/S, yUnit: NOK/M3/S)


(global_settings:reserve_group_slack_cost)=
### reserve_group_slack_cost
The cost for delivering more than the reserve obligations of any reserve type in any reserve group. Default value is 0.000001 NOK/MW. Can also be set with the command 'set reserve_slack_cost'. (xUnit: NOK/MW, yUnit: NOK/MW)


(global_settings:use_heuristic_basis)=
### use_heuristic_basis
If this parameter is set to 1 a heuristic start basis is given to CPLEX, while a value of 0 (default) does not provide CPLEX with a start basis guess. Can also be set with the command 'set optbasis'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:nodelog)=
### nodelog
Set the MIP node logging interval (100 is default) used by CPLEX when updating the CPLEX log file. Can also be set with the command 'set mip_nodelog'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:max_num_threads)=
### max_num_threads
Set the max number of threads CPLEX can use when solving a MIP problem or using the barrier solver. Default of -1 lets CPLEX use all available threads. Can also be set with the command 'set max_num_threads' (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:parallelmode)=
### parallelmode
Choose the parallel mode CPLEX uses when solving a problem in parallel: 1 (default) gives deterministic result behaviour while -1 lets CPLEX fully utilize the parallel processing. A value of 0 lts CPLEX choose based on the problem. Can also be set with the command 'set parallel_mode'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:timelimit)=
### timelimit
Maximal number of seconds that can be used to solve a SHOP iteration in CPLEX. Default value is 900 s. Can also be set with the command 'set timelimit'. (xUnit: SECOND, yUnit: SECOND)


(global_settings:mipgap_rel)=
### mipgap_rel
The maximal relative objective function gap between final integer solution and best bound in CPLEX. Default value is -1 which uses default CPLEX relative MIP gap. Can also be set with the command 'set mipgap'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:mipgap_abs)=
### mipgap_abs
The maximal objective function gap between final integer solution and best bound in CPLEX. Default value is -1 which uses default CPLEX absolute MIP gap. Can also be set with the command 'set mipgap'. (xUnit: NOK, yUnit: NOK)


(global_settings:inteps)=
### inteps
Numerical tolerance for when CPLEX will consider a decimal number to be integer. Default value is 0.00001. Can also be set with the command 'set inteps'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:input_basis_name)=
### input_basis_name
Name of the file containing a saved input basis for the optimization problem is saved. If no name is given, no input basis will be loaded. Can also be set with the command 'read optbasis'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:output_basis_name)=
### output_basis_name
Name of the file where the optimal basis from the optimization problem in the next iteration is saved. If no name is given, no basis will be saved. Can also be set with the command 'save optbasis'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:solver_algorithm)=
### solver_algorithm
Name of the solution algorithm CPLEX will use to solve linear problems, can be either 'PRIMAL', 'DUAL' (default), 'BARRIER', 'NETPRIMAL', 'NETDUAL', or 'CONCURRENT'. Can also be set with the command 'set method'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:n_seg_up)=
### n_seg_up
Number of segments to be used above best efficient point in incremental mode. Can also be set with the command 'set nseg'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:n_seg_down)=
### n_seg_down
Number of segments to be used below best efficient point in incremental mode. Can also be set with the command 'set nseg'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:n_mip_seg_up)=
### n_mip_seg_up
Number of segments to be used above best efficient point in full mode. Can also be set with the command 'set nseg'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:n_mip_seg_down)=
### n_mip_seg_down
Number of segments to be used below best efficient point in full mode. Can also be set with the command 'set nseg'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:dyn_pq_seg_flag)=
### dyn_pq_seg_flag
Flag determining whether dynamically define the segments in the building of the original PQ curve for all the units in incremental mode if no flag series on the plant is provided. Can also be set with the command 'set dyn_seg'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:dyn_mip_pq_seg_flag)=
### dyn_mip_pq_seg_flag
Flag determining whether dynamically define the number of points of the original PQ curve for all the units in full mode if no flag series on the plant or generator is provided. Can also be set with the command 'set dyn_seg'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:bypass_segments)=
### bypass_segments
Change the number of variables used to describe the flow in bypass gates. Default number of segments is 1. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:gate_segments)=
### gate_segments
Change the number of variables used to describe the flow in regular gates. Default number of segments is 3. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:overflow_segments)=
### overflow_segments
Change the number of variables used to describe the flow in spill gates. Default number of segments is 3. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:gravity)=
### gravity
The value of the acceleration due to gravity. Default value is 9.81 m/s2. Can also be set with the command 'set gravity'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:gen_reserve_min_free_cap_factor)=
### gen_reserve_min_free_cap_factor
The fraction of the maximal generator production that must be left open while the generator is delivering FCR. Default value is 0.02. Can also be set with the command 'set reserve_min_capacity'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:fcr_n_band)=
### fcr_n_band
The size of the frequency range in either direction where FCR-N is activated. Default value is 0.1 Hz (49.9 to 50.1 Hz). Can also be set with the command 'set fcr_n_band'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:fcr_d_band)=
### fcr_d_band
The size of the frequency range in upward direction where FCR-D is activated. Default value is 0.4 Hz (49.5 to 49.9 Hz). Can also be set with the command 'set fcr_d_band'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:universal_mip)=
### universal_mip
Toggle the use of binary variables for generator and pump unit commitment on (1) or off (0). Default value of -1 uses mip_flag on each plant to decide if binary variables should be used. Can also be set by the command 'set universal_mip'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:universal_overflow_mip)=
### universal_overflow_mip
Toggle the use of binary variables to for reservoir to prevent non-physical spill. Default value of -1 uses overflow_mip_flag on each reservoir to decide if binary variables should be used. Can also be set by the command 'set universal_overflow_mip'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:linear_startup)=
### linear_startup
Toggle the building of liner startup and shutdown costs for generators and pumps on (1) or off (0) when MIP is not active. Default value of -1 uses linear_startup_flag on each plant to decide if startup and shutdown costs should be used. Can also be set by the command 'set linear_startup'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:dyn_flex_mip_steps)=
### dyn_flex_mip_steps
Set the number of time steps used for dynamic flexible MIP. Default value of -1 turns off the dynamic flexible MIP functionality. Can also be set with the command 'set dyn_flex_mip'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:merge_blocks)=
### merge_blocks
Turn on (1) or off (0, default) the mering of similar and adjacent time steps for gate discharge and plant production results. A value of 2 will only keep merged blocks from the previous iteration and stop further merging. Can also be set with the command 'set merge'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:power_head_optimization)=
### power_head_optimization
Turn on (1, default) or off (0) power head optimization functionality. Can also be set with the command 'set power_head_optimization'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:droop_discretization_limit)=
### droop_discretization_limit
Set the limit for fixing the droop value of all units that have a resulting droop below the specified limit. The droop is fixed to the closest legal discrete value below the given limit, which is the closest integer below unless the unit has a defined discrete_droop_values attribute. Default value is 0.0. Can also be set with the command 'set discrete_droop_limit'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:droop_cost_exponent)=
### droop_cost_exponent
Set this value to any positive number higher than 1.0 to build a convex and increasing cost curve for the droop value instead of using a linear cost. The number represents the degree of the convex polynomial used to build the cost curve, which means that a value of 2.0 results in a quadratic cost curve. Can also be set with the command 'set droop_cost_exponent'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:droop_ref_value)=
### droop_ref_value
Used to scale the exponential droop cost when the droop_cost_exponent is higher than 1. The exponential cost will be the same as the standard linear cost for the reference value. Can also be set with the command 'set droop_ref_value'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:create_cuts)=
### create_cuts
Turn on (1) or off (0, default) the createion of cuts for the start time of the SHOP run. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:print_sim_inflow)=
### print_sim_inflow
Turn on (1) or off (0, default) the printing of simulated inflow to the simulation result text files. Can also be set with the command 'start shopsim'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:pump_head_optimization)=
### pump_head_optimization
Turn on (1) or off (0, default) the inclusion of pump variables in the power head optimization. Can also be set with the command 'set power_head_optimization'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:save_pq_curves)=
### save_pq_curves
Turn on (1) or off (0, default) the saving of the constructed PQ curves for each unit. Can also be set with the command 'save pq_curves'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:build_original_pq_curves_by_turb_eff)=
### build_original_pq_curves_by_turb_eff
Turn on (1) or off (0, default) the building of the original PQ curves by only interpolating the first points/last points of the turbine efficiency curves. Can also be set with the command 'set build_original_pq_curves_by_turb_eff'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:plant_unbalance_recommit)=
### plant_unbalance_recommit
Turn on (1) or off (0, default) the heuristic that attempts to recommit units in a better way for hours without MIP and the resulting plant discharge is smaller than the optimal discharge from solver. Can also be set with the command 'set plant_unbalance_recommit'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:prefer_start_vol)=
### prefer_start_vol
Turn on (1, default) or off (0) the preference of start_vol over start_head for reservoirs where both are specified. Initial water level will be preferred if this attribute is set to zero. Can also be set with the command 'set initial_reservoir'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:bp_print_discharge)=
### bp_print_discharge
... Can also be set with the command 'print bp_curves'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:prod_from_ref_prod)=
### prod_from_ref_prod
... Can also be set with the command 'set prod_from_ref_prod'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:bp_min_points)=
### bp_min_points
... Can also be set with the command 'set min_bp_points'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:bp_mode)=
### bp_mode
Turn on (1) or off (0, default)... Can also be set with the command 'print bp_curves'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:stop_cost_from_start_cost)=
### stop_cost_from_start_cost
Turn on (1) or off (0, default) the usage of the input generator start cost as stop cost. Can also be set with the command 'set stop_cost_from_start_cost'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:ownership_scaling)=
### ownership_scaling
Turn on (1) or off (0, default) the rescaling of the production results for plants and generators that have an ownership less than 100. The scaled results are only found in the text result files. Can also be set with the command 'set ownership_scaling'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:time_delay_unit)=
### time_delay_unit
Specifies the time unit of the time delay for plants, gates, etc. in the system. Must be either 'MINUTE', 'HOUR' or 'TIME_STEP_LENGTH' (default). Can also be set with the command 'set time_delay_unit'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:bypass_loss)=
### bypass_loss
Turn on (1) or off (0, default) the addition of the flow in bypass gates when calculating tailrace loss for plants if tailrace_loss_from_bypass_flag is not used. Can also be set with the command 'set bypass_loss'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:gen_turn_off_limit)=
### gen_turn_off_limit
A decimal number between 0 and 1 that signifies if the generator operates below the fraction (the decimal number) of its minimum operating limit in full mode without MIP, the generator will be turned off. Default value is 0.5. Can also be set with the command 'set gen_turn_off_limit'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:pump_turn_off_limit)=
### pump_turn_off_limit
A decimal number between 0 and 1 that signifies if the pump operates below the fraction (the decimal number) of its minimum operating limit in full mode without MIP, the pump will be turned off. Default value is 0.5. Can also be set with the command 'set pump_turn_off_limit'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:fcr_n_equality_flag)=
### fcr_n_equality_flag
Turn on (1) or off (0, default) the building of constraints to force the fcr_n delivery for all units to by symmetric. Can also be set with the command 'set fcr_n_equality_flag'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:delay_valuation_mode)=
### delay_valuation_mode
The value 0 (default) uses the first value in the water value description to set the value of water in transition at the end of the optimization period. Setting the value to 1 will use the middle point of the water value description instead. Can also be set with the command 'set delay_valuation_mode'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:universal_affinity_flag)=
### universal_affinity_flag
Turn on (1) or off (0) the use of affinity equations for translating turbine efficiency curves of generators. Default value of -1 uses affinity_eq_flag on each generator to decide if affinity equations should be used. Can also be set by the command 'set universal_affinity'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:ramp_code)=
### ramp_code
Toggle the building of ramping constraints on (1), off (-1), or when violated in previous iteration (0, default).  Can also be set with the command 'set ramping'.  (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:print_original_pq_curves)=
### print_original_pq_curves
Turn on (1) or off (0, default) the writing of the original PQ curves constructed by SHOP before convexification to file. Can also be set with the command 'print pq_curves'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:print_convex_pq_curves)=
### print_convex_pq_curves
Turn on (1) or off (0, default) the writing of the convexified PQ curves constructed by SHOP to file. Can also be set with the command 'print pq_curves'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:print_final_pq_curves)=
### print_final_pq_curves
Turn on (1) or off (0, default) the writing of the final PQ curves used in the optimization by SHOP to file. Can also be set with the command 'print pq_curves'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:shop_log_name)=
### shop_log_name
Name of the log file written to by SHOP, defult is 'shop.log'. Can also be set with the command 'log file'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:shop_yaml_log_name)=
### shop_yaml_log_name
Name of the yaml log file written to by SHOP, defult is 'shop_yaml.yaml'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:solver_log_name)=
### solver_log_name
Name of the log file written to by the solver, defult is 'cplex.log'. Can also be set with the command 'log file'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:model_file_name)=
### model_file_name
Name of the file where the model seen by the optimization solver will be written to in the next iteration. If no name is given, the model will not be printed to file. Can also be set with the command 'print model'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:pq_curves_name)=
### pq_curves_name
Name of the file the PQ curves will be written to if activated by setting the print_<>_pq_curves attributes. A default file name based on the iteration will be used if this attribute is not set. Can also be set with the command 'print pq_curves'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:print_loss)=
### print_loss
Turn on (1) or off (0, default) the writing of junction tunnel loss to the result files. Can also be set with the caommand 'save tunnel_loss'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:shop_xmllog)=
### shop_xmllog
Write the log to xml format if this value is set to 1 instead of the default value 0. Can also be set with the command 'set xmllog' (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:print_optimized_startup_costs)=
### print_optimized_startup_costs
Set value to 1 to only print out the startup and shutdown costs that have been seen by the optimization solver to the log file. Default value of 0 prints out the post calculated startup and shutdown costs. Can also be set with the command 'set startup_cost_printout'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:get_duals_from_mip)=
### get_duals_from_mip
Set value to 1 to fix binary variables after solving a MIP iteration and solving the resulting linear problem again to get dual values. Default value of 0 does not re-solve MIP problems to get dual values. Can also be set with the command 'set duals_from_mip'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:bid_aggregation_level)=
### bid_aggregation_level
Set the bid aggregation level of the SHARM bidding functionality to add all plants to the same bid group (0) or to create individual bid groups for each plant (1). If set to -1 (default), the plants are placed in bid groups according to the bid_group attribute on the plant. Can also be set with the command 'set bid_aggregation_level'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:simple_pq_recovery)=
### simple_pq_recovery
Turn on (1) or off (0, default) simplified building of PQ curves with a single segment for problematic generators suffering from non-physical uploading of the PQ segments. Can also be turned on with the command 'set simple_pq_recovery'. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:rr_up_schedule_slack_flag)=
### rr_up_schedule_slack_flag
Turn on (1) or off (0, default) slack variable for RR_UP schedule on generators. Penalty cost for slack is set equal to reserve_slack_cost. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:bp_ref_mc_from_market)=
### bp_ref_mc_from_market
Turn on (1) or off (0, default) functionality taking marginal cost from market description for current operating point on the best profit curve. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:bp_bid_matrix_points)=
### bp_bid_matrix_points
The maximum number of price columns allowed in the best_profit_bid_matrix on the plant object. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:ramp_scale_factor)=
### ramp_scale_factor
Used to scale all input ramping values for production and discharge on plants, gates, and reservoirs. Can also be set with the command 'set ramp_scale_factor' (xUnit: NO_UNIT, yUnit: NO_UNIT)


(global_settings:river_flow_penalty_cost)=
### river_flow_penalty_cost
The default penalty cost for breaking the min_flow and max_flow constraints defined on river objects. (xUnit: NOK/M3/S, yUnit: NOK/M3/S)


(global_settings:river_flow_schedule_penalty_cost)=
### river_flow_schedule_penalty_cost
The default penalty cost for breaking the flow_schedule constraints defined on river objects. (xUnit: NOK/M3/S, yUnit: NOK/M3/S)


(global_settings:recommit)=
### recommit
Turn on (1, default) or off (0) the general heuristic that attempts to recommit units in a better way for hours without MIP. (xUnit: NO_UNIT, yUnit: NO_UNIT)


