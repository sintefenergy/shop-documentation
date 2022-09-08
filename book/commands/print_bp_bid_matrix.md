---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: 'Python 3'
  name: python3
---

(print_bp_bid_matrix)=
# print bp_bid_matrix
Creates bid matrices for each plant in the system that is part of the best profit calculations between the two time steps given as input. The number of prices in the bid matrix is reduced down to the size defined in bp_bid_matrix_points on global_settings. The '/interpolate' option will interpolate the bid matrix on all integer prices in the range between the highest and lowest price in the BP curve before reduction. The '/merge' option will instead merge price columns within a tolerance of 1.0 before reduction. The command can only be used after a call to [print bp_curves](print_bp_curves).

|   |   |
|---|---|
|Options|/interpolate, /merge|
|License|SHOP_BEST_PROFIT|
|Release version|14.2.2.0|

```{contents}
:local:
:depth: 1
```





