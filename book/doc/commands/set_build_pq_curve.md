## Determining the building method for PQ curve
In SHOP, there are four choices as input data to set working limit for a unit: 1) Min_prod/Max_prod, given by [](generator) attributes; 2) interpolation of the first points/last points of head-dependent turb_eff_curves; 3) Time-dependent min_p_constr/max_p_constr; 4) Time-dependent min_q_constr/max_q_constr. When we build PQ curve for a unit, two methods can be chosen.

If the user chooses to build PQ including all the limits, then the possible minimum working limit of the PQ curve is defined as MAX(Min_prod, interpolation of the first points of head-dependent turb_eff_curves, Time-dependent min_p_constr, Time-dependent min_q_constr), while the possible maximum working limit is defined as MIN(Max_prod, interpolation of the last points of head-dependent turb_eff_curves, Time-dependent max_p_constr, Time-dependent max_q_constr). It there is production schedule or discharge schedule on the unit, only one point referring to the schedule will be established.

If the user chooses to build PQ curves based on the scope of the turbine efficiency curves, the possible working limit of the PQ curve is defined by interpolating the first points/last points of the turbine efficiency curves. Other limits will be linearly interpolated after the PQ curve is built. In the context, even there is a schedule, the whole PQ curve reflecting the working area of the turbine will be built.
```
set build_pq_curve /<option>
```

|<option>|Comment|
|---|---|
|all_limits|All the unit limits are taken into account|
|turb_eff_curves|Based on the scope of head-dependent turbine efficiency curves|

If command is not set: PQ curve is built by including all the limits.