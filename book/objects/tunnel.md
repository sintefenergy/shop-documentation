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

(tunnel)=
# tunnel
A pressurized tunnel object that can couple reservoirs and hydropower plants. The flow in the tunnel is calculated based on the pressure and mass balance in the tunnel network

|   |   |
|---|---|
|Input connections|<a href="reservoir.html">reservoir</a>, <a href="plant.html">plant</a>, <a href="discharge_group.html">discharge_group</a>, <a href="tunnel.html">tunnel</a>, <a href="interlock_constraint.html">interlock_constraint</a>|
|Output connections|<a href="tunnel.html">tunnel</a>, <a href="plant.html">plant</a>, <a href="reservoir.html">reservoir</a>, <a href="river.html">river</a>, <a href="interlock_constraint.html">interlock_constraint</a>, <a href="discharge_group.html">discharge_group</a>|
|License|SHOP_OPEN|
|Release version|13.5.1.a|

```{contents}
:local:
:depth: 1
```

## Introduction
The tunnel module can be used to model both single tunnels between reservoirs and complex tunnel systems leading in and out of hydropower plants. The main assumption is that flow in a tunnel can be determined by the pressure difference between inlet and outlet, and the head loss due to friction inside the tunnel. Tunnels are also allowed to have gates inside them to control the water flow.

## Commands

|Command|Options|Objects|
|:-|:-|:-|
|ignore data|None|(object_type) (data_code) (object_name) (to_object)|

## Physical properties

It is possible to input several physical properties of each tunnel. The **start_height** and **end_height** are used to determine whether the tunnel openings are submerged or not. This influences whether the reservoir level is high enough to allow water flowing through the tunnel, and the counterpressure at the far end for water flowing through the tunnel. **Diameter** and **length** are currently not in use for the optimization, but reserved for more detailed simulation of pressure wave propagation in the tunnel system. The **loss_factor** is multiplied with the square of the flow in the tunnel to obtain the pressure loss in the direction of the flow.

**Time_delay** is currently put on the tunnel object for backwards compatibility, but the plan is to move this to a new "river"-object for improved consistency and flexibility when defining delays.

## Optimization properties

### For a single tunnel

The **gate_opening_curve** XY-table is the basis for optimization of gates inside tunnels. If a tunnel does not have a gate inside it, this data is not needed. The X-values represent an arbitrary position given by increasing numbers. The Y-values represent the corresponding opening factor for each position. In the simplest case, a binary gate can be described by the X-values [0,1] and Y-values [0,1]. This means that postion "0" has an opening factor of 0. SHOP interpretes an opening factor of 0 as a fully closed gate. The position "1" is defined with an opening factor of 1. SHOP interpretes an opening factor of 1 as a fully open gate. Any number between 0 and 1 will be multiplied with the tunnel's **loss_factor** accordingly. Thus, the **loss_factor** used to describe the tunnel should correspond to the situation of a fully open gate.

To prevent too frequent adjustment of the gate, the **gate_adjustment_cost** can be used. The cost is multiplied with the change in gate opening between each timestep and the product is added to the objective function. To align the optimization with the current state of the gate, use the **initial_opening**. 

If the gate is not restricted to only the listed positions, but can be set to any position between the first and last listed position, set the **continuous_gate** parameter to 1. If the gate opening does not need to be optimized, it can be fixed to a schedule using the **gate_opening_schedule** attribute. Please pay attention that this refers to the opening, and not the position of the gate.

It is possible to define limits for min and max flow in tunnels by the attributes **min_flow** and **max_flow**. Currently, these are hard constraints without any penalty attached to them.

### Involving multiple tunnels

Some rules for operating the tunnel system depend on the state of several tunnels simultaneously. A common situation is that not all reservoirs above a plant can have open tunnels at the same time. To represent these constraints, the involved objects must be connected to an **interlock_constraint**. The simplest case contains two reservoirs, of which only one can be connected to the plant at any given time. After adding a **interlock_constraint** and connecting the tunnels from each reservoir to that constraint, set the **min_open** and the **max_open** both equal to 1.

## Results

SHOP optimizes the gate opening in all tunnels, and this **gate_opening** factor between 0 and 1 is reported. SHOP also calculates the **flow** and **end_pressure** for all tunnels. The **solver_flow** is currently reported for verification of convergence properties. A difference between **flow** and **solver_flow** means that the linearized optimization problem predicts a different flow than the non-linear post-simulation.

## Use of commands

The command **ignore data** is added to help testing the tunnel model in parallell with an existing model consisting of other objects and connections in the ascii-files. By specifying certain patterns through one or more calls to **ignore_data**, SHOP will look for matches while reading the ascii-file, and drop any data matching one or more of the patterns.

## Examples
  - [](simple-tunnel)
  

## References
  - Handling state dependent nonlinear tunnel flows in short-term hydropower scheduling {cite}`Belsnes2004`
  - Modelling Minimum Pressure Height in Short-term Hydropower Production Planning {cite}`Dorn2016`
  - Modelling tunnel network flow and minimum pressure height in short-term hydropower scheduling {cite}`Aaslid2019a`
  

