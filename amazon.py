#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt


# # importing File as csv

# In[2]:


database = pd.read_csv(r"C:\Users\OMEN\OneDrive\Desktop\Amazon Sale Report.csv", encoding="latin1")
print(database)


# In[3]:


database.head(3)


# In[4]:


database.info()


# # Data Cleaning
# Deleting columns with all null values: 'New' and 'PendingS'

# In[5]:


database.drop(columns=["New", "PendingS"], inplace=True, errors='ignore')


# Convert date to datetime

# In[9]:


database["Date"] = pd.to_datetime(database["Date"])


# Convert to categories

# In[25]:


category_columns = [
    'currency', 'Sales Channel', 'Status', 'Fulfilment', 'ship-service-level',
    'Category', 'Size', 'Courier Status', 'fulfilled-by'
]
for col in category_columns:
    database[col] = database[col].astype('category')


# convert to string

# In[11]:


database["Order ID"] = database["Order ID"] .astype("str")


# In[32]:


database.info()


# Checking Null Values

# In[13]:


database.isnull().sum()


# In[14]:


(database.isnull().sum()/database.shape[0])*100


# In[15]:


database['currency'].fillna('INR', inplace=True)


# In[16]:


database[database['Amount'] == 0].shape[0]


# In[17]:


database['Amount_was_missing'] = database['Amount'].isna()


# In[30]:


database["ship-city"]=database["ship-city"].astype(object)
database["ship-state"]=database["ship-state"].astype(object)
database["ship-postal-code"]=database["ship-postal-code"].astype(object)
database["ship-country"]=database["ship-country"].astype(object)


# In[31]:


database['ship-city'].fillna('Unknown', inplace=True)
database['ship-state'].fillna('Unknown', inplace=True)
database['ship-postal-code'].fillna(0, inplace=True)
database['ship-country'].fillna('Unknown', inplace=True)


# In[37]:


database.drop(columns=["fulfilled-by"],inplace= True)


# In[40]:


database.duplicated().sum()


# In[42]:


database.drop_duplicates(inplace=True)


# In[48]:


database["ship-city"] = database["ship-city"].str.title()
database["ship-state"] = database["ship-state"].str.title()
database["Category"] = database["Category"].str.title()


# In[50]:


print(database.info())
print(database.isna().sum())
print(database.describe(include='all'))


# In[49]:


database.to_csv("amazon_sales_cleaned.csv", index=False)


# In[54]:


status_unique=database["Status"].unique()
print(status_unique)


# In[ ]:




