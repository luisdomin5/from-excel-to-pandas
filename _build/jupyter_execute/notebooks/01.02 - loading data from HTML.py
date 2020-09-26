#!/usr/bin/env python
# coding: utf-8

# # Reading Data from Web Sites
# 
# Many times you want to add external data to your analysis. External data is often found in external web sites, usually in the format of an HTML table. You can import HTML directly into Excel using _"Import"_.
# 
# In this notebook, we will learn how to use pandas _read_html_ to load tables from web site with ease, including cases where the data is complex to retrieve. 

# ## Loading HTML data
# 
# We will load a few tables from simple sites as well as complex ones

# In[1]:


import warnings
warnings.filterwarnings('ignore')


# In[2]:


import pandas as pd
import numpy as np


# ## Loading from simple web sites 
# 
# If you have a simple web page with a single table, you can pass the URL of the page to Pandas and call read_html. 

# In[3]:


url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url)


# read_html is returning a list of all the tables in the page. If we pring the first element (index 0 in the list), we will get the first data frame/table in that page.

# In[17]:


dfs[0]


# ## Loading from complex web sites
# 
# Many times pages will be more complex and we can still extract the relevant data. 

# In[18]:


url = 'https://ncov2019.live/data'
table_id = 'sortable_table_world'


# Here we will look like a browser to the web site, as some web sites block their context to bots and crawlers. Since we are not hitting the web site a lot, pretending to be a browser is considered as acceptable usage. 
# 
# We will send to the web site a header that a browser is sending and get the reply of the page as text. The text (_r.text_) will be parsed by the _read_html_ function and create the dataframe. We will also add the HTML id of the table that we want. This id (_'sortable_table_world'_) can be found when using the _inspect_ option in Chrome, Safari, Firefox and other browsers. 

# In[19]:



import requests

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)


df_list = pd.read_html(r.text, attrs={'id': table_id})


# In[15]:


df_list[0]


# In[20]:


df = df_list[0]


# ## Simple Data Visualization
# 
# External data is often "messy", and it is a best practice to clean it up before staring to work with it. In the next cell we will make sure that the numeric columns are indeed numeric (removing "Unknown", for example). We will also resolve the conflict of having multiple columns with the same name ("Per Million", in this exammple), and translate to more meaningful names.

# In[37]:


(
    df
    .assign(confirmed_cases_per_m=lambda x: pd.to_numeric(x['Per Million'],  errors='coerce'))
    .assign(deceased_cases_per_m=lambda x: pd.to_numeric(x['Per Million.1'],  errors='coerce'))
    .fillna(0)
    # .info()
    .sort_values(by='deceased_cases_per_m',ascending=False)
    .iloc[:20,:]
    .plot
    .bar(x='Name', y=['deceased_cases_per_m'])
)


# In[ ]:




