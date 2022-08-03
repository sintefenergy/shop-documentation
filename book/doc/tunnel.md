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