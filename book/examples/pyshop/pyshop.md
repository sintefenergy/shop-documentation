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

(pyshop)=
# PyShop
```{contents}
:local:
```

## Introduction

### PyShop background and overview
The SHOP core mostly written in the programming language C. C is one of the most efficient programming languages available, so this is a good match for an optimization model like SHOP. However, C is not very user friendly in the sense that it is not very dynamic, is hard to use and low-level. Python is a programming language that is, in many ways, the complete opposite of C. It is highly dynamic, easy to use and high-level, but also not very efficient. The positive aspects of Python makes it a great candidate for simplifying the interaction with the SHOP core, and it is not detrimental that it is inefficient as long as the heavy computation is still performed by the more efficient C code. These are some of the reasons that motivated the SHOP team to offer the SHOP python API, which essentially is functions written in C that can be called in python. However, because the functions are written C, they are still limited by many of the non-user friendly aspects of C. PyShop was introduced to leverage this.

In short, PyShop is a "wrapper" written in Python to offer a more user-friendly interface for setting up and running SHOP optimizations using python. It is a wrapper in the sense that it offers more high-level functions for handling the lower-level SHOP python API calls for the user. Often, a single PyShop function/action will call multiple SHOP python API functions and at the same time ensure that any input/output data is properly handled.

The typical workflow in PyShop starts by creating a ShopSession and defining the optimization time and resolution. Next, the topology is added before time-dependent data is generated or loaded from files or a database. When all data is sent to the SHOP core, commands for optimization are executed before results are extracted.

### Documentation structure
The key parts of PyShop are for the most part covered by the "ShopSession" class and the "PyShop model structure". The former is used to organize PyShop runs and is represented by a single python class. The latter is a hierarchical python class structure that simplifies the building of the SHOP model.

We will first look at the **ShopSession**: how it is initialized and which useful methods it offers. The ShopSession itself, is used for things like setting up the optimization time, performing common operations that may affect the entire model/optimization and calling SHOP commands.

Then we will move on to the central **PyShop model structure**. The model structure is mainly used for micro-managing the topology of the model as well as setting attribute values. In this part we will explain each layer of the hierarchical structure, as well as describing specific topics like "how to navigate the topology", "how to connect SHOP objects" and which data formats the different attribute types accepts.

## ShopSession
PyShop scripts are centred around the ShopSession class. This class wraps the SHOP python API and offers a series of high level methods and workflows for setting up, querying and running SHOP models.

### Initialization
All initialization arguments are **keyword arguments**. This essentially means that they all have default values that will be used unless you provide an explicit value. Furthermore, as long as you write the arguments names explicitly, you can order the arguments arbitrarily. **Note** that it is also possible to provide arguments without explicitly writing their names, however, we strongly advise that you always use the full argument names to avoid confusion/errors arrising from improper argument ordering.

ShopSession initialization arguments:

|Argument|Description|Default value|
|-|-|-|
|silent|Set to "True" if you do not want console output.|False|  
|supress_log|Set to "True" if you do not want any SHOP log files.|False|
|log_file|Provide a path to an output log if you want to generate a **runnable python log**. This is especially useful for sending in cases for debugging errors.|""|
|log_gets|Option **used alongside "log_file"** for filtering out "query" calls in the generated python log. Query calls are any call that do not alter the internal state of the SHOP model, moslty "getters" and specialized calls for checking states. Set to "False" to filter out such calls.|True|
|license_path|Used for overriding the location where SHOP will look for the license file. See [](pyshop:license-file-location)|""|
|solver_path|Used for overriding the location where SHOP will look for solver and solver interface. See [](pyshop:solver-interface-location)|""|

Example of usage:

    shop = ShopSession(silent=True)
    shop2 = ShopSession(silent=False, log_file="my_pyshoplog.log", log_gets=False)

### Methods
ShopSession offers a set of "methods" for simplifying common operations when running SHOP models. A method is called as shown below:

    shop = ShopSession()
    shop.method(*arguments)

ShopSession methods:

