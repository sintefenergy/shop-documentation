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

# Water budgeting

+++

## Introduction

It is possible to run a simulation in SHOP with reservoir storage volume
or height as input, and in return get the inflow that would have
resulted in the given storage level. This document describes the
additional data and commands related to the inflow simulation. See the
main documentation for the simulator in SHOP for a complete description
of that functionality.

## Input data 

The main additional input for the inflow simulation is the storage level
for each reservoir. It can either be given in Mm3 or in masl. If there
are creek intakes in the system, and
inflow

| **Object type** | **Attribute name**        | **Data type** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------- | ------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reservoir       | sim\_inflow\_flag         | TXY           | This flag turns inflow simulation on or off for individual reservoirs. The global /inflow option to the "start shopsim"-command is still needed to activate the inflow simulation functionality. If this flag series is not given, the default behavior is that inflow will be simulated for all reservoirs. If this flag is set to 0, the corresponding reservoir will be simulated with inflow taken from the "inflow" TXY series as input, and the resulting reservoir storage will be given as output. |
| Reservoir       | storage                   | TXY           | Storage level in Mm3 used as basis for inflow calculation. If both head and storage are given, the storage is used as basis for the calculation.                                                                                                                                                                                                                                                                                                                                                           |
| Reservoir       | head                      | TXY           | Storage level in masl used as basis for inflow calculation. If both head and storage are given, the storage is used as basis for the calculation.                                                                                                                                                                                                                                                                                                                                                          |
| Creek intake    | sim\_inflow\_flag         | TXY           | This flag turns inflow simulation on or off for individual creek intakes. The global /inflow option to the "start shopsim"-command is still needed to activate the inflow simulation functionality. If this flag series is not given, the default behavior is that inflow will be simulated for all creek intakes. If this flag is set to 0, the corresponding creek intake will be simulated with inflow taken from the "inflow" TXY series as input.                                                     |
| Creek intake    | pressure\_height          | TXY           | If there exists data for measurement of the pressure height (in masl) of creek intakes, this TXY can be used as input to the simulation. The pressure balance and resulting inflow to the creek intake will be calculated based on the pressure\_height measurement.                                                                                                                                                                                                                                       |
| Creek intake    | inflow\_percentage        | TXY           | If the inflow to the creek intake is assumed to be a percentage of the inflow to the reservoir above, this TXY can be used to set this percentage.                                                                                                                                                                                                                                                                                                                                                         |
| Creek intake    | reservoir\_pressure\_flag | TXY           | If the creek intake tunnel is assumed to have the same pressure height as the reservoir directly above the creek intake, this TXY can be set to 1 to indicated this.                                                                                                                                                                                                                                                                                                                                       |

If neither pressure\_height, inflow\_percentage nor
reservoir\_pressure\_flag is set for a creek intake, the inflow is
calculated based on the assumption that the creek intake has the same
pressure height as the reservoir above.

## Commands 

The only command that affects the inflow simulation is the "start
shopsim" command. By adding the option /inflow after that command, the
inflow simulation is activated in the SHOP
simulator.

| **Command**   | **Options**                                                                                 | **Comment**                                                                                                                                                                                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start shopsim | /gen\_mw\_schedule, /gen\_m3s\_schedule, /plant\_mw\_schedule, /gen\_m3s\_schedule, /inflow | Run simulation. The inflow option activates the inflow simulation in the SHOP simulator. Default behavior is that all inflow will be simulated for all reservoirs and creek intakes when this option is set. See main simulator documentation for the other options. |

## Result data

The simulator calculates the physical behaviour of the system given the
input schedules, but also reports the economical value of the schedule.

The time series in the table below are returned as physical results from
the
simulation.

| **Object type** | **Attribute name** | **Data type** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------- | ------------------ | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reservoir       | sim\_inflow        | TXY           | Resulting inflow calculated by the simulator. The inflow is calculated for each timestep as the sum of end storage minus start storage plus water discharged from the reservoir through plants and gates minus water discharged into the reservoir through plants and gates                                                                                                                                                                               |
| Creek intake    | sim\_inflow        | TXY           | Resulting inflow calculated by the simulator. The inflow is calculated as the sum of discharge to the plant below the creek intake minus flow from the reservoir above the creek intake. The distribution between creek intake inflow and reservoir inflow is found by establishing a pressure- and mass balance in the junction between the creek intake and the main tunnel. The options for controlling this balance are described above in section 2. |

+++

## Examples

Examples available for water budgeting.
