#!/usr/bin/env python
# coding: utf-8

# # Loading Files
# 
# In the first chapter we will learn how to load data into Pandas DataFrames. We will load multile formats of data sources including CSV files, Excel files, tables from web sites, tables in Databases, etc. 

# To make the notebooks cleaner and easier to read we will suppress warnings. Bad practice, however, OK for a tutorial.

# In[1]:


import warnings
warnings.filterwarnings('ignore')


# ## Loading CSV file 
# 
# The comma-separated-values (CSV) format is one of the simplest and pupolar way to share (small) data. You can save an Excel files as CSV and it is the default format of many bulk download of data from databases and other sources. 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib


# The first example is using data file about permits for restaurants in NY city. It was downloaded from the open data web site [data.world](https://data.world/city-of-ny/pitm-atqc)

# In[3]:


table_df = pd.read_csv('../data/open_restaurant_applications_1.csv')


# In[4]:


table_df.head()


# In[5]:


table_df.info()


# In[6]:


table_df.describe()


# ## Simple data visualization
# 
# As part of the data exploration phase, you want to look at the columns, a few rows (_head_), column statistics (_describe_), data types and number of values (_info_). However, usually the most effective way is to visualize the data to understand it. 
# 
# In the next cell, we build a simple scatter plot of the data with _longitude_ and _latitude_ as x-axis and y-axis, respectively.

# In[7]:


(
    table_df
    .plot
    .scatter(x='longitude',y='latitude')
)


# ## Adding new columns
# 
# One of the most common tasks that we do when building an analysis is to add calcualted fields, based on the other columns in our table/DataFrame. We will discuss power of Pandas in adding new columns in the next sections of this guide. However, here is an example of calcuting the color of a data point, based on the value of _approved_for_roadway_seating_ column. It will be green (_g_) if the value is _yes_, or red (_r_) otherwise.

# In[8]:


(
    table_df
    .assign(approved=lambda x : np.where(x.approved_for_roadway_seating == 'yes','g','r'))
    .plot.scatter(x='longitude',y='latitude',c='approved')
)


# ## Loading Excel Files
# 
# You can also read files that were edited in Excel and saved in the Excel format.
# 
# If the python environment that we are using is missing part of the needed functionality, such as the ability to parse the format of the Microsoft Excel files, we need to install using the following command:

# In[9]:


get_ipython().system('pip install xlrd')


# Then, we can call _read_excel_ instead of _read_csv_

# In[10]:


table_df_from_excel = pd.read_excel('../data/open_restaurant_applications.xlsx')


# and since the data now is in the Pandas (_pd_) DataFrame format, all the rest of the commands are exactly the same. For example, here is the same chart we plotted before.

# In[11]:


(
    table_df_from_excel
    .plot
    .scatter(x='longitude',y='latitude')
)


# In[ ]:




