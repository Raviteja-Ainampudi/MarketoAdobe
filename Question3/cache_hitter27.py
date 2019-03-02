#!/usr/bin/python3
#Author - Ravi Ainampudi

from random import randint, seed
from datetime import datetime

def GetImageURL(value_1, value_2):
    """Stub Version of GetImageURL() method. This returns a random number."""
    seed(abs(value_1)+abs(value_2))
    return randint(1, 1000000) #Random number generation. 


custom_memory = {}
custom_hit = 0
custom_miss = 0
total_custom_memory = 3000

def clear_cache():
    """Clearing Cache and initializing them again to default values."""
    global custom_memory, custom_hit, custom_miss
    custom_memory = {}
    custom_hit = 0
    custom_miss = 0
    return 
    
def info_cache():
    """Cache Infomation as a list with counter of Hits, Misses, Current Length, Total Length."""
    return [custom_hit, custom_miss, len(custom_memory), total_custom_memory]
    
def find_image_url(lat_value, long_value):
    """Cache Building Function. Managing Hits, Misses and Cache Memory."""
    global custom_memory, custom_hit, custom_miss, total_custom_memory
    image_tuple = (lat_value, long_value)
    
    #When Latitude Longitude in Cache and HIT
    if image_tuple in custom_memory:
            custom_hit+=1
            custom_memory[image_tuple][1] = datetime.now()
            return custom_memory[image_tuple][0],"hit"
    
    #When Latitude Longitude NOT in Cache and MISS
    if len(custom_memory) < total_custom_memory:
            custom_miss+=1
            custom_memory[image_tuple] = [GetImageURL(*image_tuple), datetime.now()]
            return custom_memory[image_tuple][0], "miss_when_not_full"
    else:
        custom_memory = sorted([(key, list_vals) for key, list_vals in custom_memory.items()], key=lambda i:i[1][1], reverse=False)
        del custom_memory[0]
        custom_memory = dict(custom_memory)
        custom_miss+=1
        custom_memory[image_tuple] = [GetImageURL(*image_tuple), datetime.now()]
        return custom_memory[image_tuple][0], "miss_when_after_full"
            
    

    
