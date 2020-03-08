import sys
import pandas as pd
import numpy as np

def get_booked_listings(prev_listings_path, prev_calendar_path, post_listings_path, post_calendar_path, output_path):
    prev_listings = pd.read_csv(prev_listings_path)
    prev_calendar = pd.read_csv(prev_calendar_path)
    post_listings = pd.read_csv(post_listings_path)
    post_calendar = pd.read_csv(post_calendar_path)
    
    prev_listings = prev_listings.drop(["price", "minimum_nights", "last_review"], axis = 1)
    post_listings = post_listings.drop(["price", "minimum_nights", "last_review"], axis = 1)
    
    prev = prev_listings.merge(prev_calendar, left_on = "id", right_on = "listing_id")
    post = post_listings.merge(post_calendar, left_on = "id", right_on = "listing_id")
    
    prev = prev.drop(["listing_id"], axis = 1)
    post = post.drop(["listing_id"], axis = 1)
    
    merged = prev.merge(post, on = ["id", "date"], suffixes = ["_prev", "_post"])
    booking_changes = merged[(merged.available_prev == 't') & (merged.available_post == 'f')]
    booking_changes.to_csv(output_path, index=False)

prev_listings_path = sys.argv[1]
prev_calendar_path = sys.argv[2]
post_listings_path = sys.argv[3]
post_calendar_path = sys.argv[4]
output_path = sys.argv[5]
get_booked_listings(prev_listings_path, prev_calendar_path, post_listings_path, post_calendar_path, output_path)