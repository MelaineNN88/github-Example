#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

get_ipython().system("conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab")
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library

print('Libraries imported.')


# In[4]:


pip install lxml


# In[19]:


#Fetching the Data from the webpage
url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
toronto_data = pd.read_html(url, header=0)


# In[20]:


#Converting the data into a pandas dataframe
toronto_data = toronto_data[0]
toronto_data.head()


# In[25]:


#Dropping the Boroughs which are 'Not Assigned'
neighborhood_data = toronto_data[toronto_data.Borough != 'Not assigned']
neighborhood_data.reset_index(drop = True, inplace = True)
neighborhood_data.head()


# In place of the above code, we can also use the following
# neighborhood_data = toronto_data.set_index("Borough")
# neighborhood_data.drop("Not assigned")
# neighborhood_data.reset_index(drop = True, inplace = True)
# neighborhood_data.head() #to view the first five observations

# In[33]:


#Combining the neighbourhoods of different coastal areas in one row seperated by comma 
neighborhood_data = neighborhood_data.groupby(['Postcode','Borough'])['Neighbourhood'].apply(','.join)
neighborhood_data = neighborhood_data.reset_index(level = ['Postcode','Borough'])
neighborhood_data.head()


# In[39]:


#Here, we want to check the Neighbourhoods with the value 'Not assigned'
neighborhood_data[neighborhood_data.Neighbourhood == 'Not assigned']


# In[41]:


#For the Neighbourhood with the value 'Not Assigned', we name the Neighbourhood with it's 'Borough' name
#and then check is there is still any Neighbourhood with a 'Not assigned' observation.
#None exist anymore
neighborhood_data.loc[(neighborhood_data.Neighbourhood =='Not assigned'), 'Neighbourhood'] = neighborhood_data.Borough
neighborhood_data[neighborhood_data.Neighbourhood == 'Not assigned']


# In[42]:


#This code the verifies if the Neighbourhood observation of 'Not assigned' on Postcode 'M7A' has been
#Replaced by the Borough name 'Queen's Park
neighborhood_data[neighborhood_data.Postcode == 'M7A']


# In[44]:


#The shape of the data is 103 observations and 3 Variables
neighborhood_data.shape


# In[ ]:




