# AirBnB Occupancy Tax

## Update Log
### March 8th
- Completed code in `compute_reservations.py` and `compute_bookings_cutoff.py` to collect/modify data for both types of analysis.
- Completed writeup for the data portion of the thesis and outlined both types of analysis.
- Completed collection and processing of Boston data for the pre and post treatment periods (see `data_writeup.pdf` for more details)
    - For all reservations of 7/1/2019 or later, the tax came into effect 1/1/2019. Thus, data for all these reservations are collected monthly from July 2018 to June 2019 (5 'in-between' periods pre and post treatment).
    - For all reservations booked after 1/1/2019, data are collected from January 2019 to December 2019 (5 'in-between' periods pre and post treatment).

## TODO
- Determine causal method used: e.g. Differences in Differences, Synthetic controls, etc,.
- Determine counterfactual city/cities (this depends on method used)
- Determine how to best standardize data due to uneven time differences in observation time across units 
