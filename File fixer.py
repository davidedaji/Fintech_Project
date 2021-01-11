




import pandas as pd
import numpy as np
import datetime as dt
import statsmodels.api as sm
from matplotlib import pyplot
import plotly.express as px
import plotly.graph_objects as go

def fixyear(url, y, namefile):
    df = pd.read_excel(url,index_col=0, engine='openpyxl', usecols=['issue_d','int_rate','loan_amnt','grade','sub_grade','loan_status','fico_range_low','fico_range_high'])
    df['issue_d'] = df['issue_d'].map(lambda x: x.replace(year=y))
    df['issue_d'] = pd.to_datetime(df['issue_d'], format='%b-%y')
    df = df.sort_values('issue_d', ascending=True)
    df['issue_d'] = df['issue_d'].dt.strftime('%b-%y')
    df1 = df.reset_index(drop=True)
    writer = pd.ExcelWriter(namefile + '.xlsx', engine='xlsxwriter')
    df1.to_excel(writer, sheet_name='Sheet 1')
    return writer.save()
    



F_Y2019Q1 = fixyear(Y2019Q1, 2019, 'filefixed')


# In[ ]:




