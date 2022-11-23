(set_fcr_n_band)=
# set fcr_n_band
The size of the frequency range in either direction where FCR-N is activated. Default value is 0.1 Hz (49.9 to 50.1 Hz)

|   |   |
|---|---|
|Options|nan|
|License|SHOP_OPEN|
|Release version|13.0.0.a|

```{contents}
:local:
:depth: 1
```

## FCR_N band width
The band width $β^{FCR\_N}$ used for the regulation limit of FCR_N for both up- and down-regulation can be set by the commands:
```
set fcr_n_band <value>
```

If commands not set: The value $β^{FCR\_N} = 0.1$ will be used.



