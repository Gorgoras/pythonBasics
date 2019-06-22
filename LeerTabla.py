#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pyodbc
import pandas as pd
import inspect


# In[38]:


conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:vaults.database.windows.net,1433;Database=sourcedb;Uid=fallout@vaults;Pwd=Google2008;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')


# In[39]:


query = 'SELECT top 100 * FROM SalesLT.Customer'

df = pd.read_sql(query, conn)


# In[40]:


df.to_csv(path_or_buf='unificado.csv', sep='|', header=True, index=True, index_label='Indice')


# In[ ]:




