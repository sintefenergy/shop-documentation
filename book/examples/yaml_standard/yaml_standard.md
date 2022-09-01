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

(yaml-standard)=
# SHOP YAML Standard

```{contents}
:local:
```
## Reading and writing
Yaml-data can be read using the `load_yaml` function as shown below. The function can either read from a file or read a yaml string:

```{code-cell} ipython3
:Collapsed: 'false'

from pyshop import ShopSession

shop = ShopSession()
shop.load_yaml(file_path='basic_model.yaml')
shop.load_yaml(yaml_string='''
model:
  reservoir:
    Reservoir1:
      inflow:
        2018-01-23 00:00:00: 10.0
        2018-01-23 03:00:00: 15.0
''')

```

Similarly, the model can be dumped as a yaml file using the `dump_yaml` function. The function has three boolean options:
|Option|Default|Description|
|---|---|---|
|Input only|True|Only write input data to file|
|Compress txy|True|Only print timeseries value for timestep if value has changed from previous timestep to keep file compact|
|Compress connection|True|Write connections on compressed format. Don't write object type or connection type unless necessary to uniqely identify object/connection|

```{code-cell} ipython3
:Collapsed: 'false'

shop.dump_yaml('basic_model_results.yaml', False, True, True)
```

## YAML types
In order to simplify descriptions of the SHOP YAML standard, we start off with defining a set of terms for referring to different YAML constructs.

(yaml:map)=
### Map
Maps are one of the most common components for structuring data stored in YAML. They often appear in the upper levels of the documents and serve the purpose of dividing the data into smaller named subgroups/divisions. We will refer to them as “Maps”, but you should note that they are also often referred to as Dictionaries. Essentially, maps consist of a set of "key" and "value" pairs. Each key is said to "refer to" or "contain" a value. In this standard, keys will **always** be “strings”, i.e. one or more characters/words stringed together. Values, on the other hand, can contain a single scalar, a string or another structuring component like Map or List

#### Map example
The following example is extracted from a real SHOP YAML case and contains three distict examples of YAML Maps. The upper level is a Map containing the keys "Reservoir1" and "Reservoir2". Each key contains additional Maps with the keys "start_head", "max_vol", "lrl", "hrl" and "vol_head". Furthermore, the keys "vol_head" contains Maps with the keys "ref", "x" and "y". 

Note that the key and value is separated by a “:”. The value may be written just after “: ”, which is the case for keys like "start_head", "max_vol" and "ref". For more complex values, it is common to add line breaks and indentation, as you can see keys like "Reservoir1", "vol_head" and "x".
        
    Reservoir1:
      start_head: 92
      max_vol: 12
      lrl: 90
      hrl: 100
      vol_head:
        ref: 0
        x:
          - 0
          - 12
          - 14
        y:
          - 90
          - 100
          - 101
    Reservoir2:
      start_head: 43
      max_vol: 5
      lrl: 40
      hrl: 50
      vol_head:
        ref: 0
        x:
          - 0
          - 5
          - 6
        y:
          - 40
          - 50
          - 51

(yaml:list)=
### List
Lists are another common construct that can be used for structuring. Each value of a list, like the values of maps, can contain a scalar, a string or another structuring component like a Map or a List

### List example
The following example is extracted from a real SHOP YAML case and contains two distict examples of YAML Lists. The value of the "connections" key is a List of Maps and the value of the "commands" key is a List of strings.

Note that each element of the list is preceded by a “-” and for every new element, a line break is added. Also note that despite only having a single value, the value of "commands" is still formatted as a list. It is common to keep the List format when the list happens to have a single value, in order to simplify reading/loading the YAML.

    connections:
      - from: Reservoir1
        to: Plant1
      - from: Plant1_G1
        to: Plant1
      - from: Plant1
        to: Reservoir2
      - from: Reservoir2
        to: Plant2
      - from: Plant2_G1
        to: Plant2
    commands:
      - start sim 1

### Scalar
Scalars contain a single numeric value. In this standard, we deal with two different types of scalars, “integers” and “doubles”

#### Integer
Some attributes expect integer values, that is, numbers without any fractional parts.

**NOTE**: Numbers written with decimal points are typically not accepted as integers even if the fractional part is 0

    plant:
      Plant1:
        time_delay: 0     # "time_delay" is a Int attribute within SHOP
        ownership: 100    # NOTE: Ownership is a Double attribute within SHOP, YAML will typically omit ".0"

#### Double
Some attributes expect double values, that is, numbers with fractional parts. Unlike the converse for integers, it is common to accept numbers written without decimal points as doubles.

All the numerical values in the following YAML will be interpreted as doubles by SHOP because they refer to attributes that only deal with double values. Note that the values with ".0" fractional parts have been encoded as integers.

    Reservoir1:
      start_vol: 0
      start_head: 92.2
      max_vol: 12
      lrl: 90.5
      hrl: 100.5
      vol_head:
        ref: 0
        x:
          - 0
          - 12
          - 14
        y:
          - 90
          - 100
          - 101

