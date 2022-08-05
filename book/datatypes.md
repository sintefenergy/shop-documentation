(datatypes)=
# Datatypes
SHOP attributes, both inputs and outputs, uses the following datatypes:
```{contents}
:local:
:depth: 1
```
(datatype:int)=
## int
An integer, a number without decimals. For example, it is used to denote number of generators through [](generator:num_gen) attribute.
- [Yaml example](yaml:int)
- [pyshop example](pyshop:scalar)

(datatype:int_array)=
## int_array
A list of integers.
- [Yaml example](yaml:int_array)
- [pyshop example](pyshop:array)

(datatype:double)=
## double
A decimal number.
- [Yaml example](yaml:double)
- [pyshop example](pyshop:scalar)

(datatype:double_array)=
## double_array
A list of decimal numbers.
- [Yaml example](yaml:double_array)
- [pyshop example](pyshop:array)

(datatype:string)=
## string
A text string.
- [Yaml example](yaml:string)
- [pyshop example](pyshop:scalar)

(datatype:string_array)=
## string_array
A list of text strings.
<!-- [Yaml example](yaml:string_array) -->
- [pyshop example](pyshop:array)

(datatype:xy)=
## xy
An indexed table.
- [Yaml example](yaml:xy)
- [pyshop example](pyshop:xy)
- [ASCII example](ascii:xy)

(datatype:xy_array)=
## xy_array
A list of indexed tables.
- [Yaml example](yaml:xy_array)
- [pyshop example](pyshop:xy_array)

(datatype:txy)=
## txy
A time series.
- [Yaml example (deterministic)](yaml:txy)
- [Yaml example (stochastic)](yaml:stxy)
- [pyshop example](pyshop:txy)
- [ASCII example](ascii:txy)

(datatype:xyt)=
## xyt
Similar to [](datatype:xy_array), but the xy array reference value is a timestamp. Used for [best profit](best-profit) results.