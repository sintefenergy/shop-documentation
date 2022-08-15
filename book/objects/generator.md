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

(generator)=
# generator
A hydropower generating unit consisting of a hydropower turbine and a generator which uses falling water to generate electricity

|   |   |
|---|---|
|Input connections|<a href="plant.html">plant</a>, <a href="needle_combination.html">needle_combination</a>, <a href="reserve_group.html">reserve_group</a>, <a href="commit_group.html">commit_group</a>, <a href="busbar.html">busbar</a>, <a href="gen_reserve_capability.html">gen_reserve_capability</a>|
|Output connections|<a href="plant.html">plant</a>, <a href="reserve_group.html">reserve_group</a>, <a href="commit_group.html">commit_group</a>, <a href="needle_combination.html">needle_combination</a>, <a href="busbar.html">busbar</a>, <a href="gen_reserve_capability.html">gen_reserve_capability</a>|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```



## Examples
  - [](best-profit)
  - [](best-profit-basic-example)
  - [](discrete-droop)
  - [](maintenance-example)
  

## References
  - An overview on formulations and optimization methods for the unit-based short-term hydro scheduling problem {cite}`Kong2020`
  - Dynamic incorporation of nonlinearity into MILP formulation for short-term hydro scheduling {cite}`Skjelbred2020`
  - A comparison of linear interpolation and spline interpolation for turbine efficiency curves in short-term hydropower scheduling problems {cite}`Zhang2019`
  - Calculation of power compensation for a pumped storage hydropower plant with hydraulic short-circuit operation {cite}`Skjelbred2017b`
  

## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "generator"].reset_index().iloc[:, 1:]
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

(generator:type)=
### type
Specification of type of generator when using ASCII-files as input. 0 indicates Francis or Kaplan turbine while PELTON indicates a pelton unit (or a unit where forbidden operating zones is modelled as pelton) (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:num_needle_comb)=
### num_needle_comb
Number of needle combinations for pelton units (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:prod_area)=
### prod_area
Production from this generator will be sold in markets connected to the given production area (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:initial_state)=
### initial_state
The initial operation state of the generator before the optimization period: -1 = not set; 0 = not running; 1 = running (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:penstock)=
### penstock
The penstock number the generator is connected to (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:p_min)=
### p_min
Static minimum production for the generator (xUnit: MW, yUnit: MW)


(generator:p_max)=
### p_max
Static maximum production for the generator (xUnit: MW, yUnit: MW)


(generator:p_nom)=
### p_nom
The nominal production that is the rated capacity of the generator (xUnit: MW, yUnit: MW)


(generator:gen_eff_curve)=
### gen_eff_curve
The generator efficiency curve (xUnit: MW, yUnit: %)


(generator:turb_eff_curves)=
### turb_eff_curves
The head-dependent turbine efficiency curve(s) (xUnit: M3/S, yUnit: %)

<!-- Add content here -->
<!-- ### Testing -->
<!-- This is a test. -->
(generator:maintenance_flag)=
### maintenance_flag
Flag determining whether the generator is out for maintenance for a given time step (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:startcost)=
### startcost
Generator startup cost (xUnit: NO_UNIT, yUnit: NOK)


(generator:stopcost)=
### stopcost
Generator shutdown cost (xUnit: NO_UNIT, yUnit: NOK)


(generator:discharge_cost_curve)=
### discharge_cost_curve
Extra cost depending on the discharge of the generator (xUnit: M3/S, yUnit: NOK/H/M3/S)


(generator:priority)=
### priority
Time-dependent generators priority to define the uploading order among all the generators in a plant (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:committed_in)=
### committed_in
Committed status given by the user used to define the operating status of the generator in the optimization: 0 - committed not to run; 1 - committed to run (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:committed_flag)=
### committed_flag
Flag determining whether the input commit status should be used for a given time step or not (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:min_p_constr)=
### min_p_constr
Time-dependent minimum production limit for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:min_p_constr_flag)=
### min_p_constr_flag
Flag determining whether the time-dependent minimum production limit for the generator should be included in the building of the original PQ curve (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:max_p_constr)=
### max_p_constr
Time-dependent maximum production limit for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:max_p_constr_flag)=
### max_p_constr_flag
Flag determining whether the time-dependent maximum production limit for the generator should be included in the building of the original PQ curve (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:min_q_constr)=
### min_q_constr
Time-dependent minimum discharge limit for the generator (xUnit: NO_UNIT, yUnit: M3/S)


(generator:min_q_constr_flag)=
### min_q_constr_flag
Flag determining whether the time-dependent minimum discharge limit for the generator should be included in the building of the original PQ curve (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:max_q_constr)=
### max_q_constr
Time-dependent maximum discharge limit for the generator (xUnit: NO_UNIT, yUnit: M3/S)


(generator:max_q_constr_flag)=
### max_q_constr_flag
Flag determining whether the time-dependent maximum discharge limit for the generator should be included in the building of the original PQ curve (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:max_q_limit_rsv_down)=
### max_q_limit_rsv_down
Maximum generator discharge limit (m3/s) and downstream reservoir water level (meter above sea level) relation (xUnit: METER, yUnit: M3/S)


(generator:upstream_min)=
### upstream_min
Minimum water level of upstream reservoir required for running the generator (xUnit: NO_UNIT, yUnit: METER)


(generator:upstream_min_flag)=
### upstream_min_flag
Flag determining whether the minimum water level of upstream reservoir required for running the generator should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:downstream_max)=
### downstream_max
Maximum water level of downstream reservoir required for running the generator (xUnit: NO_UNIT, yUnit: METER)


(generator:downstream_max_flag)=
### downstream_max_flag
Flag determining whether the maximum water level of downstream required for running the generator should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:production_schedule)=
### production_schedule
Generator production schedule (xUnit: NO_UNIT, yUnit: MW)


(generator:production_schedule_flag)=
### production_schedule_flag
Flag determining whether the generator production schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:discharge_schedule)=
### discharge_schedule
Generator discharge schedule (xUnit: NO_UNIT, yUnit: M3/S)


(generator:discharge_schedule_flag)=
### discharge_schedule_flag
Flag determining whether the generator discharge schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:fcr_mip_flag)=
### fcr_mip_flag
Flag determining whether binary variables should be used to indicate that the generator can contribute to FCR only if its unused capacity is no less than 2% of the maximum production limit (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:p_fcr_min)=
### p_fcr_min
Temporary minimum production for the generator when delivering FCR (xUnit: NO_UNIT, yUnit: MW)


(generator:p_fcr_max)=
### p_fcr_max
Temporary maximum production for the generator when delivering FCR (xUnit: NO_UNIT, yUnit: MW)


(generator:p_rr_min)=
### p_rr_min
Temporary minimum production for the generator when delivering RR (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_up_min)=
### frr_up_min
Minimum FRR_UP delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_up_max)=
### frr_up_max
Maximum FRR_UP delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_down_min)=
### frr_down_min
Minimum FRR_DOWN delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_down_max)=
### frr_down_max
Maximum FRR_DOWN delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_up_min)=
### fcr_n_up_min
Minimum FCR_N_UP delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_up_max)=
### fcr_n_up_max
Maximum FCR_N_UP delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_down_min)=
### fcr_n_down_min
Minimum FCR_N_DOWN delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_down_max)=
### fcr_n_down_max
Maximum FCR_N_DOWN delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_up_min)=
### fcr_d_up_min
Minimum FCR_D_UP delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_up_max)=
### fcr_d_up_max
Maximum FCR_D_UP delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_down_min)=
### fcr_d_down_min
Minimum FCR_D_DOWN delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_down_max)=
### fcr_d_down_max
Maximum FCR_D_DOWN delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_up_min)=
### rr_up_min
Minimum RR_UP delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_up_max)=
### rr_up_max
Maximum RR_UP delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_down_min)=
### rr_down_min
Minimum RR_DOWN delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_down_max)=
### rr_down_max
Maximum RR_DOWN delivery for the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_up_schedule)=
### fcr_n_up_schedule
Generator FCR_N_UP delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_up_schedule_flag)=
### fcr_n_up_schedule_flag
Flag determining whether the generator FCR_N_UP delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:fcr_n_down_schedule)=
### fcr_n_down_schedule
Generator FCR_N_DOWN delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_down_schedule_flag)=
### fcr_n_down_schedule_flag
Flag determining whether the generator FCR_N_DOWN delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:fcr_d_up_schedule)=
### fcr_d_up_schedule
Generator FCR_D_UP delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_up_schedule_flag)=
### fcr_d_up_schedule_flag
Flag determining whether the generator FCR_D_UP delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:fcr_d_down_schedule)=
### fcr_d_down_schedule
Generator FCR_D_DOWN delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_down_schedule_flag)=
### fcr_d_down_schedule_flag
Flag determining whether the generator FCR_D_DOWN delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:frr_up_schedule)=
### frr_up_schedule
Generator FRR_UP delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_up_schedule_flag)=
### frr_up_schedule_flag
Flag determining whether the generator FRR_UP delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:frr_down_schedule)=
### frr_down_schedule
Generator FRR_DOWN delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_down_schedule_flag)=
### frr_down_schedule_flag
Flag determining whether the generator FRR_DOWN delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:rr_up_schedule)=
### rr_up_schedule
Generator RR_UP delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_up_schedule_flag)=
### rr_up_schedule_flag
Flag determining whether the generator RR_UP delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:rr_down_schedule)=
### rr_down_schedule
Generator RR_DOWN delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_down_schedule_flag)=
### rr_down_schedule_flag
Flag determining whether the generator RR_DOWN delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:droop_cost)=
### droop_cost
The cost for the unit droop when it is modelled as a variable in the optimization model. This cost should increase when the unit droop decreases (xUnit: NO_UNIT, yUnit: NOK)


(generator:fixed_droop)=
### fixed_droop
Fixed unit droop given as input data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:fixed_droop_flag)=
### fixed_droop_flag
Flag determining whether the fixed droop setting should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:droop_min)=
### droop_min
The lower bound of the unit droop when it is modelled as a variable in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:droop_max)=
### droop_max
The upper bound of the unit droop when it is modelled as a variable in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:discrete_droop_values)=
### discrete_droop_values
A list of all legal droop values for the generator. If the functionality for fixing the unit droop is activated by the 'set droop_discretization_limit' command, this list of discrete values will be used when fixing the generator droop (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:reserve_ramping_cost_up)=
### reserve_ramping_cost_up
Upward reserve ramping cost for changing reserve delivery of the generator (xUnit: NO_UNIT, yUnit: NOK)


(generator:reserve_ramping_cost_down)=
### reserve_ramping_cost_down
Downward reserve ramping cost for changing reserve delivery of the generator (xUnit: NO_UNIT, yUnit: NOK)


(generator:ref_production)=
### ref_production
Production of the generator indicating the planned operating point as starting point for the best profit calculation (xUnit: NO_UNIT, yUnit: MW)


(generator:schedule_deviation_flag)=
### schedule_deviation_flag
Flag determining whether the generator can deviate from the input schedule when calculating marginal cost and best profit curves. Implicitly generated based on the ref_prod attribute if the command 'set prod_from_ref_prod' is used. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:gen_turn_off_limit)=
### gen_turn_off_limit
A decimal number between 0 and 1 that signifies if the generator operates below the fraction (the decimal number) of its minimum operating limit in a full mode without MIP, the unit will be turned off. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:fcr_n_up_cost)=
### fcr_n_up_cost
The cost of allocating FCR-N up reserves on this generator (xUnit: NO_UNIT, yUnit: NOK/MW)


(generator:fcr_n_down_cost)=
### fcr_n_down_cost
The cost of allocating FCR-N down reserves on this generator (xUnit: NO_UNIT, yUnit: NOK/MW)


(generator:fcr_d_up_cost)=
### fcr_d_up_cost
The cost of allocating FCR-D up reserves on this generator (xUnit: NO_UNIT, yUnit: NOK/MW)


(generator:fcr_d_down_cost)=
### fcr_d_down_cost
The cost of allocating FCR-D down reserves on this generator (xUnit: NO_UNIT, yUnit: NOK/MW)


(generator:frr_up_cost)=
### frr_up_cost
The cost of allocating FRR up reserves on this generator (xUnit: NO_UNIT, yUnit: NOK/MW)


(generator:frr_down_cost)=
### frr_down_cost
The cost of allocating FRR down reserves on this generator (xUnit: NO_UNIT, yUnit: NOK/MW)


(generator:rr_up_cost)=
### rr_up_cost
The cost of allocating RR up reserves on this generator (xUnit: NO_UNIT, yUnit: NOK/MW)


(generator:rr_down_cost)=
### rr_down_cost
The cost of allocating RR down reserves on this generator (xUnit: NO_UNIT, yUnit: NOK/MW)


(generator:spinning_reserve_up_max)=
### spinning_reserve_up_max
Sets a maximum limit for the sum of spinning reserves delivered in the upward direction on the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:spinning_reserve_down_max)=
### spinning_reserve_down_max
Sets a maximum limit for the sum of spinning reserves delivered in the downward direction on the generator (xUnit: NO_UNIT, yUnit: MW)


(generator:eff_head)=
### eff_head
Resulting effective head of the generator (xUnit: NO_UNIT, yUnit: METER)


(generator:sim_eff_head)=
### sim_eff_head
The simulated effective head of the generator (xUnit: NO_UNIT, yUnit: METER)


(generator:head_loss)=
### head_loss
Resulting head loss of the generator, i.e. the plant gross head (gross_head) minus the effective head of the generator (eff_head) (xUnit: NO_UNIT, yUnit: METER)


(generator:production)=
### production
Resulting generator production, calculated base on discharge (xUnit: NO_UNIT, yUnit: MW)


(generator:solver_production)=
### solver_production
Preliminary result for generator production that is returned by the linearized optimization problem (xUnit: NO_UNIT, yUnit: MW)


(generator:sim_production)=
### sim_production
Simulated generator production (xUnit: NO_UNIT, yUnit: MW)


(generator:discharge)=
### discharge
Resulting generator discharge. If solver_discharge >= gen_turn_off_limit, discharge is equal to solver_discharge. Otherwise, discharge = 0. (xUnit: NO_UNIT, yUnit: M3/S)


(generator:solver_discharge)=
### solver_discharge
Preliminary result for generator discharge that is returned by the linearized optimization problem (xUnit: NO_UNIT, yUnit: M3/S)


(generator:sim_discharge)=
### sim_discharge
Simulated generator discharge (xUnit: NO_UNIT, yUnit: M3/S)


(generator:committed_out)=
### committed_out
Committed status of the generator as a result of the optimization: 0 - not running; 1 - committed to run. Note that if a Pelton is committed to run, the number of needle_comb is returned. (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:production_schedule_penalty)=
### production_schedule_penalty
Resulting penalty when the generator production schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(generator:discharge_schedule_penalty)=
### discharge_schedule_penalty
Resulting penalty when the generator discharge schedule is violated (xUnit: NO_UNIT, yUnit: MM3)


(generator:fcr_n_up_delivery)=
### fcr_n_up_delivery
Resulting generator FCR_N_UP delivery (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_down_delivery)=
### fcr_n_down_delivery
Resulting generator FCR_N_DOWN delivery (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_up_delivery)=
### fcr_d_up_delivery
Resulting generator FCR_D_UP delivery (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_down_delivery)=
### fcr_d_down_delivery
Resulting generator FCR_D_DOWN delivery (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_up_delivery)=
### frr_up_delivery
Resulting generator FRR_UP delivery (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_down_delivery)=
### frr_down_delivery
Resulting generator FRR_DOWN delivery (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_up_delivery)=
### rr_up_delivery
Resulting generator RR_UP delivery (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_down_delivery)=
### rr_down_delivery
Resulting generator RR_DOWN delivery (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_up_delivery_physical)=
### fcr_n_up_delivery_physical
Resulting physical generator FCR_N delivery in the upward direction (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_down_delivery_physical)=
### fcr_n_down_delivery_physical
Resulting physical generator FCR_N delivery in the downward direction (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_up_delivery_physical)=
### fcr_d_up_delivery_physical
Resulting physical generator FCR_D delivery in the upward direction (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_down_delivery_physical)=
### fcr_d_down_delivery_physical
Resulting physical generator FCR_D delivery in the downward direction (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_up_schedule_penalty)=
### fcr_n_up_schedule_penalty
Resulting penalty when the generator FCR_N_UP schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_n_down_schedule_penalty)=
### fcr_n_down_schedule_penalty
Resulting penalty when the generator FCR_N_DOWN schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_up_schedule_penalty)=
### fcr_d_up_schedule_penalty
Resulting penalty when the generator FCR_D_UP schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(generator:fcr_d_down_schedule_penalty)=
### fcr_d_down_schedule_penalty
Resulting penalty when the generator FCR_D_DOWN schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_up_schedule_penalty)=
### frr_up_schedule_penalty
Resulting penalty when the generator FRR_UP schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(generator:frr_down_schedule_penalty)=
### frr_down_schedule_penalty
Resulting penalty when the generator FRR_DOWN schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_up_schedule_penalty)=
### rr_up_schedule_penalty
Resulting penalty when the generator RR_UP schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(generator:rr_down_schedule_penalty)=
### rr_down_schedule_penalty
Resulting penalty when the generator RR_DOWN schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(generator:droop_result)=
### droop_result
Resulting unit droop when it is modelled as a variable in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(generator:best_profit_q)=
### best_profit_q
Optimal discharge for the generator given a certain production level of the plant (xUnit: MW, yUnit: NOK/MW)


(generator:best_profit_p)=
### best_profit_p
Optimal production for the generator given a certain production level of the plant (xUnit: MW, yUnit: NOK/MW)


(generator:best_profit_dq_dp)=
### best_profit_dq_dp
Ratio between discharge and production for the generator given a certain production level of the plant (xUnit: MW, yUnit: M3/S)


(generator:best_profit_needle_comb)=
### best_profit_needle_comb
Optimal needle combination for the generator given a certain production level of the plant (xUnit: MW, yUnit: M3/S)


(generator:startup_cost_mip_objective)=
### startup_cost_mip_objective
Cost in the objective function of the solver from startup costs originating from the time steps when MIP is used (xUnit: NO_UNIT, yUnit: NOK)


(generator:startup_cost_total_objective)=
### startup_cost_total_objective
Post-optimization calculated startup costs based on change in commitment status for both time steps with and without MIP activated (xUnit: NO_UNIT, yUnit: NOK)


(generator:discharge_fee_objective)=
### discharge_fee_objective
Cost in the objective function resulting from discharge fees for this generator (xUnit: NO_UNIT, yUnit: NOK)


(generator:feeding_fee_objective)=
### feeding_fee_objective
Cost in the objective function resulting from feed-in fees for this generator (xUnit: NO_UNIT, yUnit: NOK)


(generator:schedule_penalty)=
### schedule_penalty
Resulting penalty cost when the generator schedule (production schedule and/or discharge schedule) for the generator is voilated (xUnit: NO_UNIT, yUnit: NOK)


(generator:market_income)=
### market_income
Income in the objective function resulting from production on this generator (xUnit: NO_UNIT, yUnit: NOK)


(generator:original_pq_curves)=
### original_pq_curves
Original PQ-curve for the generator that includes non-convex regions (xUnit: M3/S, yUnit: MW)


(generator:convex_pq_curves)=
### convex_pq_curves
Convexified PQ-curve for the generator that includes all the time-dependent operating limits and removes all the nonconcave points of the original PQ curve. The slope of each segment is non-increasing. (xUnit: M3/S, yUnit: MW)


(generator:final_pq_curves)=
### final_pq_curves
Final PQ curve for the generator that is the final form included into the MILP optimization problem. The first point of the convex PQ curve is extended to Q=0. (xUnit: M3/S, yUnit: MW)


(generator:max_prod)=
### max_prod
The head dependent maximal production of the generator, most accurate in incremental iterations (xUnit: NO_UNIT, yUnit: MW)


(generator:min_prod)=
### min_prod
The head dependent minimal production of the generator, most accurate in incremental iterations (xUnit: NO_UNIT, yUnit: MW)


