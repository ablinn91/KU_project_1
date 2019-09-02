#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import matplotlib.pyplot as plt
import requests
import pandas as pd
import json
import os
import numpy as np

# Load JSON
filepath = os.path.join("Data", "CIA_WFB.json")
with open(filepath) as jsonfile:
    CIA_WFB = json.load(jsonfile)


# In[3]:


country_list = []
size_list = []
climate_list = []
pop_list = []
median_age_list = []
urbanization_list = []
life_exp_list = []
drinking_water_source_list = []
roadways_rank_list = []


countries = ["ethiopia", "germany", "japan", "kenya", "united_states", "united_kingdom"]

for country in countries:
        
    data = CIA_WFB["countries"][country]
    
  
    country_list.append((data['data']['name']))
    size_list.append((data['data']['geography']['area']['comparative']))
    climate_list.append((data['data']['geography']['climate']))
    pop_list.append((data['data']['people']['population']['total']))
    median_age_list.append((data['data']['people']['median_age']['total']['value']))
    urbanization_list.append((data['data']['people']['urbanization']['urban_population']['value']))
    life_exp_list.append((data['data']['people']['life_expectancy_at_birth']['total_population']['value']))
    drinking_water_source_list.append((data['data']['people']['drinking_water_source']['improved']['total']['value']))
    roadways_rank_list.append((data['data']['transportation']['roadways']['global_rank']))


# In[4]:


country_info_df = pd.DataFrame({'country':country_list, 
                                'size':size_list, 
                                'climate':climate_list, 
                                'population':pop_list, 
                                'median_age':median_age_list, 
                                'urbanization':urbanization_list,
                                'life_expectancy':life_exp_list,
                                'drinking_water_source':drinking_water_source_list,
                                'roads_global_rank':roadways_rank_list, 
    
})
country_info_df


# In[ ]:




