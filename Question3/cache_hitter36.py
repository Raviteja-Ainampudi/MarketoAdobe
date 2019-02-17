#!/usr/bin/python3
#Author - Ravi Ainampudi

from functools import lru_cache
from random import randint, seed
from datetime import datetime

def GetImageURL(value_1, value_2):
    """Stub Version GetImageURL() method. This returns a random number."""
    seed(abs(value_1)+abs(value_2))
    return randint(1, 1000000) #Random number generation. 

@lru_cache(maxsize=3000, typed=False) #Cache Maxsize = 3000 in that lru_cache dictionary
def find_image_url(lat_value, long_value):
    """Method which delivers the URL of the image. LRU cache implemented with its decorator."""
    image_tuple = (lat_value, long_value)
    URL = GetImageURL(*image_tuple) #Unpacking the latitude and longitude float values. 
    return URL

        
        
    

    
