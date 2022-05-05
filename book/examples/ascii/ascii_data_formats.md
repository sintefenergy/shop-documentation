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

(ascii-data)=
# ASCII data formats

+++

The listed formats and following data layouts are accepted by the ASCII interpreter in SHOP. Comments can be inserted if the first character on the line is #.

- [Single value](#Single_value)
- [XY-curve](#XY-curve)
- [TXY-series](#TXY-series)
- [OPTIMIZATION time](#Optimization_time)
- [OPTIMIZATION time_resolution](#Optimization_time_resolution)
- [CONNECT](#Connect)
- [MARKET](#Market)
- [RESERVOIR attributes](#Reservoir_attributes)
- [PLANT attributes](#Plant_attributes)
- [GENERATOR attributes](#Generator_attributes)
- [NEEDLE_COMB attributes](#Needle_comb_attributes)
- [PUMP attributes](#Pump_attributes)
- [GATE attributes](#Gate_attributes)
- [TUNNEL attributes](#Tunnel_attributes)
- [JUNCTION attributes](#Junction_attributes)
- [JUNCTION_GATE attributes](#Junction_gate_attributes)
- [CREEK_INTAKE attributes](#Creek_intake)
- [PRESSURE_POINT attributes](#Pressure_point)
- [CONTRACT definition](#Contract_definition)
- [PLANT_OUTLET](#Plant_outlet)
- [STARTRES](#Startres)
- [SHOP_WATER_VALUES](#Shop_water_values)
- [NAMELIST](#Namelist)
- [NAMELIST_ICC](#Namelist_icc)
- [SHOP_EXT_WATER_VALUES](#Shop_ext_water_values)
- [CUTORDER](#Cutorder)
- [LOSE_SPILL](#Lose_spill)
- [INITIAL_STATE](#Initial_state)
- [MULTI_OBJECT_DATA](#Multi_object_data)

To identify the data layout of the following lines, the ASCII interpreter in SHOP reads up to five identifiers on the line preceding the actual data. They must be ordered as in the table below.

|Name|Comment|
|-|-|
|Object type|Refers to which object type the data describes|
|Attribute|Refers to which attribute the data describes|
|Object name|Name identifying the object the data should be applied to|
|Second object_name|Name identifying the second object, if data is given as a relation between two objects|
|Third object_name|Name identifying the third object, if data is given as a relation between three objects|

+++

## Single value <a name="Single_value"></a>

A single value can be input to SHOP by preceding it with a line identifying the **object_type**, **attribute** and **object_name** that it refers to. Below is an example of setting a single value for gate "Gate1".

    #Object_type Attribute  Object_name
     GATE        slackflag  Gate1
    #value 
     0 

All attributes in the <a href="https://shop.sintef.energy/shop-object-attributes/" target="_parent">reference table</a> with datatype **int**, **double** and **string** can generally be input using the ASCII Single value-format described here. Exceptions from this rule are listed in the [exception table].

+++

## XY-curve <a name="XY-curve"></a>

The structure is used to store a single XY function that consists of the elements given in the table below.

|Name|Comment|
|-|-|
|Id|Id number (not used internally, set to 0)
|Number|Unit number (not used internally, set to 0)
|Reference|Reference value (depends – if not used, set to 0)
|Pts|The number of data pairs
|X_unit|MW, METER, PERCENT etc.
|Y_unit|MW, MM3, PERCENT etc.
|pairs of (x,y)|Related values of data pairs x and y

The **Id** and **Number** fields are not used by SHOP. We simply set these values to 0. The **Reference** is for example used for efficiency curves to hold the reference head (meters) for the given curves. However, reference is not always used for each individual case. If a XY function does not need reference, we can simply set the value to 0. The **X_unit** and **Y_unit** must match the SHOP-definition for the given function. Below is an example of an XY function about the relationship between water volume and level of a reservoir.

    #Object_type Attribute  Object_name
     RESERVOIR   vol_head   Reservoir1
    #Id Number Reference Pts X_unit Y_unit
     0  0      0         5   MM3    METER
    #x      y
     0.00   860.00
     5.07   870.00
     10.34  878.00
     21.10  890.00
     30.36  898.00

All attributes in the <a href="https://shop.sintef.energy/shop-object-attributes/" target="_parent">reference table</a> with datatype XY can generally be input using the ASCII XY-format described here. XYN functions can be input by repeating XY formats with different reference. Exceptions from this rule are listed in the [exception table].

+++

## TXY-series <a name="TXY-series"></a>
This data structure is used for the time-dependent values. The structure consists of the elements listed in the table below.

|Name|Comment|
|-|-|
|Id|Id number (not used internally, set to 0)|
|Number|Unit number (not used internally, set to 0)|
|Start_time|Start time of first data in the series|
|Time_unit|MINUTE, HOUR, DAY, WEEK etc.|
|Period|Period length, if data is repeatable|
|Data_type|-1 or 0 (tells how to interpret series values)|
|Y_unit|MW, MM3, PERCENT etc.|
|Pts|The number of data pairs|
|pairs of (time,y)|Related values of data pairs time and y|

The **Id** and **Number** fields are not used by SHOP. The **Start_time** is the time of the first y-value. The time format can be 17 digits yyyymmddhhmmssmmm <year, month (1-12), day (1-31), hour (0-23), minute (0-59), second (0-59) millisecond (0-999)>. If fewer digits are used, it is assumed that the omitted digits are all zero. The **Time_unit** is MINUTE or HOUR according to the definition of given data. If **Period** = 0, complete data must be given for the whole planning period; If Period > 0, the last value will be repeatedly used until the end of planning period; If data is specified in hours for a given day and the Period = 24, the data will be used repeatedly for each day in the optimization period. The **Data_type** describes how the data for a point of time between the specified two points will be interpreted. If Data_type = 0, the current value is a linear interpolation based on the two points on either side or an extrapolation before or after the end; If Data_type = –1, the current value is set to the value of the nearest previous value (most commonly used). The **Y_unit** must match the SHOP-definition for the given function. The time values are start times for the corresponding y values. The first t-value must always be equal to the Start_time. Most time series in SHOP can be deactivated by writing NaN as the value. The table below shows an example of a TXY function that is a minimum production constraint on the discharge of a hydropower plant. The constraint is active until January 1st 18:00.

    #Object_type Attribute    Object_name
     PLANT       min_p_constr Plant1
    #Id Number Start_time Time_unit Period Data_type Y_unit Pts
     0  0      2021010100 HOUR      24     -1        MW     4
    #time       y
     2021010100 200.00
     2021010108 400.00
     2021010112 300.00
     2021010118 NaN

All attributes in the <a href="https://shop.sintef.energy/shop-object-attributes/" target="_parent">reference table</a> with datatype TXY can generally be input using the ASCII TXY-format described here. Exceptions from this rule are listed in the [exception table].

+++

## OPTIMIZATION time <a name="Optimization_time"></a>

The duration of the optimization period is defined by the **Start_time** and the **End_time**. The Start_time is the first point in time that is included in the optimization horizon, and the End_time is the first point in time that is after the optimization horizon. In the example below the optimization period will be one week.

    #Object_type  Attribute
     OPTIMIZATION time
    #Start_time End_time
     2021010100 2021010800

+++

## OPTIMIZATION time_resolution <a name="Optimization_time_resolution"></a>

SHOP accepts both fixed and time-dependent resolution in the optimization period. The time_resolution uses the standard **TXY** format, but must be given *directly after the OPTIMIZATION time, and before any other data* is input to SHOP. In the example below the time resolution is 1 hour for the first day, and 3 hours for the remaining days. 

    #Object_type  Attribute
     OPTIMIZATION time_resolution
    #Id Number Start_time Time_unit Period Data_type Y_unit Pts
     0  0      2021010100 HOUR      8760   -1        HOUR   2
    #time       y
     2021010100 1
     2021010200 3

+++

## CONNECT <a name="Connect"></a>

Connection of the different components is done using the object_type CONNECT. In addition there is used a number of identification words which tells what type of elements to connect. The general syntax is defined on the following line.

    CONNECT <from_object_type>/<to_object_type> <from_object_name> <to_object_name>

In the example below the plant Plant1 is connected as output from Reservoir1.

    #Object_type Attribute       Object_name Second_object_name
    CONNECT      RESERVOIR/PLANT Reservoir1  Plant1

+++

## MARKET <a name="Market"></a>

The market is described as an XY-table that contains options for buying and selling electricity. The **x-value** is the trading volume in MW and **y-value** is the price per MWH. SHOP does not need to know which monetary unit is used, it is the users responsibility to use the monetary unit consistently for all values input to SHOP. SHOP designates monetary units by KRONER or NOK, but this does not mean that Norwegian Kroner has to be used as the actual unit.

Each of these market functions has a **Start_time** that defines from which interval the function is used. One function is valid until the next one become active.  
The market options must be applied in order from selling to buying sorted by the size of the options. The amount for selling is negative and the one for buying is positive.

The market structure can be divided into an **area** description. One market for each area must be supplied. A market description for one area is shown in the table below. Take for example the description for the first hour. This description applies an option for selling at price 170.070 KRONER/MWH with a 500 MW capacity limit. Option Two tells that it is possible to buy maximum 500 MW capacity for the price of 170.072 KRONER/MWH.

    #Object_type Area_no
     MARKET      1
    #Number of XY-table for Area 1
     5
    #Start_time for 1st XY-table
     2021010100
    #Id Number Reference Pts _unit Y_unit
     0  0      0         2    MW   KRONER
    #x       y
     -500.00 170.070
     500.00  170.072
    #Start_time for 2nd XY-table
     2021010107
    #Id Number Reference Pts _unit Y_unit
     0  0      0         2    MW   KRONER
    #x       y
     -500.00 200.420
     500.00  200.422
    #Start_time for 3rd XY-table
     2021010112
    #Id Number Reference Pts _unit Y_unit
     0  0      0         2    MW   KRONER
    #x       y
     -500.00 180.290
     500.00  180.292
    #Start_time for 4th XY-table
     2021010116
    #Id Number Reference Pts _unit Y_unit
     0  0      0         2    MW   KRONER
    #x       y
     -500.00 171.380
     500.00  171.382
    #Start_time for 5th XY-table
     2021010120
    #Id Number Reference Pts _unit Y_unit
     0  0      0         2    MW   KRONER
    #x       y
     -500.00 165.110
     500.00  165.112


+++

## RESERVOIR attributes <a name="Reservoir_attributes"></a>

Using an ASCII input file the reservoir structure for attributes is shown below.

    #Object_type Attribute  Object_name
     RESERVOIR	 attributes	Reservoir1
    #Id Water_course Type Maxvol Lrl    Hrl
     0  0            0    300.00 400.00 450.00

+++

## PLANT attributes <a name="Plant_attributes"></a>

Using an ASCII input file the plant structure for attributes is shown below.

    #Object_type Attribute  Object_name
     PLANT       attributes Plant1
    #id water_course type bid_area prod_area num_units num_pump
     1  1            0    1        1         2         0
    #num_main_segm num_penstock time_delay prod_factor outlet_line
     1             2            0          0.000       100.000
    #main_loss
     0.00001
    #penstock_loss
     0.00001 0.000011

+++

## GENERATOR attributes <a name="Generator_attributes"></a>

Using an ASCII input file the generator structure for attributes can have two formats. The first format must be used if the **type** of generator is given as **0 or 1**, while the second format must be used if the type of generator is given as **pelton**. The generator is identified by the name of the plant and the following number of the unit. In the example below attributes are set for generator 1 and generator 2 in Plant1. The first generator is not a pelton unit, while the second one is.

### Non-pelton format

    #Object_type Attribute  Object_name Second_object_name
     GENERATOR   attributes Plant1      1
    #id type penstock nomprod minprod maxprod start_cost
     0  0    1        45.000  15.000  50.000  2100.0

### Pelton format

    #Object_type Attribute  Object_name Second_object_name
     GENERATOR   attributes Plant1      2
    #id type   penstock start_cost no_needle_comb
     0  pelton 2        2100.0     3

+++

## NEEDLE_COMB attributes <a name="Needle_comb_attributes"></a>

Using an ASCII input file the needle_comb structure for attributes is shown below. In the example attributes are set for needle combination 1 of generator 1 in Plant1. The needle combination number is given as the third object name, while the generator number is given as the second object name.

    #Object_type Attribute  Object_name Second_object_name Third_object_name
     NEEDLE_COMB attributes Plant1      1                  1
    #id type nom_prod min_prod max_prod
     0  0    120      70       120

+++

## PUMP attributes <a name="Pump_attributes"></a>

Using an ASCII input file the pump structure for attributes is shown below. The pump is identified by the name of the plant and the following number of the unit. In the example below attributes are set for pump 1 in Plant1.

    #Object_type Attribute  Object_name Second_object_name
     PUMP        attributes Plant1      1
    #id type penstock nomprod start_cost minprod maxprod
     0  0    1        45.000  5000.0     80      100

+++

## GATE attributes <a name="Gate_attributes"></a>

Using an ASCII input file the gate structure for attributes is shown below.

    #Object_type Attribute  Object_name
     GATE        attribute  Gate1
    #Id water_course type time_delay num_parallel_gates gate_slack
     1  1            0    0          1                  0

+++

## TUNNEL attributes <a name="Tunnel_attributes"></a>

Using an ASCII input file the tunnel structure for attributes is shown below.

    #Object_type Attribute  Object_name
     TUNNEL      attributes Tunnel1
    #loss_factor start_height end_height diameter length
     0.00016     90           90         3        2022

+++

## JUNCTION attributes <a name="Junction_attributes"></a>

Using an ASCII input file the junction structure for attributes is shown below. The tunnel losses are given first for tunnel1 and on the next line for tunnel2.

    #Object_type Attribute  Object_name
     JUNCTION    attributes Junction1
    #id type num_inputs altitude junc_slack
     0  0    2          80.0     0
    #Tunnel loss
     0.0004
     0.0002

+++

## JUNCTION_GATE attributes <a name="Junction_gate_attributes"></a>

Using an ASCII input file the junction_gate structure for attributes is shown below. The tunnel losses are given first for tunnel1 and on the next line for tunnel2.

    #Object_type Attribute  Object_name
     JUNCTION    attributes JunctionGate1
    #id type num_inputs altitude junc_slack
     0  0    2          80.0     0
    #Tunnel loss
     0.0004
     0.0002

+++

## CREEK_INTAKE attributes <a name="Creek_intake_attributes"></a>

Using an ASCII input file the creek_intake structure for attributes is shown below.

    #Object_type  Attribute  Object_name
     CREEK_INTAKE attributes Creek1
    #Id main_tunnel_loss tunnel_loss creek_level cap_mode
     0  0.0005           0.0001      456.2       0

+++

## PRESSURE_POINT attributes <a name="Pressure_point_attributes"></a>

Using an ASCII input file the pressure_point structure for attributes is shown below.

    #Object_type    Attribute  Object_name
     PRESSURE_POINT attributes PressurePoint1
    #id loss_factor
     0  0.001

+++

## CONTRACT definition <a name="Contract_definition"></a>

Using an ASCII input file the definition of contracts is shown below. It is similar to the **MARKET** format, but using the **definition** keyword and without the connection to a production area.

    #Object_type Attribute  Object_name
    CONTRACT	 definition	Contract1
    #Number of XY functions for this contract
     3
    #Start time for this contract
     2021010100
    #Id Number Reference Npts x_unit y_unit
     0  1      0.0       4    MW     NOK/MWH
    #x    y
     -500 100
     -200 140
     100  150
     500  180
    #Start time for this contract
     2021010101
    #Id Number Reference Npts x_unit y_unit
     0  1      0.0       4    MW     NOK/MWH
    #x    y
     100  160
     500  190
     700  205
     1100 210
    #Start time for this contract
     2021010102
    #Id Number Reference Npts x_unit y_unit
     0  1      0.0       4    MW     NOK/MWH
    #x   y
     100 130
     300 145
     400 190
     575 220

+++

## PLANT_OUTLET <a name="Plant_outlet"></a>

Using an ASCII input file the plant_outlet structure is shown below. In contrast to other objects, the **name** of the plant_outlet is given at the second position of the line, normally used for attributes.

    #Object_type Name
    PLANT_OUTLET Outlet1
    #num_main_seg
     2
    #Main_segment_loss no_of_plants plant_names
     0.001             2            Plant1 Plant2
     0.002             3            Plant1 Plant2 Plant3

+++

## STARTRES <a name="Startres"></a>

Using an ASCII input file the startres structure is shown below. In contrast to other objects, the position normally used for the attribute name is here used for the **number of upcoming lines** with start reservoir data. The **unit** can either be METER or MM3 and must be the same for all reservoirs in one STARTRES definition.

    #Object_type num_of_rsv unit
     STARTRES    2          METER
    #Object_name value
     Reservoir1  872.62
     Reservoir2  694.20

+++

## SHOP_WATER_VALUES <a name="Shop_water_values"></a>

Using an ASCII input file the SHOP_WATER_VALUES structure for sending cut data in to SHOP is shown below. The module numbers are connected to SHOP reservoirs by the **NAMELIST** or **NAMELIST_ICC** data format, which must be read before the SHOP_WATER_VALUES.

    #Object_type
    SHOP_WATER_VALUES
    #Start set block
    <Number of cuts> <Number of reservoirs in this set>
    #Start cut block 1
    <Cut number> <Future cost in 1000. NOK>
    <Water values for all reservoirs in this set in 0.01 NOK/M3>
    <Reservoir levels for all reservoirs in this set in %>
    #End cut block 1
    #Start cut block 2
    :
    #One cut block for each cut
    :
    #End block <Number of cuts>
    <List of local energy conversion factors for all reservoirs in this set>
    <List of module numbers for all reservoirs in this set>
    #End block 1
    #Start set block 2
    :
    #One set block for each area/watercourse :
    #End set block N
    -1

The following example sets 11 cuts for one watercourse with 3 reservoirs.

    #Object_type
    SHOP_WATER_VALUES
    #Number_of_cuts Number_of_reservoirs
     3              11
    #Cut_number Future_cost_in_1000_NOK
     1          553312.1
    #Water values for eleven reservoirs in 0.01 NOK/M3
    28.5524 16.16501 30.05662 27.31609 18.33097 31.69323 18.33097 23.42278 23.42282 18.18101 0.553201
    #Reservoir levels for eleven reservoirs in %
    52.02749 56.55629 47.51908 50.97015 48.0 55.62481 49.70543 56.47799 60.0 65.08929 0.0
    #Cut_number Future_cost_in_1000_NOK
     2          570255.6
    #Water values for eleven reservoirs in 0.01 NOK/M3
    28.39524 16.06559 29.71364 27.1114 18.07443 31.32807 18.07443 21.75594 21.75604 17.91683 0.526877
    #Reservoir levels for eleven reservoirs in %
    59.36426 59.85431 56.94656 57.70149 57.82609 59.23583 57.78295 59.84277 62.5 78.75 56.66
    #Cut_number Future_cost_in_1000_NOK
     3          577362.1
    #Water values for eleven reservoirs in 0.01 NOK/M3
    27.75463 15.46218 29.55889 27.048 17.98072 31.18911 17.98072 21.38204 21.3822 17.81284 0.525238
    #Reservoir levels for eleven reservoirs in %
    63.43642 61.74834 60.57252 60.1194 61.56522 60.74695 60.75969 61.32076 67.5 95.0 81.94
    #Water conversion factors kwh/m3
    0.662361 0.841444 0.587607 0.428571 0.0 0.729769 0.0 0.0 0.607639 0.985663 2.79412E-02
    #Module numbers
    7811 7810 7814 7815 7906 7818 7903 7911 7813 7812 7809
    -1

+++

## NAMELIST <a name="Namelist"></a>

Using an ASCII input file there are two formats for connecting module numbers in the **SHOP_WATER_VALUE** and **SHOP_EXT_WATER_VALUE** data to reservoir names in SHOP, **NAMELIST** and **NAMELIST_ICC**. The general structure of the **NAMELIST** format is shown below.

    NAMELIST
    <Reservoir name 1>	<module number 1>
    <Reservoir name 2>	<module number 2>
    <Reservoir name 3>	<module number 3>
    -1	

In the following example, Reservoir1 corresponds to module 8001 in the SHOP_WATER_VALUE data, Reservoir2 and Reservoir3 are aggregated in module 8002 while Reservoir4 corresponds to module 8003.

    #Object_type
    NAMELIST
    Reservoir1 8001
    Reservoir2 8002
    Reservoir3 8002
    Reservoir4 8003
    -1

+++

## NAMELIST_ICC <a name="Namelist_icc"></a>

Using an ASCII input file there are two formats for connecting module numbers in the **SHOP_WATER_VALUE** and **SHOP_EXT_WATER_VALUE** data to reservoir names in SHOP, **NAMELIST** and **NAMELIST_ICC**. The general structure of the **NAMELIST_ICC** format is shown below.

    NAMELIST_ICC
    <number1>, <value1>
    <number2>, <value2>
    <number3>, <value3>
    -1
    
The number may be one of the following.
- 0, Comment line, line ignored. (In addition lines started by #, blank lines and lines started with unknown numbers are also treated as comments.) 
- 2, The value is a module number. 
- 3, The value is a name belonging to the most recently read module number. The name is assumed to contain no blanks. 

The same example provided for the **NAMELIST** format is repeated here in the **NAMELIST_ICC** format.

    #Object_type
    NAMELIST_ICC
    0, Example of a namelist.
    #Reservoir1 is module 8001
    2, 8001
    3, Reservoir1
    #In the SHOP_WATER_VALUE data, Reservoir2 and Reservoir3 are aggregated in module 8002
    2, 8002
    3, Reservoir2
    3, Reservoir3
    #Reservoir4 is module 8003
    2, 8003
    3, Reservoir4
    -1


+++

## SHOP_EXT_WATER_VALUES <a name="Shop_ext_water_values"></a>

Using an ASCII input file the SHOP_EXT_WATER_VALUES structure for sending price- and inflow-dependent cut data in to SHOP is shown below. The module numbers and inflow series are connected to SHOP reservoirs by the **NAMELIST** or **NAMELIST_ICC** data format and the order of modules and inflow series on the cut file is defined by the **CUTORDER** data format. Both NAMELIST or NAMELIST_ICC and CUTORDER data must be read before the SHOP_EXT_WATER_VALUES.

- The first column is the price level in 0.01 NOK/kWh the cut is generated for.
- Second column is the expected future value of the cut in 1000 NOK.
- Third column is the number of modules in the cut, n_mod.
- The next columns are n_mod pairs of cut coefficients in 0.01 NOK/M3 and reference volume in % for each module.
- The following column is the number of inflow series in the cut, n_inflow.
- The final n_inflow columns are the inflow coefficients for each inflow series.

The example below shows cuts for two price levels, three modules and three inflow series

    #Object_type
    SHOP_EXT_WATER_VALUES
    #Price Future_value n_mod coeff_mod1 ref_mod1 coeff_mod2 ref_mod2 coeff_mod3 ref_mod3 n_inflow coeff_inflow1 coeff_inflow2 coeff_inflow3
     13.5  1505341.2    3    37.4       4.1      37.4       0.007    51.0       1.1       3        0.0           0.0           0.0
     13.5  1505690.3    3    76.1       0.2      55.5       0.08     91.9       0.8       3        0.0           0.0           0.0
     15.9  1518310.1    3    44.2       4.1      44.2       0.007    59.4       1.1       3        0.0           0.0           0.0
     15.9  1518738.0    3    84.7       0.2      59.8       0.08     100.7      0.8       3        0.0           0.0           0.0

+++

## CUTORDER <a name="Cutorder"></a>

Using an ASCII input file the CUTORDER format is used for defining the order of modules and inflow series in the **SHOP_EXT_WATER_VALUE** data. The NAMELIST or NAMELIST_ICC format must be read first to connect module numbers with reservoir names in SHOP.

- The first column is the order of the module. 0 means that no cut data is given for this module.
- The second column is the number of the module.
- The third column is the order of the regulated inflow series for the module.
- The fourth column is the order of the unregulated inflow series for the module.

The example below shows that cut coefficients are given for modules 8001, 8002 and 8003 in that order. No cut coefficients are given for module 8000. Modules 8001 and 8002 both share the first inflow series, while 8003 has the second inflow series. The inflow series for module 8000 is the last one in the cut file.

    #Object_type
    CUTORDER
       1     8001   1   1
       2     8002   1   1
       3     8003   2   2
       0     8000   3   3

+++

## LOSE_SPILL <a name="Lose_spill"></a>

Using an ASCII input file the lose spill structure is shown below. If the spill is directed somewhere by a spill gate, this connection is ignored, and the spill is lost. In the example Reservoir1 and Reservoir2 will both lose their spill.

    #Object_name Number_of_reservoirs
     LOSE_SPILL  2
    #Reservoir_name
     Reservoir_1
     Reservoir_2

+++

## INITIAL_STATE <a name="Initial_state"></a>

Using an ASCII input file the initial state structure is shown below. After INITIAL_STATE follows the number of aggregates /pumps with an initial state. The next line contains the plant name, generator or pump object type, the generator- or pump number and finally the initial state.

    #Object_type Number_of_aggregates_and_pumps
    INITIAL_STATE 3
    #Plant_name GENERATOR_or_PUMP unit_number initial_state
     Plant1     GENERATOR         1           0
     Plant1     GENERATOR         2           1
     Plant2     PUMP              1           1

+++

## MULTI_OBJECT_DATA <a name="Multi_object_data"></a>

Using an ASCII input file the multi object data structure is shown below. MULTI_OBJECT_DATA marks the start tag of a multi object constraint, and /MULTI_OBJECT_DATA defines the closing of the multi object data. A multi object constraint contains sections defined by specified start and end tags. The multi object must contain an object list section and a data value section, and may contain one interval and penalty cost section.

    #Object_type      Attribute Object_name Second_object_name
    MULTI_OBJECT_DATA keyword   sense       name
    OBJECT_LIST
    object_type1 name1
    objevt_type2 name2
    ...
    /OBJECT_LIST
    TIME_INTERVAL
    start_time end_time
    /TIME_INTERVAL
    PENALTY_COST unit
    UP value unit
    DOWN value unit
    /PENALTY_COST
    DATA_VALUE
    data value unit
    /DATA_VALUE
    /MULTI_OBJECT_DATA

Valid values for MULTI_OBJECT_DATA: 
- Type of constraint <keyword>: 
    - Sum for each time step: sum_discharge, sum_production_time_step, spinning_reserve, total_reserve, contract_volume_time_step; 
    - Sum/Average in a time interval: average_discharge, sum_production_time_period; 
    - Ramping specific: power_ramping, discharge_ramping, storage_ramping; 
- Sense of constraint <sense> : 
    - Less than: L or l (if the constraint is of type a+b≤c), 
    - Greater than: G or g (constraints of type a+b≥c), 
    - Equal to: E or e (constraints of type a+b=c); 
Name of restriction <name>: string
    - The name should be unique within the set of names used for constraints. 

The sense of a constraint has a different meaning for ramping. Namely, L stands for ramping up and G stands for ramping down. E is not used in combination with ramping.

The object list is a list of the objects involved in the constraint. The list can be of any length, excet for ramping which only accepts single objects).

Valid values for OBJECT_LIST: 
- object_type: PLANT, GATE, RESERVOIR 
- name: The name of the plant, gate and reservoir, respectively. 

    OBJECT_LIST MyList
    object_type1 name1
    objevt_type2 name2
    ...
    /OBJECT_LIST

Valid values for TIME_INTERVAL: 
- start_time: yyyymmddhhmmssmmm
- end_time: yyyymmddhhmmssmmm
    
Default value (if time_interval is not included) is the whole optimization period.  
Valid values for PENALTY_COST: 
- value: double 
- unit: NOK_H_M3_S — (money_units/hour)/(m3/s); NOK_MWH — money_units/ mega_watt_hour. 
Valid values for DATA_VALUE: 
- data_value: double 
- unit: M3SEC; MW; MWH; MM3; METER. 

The allowed combinations that can be used in multi object format are listed below.

    
|Attribute|Object_types|Unit|Penalty_unit|
|-|-|-|-|    
|sum_discharge|PLANT,GATE|M3SEC|NOK_H_M3_S|
|sum_production_time_step|PLANT,CONTRACT|MW|NOK_MWH|
|spinning_reserve|PLANT,CONTRACT|MW|NOK_MWH|
|total_reserve|PLANT,CONTRACT|MW|NOK_MWH|
|contract_volume_time_step|PLANT,CONTRACT|MW|NOK_MWH|
|average_discharge|PLANT,GATE|M3SEC,MM3|NOK_H_M3_S|
|sum_production_time_period|PLANT,CONTRACT|MWH,MW|NOK_MWH|
|power_ramping|PLANT,CONTRACT|MW|NOK_MWH|
|discharge_ramping|PLANT,GATE|M3SEC|NOK_H_M3_S|
|storage_ramping|RESERVOIR|MM3,METER|NOK_MM3|