### String
Strings are a common data type in programming and are essentially strings of characters/words. In YAML, strings can be written with or without quotes. Both “ and ‘ can be used as quotation marks, but you need to close the quote with the same quotation mark it was opened with.

**Note** that it is common to omit quotation unless they are needed to avoid ambiguity, which is the case for the vast majority of string. String representations of numbers is an example of a class of strings that do need quotation to retain their string nature

    connections:
    - from: Reservoir1
      to: Plant1
      from_type: reservoir
      to_type: plant
      connection_type: connection_standard
      order: 0
    - from: "Plant1_G1"                      # Note: The original example dropped quotation for all strings
      to: 'Plant1'                           # And you would most likely not mix quotation types
      from_type: generator
      to_type: "plant"
      connection_type: 'connection_standard'
      order: 1
 
(yaml:timestamp)=
#### Timestamp
A typical SHOP YAML case will typically contain many strings representing timestamps. Timestamps are used when setting optimization start and end time and the time index of every time series (TODO). Shop expects the format “YYYY-mm-dd HH-MM-ss”.

    time:
      starttime: 2018-02-27 00:00:00    # Note: the time part can be omitted because it is 00:00:00
      endtime: 2018-02-28 00:00:00
      timeunit: hour
      timeresolution:
        2018-02-27 00:00:00: 1

## SHOP YAML case
SHOP YAML case consist of four different types of content.

YAML case :

- time
- model
- connections
- commands

There are currently two different ways of defining a YAML case :

- Split up the data in 4 different files, named after the data they house, e.g. “time.yaml”
  - External python class is also capable of reading a ZipCase, which is these 4 files zipped together
- Put everything in the same file/string, where the upper level is a Map with keys for the 4 different types of content

## time
The "time" part contains the optimization time definition. The upper level is a [Map](yaml:map) with the mandatory keys “starttime”, “endtime” and “timeunit”.

“starttime” and “endtime” both expect [timestamp strings](yaml:timestamp).

“timeunit” can be either “minute” or “hour”.

The upper level map of this can also have the optional key “timeresolution”. If present, "timeresolution" contains a [Txy](yaml:txy) specifying the time resolution throughout the optimization time.

### time example

    time:
      starttime: 2018-02-27 00:00:00
      endtime: 2018-02-28 00:00:00
      timeunit: hour
      timeresolution:
        2018-02-27 00:00:00: 1

(yaml:model)=
### model
The "model" part defines all objects and attributes defined/set in the SHOP model as well as the values of the defined attributes. The upper three levels of this part are nested [Maps](yaml:map).

The uppermost level, referred to as the “object type level”, is a map with keys for each object type present in the case.

The next level, referred to as the “object name level”, consists of a set of maps with keys for each distinct object in the case. So the uppermost level map might have a map under the key “reservoir”, which in turn have maps under “Reservoir1” and “Reservoir2”

The third level, referred to as the “attribute name level”, consists of a set of maps with keys for each defined attributes of its parent object in the case. So the second level map “Reservoir1”, under the uppermost key “reservoir”, might contain the keys “lrl”, “hrl” etc

At the fourth level, the structure and content is defined by the attribute type that is represented. Details can be found in [](yaml:attributes).

### model example
The following example is based on a real SHOP YAML case where some attributes and objects have been omitted to give a better overview:

    model:
      reservoir:
        Reservoir1:
          lrl: 90
          hrl: 100
          vol_head:
            ref: 0
            x:
              - 0
              - 12
              - 14
            y:
              - 90
              - 100
              - 101
          inflow:
            2018-02-27 00:00:00: 101
            2018-02-27 01:00:00: 50
        Reservoir2:
          lrl: 40
          hrl: 50
      plant:
        Plant1:
          less_distribution_eps: 0.001
          main_loss:
            - 0.0002
          penstock_loss:
            - 0.0001
        Plant2:
          less_distribution_eps: 0.001
          main_loss:
            - 0.0002
          penstock_loss:
            - 0.0001
      generator:
        Plant1_G1:
          p_min: 25
          p_max: 100
          p_nom: 100
          turb_eff_curves:
            - ref: 90
              x:
                - 25
                - 90
                - 100
              y:
                - 80
                - 95
                - 90
            - ref: 100
              x:
                - 25
                - 90
                - 100
              y:
                - 82
                - 98
                - 92
          startcost:
            2018-02-27 00:00:00: 500

(yaml:connections)=
### connections
The "connections" part contains information about how the objects in the case are connected. This content is made up of a [List](yaml:list) of [Maps](yaml:map), where each map is a fully describes what SHOP needs to recreate the connection.

The full connection format is quite verbose, however, you can often omit specific information. See the table below for details

|Keys|Mandatory|Situational Description|Description|
|-|-|-|-|
|"to", "from"|Always|Always needed|Names of to/from objects respectively|
|"to_type", "from_type"|Situational|Needed when object names are ambiguous. E.g. a plant and a generator has the same name|Types of to/from objects respectively|
|"connection_type"|Situational|Only needed when connecting a **reservoir** to a "spill" or "bypass" **gate**|Specification of connection type|
|"order"|Situational|Needed when connection order matters. Currently only needed for connections to **junction** or to **junction_gate**|Integer indicating connection order. "0" will be connected before "1", "1" before "2" and so on|

#### connections example
The following example is constructed to illustrate the most relevant use-cases.

    connections:
    - from: Reservoir1                     # Verbose connection
      to: Plant1
      from_type: reservoir
      to_type: plant
      connection_type: connection_standard
      order: 0
      
    - from: Reservoir2                     # Simplified connection: Requires non-ambiguos object names
      to: Plant2
      
    - from: Reservoir3                     # Connections to Junctions require "order"
      to: Junction2
      order: 0
    - from: Junction1
      to: Junction2
      order: 1
      
    - from: Reservoir4                     # Spill and Bypass gates are defined by specifying "connection_type"
      to: Gate1
      connection_type: connection_spill

(yaml:commands)=
### commands
The "commands" part contains all SHOP commands executed in the case. The upper level of this file is a [List](yaml:list) of strings. The command format is identical to the one used in the SHOP executable (TODO).

#### commands example

    commands:
      - start sim 1 
      - set code /incremental
      - start sim 3

(yaml:attributes)=
## SHOP attribute type formats
Each SHOP attribute has a designated "type". The type is determined by how the attribute is used and specifies what kind of data is stored within the attribute. This section describes the format of the different SHOP attribute types when stored in YAML.

(yaml:int)=
### int
Represented by a single [integer](datatype:int). Remember to rafrain from adding a decimal point.

    plant:
      Plant1:
        time_delay: 0           # int attribute example
    
(yaml:double)=
### double
Represented by a single [double](datatype:double).

    reservoir:
      Reservoir1:
        lrl: 90.2               # double attribute example

(yaml:string)=
### string
Represented by a single [string](datatype:string).

    market:
      Market1:
        market_type: ENERGY     # string attribute example

(yaml:int_array)=
### int_array
Represented by a [List](yaml:list) of [Integers](yaml:int). Remember to rafrain from adding a decimal points.

    plant:
      Plant1:
        gen_priority:           # int_array attribute example
          - 1
          - 2

(yaml:double_array)=
### double_array
Represented by a [List](yaml:list) of [Doubles](yaml:double).

    plant:
      Plant1:
        main_loss:              # double_array attribute example 
          - 0.0002

(yaml:xy)=
### xy
Represented by a [Map](yaml:map) with the mandatory keys "x", "y" and "ref".

Keys "x" and "y" both contain [double_arrays](yaml:double_array).

"ref" contains a [Double](yaml:double).


    reservoir:
      Reservoir1:
        vol_head:               # xy attribute example
          ref: 0
          x:
            - 0
            - 12
            - 14
          y:
            - 90
            - 100
            - 101

(yaml:xy_array)=
### xy_array
Represented by a [List](yaml:list) of [Xy](yaml:xy).

    plant:
      Plant1:
        turb_eff_curves:        # xy_array attribute example
          - ref: 90
            x:
              - 25
              - 90
              - 100
            y:
              - 80
              - 95
              - 90
          - ref: 100
            x:
              - 25
              - 90
              - 100
            y:
              - 82
              - 98
              - 92

(yaml:txy)
### txy
Represented by a [Map](yaml:map) of [Doubles](yaml:double). The keys are [Timestamps](yaml:timestamp) and make out the time index

**Note**: A different format is required for multi-scenario txy, [txy(stochastic)](yaml:stxy)

    reservoir:
      Reservoir1:
        inflow:                      # txy attribute example 
          2018-02-27 00:00:00: 101
          2018-02-27 01:00:00: 50

(yaml:stxy)=
### txy(stochastic)
Represented by a [Map](yaml:map) of [strings](yaml:string). The first key and value make out a "header".

The first key is "         Scenario#". The first value is not really important, but for the sake of clarity in the file you might want to use it to enumerate the scenarios. E.g. " 1 2 3 4 5 6" if there are six scenarios.

The remaining keys are all [Timestamps](yaml:timestamp).

The remaining values are [strings](yaml:string) that can be split on whitespace and cast to double in order to get one value for each scenario.

    market:
      Market1:
        sale_price:              # txy (stochastic) attribute example
          "         Scenario #": "    1    2    3    4    5    6    7    8    9   10   11   12"
          "2018-02-27 00:00:00": "   39   39   39   39   39   39   39   39   39   39   39   39"
          "2018-02-27 01:00:00": " 38.5   39 39.5   40 38.5   39 39.5   40 38.5   39 39.5   40"
