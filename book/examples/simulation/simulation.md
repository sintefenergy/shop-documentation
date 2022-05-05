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

# Simulation

+++

# Introduction

It is now possible to run a simulation on an entire watercourse in SHOP.
When running a simulation, no constraints are taken into account. The
model is neither run through the same validation functions as for
optimization. The purpose is to return the physical response of the
system given all user-controllable decisions as input.

# Input data 

Input of model and data is done using the same format as for
optimization. For the simulation, most decisions that otherwise are made
by the optimization must be given as schedules. Plants are operated
based on input schedules. The following table sums up the possible
schedule settings for each
plant.

| **TXY attribute**          | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sim\_gen\_mw\_flag         | Use data from generator "production\_schedule" attribute (in MW)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| sim\_gen\_m3s\_flag        | Use data from generator "discharge\_schedule" attribute (in m3/s)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| sim\_plant\_mw\_flag       | Use data from plant "production\_schedule" attribute (in MW). The production will be distributed in an optimal way for the best unit combination on the plant. The best unit combination is selected among those combinations that can be constructed by only adding or removing units from the combination that was used in the previous timestep.                                                                                                                                                                                                                                                                                                                                                       |
| sim\_plant\_m3s\_flag      | Use data from plant "discharge\_schedule" attribute (in m3/s). The discharge will be distributed in an optimal way for the best unit combination on the plant. The best unit combination is selected among those combinations that can be constructed by only adding or removing units from the combination that was used in the previous timestep.                                                                                                                                                                                                                                                                                                                                                       |
| sim\_reservoir\_masl\_flag | Use data from "masl\_schedule" attribute (in m) for the reservoir directly above the plant. If the plant is below a junction or creek intake, this functionality cannot be used. Only the discharge of this plant and its bypass gate will be used to fulfil this schedule. If the discharge needed to keep the schedule is larger than the maximum capacity of the plant, it will use the bypass gate. The discharge in the plant will be distributed in an optimal way for the best unit combination on the plant. The best unit combination is selected among those combinations that can be constructed by only adding or removing units from the combination that was used in the previous timestep. |

If several of the flags are set to 1 in the same timestep for the same
plant, they will have the same priority order as in the table above.
That is, sim\_gen\_mw\_flag has the highest priority while
sim\_reservoir\_masl\_flag has the lowest priority. In addition, the
following data is required as input to the simulation.

  - All standard gates and bypass gates must have schedules in m3/s.

  - All reservoirs must have start volume set.

  - All pumps must have committed status set.

If a schedule is missing on a plant or unit, but the simulation is
started in the same session as an optimization, the result from the
optimization will be used as schedule. Otherwise, the schedule will be
set to 0. If a start reservoir is missing, it is set to 0.

# Simulation rules 

If the decisions lead to situations that are physically infeasible or
not adequately described by the input data the rules listed below are
applied.

  - If there is discharge from an empty reservoir, the discharge remains
    unchanged and the reservoir remains empty. The artificial volume
    added is reported as a warning.

  - If there is inflow or discharge into a full reservoir without
    overflow possibilities, the discharge and inflow remains unchanged
    and the reservoir remains full. The artificial volume removed is
    reported as a warning.

  - If the schedule of a generator results in a flow below zero, the
    flow remains unchanged and the amount below zero is reported as a
    warning.

  - If the schedule of a generator results in a flow more than 20% above
    the maximum from the turbine efficiency curves, the flow remains
    unchanged and the amount maximum is reported as a warning.

# Commands 

The commands listed in the table below are added to SHOP to interface
the simulator. There are two main modes for reservoir simulation.
Without any options set, the command "start shopsim" will calculate and
output the storage trajectory of each reservoir. With the
"/inflow"-option set, the command will calculate and output the inflow
to each reservoir and creek intake needed to reproduce the input
reservoir storage time
series.

