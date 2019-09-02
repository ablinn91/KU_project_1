#!/usr/bin/env python
# coding: utf-8

# In[98]:


import csv
import matplotlib.pyplot as plt
import requests
import pandas as pd
import json
import os
import numpy as np
import csv
api_key = "bc1fb38cb0ec446b83221156192908"
csvpath = os.path.join("Data", "majors_dates.csv")


# In[99]:


major_dates_csv = "Data/majors_dates.csv"


# In[100]:


major_dates_df = pd.read_csv(major_dates_csv)


# In[101]:


major_dates_df


# In[111]:




url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
params = {
    "key": "bc1fb38cb0ec446b83221156192908",  
    "tp": 6,
    "format": "json",
    "date": "2013/05/07"
}
# use iterrows to iterate through pandas dataframe
for index, row in major_dates_df.iterrows():

    city = row['major']
#     dates = row['13 majors']
    params['q'] = city 

    response = requests.get(url, params=params).json()
    print(response)
    


# In[ ]:




