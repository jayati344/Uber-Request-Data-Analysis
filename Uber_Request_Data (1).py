#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("Uber Request Data.csv")


# In[4]:


df.head


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df["Request timestamp"].value_counts()


# In[9]:


df["Request timestamp"]=df["Request timestamp"].astype(str)
df["Request timestamp"] = df["Request timestamp"].str.replace("/", "-", regex=False)
df["Request timestamp"] = pd.to_datetime(df["Request timestamp"], dayfirst=True, errors='coerce')
df.info()


# In[11]:


df["Drop timestamp"] = pd.to_datetime(df["Drop timestamp"], dayfirst=True, errors='coerce')
df.info()


# In[12]:


df["Drop timestamp"]


# In[14]:


req_hour=df["Request timestamp"].dt.hour
len(req_hour)
df["req_hour"]=req_hour
req_day=df["Request timestamp"].dt.day
df["req_day"]=req_day


# In[16]:


sns.countplot(x="req_hour",data=df,hue="Status")
plt.show()


# In[17]:


sns.catplot(x="req_hour",data=df,row="req_day",hue="Status",kind="count")
plt.show()


# In[18]:


sns.catplot(x="req_hour",data=df,row="req_day",hue="Pickup point",kind="count")
plt.show()


# In[19]:


sns.catplot(x="req_hour",data=df,hue="Pickup point",kind="count")
plt.show()


# In[20]:


df["Time_Slot"]=0
df


# In[22]:


j=0
for i in df["req_hour"]:
    if df.iloc[j,6]<5:
        df.iloc[j,8]="Pre_Morning"
    elif 5<=df.iloc[j,6]<10:
        df.iloc[j,8]="Morning_Rush"
        
    elif 10<=df.iloc[j,6]<17:
        df.iloc[j,8]="Day_Time"
        
    elif 17<=df.iloc[j,6]<22:
        df.iloc[j,8]="Evening_Rush"
    else:
        df.iloc[j,8]="Late_Night"
    j=j+1


# In[23]:


def get_time_period(x):
    if x < 5:
        return "Pre_morning"
    elif 5 <= x < 10:
        return "Morning Rush"
    elif 10 <= x < 17:
        return "Day_time"
    elif 17 <= x < 22:
        return "Evening rush"
    else:
        return "Late night"
df


# In[25]:


df["Time_Slot"].value_counts()


# In[26]:


plt.figure(figsize=(10,6))
sns.countplot(x="Time_Slot",hue="Status",data=df)
plt.show()


# In[27]:


df_morning_rush=df[df['Time_Slot']=='Morning_Rush']
sns.countplot(x="Pickup point",hue="Status",data=df_morning_rush)


# In[28]:


df_airport_cancelled=df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport") & (df_morning_rush["Status"]=="Cancelled")]
df_airport_cancelled.shape[0]


# In[29]:


df_city_cancelled=df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City") & (df_morning_rush["Status"]=="Cancelled")]
df_city_cancelled.shape[0]


# In[30]:


df_morning_rush


# In[32]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City")].shape[0]


# In[33]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City") & (df_morning_rush["Status"]=="Trip Completed")].shape[0]


# In[34]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport")].shape[0]


# In[35]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport") & (df_morning_rush["Status"]=="Trip Completed")].shape[0]


# In[37]:


df_evening_rush=df[df['Time_Slot']=='Evening_Rush']
df_city_cancelled=df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City") & (df_evening_rush["Status"]=="Cancelled")]
sns.countplot(x="Pickup point",hue="Status",data=df_evening_rush)


# In[38]:


df_city_cancelled.shape[0]


# In[39]:


df_evening_rush["Status"].value_counts()


# In[40]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City") & (df_evening_rush["Status"]=="Trip Completed")].shape[0]


# In[41]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="Airport") & (df_evening_rush["Status"]=="Trip Completed")].shape[0]


# In[42]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="Airport") & (df_evening_rush["Status"]=="Cancelled")].shape[0]


# In[43]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City") & (df_evening_rush["Status"]=="Cancelled")].shape[0]


# In[ ]:




