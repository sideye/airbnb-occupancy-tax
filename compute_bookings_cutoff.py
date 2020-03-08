import sys
import pandas as pd
import numpy as np
from datetime import datetime
import os

def get_booked_listings(prev_listings_path, prev_calendar_path, post_listings_path, post_calendar_path):
    prev_listings = pd.read_csv(prev_listings_path)
    prev_calendar = pd.read_csv(prev_calendar_path)
    post_listings = pd.read_csv(post_listings_path)
    post_calendar = pd.read_csv(post_calendar_path)
    
    prev_calendar['date'] = pd.to_datetime(prev_calendar.date)
    post_calendar['date'] = pd.to_datetime(post_calendar.date)
    prev_calendar = prev_calendar[prev_calendar.date >= datetime(2019,7,1)]
    post_calendar = post_calendar[post_calendar.date >= datetime(2019,7,1)]
    prev_listings = prev_listings.drop(["price", "minimum_nights", "last_review"], axis = 1)
    post_listings = post_listings.drop(["price", "minimum_nights", "last_review"], axis = 1)
    
    prev = prev_listings.merge(prev_calendar, left_on = "id", right_on = "listing_id")
    post = post_listings.merge(post_calendar, left_on = "id", right_on = "listing_id")
    
    prev = prev.drop(["listing_id"], axis = 1)
    post = post.drop(["listing_id"], axis = 1)
    
    merged = prev.merge(post, on = ["id", "date"], suffixes = ["_prev", "_post"])
    booking_changes = merged[(merged.available_prev == 't') & (merged.available_post == 'f')]
    return booking_changes

path = sys.argv[1]
output_path = sys.argv[2]
months = ["jul_2018", "aug_2018", "sep_2018", "oct_2018", "nov_2018", "dec_2018", "jan_2019", "feb_2019", "mar_2019", "apr_2019", "may_2019", "jun_2019"]
for index, m in enumerate(months[1:]):
    prev_listings_path = path + months[index] + "_listings.csv"
    prev_calendar_path = path + months[index] + "_calendar.csv"
    post_listings_path = path + m + "_listings.csv"
    post_calendar_path = path + m + "_calendar.csv"

    results = get_booked_listings(prev_listings_path, prev_calendar_path, post_listings_path, post_calendar_path)
    results.to_csv(output_path + months[index] + "_" + m + ".csv", index = False)