|Method|Description|Arguments(default values)|
|-|-|-|
|set_time_resolution|Sets the optimization time. "time_resolution" has to be provided if the resolution is not one time unit across the entire time horizon.|starttime, endtime, timeunit, time_resolution(None)|
|get_time_resolution|Retrieves the optimization time||
|get_messages|A method for retrieving SHOP messages through the python API. SHOP messages are usually written to logs and/or console. Unless "all_messages" is set to "True", this will only return the new messages since the last time the call was made.|all_messages(False)|
|execute_command|Older method for executing SHOP commands. Takes no arguments and returns a Python object. Example of usage: "shop.execute_command().start_sim.set([], ['3'])". More or less **replaced** by *.shop_command(options, values)* and "execute_full_command".||
|execute_full_command|An alternative method for calling a SHOP command using a single string of the same format expected by the SHOP executable.|full_command|
|get_executed_commands|A method for retrieving a list of all SHOP commands called so far.||
|read_ascii_file|A method for reading in a Ascii file using the file path provided (TODO: ref ascii)|file_path|
|load_yaml|A method for loading a case/data from YAML. Provide "file_path" if it is to be loaded from file or "yaml_string" if it is to be loaded directly from string.|file_path(""), yaml_string("")|
|dump_yaml|Dumps SHOP session to YAML. Dumps to string unless "file_path" is provided. Options for only outputting input attributes, compressing time series and compressing connection format.|file_path(""), input_only(False), compress_txy(False), compress_connection(False)|
|run_command_file|A method for reading command files used in the SHOP exe model. The user has to specify both path to folder ('' can be used for files in workdir) and filename|folder, command_file|
|run_command_file_progress|Similar to run_command_file, but this option releases the Python GIL. This means that you can query SHOP for progress using "get_messages" in a different thread during the execution of the command file.|folder, command_file|
|get_shop_version|Returns the SHOP version.||
|-|-|-|
|*shop_command*|Every SHOP command is dynamically given its own method in PyShop. In order to call them you have to replace any spaces in the command with "\_". E.g. "shop.start_sim([], ['3']) can be used for calling "start sim 3" and "shop.set_code(['incremental'], []) can be used for calling "set code /incremental".|options, values|

## PyShop model structure
**Note**: This section will frequently refer to both SHOP objects and python objects. SHOP objects exists within SHOP and have types such as "reservoir", "plant", "market". Python objects will, in this section, usually be wrappers for structuring different SHOP concepts in PyShop and simplify intraction with the internal representations using the python API.

The interaction with the SHOP topology through PyShop is centered around a dynamic model structure. The model structure is located in the ShopSession under the value "model", and it is mainly used for dynamically adding SHOP objects, connecting SHOP objects and setting/getting attribute values. It also offers some additional features like a method for plotting the topology and methods for retrieving object/attribute metadata, and also simplifies operations such as "iterating over all generators in the system".

### Note on what happens behind the scenes
The model structure is hierarchically structured in a way that simplifies navigation and properly relays the outcome of highly generic calls. E.g. "model.reservoir.add_object('Reservoir1')" will add a new "Reservoir". Note that the final method is simply "add_object" and does not itself relay the information that the new object is a Reservoir. What really happens in this simple line is that "model.reservoir" returns a "SHOP object type"-level python object that represents the SHOP object type reservoir. When the method "add_object" is called on this python object, it calls the low-level python API call "shop_api.AddObject(object_type, object_name)" using the stored SHOP object type and the provided object name. This call itself returns a "SHOP object"-level python object, which represents a specific SHOP object hierarchically placed under its "object type" in the model structure. This python object can be interacted with to go further down the model structure, e.g. "Attribute"-level, or to connect the internal SHOP object with another SHOP object. It can also now be referenced by "model.reservoir.object_name".

    # Complex chain
    model.reservoir.Reservoir1.lrl.set(90)
    
    # Broken down parts
    model.reservoir         # Returns "SHOP object type"-level python object, stores "reservoir" as object type
    ...reservoir.Reservoir1 # Returns "SHOP object"-level python object, stores "Reservoir1" as object name
    ...Reservoir1.lrl       # Returns "Attribute"-level python object, stores "lrl" as attribute
    ...lrl.set(90)          # Calls "shop_api.SetDoubleValue(object_type, object_name, attribute, 90)" using stored info

### Note on accessing the next model level
When accessing the next level you essentially use a string identifier to refer to a specific instance. In the model-level you can use the name of a SHOP object type for accessing the "SHOP object type"-level and in the "SHOP object"-level you can use the name of a specific attribute to access the "Attribute"-level. This can be achieved by using "dot-notation" **as long as** the name does not contain any characters that are disallowed in python identifiers. The only level that may contain names with disallowed charcters is the "SHOP object"-level because users are free to name these. Thus, dot-notation is always usable for all other levels. Alternatively, it is possible to use "square-bracket accessing" regardless of characters in the name.

    # Dot notation, only possible when the name does not contain any characters disallowed in python identifiers
    model.reservoir
    object_type_level.Reservoir1
    object_level.lrl
    
    # Square bracket accessing, always applicable
    model['reservoir']
    object_type_level['Reservoir@']
    object_level['lrl']
    
    # You can freely mix notations
    model.reservoir['Reservoir@'].lrl

### Auto-completion support
The highly dynamic nature of the model structure allows PyShop to offer extensive auto-completion when running python interactively. This means that you will get suggestions for all available SHOP object types when writing "model.", all defined  SHOP reservoirs when writing "model.reservoir." and all available attributes of SHOP reservoirs when writing "model.reservoir.my_reservoir.". Auto-completion will also list any avilable methods in each respective levels.

### Model hierarchy
This subsection will look at the different levels of the PyShop model structure and describe what can be done at each level.

#### Model hierarchy overview

    # Model hierarchy overview shown in explicit PyShop code
    model = shop.model
    model                                        # Model level
    model.object_type                            # SHOP object type level
    model.object_type.object_name                # SHOP object level
    model.object_type.object_name.attribute      # Attribute level
    
    # Note that you usually store intermediate pyshop object in their own variables to simplify future usage of the level
    model = shop.model
    model                                        # Model level
    model.object_type                            # SHOP object type level
    my_object = model.object_type.add_object("MyObject")
    my_object                                    # SHOP object level
    my_object.attribute                          # Attribute level

#### Model level
Upper level of the model structure.

|Method|Description|Arguments(default values)|
|-|-|-|
|build_connection_tree|Plots the SHOP topology. You can customize filename and turn on writing to file.|filename('topology'), write_file(False)|
|update|A method for updating the "PyShop-side" representation of the SHOP model. It is used internally by PyShop every time the topology may have changed, e.g. after loading ascii/yaml file. **Note** there should not be any scenarios left where the user have to call this explicitly, please let ut know if you identify a scenario where you do have to call this to update the python side representation of the topology.||

    # Usage examples
    model = shop.model
    
    model.build_connection_tree()
    model.reservoir...              # Access the next level

#### SHOP object type level
Represents a specific SHOP object type and allows you to creat new SHOP object of said type. At this level the SHOP object type is known and will be referred to as *object_type*.

|Method|Description|Arguments(default values)|
|-|-|-|
|add_object|Creates a new SHOP object with the provided name and type = *object_type*. Returns a SHOP object level python object representing the new SHOP object.|object_name|
|get_object_names|Returns a list containing the names of all SHOP object of type = *object_type*||
|info|Returns a python dictionary containing meta data of *object_type*||
|-|-|-|
|*\_\_iter\_\_*|**Note** this is not called directly, but is a method that allows for elegant python iteration. See usage example to see how to iterate over all SHOP objects of type = *object_type*||


    # Usage examples
    object_type_level = shop.model.reservoir
    
    reservoir_names = object_type_level.get_object_names()
    rsv1 = object_type_level.add_object('Reservoir1')
    
    for reservoir in object_type_level:                     # You can easily loop over all objects in the next level
        # Do things with python object representing each reservoir
        
    object_type_level.Reservoir1                            # Access the next level, equvalent of "rsv1" in this example

(pyshop:object-level)=
#### SHOP object level
Represents a specific SHOP object and allows you to connect the SHOP object with other SHOP objects. At this level the SHOP object type and SHOP object name are known and will be referred to as *object_type* and *object_name* respectively.

|Method|Description|Arguments(default values)|
|-|-|-|
|get_type|Returns *object_type*.||
|get_name|Returns *object_name*.||
|get_relations|Returns a list of "SHOP object level" representations of all SHOP objects connected to *object_name*. Options for filtering based on "direction", "relation type" and "relation category"|direction(both), relation_type="all", relation_category('both')|
|connect|An old method for connecting SHOP objects. See [](pyshop:connecting-objects)|connection_type("")|
|connect_to|A new method for connecting SHOP object using a SHOP object level python object. See [](pyshop:connecting-objects)|related_object, connection_type("")|

    # Usage examples
    object_level = shop.model.reservoir.Reservoir1
    
    object_type = object_level.get_type()
    object_level.connect_to(plant1)
    connected_objects = object_level.get_relations(direction='input', relation_category='physical')
    rsv1 = object_type_level.add_object('Reservoir1')
    object_level.lrl                                   # Access the next level

#### Attribute level
Represents a specific attribute. At this level the SHOP object type, SHOP object name and attribute are known and will be referred to as *object_type*, *object_name* and *attribute* respectively.

|Method|Description|Arguments(default values)|
|-|-|-|
|get|Returns attribute value of *attribute* of *object_name*. **Special behaviour for attributes of type Xyt**||
|set|Sets value of *attribute* of *object_name*. Value has to be of a format accepted by the datatype of *attribute*.|value|
|info|Returns a python dictionary containing meta data of *attribute*.||
|help|Returns a description of the *attribute*.||
|-|-|-|
|*get*|If *attribute* has the data type Xyt you have the ability to filter the output using "start_time" and "end_time".|start_time(None), end_time(None)|

    # Usage examples
    attribute_level = shop.model.reservoir.Reservoir1.lrl
    attribute_level.set(90)
    lrl_value = attribute_level.get()
    lrl_info = attribute_level.info()
    print(attribute_level.help())

### Relations
Relations are a central part of SHOP optimization and is supported in the PyShop model structure. You can connect SHOP objects in two similar, but slightly different ways.

#### Relation terms
Before SHOP 14, you had to provide a specific **relation type** when connecting most objects. SHOP 14 removed the need for doing so for all but one combination. For connections from reservoirs to gates, you still have to state if you want to add a **spill or bypass** relation. SHOP 14 also exposed an array of **logical** relations to the APIs. **Physical** connections have a distrinct order in the sense that connecting "Reservoir1" to "Plant1" indicates that the water flows from "Reservoir1" to "Plant1", this is not the case for **Logical** connections like "Plant1" and "Generator1" where the plant serves more as a grouping of certain properties that applies to all its generators. This, along with the loss of **implied direction** in the many different **relation types**, made us introduce the concept of **relation category**.

|Term|Description|
|-|-|
|relation type|Currently only used for Reservoir->Gate relations where you might want to specify that the connection is **spill** or **bypass**. Note, it can also be standard, in which case you do not have to provide anything.|
|relation category|Each relation is either **Physical** (directional) or **Logical**(bidirectional). The implication of this is that input/output does not make sense for the latter. This, in turn, has implications for how connections are retrieved|
|relation direction|**Pyhsical** relations have directions determined by which way the water flows. **Logical** relations are bidirectional.|

(pyshop:connecting-objects)=
#### Connecting SHOP objects
You can connect SHOP object using two different methods of the "SHOP object" level in the PyShop model structure. These are listed in [](pyshop:object-level) but also warrent some further explanation due to their importance. When connecting **physical** relations the water is implied to flow from the first object to the second object. Note in the examples below that you can provide the relation type through a keyword argument in both alternatives.

    # Available SHOP objects and PyShop variables
    rsv1 = model.reservoir.add_object('Reservoir1')
    plant1 = model.reservoir.add_object('Plant1')    
    model.reservoir.add_object('Gate1')
    gate2 = model.reservoir.add_object('Gate2')
    
    # ALT 1: connect_to(). New, simpler. Requires a reference to a PyShop representation of the SHOP object connected to
    rsv1.connect_to(plant1)
    rsv1.connect_to(model.gate.Gate1)
    rsv1.connect_to(gate2, connection_type='spill')
    
    # ALT 2: connect(). Old, more verbose
    rsv1.connect().plant.Plant1.add()
    rsv1.connect().gate.Gate1.add()
    rsv1.connect().gate.Gate2.add(connection_type='spill')

