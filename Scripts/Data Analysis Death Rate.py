
# coding: utf-8

# In[1]:


import numpy as np
import tensorflow as tf
import pandas as pd
df = pd.DataFrame(pd.read_csv('../Data/Hospital_Revised_Flatfiles/Deaths.csv', sep=','))
df = df.drop(['Provider ID', 'Address', 'City','ZIP Code','County Name', 'Phone Number', 'Compared to National','Lower Estimate', 'Higher Estimate', 'Footnote', 'Measure Start Date', 'Measure End Date'], axis=1)
cf = df.pivot(columns=["Measure Name", 'Measure ID', 'Denominator', 'Score'], index=["State","Hospital Name"])
print cf