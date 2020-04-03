# AirBnB Occupancy Tax

## Update Log
### March 8th
- Completed code in `compute_reservations.py` and `compute_bookings_cutoff.py` to collect/modify data for both types of analysis.
- Completed writeup for the data portion of the thesis and outlined both types of analysis.
- Completed collection and processing of Boston data for the pre and post treatment periods (see `data_writeup.pdf` for more details)
    - For all reservations of 7/1/2019 or later, the tax came into effect 1/1/2019. Thus, data for all these reservations are collected monthly from July 2018 to June 2019 (5 'in-between' periods pre and post treatment).
    - For all reservations booked after 1/1/2019, data are collected from January 2019 to December 2019 (5 'in-between' periods pre and post treatment).

### March 23rd
- Amend data processing to restrict analysis to listings with more than 100+ nights available at any stage during the year.
- Update writeup to include the above change, and also describe caveat of bookings with the check in date and date booked within the same scraping interval.

### March 25th
- Amend data processing to restrict analysis of reservation dates to listings that were both on the market in the month before and after the treatment effect. This removes units that become deleted before the treatment was administered and units that enter after the treatment was administered, accounting for attrition and its opposite effect in the study. 
- Add notebook to validate transactions by reviews. Depending on how we aggregate the data (by month vs by unit), the results are somewhat different. There is no virtually no correlation on the unit level between reviews and imputed nights, while a very strong correlation can be seen on the month level (across all units) between reviews and nights. 
    - This indicates that validation by reviews is not a very 'clean' predictor of imputed nights, making it a poor validator.
    - However, if we follow through with the month level aggregation that yields a higher correlation, we do find that our imputed transactions are within ballpark figures of estimated nights based on reviews. The regression returns a slope of 4 (imputed nights per review), so that assuming an average of 3 nights per stay  / 70% review rate per stay = ~4.3 nights per review.

### March 27th
- Amend data processing to restrict analysis to listings that are booked for >14 nights a year, since only these listings are affected by the tax. 
- Scrape data for cities: Montreal, Rhode Island, Washington DC, Quebec City

### April 2nd
- Scrape data for cities: Nashville, San Francisco, Chicago, 
- Collect tax data (rates and enactment date) on control units, see `control_cities.xlsx`

## TODO
- Determine causal method used: e.g. Differences in Differences, Synthetic controls, etc,.
- Determine counterfactual city/cities (this depends on method used)
- Determine how to best standardize data due to uneven time differences in observation time across units 