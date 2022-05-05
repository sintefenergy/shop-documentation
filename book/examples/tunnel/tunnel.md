---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

<style>
th {
  font-size: 14px
}
td {
  font-size: 14px
}
</style>

+++

# Tunnel modelling
## Introduction
The tunnel module can be used to model both single tunnels between reservoirs and complex tunnel systems leading in and out of hydropower plants. The main assumption is that flow in a tunnel can be determined by the pressure difference between inlet and outlet, and the head loss due to friction inside the tunnel. Tunnels are also allowed to have gates inside them to control the water flow.

+++

## Object types

|Object type|Description|
|:-|:-|
|tunnel|Pressurized pipe for water flow|
|interlock_constraint|Restriction on simultaneously open/closed gates in a set of tunnels|
|balance_constraint|Restriction on minimum pressure balancing time before switching between two tunnels|

## Attributes

|Object type|Attribute|Data type|I/O|Description|
|:-|:-|:-|:-|:-|
|tunnel            |start_height         |double|Input |Height at start of tunnel                |
|tunnel            |end_height           |double|Input |Height at end of tunnel                  |
|tunnel            |diameter             |double|Input |Diameter of tunnel                       |
|tunnel            |length               |double|Input |Length of tunnel                         |
|tunnel            |loss_factor          |double|Input |Friction loss factor for the whole tunnel|
|tunnel            |time_delay           |int   |Input |Time delay after the tunnel              |
|tunnel            |gate_opening_curve       |xy    |Input |Available points for gate opening and related friction loss scaling factor|
|tunnel            |gate_adjustment_cost |txy   |Input |Cost for changing the gate opening       |
|tunnel            |gate_opening_schedule|txy   |Input |Schedule for gate opening                |
|tunnel            |initial_opening     |int   |Input |Initial position of the gate             |
|tunnel            |continuous_gate      |int   |Input |Flag allowing gate throttling            |
|tunnel            |min_flow             |txy   |Input |Minimum flow in tunnel                   |
|tunnel            |max_flow             |txy   |Input |Maximum flow in tunnel                   |
|tunnel            |end_pressure         |txy   |Output|End tunnel pressure                      |
|tunnel            |flow                 |txy   |Output|Flow in the tunnel                       |
|tunnel            |solver_flow          |txy   |Output|Flow in the tunnel as reported by solver |
|tunnel            |gate_opening         |txy   |Output|Gate opening                             |
|tunnel            |network_no           |int   |Output|Tunnel network number                    |
|interlock_constraint|min_open           |txy   |Input |Minimum number of open objects           |
|interlock_constraint|max_open           |txy   |Input |Maximum number of open objects           |
|balance_constraint|min_balance_time     |txy   |Input |Minimum time for balancing pressure (without plant discharge) before switching between tunnels|

## Connections

|From|To|Description|
|:-|:-|:-|
|reservoir|tunnel|Tunnel with main flow direction out of the reservoir|
|tunnel|reservoir|Tunnel with main flow direction into the reservoir|
|tunnel|tunnel|Tunnel connected to another tunnel|
|plant|tunnel|Plant sending water from turbines into the tunnel|
|tunnel|plant|Plant receiving water for turbines from the tunnel|
|tunnel|interlock_constraint|Tunnel being part of an interlock constraint|
|interlock_constraint|interlock_constraint|Constraint between sub-groups of tunnels|
|tunnel|balance_constraint|Tunnel being part of a minimum balance time constraint|
|reservoir|balance_constraint|Reservoir being part of a minimum balance time constraint|

## Commands

|Command|Options|Objects|
|:-|:-|:-|
|ignore data|None|(object_type) (data_code) (object_name) (to_object)|

+++

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

+++

## Related examples

Examples available for tunnel modelling.

- [Simple tunnel example](simple-tunnel) (using a continuous tunnel gate to optimize head for a plant)
- [Advanced tunnel example](advanced-tunnel) (complex tunnel network with pumping, continuous gate and mutiple binary gates)
