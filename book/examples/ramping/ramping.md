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

(ramping)=
# Ramping

+++

## Standard ramping functionality

The standard ramping functionality in SHOP enables the user to set an upper limit on the change of a variable between two consecutive timesteps. Different limits can be set for maximum up-ramping (increase in variable value between two timesteps) and maximum down-ramping (decrease in variable value between two timesteps). In addition, a penalty cost may be given for breaking the ramping constraint. The table below gives an overview of the variable types that can have ramping restrictions. 

|Object type|Variable|Direction|Ramping attribute|Unit|Global penalty|Object penalty|
|-|-|-|-|-|-|-|
|[](reservoir)|volume|up|[](reservoir:volume_ramping_up)|Mm$^3$/h|[](global_settings:volume_ramp_penalty_cost)||
|[](reservoir)|volume|down|[](reservoir:volume_ramping_down)|Mm$^3$/h|[](global_settings:volume_ramp_penalty_cost)||
|[](reservoir)|level|up|[](reservoir:level_ramping_up)|m/h|[](global_settings:level_ramp_penalty_cost)||
|[](reservoir)|level|down|[](reservoir:level_ramping_down)|m/h|[](global_settings:level_ramp_penalty_cost)||
|[](plant)|production|up|[](plant:production_ramping_up)|MW/h|[](global_settings:production_ramp_penalty_cost)||
|[](plant)|production|down|[](plant:production_ramping_down)|MW/h|[](global_settings:production_ramp_penalty_cost)||
|[](plant)|discharge|up|[](plant:discharge_ramping_up)|m3s/h|[](global_settings:production_ramp_penalty_cost)||
|[](plant)|discharge|down|[](plant:discharge_ramping_down)|m3s/h|[](global_settings:production_ramp_penalty_cost)||
|[](gate)|discharge|up|[](gate:discharge_ramping_up)|m3s/h|[](global_settings:gate_ramp_penalty_cost)|[](gate:ramp_penalty_cost)|
|[](gate)|discharge|down|[](gate:discharge_ramping_down)|m3s/h|[](global_settings:gate_ramp_penalty_cost)|[](gate:ramp_penalty_cost)|
|[](contract)|outtake|up|ramping_up|MW/h||ramping_penalty_cost_up|
|[](contract)|outtake|down|ramping_down|MW/h||ramping_penalty_cost_down|

As seen from the units, max ramping is specified per hour. If the timestep length is different than one hour, the max ramping value will be scaled accordingly by the model to keep the limit per hour constant.

## Special ramping functionality

### Reservoir

#### Non-sequential volume ramping

Non-sequential ramping consists of two input TXY-series. The first, **nonseq_ramping_steplength**, indicates how many timesteps the ramping restriction spans. The second, **nonseq_ramping_limit**, indicates the maximum ramping allowed between the start and end timestep. As an example, nonseq_ramping_steplength is set to the constant value of 24, and the optimization time resolution is measured in hours. The nonseq_ramping_limit is set to 0.1 for 01.01.2021 00h00, 0.2 for 02.01.2021 00h00 and 0.3 for 03.01.2021 00h00. This results in six ramping restrictions being added to the problem, as shown in the table below.

|Start time|End time|Max ramping|
|-|-|-|
|01.01.2021 00h00|02.01.2021 00h00|0.1 Mm$^3$|
|02.01.2021 00h00|03.01.2021 00h00|0.2 Mm$^3$|
|03.01.2021 00h00|04.01.2021 00h00|0.3 Mm$^3$|

If a timestep in the nonseq_ramping_steplength series is given a value of 0, it means that there is no ramping constraint from that timestep.

#### Amplitude volume ramping

Amplitude ramping consists of two input TXY-series. The first, **amplitude_ramping_duration**, indicates how many timesteps the ramping restriction lasts. The second, **amplitude_ramping_limit**, indicates the maximum ramping allowed between the start and each of the timesteps in the duration. As an example, amplitude_ramping_duration is set to the constant value of 2, and the optimization time resolution is measured in hours. The amplitude_ramping_limit is set to 0.1 for 01.01.2021 00h00, 0.2 for 01.01.2021 02h00 and 0.3 for 01.01.2021 04h00. This results in six ramping restrictions being added to the problem, as shown in the table below.

|Start time|End time|Max ramping|
|-|-|-|
|01.01.2021 00h00|01.01.2021 01h00|0.1 Mm$^3$|
|01.01.2021 00h00|01.01.2021 02h00|0.1 Mm$^3$|
|01.01.2021 02h00|01.01.2021 03h00|0.2 Mm$^3$|
|01.01.2021 02h00|01.01.2021 04h00|0.2 Mm$^3$|
|01.01.2021 04h00|01.01.2021 05h00|0.3 Mm$^3$|
|01.01.2021 04h00|01.01.2021 06h00|0.3 Mm$^3$|

If a timestep in the amplitude_ramping_duration series is given a value of 0, it means that there is no ramping constraint from that timestep.

### Contract

#### Max capacity on ramping violation

A maximum limit on the violation of ramping restrictions on contracts can be set by the attributes **ramping_penalty_capacity_up** and **ramping_penalty_capacity_down**.

+++

## Examples

Examples available for ramping.
