#!/usr/bin/env python
# coding: utf-8

# In[141]:


import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
from pprint import pprint
from stats import median

csvpath = os.path.join("Data", "city_codes.csv")
csvpath = os.path.join("Data", "majors_dates.csv")
csvpath = os.path.join("Data", "rift_weath_sol_equ.csv")


# In[142]:


city_codes_csv = "Data/city_codes.csv"


# In[143]:


city_codes_df = pd.read_csv(city_codes_csv)


# In[108]:


major_dates_csv = "Data/majors_dates.csv"


# In[109]:


major_dates_df = pd.read_csv(major_dates_csv)


# In[110]:


major_dates_df


# In[111]:


city_13_list = []
feel_13_list = []


url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
params = {
    "key": "bc1fb38cb0ec446b83221156192908",  
    "tp": 24,
    "format": "json",    
}

for index, row in major_dates_df.iterrows():
 
    params['q'] = row['major']
    params['date'] = row['13 majors']
    
    response = requests.get(url, params=params).json()
    
    city_13_list.append(row['major'])
    feel_13_list.append((response['data']['weather'][0]['hourly'][0]['FeelsLikeF']))
    pprint(response)


# In[112]:


print(feel_13_list)


# In[113]:


majors_weather_dict = {
    "city": city_13_list,
    "feels_like_13": feel_13_list,
}
majors_13_weather_df = pd.DataFrame(majors_weather_dict)
majors_13_weather_df.head()


# In[114]:


city_14_list = []
feel_14_list = []


url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
params = {
    "key": "bc1fb38cb0ec446b83221156192908",  
    "tp": 24,
    "format": "json",    
}

for index, row in major_dates_df.iterrows():
 
    params['q'] = row['major']
    params['date'] = row['14 majors']
    
    response = requests.get(url, params=params).json()
    
    city_14_list.append(row['major'])
    feel_14_list.append((response['data']['weather'][0]['hourly'][0]['FeelsLikeF']))
    pprint(response)


# In[115]:


majors_weather_dict = {
    "city": city_14_list,
    "feels_like_14": feel_14_list,
}
majors_14_weather_df = pd.DataFrame(majors_weather_dict)
majors_14_weather_df.head()


# In[116]:


city_15_list = []
feel_15_list = []


url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
params = {
    "key": "bc1fb38cb0ec446b83221156192908",  
    "tp": 24,
    "format": "json",    
}

for index, row in major_dates_df.iterrows():
 
    params['q'] = row['major']
    params['date'] = row['15 majors']
    
    response = requests.get(url, params=params).json()
    
    city_15_list.append(row['major'])
    feel_15_list.append((response['data']['weather'][0]['hourly'][0]['FeelsLikeF']))
    pprint(response)


# In[117]:


majors_weather_dict = {
    "city": city_15_list,
    "feels_like_15": feel_15_list,
}
majors_15_weather_df = pd.DataFrame(majors_weather_dict)
majors_15_weather_df.head()


# In[120]:


city_16_list = []
feel_16_list = []


url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
params = {
    "key": "bc1fb38cb0ec446b83221156192908",  
    "tp": 24,
    "format": "json",    
}

for index, row in major_dates_df.iterrows():
 
    params['q'] = row['major']
    params['date'] = row['16 majors']
    
    response = requests.get(url, params=params).json()

    city_16_list.append(row['major'])
    feel_16_list.append((response['data']['weather'][0]['hourly'][0]['FeelsLikeF']))
    pprint(response)


# In[121]:


majors_weather_dict = {
    "city": city_16_list,
    "feels_like_16": feel_16_list,
}
majors_16_weather_df = pd.DataFrame(majors_weather_dict)
majors_16_weather_df.head()


# In[122]:


city_17_list = []
feel_17_list = []

url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
params = {
    "key": "bc1fb38cb0ec446b83221156192908",  
    "tp": 24,
    "format": "json",    
}

for index, row in major_dates_df.iterrows():
 
    params['q'] = row['major']
    params['date'] = row['17 majors']
    
    response = requests.get(url, params=params).json()

    city_17_list.append(row['major'])
    feel_17_list.append((response['data']['weather'][0]['hourly'][0]['FeelsLikeF']))
    pprint(response)


# In[123]:


majors_weather_dict = {
    "city": city_17_list,
    "feels_like_17": feel_17_list,
}
majors_17_weather_df = pd.DataFrame(majors_weather_dict)
majors_17_weather_df.head()


# In[124]:


city_18_list = []
feel_18_list = []

url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
params = {
    "key": "bc1fb38cb0ec446b83221156192908",  
    "tp": 24,
    "format": "json",    
}