| **Command**               | **Options **                                                                                | **Comment**                                                                                                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| save optres\_for\_shopsim |                                                                                             | Save generator schedule in MW, pump schedule in MW, gate schedule in m3/s to an ascii file that can be used as input data for simulation. Specify file name after the command.                      |
| start shopsim             | /gen\_mw\_schedule, /gen\_m3s\_schedule, /plant\_mw\_schedule, /gen\_m3s\_schedule, /inflow | Run simulation. Default setting is /gen\_mw\_schedule. The schedule options are used on plants where no corresponding txy flag is set. See separate documentation for the inflow simulation option. |
| return shopsimres         | /generator                                                                                  | Write results from simulation to ascii file.                                                                                                                                                        |
| save shopsimseries        | /start, /end, /removeequal                                                                  | Write results from simulation to ser file.                                                                                                                                                          |
| save xmlshopsimseries     | /start, /end, /removeequal                                                                  | Write results simulation to xml file.                                                                                                                                                               |

# Result data

The simulator calculates the physical behaviour of the system given the
input schedules, but also reports the economical value of the schedule.

## Physical results

The time series in the table below are returned as physical results from
the
simulation.

| **Object type** | **Attribute name**   | **Data type** | **Comment**                                                                                                        |
| --------------- | -------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------ |
| Reservoir       | sim\_storage         | TXY           | Start volume for each time step, length is number of time steps plus 1 to include end reservoir                    |
| Reservoir       | sim\_height          | TXY           | Reservoir height in masl volume for each time step, length is number of time steps plus 1 to include end reservoir |
| Plant           | sim\_discharge       | TXY           | Discharge in m3/s                                                                                                  |
| Plant           | sim\_production      | TXY           | Production in MW                                                                                                   |
| Generator       | sim\_discharge       | TXY           | Discharge in m3/s                                                                                                  |
| Generator       | sim\_production      | TXY           | Production in MW                                                                                                   |
| Pump            | sim\_upflow          | TXY           | Flow in m3/s (positive for upward flow)                                                                            |
| Pump            | sim\_consumption     | TXY           | Consumption in MW                                                                                                  |
| Gate            | sim\_discharge       | TXY           | Discharge in m3/s                                                                                                  |
| Junction        | sim\_tunnel\_flow\_1 | TXY           | Flow through first input tunnel in m3/s                                                                            |
| Junction        | sim\_tunnel\_flow\_2 | TXY           | Flow through second input tunnel in m3/s                                                                           |
| Junction\_gate  | sim\_tunnel\_flow\_1 | TXY           | Flow through first input tunnel in m3/s                                                                            |
| Junction\_gate  | sim\_tunnel\_flow\_2 | TXY           | Flow through second input tunnel in m3/s                                                                           |

## Economical results

As a post-processing operation after the simulation, the value of the
simulated schedule is calculated. The table below summarizes the data
provided by the
calculation.

| **Object type** | **Attribute name**     | **Data type** | **Description**                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------- | ---------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Objective       | sim\_grand\_total      | double        | Overall objective, calculated as the sum of sim\_rsv\_end\_value plus sim\_market\_sale\_buy minus sim\_startup\_costs minus sim\_rsv\_penalty                                                                                                                                                                                                                                                  |
| Objective       | sim\_rsv\_end\_value   | double        | Value of the simulated end storage of water in the reservoirs. The end valuation is done in the same way as in the optimization. If the endpoint\_desc is given in €/MWh, it is converted based on the start reservoir and the best efficiency point of the plant. If cuts are used, water values from the most restrictive cut given the end volume of all reservoirs in the systems are used. |
| Objective       | sim\_vow\_in\_transit  | double        | Value of the simulated end storage of water in the reservoirs. The same water value is used as for the reservoir below.                                                                                                                                                                                                                                                                         |
| Objective       | sim\_market\_sale\_buy | double        | Market price times the simulated production and consumption for all units in the system.                                                                                                                                                                                                                                                                                                        |
| Objective       | sim\_startup\_costs    | double        | Startup and shutdown costs for all changes in production between 0 and any number larger than 1.0e-3 for all timesteps when mip\_flag is activated for the plant.                                                                                                                                                                                                                               |
| Objective       | sim\_rsv\_penalty      | double        | The sum of absolute values of artificially added and removed water from reservoirs in the simulation multiplied with the reservoir penalty cost used in the optimization.                                                                                                                                                                                                                       |

+++

## Examples

Examples available for simulation.
