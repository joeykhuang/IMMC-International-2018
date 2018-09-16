
# coding: utf-8

# In[3]:


import csv
import pandas as pd
import numpy as np


# In[20]:


df = pd.read_csv('HosCateData.csv')


# In[6]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[21]:


df[2000:3000]


# In[26]:


gf = df.pivot_table(values='Ranking', index=['State'], columns=['Category'], aggfunc=np.sum)


# In[25]:


print gf