### Expected data formats of attribute datatypes

(pyshop:scalar)=
#### Scalar
Scalar covers both [](datatype:int), [](datatype:double) and [](datatype:string) attributes. PyShop will expect python numericals when setting such attributes. PyShop will take care off casting from/to integer/float/string.

    # Examples:
    plant1.time_delay.set(5)         # plant time_delay is an Int attribute
    
    rsv1.lrl.set(90.0)               # reservoir lrl is a Double attribute
    rsv1.lrl.set(90)                 # PyShop will handle casting to float
    
(pyshop:array)=
#### Array
Array covers both [](datatype:int_array), [](datatype:double_array) and [](datatype:string_array) attributes. PyShop will expect arrays of integers and floats respectively for these types.

    # Examples:
    plant1.gen_priority.set([1,2])         # plant gen_priority is an Int_array attribute
    
    plant1.main_loss.set([0.0002])         # reservoir main_loss is a Double_array attribute

(pyshop:xy)=
#### Xy
Xy attributes can be set using two different formats. The first is a simple python dictionary with the keys "xy" and "ref" where "xy" contains a python list of xy-pairs (python tuple or list with two elements) and "ref" contains the reference as a float. The second format is using the popular python library "pandas", specifically the "pandas.Series". The "x" values are put into the "index", the "y" values into "data" and "ref" into the "name".

    # Examples
    xy_pandas = pd.Series([90, 100, 101], index=[0, 12, 14], name=0.0)    # Pandas Series format
    rsv1.vol_head.set(xy_pandas)
    
    xy_dict = {'xy': [(0,90), (12,100), (14,101)], 'ref': 0.0}            # Python dict format
    rsv1.vol_head.set(xy_dict)

(pyshop:xy_array)=
#### Xy_array
Xy_array attributes can be set using a python list of either accepted formats of Xy.

    # Examples
    xy_array_pandas = [pd.Series([80, 95, 90], index=[25, 90, 100], name=90.0),
                          pd.Series([82, 98, 92], index=[25, 90, 100], name=100.0)]  # List of Pandas Series format
    gen1.turb_eff_curves.set(xy_array_pandas)
    
    xy_array_dict = [{'xy': [(25,80), (90,95), (100,90)], 'ref': 90.0},
                        {'xy': [(25,82), (90,98), (100,92)], 'ref': 100.0}]          # List of Python dict format
    gen1.turb_eff_curves.set(xy_array_pandas)

(pyshop:txy)=
#### Txy
Txy attributes can be set either using a Pandas Series or a Pandas DataFrame with a **timestamp index**. PyShop also accepts a single numerical value, in which case a constant Txy will be created using the provided value.

    # Examples
    day_ahead = model.market.add_object('Day_ahead')
    day_ahead.buy_price.set(40.01)                            # PyShop will create a constant time series
    
    # Pandas format, Non-stochastic
    starttime = pd.Timestamp('2018-02-27')
    txy_value = pd.Series([101, 50], index=[starttime, starttime + pd.Timedelta(hours=1)])
    day_ahead.inflow.set(txy_value)
    
    # Pandas format, Stochastic
    starttime = pd.Timestamp('2018-02-27')
    stochastic_txy_value = pd.DataFrame({'1': [101, 50],
                                         '2': [101, 50],
                                         index=[starttime, starttime + pd.Timedelta(hours=1)],
                                         columns=['1', '2'])
    day_ahead.inflow.set(stochastic_txy_value)

## Installation

### General note
PyShop is distributed in three different packages. There are two packages bundled with CPLEX, one for Windows and one for Linux. The final packages is also for Windows but is distributed without CPLEX. All packages are installed locally using the python package manager "pip".

(pyshop:license-file-location)=
### License file location
Like the SHOP executable, PyShop expects to find the license file using an "environment variable" named "ICC_COMMAND_PATH" by default. This has to be defined locally on the system running SHOP. We recommend you to look at resources on the web if you are unfamiliar with environment variables. It is fairly simple to set up and is a common pratice so you should not have any problems with this step. **Note**: keep in mind that many running programs needs to be restarted to get new/updated environment variables.

PyShop allows you "override" the license path by providing a path to your license using the "license_path" parameter when initializing the ShopSession.

(pyshop:solver-interface-location)=
### Solver interface+ location
**Windows** will by default look for the solver interface and the solver within the PyShop installation itself. For the package bundled with CPLEX you can simply install the zip file as it is and the solver files will be taken care of. For the package bundled without CPLEX, you will have to copy in your own CPLEX solver in the unpacked package before installing, **if** you want to use CPLEX.

**Linux** will by default look for the solver interface in the environment variable ICC_COMMAND_PATH. Note that you only have to take care of the solver interface in Linux as it contains the solver as well. 

You can override default solver path in all versions of PyShop by using the parameters solver_path when calling ShopSession(). E.g. shop = ShopSession(solver_path=’your/solver/path’). If you plan on doing this, you might want to adjust the installation procedure accordingly.

### Support for different python versions
The default PyShop packages are all distributed with a "SHOP python API" built for python 3.7. Additionally, we also build the "SHOP python API" for python 3.8, but to use this you will have to replace "pyshop/shop_pybind.pyd/so" within the default package with the alternative "shop_pybind.pyd/so" for python 3.8 **before** installing.

### Note on pip
Pip is bundled with most python installations, but in case it not recognized in your terminal we have some suggestions that might help you out.

 - If you have installed python through the "anaconda" distribution, you will most likely be able to use pip within the bundled "anaconda prompt" terminal.
 - If you have managed to set up python correctly in an IDE like PyCharm or VScode, you will likely be able to use pip in a terminal started by the IDE.
 - Look for online resources on how to set up python. We recommend the popular Anaconda distribution.

### PyShop(Windows, bundled with CPLEX), step-by-step guide
1. Download “pyshop-13.x.x.x.zip” where the x’es reflect the specific version number, e.g 0.0.b.
2. Open a terminal, e.g. cmd or anaconda prompt, in the directory containing the zip and run “pip install pyshop-13.x.x.x.zip”

### PyShop(Windows, no CPLEX), step-by-step guide

1. Download “pyshop-13.x.x.x_no_cplex.zip” where the x’es reflect the specific version number, e.g 0.0.b.
2. Extract the zip file
3. Copy your solver, e.g. cplex1263.dll, into pyshop-13.x.x.x/pyshop/
4. Open a terminal in pyshop-13.x.x.x/ directory(this should contain a directory called “pyshop”, a file called “PKG-INFO” and a file called “setup.py”) and run “pip install .” (note the final “.”)

### PyShop(Linux), step-by-step guide
1. Download “linux_pyshop-version.zip” and “libs.zip”
2. Install PyShop by running “pip install linux_pyshop-version.zip”
3. Unpack the solver interface library from libs.zip to where you plan on keeping your license file
4. By default, PyShop Linux expects to find the solver interface and license file in the location defined in the environment variable ICC_COMMAND_PATH. This can be done by either creating the variable and moving the files explicitly or by passing the path of the files, when initializing a ShopSession, through the argument “license_path”. E.g. “shop = ShopSession(license_path=’libs’)

### Getting started with PyShop in Docker
1. Download “linux_pyshop-version.zip” and “libs-version.zip”, and “pyshop_docker.zip” from : Docker package
2. Unzip each downloaded archive
3. Move pyshop files to the SDK folder within the unpacked docker archive (SDK should contain a folder named pyshop, setup.py and PKG-INFO)
4. Move the interface library(e.g. shop_cplex_interface.so) and your license file to the folder named “libs”
5. Move “basic.py” from “examples-version.zip” to the root docker folder. This folder should now contain “SDK”, “libs”, “Dockerfile”, “requirements.txt” and “basic.py”
6. Open a terminal in the root docker folder
7. Build image with “docker build -t name .”
8. Check that everything works as it should with “docker run -rm name basic.py”
9. Look at the comments in the Dockerfile for more ideas