for index, row in major_dates_df.iterrows():
 
    params['q'] = row['major']
    params['date'] = row['18 majors']
    
    response = requests.get(url, params=params).json()

    city_18_list.append(row['major'])
    feel_18_list.append((response['data']['weather'][0]['hourly'][0]['FeelsLikeF']))
    pprint(response)


# In[125]:


majors_weather_dict = {
    "city": city_18_list,
    "feels_like_18": feel_18_list,
}
majors_18_weather_df = pd.DataFrame(majors_weather_dict)
majors_18_weather_df.head()


# In[174]:


merge_weather_1 = pd.merge(majors_13_weather_df, majors_14_weather_df, on="city")
merge_weather_1


# In[175]:


merge_weather_2 = pd.merge(merge_weather_1, majors_15_weather_df, on="city")
merge_weather_2


# In[176]:


merge_weather_3 = pd.merge(merge_weather_2, majors_16_weather_df, on="city")
merge_weather_3


# In[177]:


merge_weather_4 = pd.merge(merge_weather_3, majors_17_weather_df, on="city")
merge_weather_4


# In[178]:


merge_weather_5 = pd.merge(merge_weather_4, majors_18_weather_df, on="city")
merge_weather_5
merge_weather_5 = merge_weather_5.rename(columns={"feels_like_13":"2013", "feels_like_14":"2014", "feels_like_15":"2015","feels_like_16":"2016","feels_like_17":"2017","feels_like_18":"2018",})
merge_weather_5


# In[185]:


merge_weather_df = pd.merge(merge_weather_5, city_codes_df, on="city")
merge_weather_df


# In[186]:


merge_weather_df = merge_weather_df.set_index("city_code")
merge_weather_df


# In[189]:


merge_weather_df=merge_weather_df.astype(float)


# In[188]:


average_heat_index = merge_weather_df.mean()
average_heat_index
print(average_heat_index)


# In[150]:


# merge_weather_df.loc['TYO', "2013":"2018"].plot(label="Tokyo")
# plt.legend()
# plt.show()


# In[151]:


average_heat_index = merge_weather_df.mean()
average_heat_index
merge_weather_df.mean()


# In[27]:


# country_one, = plt.plot(years, merge_weather_df.loc['JPN',["2013","2014","2015","2016","2017","2018"]], color="green",label="Tokyo Marathon"
# plt.legend()
# plt.show


# In[ ]:


# Select two countries' worth of data.
heat_index_13 = merge_weather_df.loc[1]
heat_index_14 = merge_weather_df.loc[2]
heat_index_15 = merge_weather_df.loc[3]

# Plot with differently-colored markers.
years = [2013, 2014, 2015, 2016, 2017, 2018]
plt.plot(x= ["years"], y=["heat_index_13", "heat_index_14", "heat_index_15"], kind="bar")
# plt.plot(['city'], heat_index_13, 'b-', label='Majors 2013')
# plt.plot(['city'], heat_index_14, 'g-', label='Majors 2014')

# Create legend.
plt.legend()
plt.xlabel('Year')


# In[ ]:


merge_weather_df=merge_weather_df.astype(float)


# In[ ]:


merge_weather_df.plot.bar()
plt.legend(loc="best")
plt.title("Historical Heat Index At The Abbot Majors")
plt.xlabel("Country")
plt.ylabel("Number of Medals")


# In[ ]:


merge_weather_df.columns


# In[ ]:


merge_weather_df.set_index('city')


# In[ ]:


merge_weather_df.plot.bar()
plt.legend(loc="best")
plt.title("Historical Heat Index At The Abbot Majors")
plt.xlabel("Country")
plt.ylabel("Number of Medals")


# In[160]:


rift_dates_csv = "Data/rift_weath_sol_equ.csv"


# In[161]:


rift_dates_df = pd.read_csv(rift_dates_csv)
rift_dates_df


# In[162]:


city_rift_list = []
feel_rift_list = []

url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
params = {
    "key": "bc1fb38cb0ec446b83221156192908",  
    "tp": 24,
    "format": "json",    
}

for index, row in rift_dates_df.iterrows():
 
    params['q'] = row['city']
    params['date'] = row['sumsol_13']
    
    response = requests.get(url, params=params).json()
    
    city_rift_list.append(row['city'])
    feel_rift_list.append((response['data']['weather'][0]['hourly'][0]['FeelsLikeF']))
    pprint(response)


# In[ ]:


print(temp_rift_list)


# In[ ]:


major_dates_df


# In[ ]:


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()

