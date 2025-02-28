#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[5]:


df = pd.read_csv('/Users/gowtham/Downloads/archive/TWO_CENTURIES_OF_UM_RACES.csv')


# In[7]:


df.head(10)


# In[9]:


df.describe()


# In[21]:


df.isnull().sum()


# In[13]:


df.dtypes


# In[39]:


#clean up data
#looking for USA Races, 50K or 50Mi, 2020


# In[ ]:


# Step-1 
# fatch the records with min of 50K or 50mi and country = USA


# In[31]:


df['country'] = df['Event name'].str.extract(r'\((\w+)\)')


# In[35]:


df2 = df[(df['Event distance/length'].isin(['50mi','50km'])) & (df['Year of event']==2020) & (df['country'] == 'USA')]


# In[37]:


df2


# In[39]:


df2.head(10)


# In[41]:


df2.shape


# In[45]:


df2['Event name'] = df2['Event name'].str.split('(').str.get(0)
df2.head()


# In[ ]:


#clean up Athlete age


# In[47]:


df2['Athlete_age'] = 2020 - df2['Athlete year of birth']


# In[49]:


df2.head()


# In[ ]:


# remove 'h' from athlete Preformance


# In[51]:


df2['Athlete performance'] = df2['Athlete performance'].str.split(' ').str.get(0)
df2.head()


# In[ ]:


## drop coloumns: Athletes club , Athlete Country, Athelete year of birth, Athelete Age Category


# In[55]:


df2 = df2.drop(['Athlete club','Athlete country','Athlete year of birth','Athlete age category'],axis =1)
df2.head()


# In[ ]:


#clean up null values


# In[57]:


df2.isnull().sum()


# In[59]:


df2['Athlete_age'].isnull()


# In[61]:


df2[df2['Athlete_age'].isnull()]


# In[63]:


df2=df2.dropna()


# In[65]:


df2.isnull().sum()


# In[ ]:


#check for duplicated


# In[67]:


df2[df2.duplicated()]


# In[ ]:


#reset index


# In[71]:


df2.reset_index(drop = True)


# In[ ]:


#set types


# In[77]:


df2.dtypes


# In[83]:


df2['Athlete_age'] = df2['Athlete_age'].astype(int)
df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)
df2.dtypes
df2.head()


# In[ ]:


#rename Coloumns


# In[97]:


df2 = df2.rename(columns = {'Year of event':'year','Event dates':'race_day','Event name':'race_name','Event distance/length':'race_length',
                            'Event number of finishers':'race_number_of_finishers','Athlete performance':'athlete_performance',
                            'Athlete gender':'athlete_gender','Athlete average speed':'athlete_average_speed','Athlete ID':'athlete_id','Athlete_age':'athlete_age'})


# In[99]:


df2.head()


# In[ ]:


#reorder Columns


# In[101]:


df2.dtypes


# In[103]:


df3 = df2[['race_day','race_name','race_length','race_number_of_finishers','athlete_id','athlete_gender','athlete_average_speed','athlete_age','athlete_performance','country','year']]


# In[105]:


df3.head()


# In[109]:


df3[df3['race_name'] == 'Everglades 50 Mile Ultra Run ']


# In[111]:


#222509
df3[df3['athlete_id']== 222509]


# In[115]:


sns.histplot(df3['race_length'])


# In[125]:


sns.histplot(df3,x = 'race_length',hue = 'athlete_gender')


# In[127]:


sns.displot(df3[df3['race_length']=='50mi']['athlete_average_speed'])


# In[141]:


sns.histplot(df3,x='race_length',bins= 5, kde=True,hue='athlete_gender')


# In[145]:


sns.violinplot(data = df3,x='race_length',y='athlete_average_speed',hue = 'athlete_gender',split = True)


# In[153]:


sns.lmplot(data=df3,x ='athlete_age',y='athlete_average_speed',hue = 'athlete_gender')


# In[ ]:


#question to find from data


# In[ ]:


# difference in speed in 50km,50mi in male and female


# In[157]:


df3.groupby(['race_length','athlete_gender'])['athlete_average_speed'].mean()


# In[165]:


result = df3.groupby(['race_length','athlete_gender'])['athlete_average_speed'].mean().reset_index()
sns.barplot(data =result ,x= 'race_length',y = 'athlete_average_speed',hue = 'athlete_gender')


# In[ ]:


#what age groups are best at 50 mi race (atleast 20+ races)


# In[177]:


#filtering the rows with only 50 mi
#step - 1
df_filter = df3[df3['race_length']== '50mi']
df_filter


# In[189]:


#Count the Number of Races for Each Age Group
age_counts = df_filter.groupby(['athlete_age'])['race_number_of_finishers'].count()
age_counts


# In[213]:


df_filter.groupby(['athlete_age'])['race_number_of_finishers'].count()


# In[ ]:





# In[ ]:





# In[223]:


#Age Groups That Have Raced at Least 20 Times

df_50mi_filtered = df_filter[df_filter['athlete_age'].isin(age_counts[age_counts >= 20].index)]
df_50mi_filtered


# In[195]:


#average speed for each remaining age group
best_age_groups = df_50mi_filtered.groupby('athlete_age')['athlete_average_speed'].mean().reset_index()
best_age_groups


# In[197]:


#Age Groups from Fastest to Slowest

best_age_groups = best_age_groups.sort_values(by='athlete_average_speed', ascending=False)
best_age_groups


# In[205]:


sns.barplot(data = best_age_groups, x= 'athlete_age',y = 'athlete_average_speed')


# In[229]:


get_ipython().system('jupyter nbconvert --to script Pandas_Project.ipynb')


# In[233]:


import os
print(os.listdir())  # Lists all files in the current folder



# In[ ]:




