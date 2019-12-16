#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

get_ipython().system("conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab")
import folium # map rendering library

print('Libraries imported.')


# ##### We define the Foursqure Credentials

# In[6]:


CLIENT_ID = 'F3MJ1QJPRHR3QIUN4UFG0GCMJJM53NC2RXKOGENYKFCDTVOK' # your Foursquare ID
CLIENT_SECRET = 'ESQQJ2EZNYXRSKN30MFHEXHZHRR3WADCB5TJ2LPSL3YIHSU3' # your Foursquare Secret
VERSION = '20191216' # Foursquare API version

print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)


# In[3]:


get_ipython().system("conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab")
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values


# In[4]:


address = 'Yaounde, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Yaounde are {}, {}.'.format(latitude, longitude))


# ### We get the First 50 venues within a radius of 10,000 meters in Yaounde

# In[7]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 10000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude, 
    longitude, 
    radius, 
    LIMIT)
url


# In[8]:


results  = requests.get(url).json()
results


# In[9]:


# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[10]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
yde_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
yde_venues =yde_venues.loc[:, filtered_columns]

# filter the category for each row
yde_venues['venue.categories'] = yde_venues.apply(get_category_type, axis=1)

# clean columns
yde_venues.columns = [col.split(".")[-1] for col in yde_venues.columns]

yde_venues.head()


# In[11]:


yde_venues['City'] = 'Yaounde'
yde_venues = yde_venues[['City', 'name', 'categories', 'lat', 'lng']] # To index the City column to the first
yde_venues.head()


# ### Venues in Douala 

# In[12]:


# We get all vebues within a radius of 50000 meters in the city Douala 
address = 'Douala, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude_dla = location.latitude
longitude_dla = location.longitude
print('The geograpical coordinates of Douala are {}, {}.'.format(latitude_dla, longitude_dla))


# In[13]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 10000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude_dla, 
    longitude_dla, 
    radius, 
    LIMIT)
url


# In[14]:


results  = requests.get(url).json()
results


# In[15]:


# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[16]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
dla_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
dla_venues =dla_venues.loc[:, filtered_columns]

# filter the category for each row
dla_venues['venue.categories'] = dla_venues.apply(get_category_type, axis=1)

# clean columns
dla_venues.columns = [col.split(".")[-1] for col in dla_venues.columns]

dla_venues.head()


# In[17]:


dla_venues['City'] = 'Douala'
dla_venues = dla_venues[['City', 'name', 'categories', 'lat', 'lng']] # To index the City column to the first
dla_venues.head()


# In[19]:


pd1 = pd.concat([yde_venues, dla_venues], ignore_index = True)
pd1.head()


# ### Venues in Bamenda

# In[20]:


# We get all vebues within a radius of 50000 meters in the city Bamenda 
address = 'Bamenda, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude_bda = location.latitude
longitude_bda = location.longitude
print('The geograpical coordinates of Bamenda are {}, {}.'.format(latitude_bda, longitude_bda))


# In[21]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 10000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude_bda, 
    longitude_bda, 
    radius, 
    LIMIT)
url


# In[22]:


results  = requests.get(url).json()
results


# In[23]:


# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[24]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
bda_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
bda_venues =bda_venues.loc[:, filtered_columns]

# filter the category for each row
bda_venues['venue.categories'] = bda_venues.apply(get_category_type, axis=1)

# clean columns
bda_venues.columns = [col.split(".")[-1] for col in bda_venues.columns]

bda_venues.head()


# In[25]:


bda_venues['City'] = 'Bamenda'
bda_venues = bda_venues[['City', 'name', 'categories', 'lat', 'lng']] # To index the City column to the first
bda_venues.head()


# In[29]:


pd2 = pd.concat([pd1, bda_venues], ignore_index = True)
pd2.tail()


# ### Venues in Bafoussam

# In[30]:


# We get all vebues within a radius of 50000 meters in the city Bafoussam
address = 'Bafoussam, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude_baf = location.latitude
longitude_baf = location.longitude
print('The geograpical coordinates of Bafoussam are {}, {}.'.format(latitude_baf, longitude_baf))


# In[31]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 10000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude_baf, 
    longitude_baf, 
    radius, 
    LIMIT)
url


# In[32]:


results  = requests.get(url).json()
results


# In[33]:


# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[34]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
baf_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
baf_venues =baf_venues.loc[:, filtered_columns]

# filter the category for each row
baf_venues['venue.categories'] = baf_venues.apply(get_category_type, axis=1)

# clean columns
baf_venues.columns = [col.split(".")[-1] for col in baf_venues.columns]

baf_venues.head(50)


# In[37]:


baf_venues['City'] = 'Bafoussam'
baf_venues = baf_venues[['City', 'name', 'categories', 'lat', 'lng']] # To index the City column to the first
baf_venues.head()


# In[39]:


pd3 = pd.concat([pd2, baf_venues], ignore_index = True)
pd3.tail(10)


# ## Venues in Buea

# In[40]:


# We get all vebues within a radius of 50000 meters in the city Bafoussam 
address = 'Buea, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude_buea = location.latitude
longitude_buea = location.longitude
print('The geograpical coordinates of Buea are {}, {}.'.format(latitude_buea, longitude_buea))


# In[41]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 10000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude_buea, 
    longitude_buea, 
    radius, 
    LIMIT)
url


# In[42]:


results  = requests.get(url).json()
results


# In[43]:


# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[45]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
buea_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
buea_venues =buea_venues.loc[:, filtered_columns]

# filter the category for each row
buea_venues['venue.categories'] = buea_venues.apply(get_category_type, axis=1)

# clean columns
buea_venues.columns = [col.split(".")[-1] for col in buea_venues.columns]

buea_venues.head()


# In[46]:


buea_venues.head(10)


# In[47]:


buea_venues['City'] = 'Buea'
buea_venues = buea_venues[['City','name','categories','lat','lng']]
buea_venues


# In[49]:


pd4 = pd.concat([pd3, buea_venues], ignore_index = True)
pd4.tail(20)


# ### Venues in Bertoua

# In[51]:


# We get all vebues within a radius of 50000 meters in the city Bertoua 
address = 'Bertoua, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude_bert = location.latitude
longitude_bert = location.longitude
print('The geograpical coordinates of Bertoua are {}, {}.'.format(latitude_bert, longitude_bert))


# In[52]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 10000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude_bert, 
    longitude_bert, 
    radius, 
    LIMIT)
url


# In[53]:


results  = requests.get(url).json()
results


# In[54]:


# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[55]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
bert_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
bert_venues =bert_venues.loc[:, filtered_columns]

# filter the category for each row
bert_venues['venue.categories'] = bert_venues.apply(get_category_type, axis=1)

# clean columns
bert_venues.columns = [col.split(".")[-1] for col in bert_venues.columns]

bert_venues.head()


# In[56]:


bert_venues['City'] = 'Bertoua'
bert_venues = bert_venues[['City','name','categories','lat','lng']]
bert_venues


# In[57]:


pd5 = pd.concat([pd4,bert_venues], ignore_index = True)
pd5.tail()


# ### Venues in Maroua

# In[58]:


# We get all vebues within a radius of 50000 meters in the city Maroua 
address = 'Maroua, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude_Mar = location.latitude
longitude_Mar = location.longitude
print('The geograpical coordinates of Maroua are {}, {}.'.format(latitude_Mar, longitude_Mar))


# In[62]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 20000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude_Mar, 
    longitude_Mar, 
    radius, 
    LIMIT)
url


# In[63]:


results  = requests.get(url).json()
results


# In[64]:


def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[66]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
Mar_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
Mar_venues =Mar_venues.loc[:, filtered_columns]

# filter the category for each row
Mar_venues['venue.categories'] = Mar_venues.apply(get_category_type, axis=1)

# clean columns
Mar_venues.columns = [col.split(".")[-1] for col in Mar_venues.columns]

Mar_venues.head()


# In[67]:


Mar_venues['City'] = 'Maroua'
Mar_venues = Mar_venues[['City','name','categories','lat','lng']]
Mar_venues


# In[68]:


pd6 = pd.concat([pd5,Mar_venues], ignore_index = True)
pd6.tail()


# ### Venues in Garoua

# In[70]:


# We get all vebues within a radius of 50000 meters in the city Garoua 
address = 'Garoua, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude_Gar = location.latitude
longitude_Gar = location.longitude
print('The geograpical coordinates of Garoua are {}, {}.'.format(latitude_Gar, longitude_Gar))


# In[75]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 10000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude_Gar, 
    longitude_Gar, 
    radius, 
    LIMIT)
url


# In[76]:


results = requests.get(url).json()
results


# In[77]:


def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[78]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
Gar_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
Gar_venues =Gar_venues.loc[:, filtered_columns]

# filter the category for each row
Gar_venues['venue.categories'] = Gar_venues.apply(get_category_type, axis=1)

# clean columns
Gar_venues.columns = [col.split(".")[-1] for col in Gar_venues.columns]

Gar_venues.head()


# In[79]:


Gar_venues['City'] = 'Garoua'
Gar_venues = Gar_venues[['City','name','categories','lat','lng']]
pd7 = pd.concat([pd6,Gar_venues], ignore_index = True)
pd7.tail(10)


# ### Venues in  Ngoundere

# In[81]:


# We get all vebues within a radius of 50000 meters in the city Ngoundere 
address = 'Ngaoundéré, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude_ngoun = location.latitude
longitude_ngoun = location.longitude
print('The geograpical coordinates of Ngaoundere are {}, {}.'.format(latitude_ngoun, longitude_ngoun))


# In[82]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 10000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude_ngoun, 
    longitude_ngoun, 
    radius, 
    LIMIT)
url


# In[83]:


results = requests.get(url).json()
results


# In[84]:


def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[85]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
ngaoun_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
ngaoun_venues =ngaoun_venues.loc[:, filtered_columns]

# filter the category for each row
ngaoun_venues['venue.categories'] = ngaoun_venues.apply(get_category_type, axis=1)

# clean columns
ngaoun_venues.columns = [col.split(".")[-1] for col in ngaoun_venues.columns]

ngaoun_venues.head()


# In[86]:


ngaoun_venues['City'] = 'Ngaoundere'
ngaoun_venues = ngaoun_venues[['City','name','categories','lat','lng']]
pd8 = pd.concat([pd7,ngaoun_venues], ignore_index = True)
pd8.tail(10)


# ### Venues in Ebolowa

# In[87]:


# We get all vebues within a radius of 50000 meters in the city Ebolowa 
address = 'Ebolowa, Cameroon'

geolocator = Nominatim(user_agent="Foursquare_agent")
location = geolocator.geocode(address)
latitude_ebl = location.latitude
longitude_ebl = location.longitude
print('The geograpical coordinates of Ebolowa are {}, {}.'.format(latitude_ebl, longitude_ebl))


# In[88]:


# type your answer here
LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 10000 # define radius
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    latitude_ebl, 
    longitude_ebl, 
    radius, 
    LIMIT)
url


# In[89]:


results = requests.get(url).json()
results


# In[90]:


def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# In[91]:


# Let us get the Data into a Pandas Data Frame
venues = results['response']['groups'][0]['items']
    
ebl_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
ebl_venues =ebl_venues.loc[:, filtered_columns]

# filter the category for each row
ebl_venues['venue.categories'] = ebl_venues.apply(get_category_type, axis=1)

# clean columns
ebl_venues.columns = [col.split(".")[-1] for col in ebl_venues.columns]

ebl_venues.head()


# In[92]:


ebl_venues['City'] = 'Ebolowa'
ebl_venues = ebl_venues[['City','name','categories','lat','lng']]
cmr_venues_data = pd.concat([pd8,ebl_venues], ignore_index = True)
cmr_venues_data.tail(10)


# At tis point we have collected all the relevant data and combined inone dataset named 'cmr_venues_data'.
# The next task is to get the most frequent venue overall and the most frequent per city

# In[93]:


# We check the frequency of the different categories of venues
cmr_venues_data.groupby('categories').count()


# In[94]:


# We get the number of unique categories
print('There are {} uniques categories.'.format(len(cmr_venues_data['categories'].unique())))


# ## We Analyze each city as per the different categories in the city, using one hot encoding

# In[96]:


# We use OneHotEncoding and analyze each city
# one hot encoding
cameroon_onehot = pd.get_dummies(cmr_venues_data[['categories']], prefix="", prefix_sep="")

# add City column back to dataframe
cameroon_onehot['City'] = cmr_venues_data['City'] 

# move City column to the first column
fixed_columns = [cameroon_onehot.columns[-1]] + list(cameroon_onehot.columns[:-1])
cameroon_onehot = cameroon_onehot[fixed_columns]

cameroon_onehot


# In[97]:


cameroon_onehot.shape #Getting the shape of the Dataset


# #### We now group the rows by city and by taking the mean frequency of occurrence of each of the categories

# In[98]:


cameroon_grouped = cameroon_onehot.groupby('City').mean().reset_index()
cameroon_grouped


# In[100]:


cameroon_grouped.shape


# #### We now print each city with the top 5 venue categories in the city

# In[104]:


num_top_venues = 5

for City in cameroon_grouped['City']:
    print("----"+City+"----")
    temp = cameroon_grouped[cameroon_grouped['City'] == City].T.reset_index()
    temp.columns = ['venue','freq']
    temp = temp.iloc[1:]
    temp['freq'] = temp['freq'].astype(float)
    temp = temp.round({'freq': 2})
    print(temp.sort_values('freq', ascending=False).reset_index(drop=True).head(num_top_venues))
    print('\n')


# #### We then create a dataframe displaying the top 5 business category in each city. But first, we write a function to sort the venues in descending order

# In[107]:


def return_most_common_venues(row, num_top_venues):
    row_categories = row.iloc[1:]
    row_categories_sorted = row_categories.sort_values(ascending=False)
    
    return row_categories_sorted.index.values[0:num_top_venues]


# In[120]:


# We then create a new dataframe and display the top 5 venues in each city
num_top_venues = 3

indicators = ['st', 'nd', 'rd']

# create columns according to number of top venues
columns = ['City']
for ind in np.arange(num_top_venues):
    try:
        columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
    except:
        columns.append('{}th Most Common Venue'.format(ind+1))

# create a new dataframe
city_venues_sorted = pd.DataFrame(columns=columns)
city_venues_sorted['City'] = cameroon_grouped['City']

for ind in np.arange(cameroon_grouped.shape[0]):
    city_venues_sorted.iloc[ind, 1:] = return_most_common_venues(cameroon_grouped.iloc[ind, :], num_top_venues)

city_venues_sorted.head(12)


# ### By handing over the data to the Chinese investors, the Data Scientists project is finished.

# In[ ]:




