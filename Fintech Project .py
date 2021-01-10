#!/usr/bin/env python
# coding: utf-8

# In[110]:


import pandas as pd
import numpy as np
import datetime as dt
import statsmodels.api as sm
from matplotlib import pyplot
import plotly.express as px
import plotly.graph_objects as go

urlq1 = 'https://github.com/davidedaji/Fintech_Project/raw/main/2019Q1.xlsx'
urlq2 = 'https://github.com/davidedaji/Fintech_Project/raw/main/2019Q2.xlsx'
urlq3 = 'https://github.com/davidedaji/Fintech_Project/raw/main/2019Q3.xlsx'
urlq4 = 'https://github.com/davidedaji/Fintech_Project/raw/main/2019Q4.xlsx'
url2020full = 'https://github.com/davidedaji/Fintech_Project/raw/main/2020F.xlsx'


# In[65]:


def average_int(url):
    df = pd.read_excel(url,index_col=0, engine='openpyxl')
    df['issue_d'] = pd.to_datetime(df['issue_d'])
    df.drop(['Amount'], axis='columns', inplace=True)
    dg = df.groupby(pd.Grouper(key='issue_d', freq='1M')).mean().reset_index().rename(columns={'int_rate':'Average'})
    dg1 = df.groupby(pd.Grouper(key='issue_d', freq='1M')).quantile(q=0.05).reset_index().rename(columns={'int_rate':'5% percentile'})
    dg2 = df.groupby(pd.Grouper(key='issue_d', freq='1M')).quantile(q=0.95).reset_index().rename(columns={'int_rate':'95% percentile'})
    result = pd.merge(dg, dg1, on='issue_d', how='inner')
    result = pd.merge(result, dg2, on='issue_d', how='inner')
    result['issue_d'] = result['issue_d'].dt.strftime('%b-%y')
    return result



Q1_2019 = average_int(urlq1)
Q2_2019 = average_int(urlq2)
Q3_2019 = average_int(urlq3)
Q4_2019 = average_int(urlq4)
Full2020 = average_int(url2020full)

print(Q1_2019)
print(Q2_2019)
print(Q3_2019)
print(Q4_2019)
print(Full2020)


# In[66]:


def put_together(q1,q2,q3,q4):
    final = pd.concat([q1,q2,q3,q4])
    final = final.reset_index(drop=True)
    return final
def put_togethertwo(df1,df2):
    final = pd.concat([df1,df2])
    final = final.reset_index(drop=True)
    return final

Year2019 = put_together(Q1_2019,Q2_2019,Q3_2019,Q4_2019)

Year2019_2020 = put_togethertwo(Year2019, Full2020)

print(Year2019_2020)


# In[69]:


def excelize(namefile, df):
    writer = pd.ExcelWriter(namefile + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet 1')
    return writer.save()

excelize('Fintech_Project comparison',Year2019_2020)
    


# In[88]:


Year2019_2020.plot()
pyplot.show()


# In[87]:


fig = go.Figure()
fig = px.line(Year2019_2020, x='issue_d', y="Average", title='P2P interest rate over time')
fig.add_trace(go.Scatter(x=Year2019_2020['issue_d'], y=Year2019_2020['95% percentile'], name='95th percentile',
                         line = dict(color='green', width=2, dash='dash')))
fig.add_trace(go.Scatter(x=Year2019_2020['issue_d'], y=Year2019_2020['5% percentile'], name='5th percentile',
                         line = dict(color='red', width=2, dash='dash')))
fig.update_layout(title='P2P interest rate',
                   xaxis_title='Months',
                   yaxis_title='Interest rate')
fig.show()


# In[109]:


fig = go.Figure()
fig = px.line(Year2019_2020, x='issue_d', y="Average", title='P2P interest rate over time')
fig.update_layout(yaxis_range=[0.1225,0.136])
fig.update_layout(title='P2P interest rate',
                   xaxis_title='Months',
                   yaxis_title='Interest rate')
fig.update_yaxes(tick0=0.0000, dtick=0.001)
fig.show()


# In[ ]:




