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

(pump)=
# pump
A hydropower pumping unit which consumes electricity to pump water between reservoirs

|   |   |
|---|---|
|Input connections|<a href="plant.html">plant</a>, <a href="reserve_group.html">reserve_group</a>, <a href="commit_group.html">commit_group</a>, <a href="busbar.html">busbar</a>, <a href="pump_reserve_capability.html">pump_reserve_capability</a>|
|Output connections|<a href="plant.html">plant</a>, <a href="reserve_group.html">reserve_group</a>, <a href="commit_group.html">commit_group</a>, <a href="busbar.html">busbar</a>, <a href="pump_reserve_capability.html">pump_reserve_capability</a>|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```



## Examples
  - [](basic-pump-example)
  

## References
  - Short-term hydro scheduling of a variable speed pumped storage hydropower plant considering head loss in a shared penstock {cite}`Kong2019`
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
object_attributes = table[table["Object type"] == "pump"].reset_index().iloc[:, 1:]
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

(pump:initial_state)=
### initial_state
The initial operation state of the pump before the optimization period: -1 = not set; 0 = not running; 1 = running (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:penstock)=
### penstock
The penstock number the pump is connected to (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:p_min)=
### p_min
Static minimum consumption for the pump  (xUnit: MW, yUnit: MW)


(pump:p_max)=
### p_max
Static maximum consumption for the pump (xUnit: MW, yUnit: MW)


(pump:p_nom)=
### p_nom
The nominal consumption that is the rated capacity of the pump (xUnit: MW, yUnit: MW)


(pump:gen_eff_curve)=
### gen_eff_curve
The efficiency curve for the machine powering the pump (xUnit: MW, yUnit: %)


(pump:turb_eff_curves)=
### turb_eff_curves
The head-dependent turbine efficiency curves in pumping mode (xUnit: M3/S, yUnit: %)


(pump:maintenance_flag)=
### maintenance_flag
Flag determining whether the pump is out for maintenance for a given time step (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:startcost)=
### startcost
Pump startup cost (xUnit: NO_UNIT, yUnit: NOK)


(pump:stopcost)=
### stopcost
Pump shutdown cost (xUnit: NO_UNIT, yUnit: NOK)


(pump:committed_in)=
### committed_in
Committed status given by the user used to define the operating status of the pump in the optimization: 0 - committed not to run; 1 - committed to run (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:committed_flag)=
### committed_flag
Flag determining whether to use the input commit status should be used for a given time step or not (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:upstream_max)=
### upstream_max
Maximum water level of upstream reservoir required for operating the pump (xUnit: NO_UNIT, yUnit: METER)


(pump:upstream_max_flag)=
### upstream_max_flag
Flag determining whether the maximum water level of upstream reservoir required for operating the pump should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:downstream_min)=
### downstream_min
Minimum water level of downstream reservoir required for operating the pump (xUnit: NO_UNIT, yUnit: METER)


(pump:downstream_min_flag)=
### downstream_min_flag
Flag determining whether the minimum water level of downstream reservoir required for operating the pump should be included in the optimization model (xUnit: NO_UNIT, yUnit: METER)


(pump:consumption_schedule)=
### consumption_schedule
Consumption schedule (xUnit: NO_UNIT, yUnit: MW)


(pump:consumption_schedule_flag)=
### consumption_schedule_flag
Flag determining whether the pump consumption schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:upflow_schedule)=
### upflow_schedule
Pump upflow schedule (xUnit: NO_UNIT, yUnit: M3/S)


(pump:upflow_schedule_flag)=
### upflow_schedule_flag
Flag determining whether the pump upflow schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:fcr_mip_flag)=
### fcr_mip_flag
Flag determining whether binary variables should be used to enforce minimum available capacity requirement when delivering FCR (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:p_fcr_min)=
### p_fcr_min
Temporary minimum consumption for the pump when delivering FCR (xUnit: NO_UNIT, yUnit: MW)


(pump:p_fcr_max)=
### p_fcr_max
Temporary maximum consumption for the pump when delivering FCR (xUnit: NO_UNIT, yUnit: MW)


(pump:p_rr_min)=
### p_rr_min
Temporary minimum consumption for the pump when delivering RR (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_up_min)=
### frr_up_min
Minimum FRR_UP delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_up_max)=
### frr_up_max
Maximum FRR_UP delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_down_min)=
### frr_down_min
Minimum FRR_DOWN delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_down_max)=
### frr_down_max
Maximum FRR_DOWN delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_up_min)=
### fcr_n_up_min
Minimum FCR_N_UP delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_up_max)=
### fcr_n_up_max
Maximum FCR_N_UP delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_down_min)=
### fcr_n_down_min
Minimum FCR_N_DOWN delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_down_max)=
### fcr_n_down_max
Maximum FCR_N_DOWN delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_up_min)=
### fcr_d_up_min
Minimum FCR_D_UP delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_up_max)=
### fcr_d_up_max
Maximum FCR_D_UP delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_down_min)=
### fcr_d_down_min
Minimum FCR_D_DOWN delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_down_max)=
### fcr_d_down_max
Maximum FCR_D_DOWN delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_up_min)=
### rr_up_min
Minimum RR_UP delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_up_max)=
### rr_up_max
Maximum RR_UP delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_down_min)=
### rr_down_min
Minimum RR_DOWN delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_down_max)=
### rr_down_max
Maximum RR_DOWN delivery for the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_up_schedule)=
### fcr_n_up_schedule
Pump FCR_N_UP delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_up_schedule_flag)=
### fcr_n_up_schedule_flag
Flag determining whether the pump FCR_N_UP delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:fcr_n_down_schedule)=
### fcr_n_down_schedule
Pump FCR_N_DOWN delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_down_schedule_flag)=
### fcr_n_down_schedule_flag
Flag determining whether the pump FCR_N_DOWN delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:fcr_d_up_schedule)=
### fcr_d_up_schedule
Pump FCR_D_UP delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_up_schedule_flag)=
### fcr_d_up_schedule_flag
Flag determining whether the pump FCR_D_UP delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:fcr_d_down_schedule)=
### fcr_d_down_schedule
Pump FCR_D_DOWN delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_down_schedule_flag)=
### fcr_d_down_schedule_flag
Flag determining whether the pump FCR_D_DOWN delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:frr_up_schedule)=
### frr_up_schedule
Pump FRR_UP delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_up_schedule_flag)=
### frr_up_schedule_flag
Flag determining whether the pump FRR_UP delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:frr_down_schedule)=
### frr_down_schedule
Pump FRR_DOWN delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_down_schedule_flag)=
### frr_down_schedule_flag
Flag determining whether the pump FRR_DOWN delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:rr_up_schedule)=
### rr_up_schedule
Pump RR_UP delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_up_schedule_flag)=
### rr_up_schedule_flag
Flag determining whether the pump RR_UP delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:rr_down_schedule)=
### rr_down_schedule
Pump RR_DOWN delivery schedule (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_down_schedule_flag)=
### rr_down_schedule_flag
Flag determining whether the pump RR_DOWN delivery schedule should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:droop_cost)=
### droop_cost
The cost for the unit droop when it is modelled as a variable in the optimization model. This cost should increase when the unit droop decreases (xUnit: NO_UNIT, yUnit: NOK)


(pump:fixed_droop)=
### fixed_droop
Fixed unit droop given as input data (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:fixed_droop_flag)=
### fixed_droop_flag
Flag determining whether the fixed droop setting should be included in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:droop_min)=
### droop_min
The lower bound of the unit droop when it is modelled as a variable in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:droop_max)=
### droop_max
The upper bound of the unit droop when it is modelled as a variable in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:reserve_ramping_cost_up)=
### reserve_ramping_cost_up
Upward reserve ramping cost for changing reserve delivery of the pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:reserve_ramping_cost_down)=
### reserve_ramping_cost_down
Downward reserve ramping cost for changing reserve delivery of the pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:discrete_droop_values)=
### discrete_droop_values
A list of all legal droop values for the pump. If the functionality for fixing the unit droop is activated by the 'set droop_discretization_limit' command, this list of discrete values will be used when fixing the pump droop (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:fcr_n_up_cost)=
### fcr_n_up_cost
The cost of allocating FCR-N up reserves on this pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:fcr_n_down_cost)=
### fcr_n_down_cost
The cost of allocating FCR-N down reserves on this pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:fcr_d_up_cost)=
### fcr_d_up_cost
The cost of allocating FCR-D up reserves on this pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:fcr_d_down_cost)=
### fcr_d_down_cost
The cost of allocating FCR-D down reserves on this pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:frr_up_cost)=
### frr_up_cost
The cost of allocating FRR up reserves on this pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:frr_down_cost)=
### frr_down_cost
The cost of allocating FRR down reserves on this pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:rr_up_cost)=
### rr_up_cost
The cost of allocating RR up reserves on this pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:rr_down_cost)=
### rr_down_cost
The cost of allocating RR down reserves on this pump (xUnit: NO_UNIT, yUnit: NOK/MW)


(pump:spinning_reserve_up_max)=
### spinning_reserve_up_max
Sets a maximum limit for the sum of spinning reserves delivered in the upward direction on the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:spinning_reserve_down_max)=
### spinning_reserve_down_max
Sets a maximum limit for the sum of spinning reserves delivered in the downward direction on the pump (xUnit: NO_UNIT, yUnit: MW)


(pump:eff_head)=
### eff_head
Resulting effective head of the pump (xUnit: NO_UNIT, yUnit: METER)


(pump:head_loss)=
### head_loss
Resulting head loss of the generator, i.e. the effective head of the pump (eff_head) minus the plant gross head (gross_head) (xUnit: NO_UNIT, yUnit: METER)


(pump:consumption)=
### consumption
Resulting pump consumption, calculated based on upflow (xUnit: NO_UNIT, yUnit: MW)


(pump:sim_consumption)=
### sim_consumption
Simulated pump consumption, calculated based on upflow (xUnit: NO_UNIT, yUnit: MW)


(pump:solver_consumption)=
### solver_consumption
Preliminary result for pump consumption that is returned by the linearized optimization problem (xUnit: NO_UNIT, yUnit: MW)


(pump:upflow)=
### upflow
Resulting pump upflow. If solver_upflow >= pump_turn_off_limit, upflow = solver_upflow. Otherwise, upflow = 0. (xUnit: NO_UNIT, yUnit: M3/S)


(pump:sim_upflow)=
### sim_upflow
Simulated pump upflow. (xUnit: NO_UNIT, yUnit: M3/S)


(pump:solver_upflow)=
### solver_upflow
Preliminary result for pump upflow that is returned by the linearized optimization problem (xUnit: NO_UNIT, yUnit: M3/S)


(pump:committed_out)=
### committed_out
Committed status of the pump as a result of the optimization: 0 - not running; 1 - committed to run (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:consumption_schedule_penalty)=
### consumption_schedule_penalty
Resulting penalty when the pump consumption schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(pump:upflow_schedule_penalty)=
### upflow_schedule_penalty
Resulting penalty when the pump upflow schedule is violated (xUnit: NO_UNIT, yUnit: MM3)


(pump:fcr_n_up_delivery)=
### fcr_n_up_delivery
Resulting pump FCR_N_UP delivery (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_down_delivery)=
### fcr_n_down_delivery
Resulting pump FCR_N_DOWN delivery (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_up_delivery)=
### fcr_d_up_delivery
Resulting pump FCR_D_UP delivery (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_down_delivery)=
### fcr_d_down_delivery
Resulting pump FCR_D_DOWN delivery (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_up_delivery)=
### frr_up_delivery
Resulting pump FRR_UP delivery (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_down_delivery)=
### frr_down_delivery
Resulting pump FRR_DOWN delivery (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_up_delivery)=
### rr_up_delivery
Resulting pump RR_UP delivery (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_down_delivery)=
### rr_down_delivery
Resulting pump RR_DOWN delivery (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_up_delivery_physical)=
### fcr_n_up_delivery_physical
Resulting physical pump FCR_N delivery in the upward direction (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_down_delivery_physical)=
### fcr_n_down_delivery_physical
Resulting physical pump FCR_N delivery in the downward direction (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_up_delivery_physical)=
### fcr_d_up_delivery_physical
Resulting physical pump FCR_D delivery in the upward direction (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_down_delivery_physical)=
### fcr_d_down_delivery_physical
Resulting physical pump FCR_D delivery in the downward direction (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_up_schedule_penalty)=
### fcr_n_up_schedule_penalty
Resulting penalty when the pump FCR_N_UP schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_n_down_schedule_penalty)=
### fcr_n_down_schedule_penalty
Resulting penalty when the pump FCR_N_DOWN schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_up_schedule_penalty)=
### fcr_d_up_schedule_penalty
Resulting penalty when the pump FCR_D_UP schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(pump:fcr_d_down_schedule_penalty)=
### fcr_d_down_schedule_penalty
Resulting penalty when the pump FCR_D_DOWN schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_up_schedule_penalty)=
### frr_up_schedule_penalty
Resulting penalty when the pump FRR_UP schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(pump:frr_down_schedule_penalty)=
### frr_down_schedule_penalty
Resulting penalty when the pump FRR_DOWN schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_up_schedule_penalty)=
### rr_up_schedule_penalty
Resulting penalty when the pump RR_UP schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(pump:rr_down_schedule_penalty)=
### rr_down_schedule_penalty
Resulting penalty when the pump RR_DOWN schedule is violated (xUnit: NO_UNIT, yUnit: MW)


(pump:droop_result)=
### droop_result
Resulting unit droop when it is modelled as a variable in the optimization model (xUnit: NO_UNIT, yUnit: NO_UNIT)


(pump:original_pq_curves)=
### original_pq_curves
Original PQ-curve for the pump that includes non-convex regions (xUnit: M3/S, yUnit: MW)


(pump:convex_pq_curves)=
### convex_pq_curves
Convexified PQ-curve for the pump that removes all the nonconcave points of the original PQ curve. The slope of each segment is non-decreasing. (xUnit: M3/S, yUnit: MW)


(pump:final_pq_curves)=
### final_pq_curves
Final PQ curve for the pump that is the final form included into the MILP optimization problem. The first point of the convex PQ curve is extended to Q=0. (xUnit: M3/S, yUnit: MW)


(pump:max_cons)=
### max_cons
The head dependent maximal consumption of the pump, most accurate in incremental iterations (xUnit: NO_UNIT, yUnit: MW)


(pump:min_cons)=
### min_cons
The head dependent minimal consumption of the pump, most accurate in incremental iterations (xUnit: NO_UNIT, yUnit: MW)


