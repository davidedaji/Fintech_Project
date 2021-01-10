#!/usr/bin/env python
# coding: utf-8

# In[24]:




import pandas as pd
import numpy as np
import datetime as dt
import statsmodels.api as sm

url = 'https://github.com/davidedaji/Fintech_Project/raw/main/2019Q4.xlsx'


# In[26]:


df = pd.read_excel(url,index_col=0, engine='openpyxl')
df['issue_d'] = pd.to_datetime(df['issue_d'])
df['issue_d'] = df['issue_d'].map(lambda x: x.replace(year=2019))
writer = pd.ExcelWriter('Ex1_DATA.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='PCA')
writer.save()


print(df)


# In[11]:


df['issue_d'] = df['issue_d'].dt.strftime('%b-%y')

print(df)


# In[ ]:




