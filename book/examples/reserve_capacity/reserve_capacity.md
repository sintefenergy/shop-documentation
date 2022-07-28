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

# Reserves

+++

SHOP can model 7 different types of reserve capacity products with different technical limitations. The names of the different reserve capacities are:

- FCR-N up and down
- FCR-D up
- FRR up and down
- RR up and down

The names are based on a naming convention from the Norwegian TSO which is now outdated, but the reserve capcity products still persist.

The **FCR-N** reserve capacity corresponds to capacity used for primary frequency control in the normal deviation band, defined as 50 $\pm$ 0.1 Hz in Norway. FCR-N reserve capacity can be defined for both upward and downward directions, though a symmetric requirement is usually imposed. The **FCR-D** reserve capacity is used for frequency control for deviations outside the normal range of 0.1 Hz, but currently only exists in the upward direction (deviations between 49.9 and 49.5 Hz). **FRR** reserve capacity in the upward and downward directions are slower secondary reserves that still have to be rotating, while the tertiary reserves, labled as **RR** reserves in SHOP, can be delivered even if the unit is not spinning.

The amount of reserves that can be delivered from a spinning generating unit is normally limited by the static **p_max** and **p_min** attributes on the unit, in addition to the optimized production level. Active production constraints on the unit, see the **min/max_p_constr** generator attributes, are also considered in the reserve capcity constraints. An example illustration of a reserve capacity allocation on a generator is shown in the figure below. The behaviour is similar for variable speed pumps, though the upward and downward directions are flipped since the pump is consuming power.

<p align="center">
 <img src="./img/reserve_allocation.png">
</p>
    
As indicated by the picture above, the amount of reserve capacity possible to allocate on a single unit is closely linked to the unit commitment (on/off) constraints of the uit. It is therefore reccomended that binary unit commitment variables are active for units participating in the delivery of reserve capacity in the full SHOP iterations. This can be controlled by the **mip_flag** attribute on the plant objects, or by the `set universal_mip` command. If a unit is delivering reserve capacity in a time period without binary on/off variables, unexpected behaviour due to the relaxed unit commitment constraints can occur. For instance, a fractional startup will shift the upper and lower limits in the figure above and alter the amount of reserve capacity that can be delivered. This can again lead to penalties in incremental iterations when all units are fully turned on or off.

All of the reserve capacity functionality implemented in SHOP is tied to the **SHOP_RESERVE_GROUP** license. Other ancillary services, such as activation of reserve *energy*, is not currently implemented in SHOP.

+++

## Primary reserves

The FCR-N and FCR-D reserves are limited by the droop setting of the unit in addition to the standard capacity limits visualized in the figure above. The amount of FCR reserves that can be delivered $\left(r_{fcr}\right)$ depends on the static nominal unit production $\left(P_{nom}\right)$, the size of the frequency band $\left(\Delta_f\right)$, and the inverse of the unit droop $\left(d\right)$:

$r_{fcr} \leq 2\cdot\Delta_f\cdot P_{nom}\cdot \frac{1}{d}$.

The nominal production is specified by the **nom_prod** double attribute on the generator and pump objects, and the default value of the frequency band is 0.1 for FCR-N and 0.4 for FCR-D. The frequency ranges can be changed by setting the double attributes **fcr_n_band** and **fcr_d_band** on the global_settings object.

The default behaviour in SHOP is to let the unit droop be a free variable bound between 1 and 12: $1 \leq d \leq 12$. A generator/pump TXY attribute called **fixed_droop** with an accompanying **fixed_droop_flag** can be specified to lock the droop variable to the given value. Other TXY attributes on the generator/pump object can be specified to change the upper and lower droop bounds, namely **droop_min** and **droop_max**. The output TXY attribute **droop_result** holds the optimized value of the droop. It is also possible to define a TXY attribute **droop_cost** for each generator/pump, which adds a cost in the objective function for the droop variable. However, since the *inverse* of the droop appears in the FCR reserve limit constraint, SHOP uses the *inverse* of the droop as a variable to keep the constraints linear. This means that a high droop_cost will be applied to the inverse droop variable, favouring high droop settings (low inverse droop). 

The droop is often restricted to take on a set of discrete values in the real world, such as the integers from 1 to 12 instead of all real numbers in the same range. The **droop discretization functionality** in SHOP is a heuristic approach for fixing the droop variables to pre-defined legal droop values between iterations. A link to a separate example describing the droop discretization functionality in more detail is found at the bottom of this tutorial.

It is possible to specify upper and lower production limits for the delivery of FCR reserves that are less strict than the normal minimum and maximum production limits of the unit. The TXY attributes **p_fcr_min** and **p_fcr_max** on the generator and pump objects overrides the normal bounds for FCR reserves.

Several system operators require that the procured fcr_n reserve capacity on every unit is symmetric in the upward and downward directions. The building of symmetric fcr_n constraints can be turned on and off by changeing the **fcr_n_equality_flag** attribute on the global_settings object.

In some cases, the TSO may stipulate a capacity limit rule which requires a certain fraction of a generator's maximal production capacity to be available if the unit is used to provide FCR reserve capacity. This constraint can be activated with the **fcr_mip_flag** TXY attribute on the generator object, and will additional binary variables to enforce the limit. The free capacity limit can be changed from the default value of 2% by changing the **gen_reserve_min_free_cap_factor** attribute on the global_settings object.

+++

## Secondary reserves
Unlike the primary reserves, there are no special constraints that have to be enforced for the secondary FRR reserves, although the unit must still be running to provide FRR capacity. The FRR capacity it is possible to deliver is limited by the distance between scheduled production/consumption and the minimum and maximum generation limits, as well as the delivery of the other reserve types.

+++

## Tertiary reserves
The RR reserve capacity can be delivered from units that are turned off, which means that RR_UP is handled in a special way for generators to allow delivery from offline units, and RR_DOWN is handled in an equivalent way for pumps. This requires binary variables for a precise modelling, so allowing SHOP to use binary variables for generators delivering RR_UP and pumps delivering RR_DOWN is especially beneficial. A **p_rr_min** TXY attribute for generators and pumps can be specified to allow the unit to deliver RR reserves below the minimum production limit, typically down to zero. 

+++

## Optimal reserve capacity distribution

The reserve capcity functionality in SHOP was tailored to be used with the **reserve_group** object to optimally distribute a shared reserve capacity obligation among a defined group of units. The reserve_group object is used to specify the different reserve obligations as TXY attributes called ***\<reserve_type\>_\<direction\>_obligation***, such as **fcr_n_up_obligation** and **rr_down_obligation**. The reserve obligation(s) in the reserve_group has to be covered by the connected generator and pump objects. Unlike the energy obligation in the spot market, reserving more capacity than specified in the reserve_group obligation is not inherently problematic. Any overfulfillment is recorded by the TXY attributes ***\<reserve_type\>_\<direction\>_slack*** in the reserve_group object, and is penalized by a low cost in the objective function, see the **reserve_group_slack_cost** attribute on the global_settings object. A much higher penalty is incurred if the amount of allocated reserve capacity is less than the obligation, recorded as ***\<reserve_type\>_\<direction\>_violation*** on the reserve_group object. Violations of the reserve obligation are penalized by either the general **reserve_group_penalty_cost** attribute on global_settings or the reserve_group specific ***\<reserve_type\>_penalty_cost*** attributes.

+++

## Fixed reserve capacity schedules

It is possible to specify fixed reserve schedules for individual units by using the TXY attributes called ***\<reserve_type\>_\<direction\>_schedule***, such as **fcr_d_up_schedule**, on the generator and pump objects. The reserve capacity schedule constraints will be built independent of the reserve_group constraints, but will also count towards a reserve_group obligation if the unit is connected to a reserve_group. Not following the reserve schedule is penalized by the general **reserve_schedule_penalty_cost** attribute found on the global_settings object, and the unit specific output TXY attributes ***\<reserve_type\>_\<direction\>_schedule_penalty*** record the amount of scheduled reserve capacity that has not been fulfilled.

+++

## Reserve capacity markets

A reserve capacity market can be defined in SHOP by specifying the **market_type** attribute on the market object and connecting the market to a reserve_group object. The markte_type signifies which reserve capacity that can be traded in the market. If there is a reserve obligation mattching the market_type in the reserve_group connected to a reserve market, this is added as a load to the reserve market balance constraints. The penalties for violating the reserve market load is the same as described for the reserve_group obligation. The reserve market will otherwise function similarly to a normal energy market in SHOP, where the reserve capacity sold is remunerated with the sale price defined for the market object.

+++

## Minimum and maximum reserve capacity limits

It is possible to specify minimum and maximum limits for the reserve capacity participation of individual unts. The TXY attributes are called ***\<reserve_type\>_\<direction\>_max*** and ***\<reserve_type\>_\<direction\>_min***, such as **rr_up_max** and **fcr_n_down_min**. These max and min limits bound the delivery of a single reserve type and should not be confused with the p_fcr_min, p_fcr_max, and p_rr_min attributes described earler. For instance, the fcr_n_up_max TXY attribute applies a direct bound on the amount of FCR-N capacity the unit can deliver in the upward direction, while p_fcr_max extends the physical upper production limit of the unit for delivery of FCR-N and FCR-D. 

Applying these min and max constraints are treated similarly to the production bound constraints for generating units, as a new binary variable ($u$) is introduced to force the reserve capacity allocation ($r$) to be either zero or between the specified min and max bounds: $R^{min}\cdot u \leq r \leq R^{max}\cdot u$. Be aware that it is easy to create conflicting constraints when min and max reserve delivery constraints are used together with reserve schedules and reserve group obligations, which could lead to penalties and otherwise unexpected behaviour.

+++

## Plant reserve limits

Some reserve capacity constraints can be specified for the generators located in the same plant. Minimum and maximum limits for the amount of FRR reserves delivered from each plant can be specified using the TXY attributes **frr_\<direction\>_\<max/min\<** on the plant object. A TXY attribute for the minimum amount of allocated RR reserves in the upward direction, **rr_up_min**, also exists on the plant level, but there are no plant level FCR constraints. The minimum and maximum constraints are implimented in a similar way to the unit-specific reserve constraints mentioned above. In addition, the **frr_symmetric_flag** TXY flag series attribute can be used to make the total FRR reserve capacity allocated on the plant symmetric in the time steps where the flag is non-zero.

+++

## Reserve ramping and clustering

There is no explicit cost difference between delivering reserve capacity on two different units in SHOP. If there is available capacity on both units, meaning that the optimal production set point does not have to be changed to create the available capacity, the optimization solver used in SHOP will arbitrarily choose how to distribute the capacity between the two units. This can lead to a reserve capacity allocation that switches often between the units, which is not ideal for real world applications. Using a small cost for changing the reserve capaicty allocation between time steps will encourage a more stable allocation. Reserve ramping costs can be defined by attributes on the global_settings object, **gen_reserve_ramping_cost** and **pump_reserve_ramping_cost**, or by using the unit specific and directional TXY attributes **reserve_ramping_cost_up** and **reserve_ramping_cost_down** on the generator and pump objects. 

Note that the reserve ramping functionality requires the **SHOP_RESERVE_CLUSTERING** license. The license also enables users to set a **reserve_contribution_cost** double attribute on the global_settings object to add a cost to the objective function for each unit that has any reserve capacity allocated in each time step. Adding a reserve contribution cost can help aggregate the reserve capacity allocation so that fewer units are used to reserve capacity.

+++

# Related Examples
Examples showing the use of some of the reserve capacity functionality is available here:

- [Basic usage of the reserve capacity functionality](reserve-example)
- [Usage of the droop discretization functionality](discrete-droop)