## Attributes
```{code-cell} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
from IPython.core.display import HTML

table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "tunnel"].reset_index().iloc[:, 1:]
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

(tunnel:start_height)=
### start_height
The lowest part of the opening of the tunnel at the point defined as the starting point of the tunnel (xUnit: METER, yUnit: METER)


(tunnel:end_height)=
### end_height
The lowest part of the opening of the tunnel at the point defined as the ending point of the tunnel (xUnit: METER, yUnit: METER)


(tunnel:diameter)=
### diameter
The diameter of the tunnel. This is reserved for use in the simulation (xUnit: METER, yUnit: METER)


(tunnel:length)=
### length
The length of the tunnel. This is reserved for use in the simulation (xUnit: METER, yUnit: METER)


(tunnel:loss_factor)=
### loss_factor
Friction loss factor for the tunnel. The head loss in the tunnel is found by multiplying the loss_factor with the square of the flow. The loss_factor is also divided with the gate_opening_curve y-value if the gate is not fully open. (xUnit: S2/M5, yUnit: S2/M5)


(tunnel:weir_width)=
### weir_width
Width of weir at tunnel entrance. Tunnel flow is limited by the amount of water that may flow over the weir, depending on the head of the reservoir above. (xUnit: METER, yUnit: METER)


(tunnel:time_delay)=
### time_delay
The delay between the water leaving the tunnel and until it ends up in the downstream reservoir. This can only be used on tunnels with end_height above the HRL of the downstream reservoir (xUnit: NO_UNIT, yUnit: NO_UNIT)


(tunnel:gate_opening_curve)=
### gate_opening_curve
Relationship between gate positions and related scaling of the pressure loss in the gate. The X-values represent an arbitrary position given by increasing numbers. The Y-values represent the corresponding opening factor for each position. The tunnel loss_factor is divided with the y-value if the gate is not fully open. An y-value of 0 represents a fully closed gate and will not be used for any division (xUnit: NO_UNIT, yUnit: NO_UNIT)


(tunnel:gate_adjustment_cost)=
### gate_adjustment_cost
A cost for changing the gate position between each time step. The given cost is multiplied with the change in gate opening between each time step and the product is added to the objective function (xUnit: NOK, yUnit: NOK)


(tunnel:gate_opening_schedule)=
### gate_opening_schedule
Schedule for gate opening corresponding to the x-values of the gate_opening_curve (xUnit: NO_UNIT, yUnit: NO_UNIT)


(tunnel:initial_opening)=
### initial_opening
Initial position of the gate used as basis for calculating adjustment costs in the first time step (xUnit: NO_UNIT, yUnit: NO_UNIT)


(tunnel:continuous_gate)=
### continuous_gate
Flag determining whether the gate can be set to any position between listed positions in the gate_opening_curve. A value of 0 means that it can only be set at the given positions while a value of 1 means that it can be set to any position between the first and last listed position (xUnit: NO_UNIT, yUnit: NO_UNIT)


(tunnel:end_pressure)=
### end_pressure
Resulting pressure from the optimization at the end of the tunnel (xUnit: METER, yUnit: METER)


(tunnel:sim_end_pressure)=
### sim_end_pressure
Resulting pressure from the simulated at the end of the tunnel (xUnit: METER, yUnit: METER)


(tunnel:flow)=
### flow
Resulting flow in the tunnel from the optimization (xUnit: M3/S, yUnit: M3/S)


(tunnel:physical_flow)=
### physical_flow
Post-calculated physical flow in the tunnel after all optimization decisions are fixed (xUnit: M3/S, yUnit: M3/S)


(tunnel:sim_flow)=
### sim_flow
Simulated flow in the tunnel (xUnit: M3/S, yUnit: M3/S)


(tunnel:gate_opening)=
### gate_opening
Resulting position of the tunnel gate after optimization (xUnit: NO_UNIT, yUnit: NO_UNIT)


(tunnel:network_no)=
### network_no
Network identification number set by the model to indicate which tunnel network this tunnel is part of (xUnit: NO_UNIT, yUnit: NO_UNIT)


(tunnel:min_flow)=
### min_flow
Minimum allowed flow in this tunnel (xUnit: M3/S, yUnit: M3/S)


(tunnel:max_flow)=
### max_flow
Maximum allowed flow in this tunnel (xUnit: M3/S, yUnit: M3/S)


(tunnel:min_flow_penalty_cost)=
### min_flow_penalty_cost
Given penalty cost for violating minimum flow in this tunnel (xUnit: NOK, yUnit: NOK)


(tunnel:max_flow_penalty_cost)=
### max_flow_penalty_cost
Given penalty cost for violating maximum flow in this tunnel (xUnit: NOK, yUnit: NOK)


(tunnel:min_start_pressure)=
### min_start_pressure
Minimum allowed pressure at the start of this tunnel (xUnit: METER, yUnit: METER)


