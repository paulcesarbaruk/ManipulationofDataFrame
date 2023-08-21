#!/usr/bin/env python
# coding: utf-8

# # Studying manipulation of DataFrame with the libs pandas and numpy

# In[17]:


import numpy as np
import pandas as pd


# In[18]:


np.random.seed(101)


# In[19]:


df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'. split(), columns='W X Y Z'.split())


# In[20]:


df


# In[21]:


df['Z']


# In[22]:


df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'. split(), columns='W X Y Z'.split())


# In[23]:


df


# In[10]:


df['X']


# In[24]:


df = pd.DataFrame(np.random.randn(7, 6), index='A B C D E F G'. split(), columns='Q R S T U V'.split())


# In[25]:


df


# In[26]:


df['Q']


# In[22]:


type(df['Q'])


# In[27]:


type(df)


# In[28]:


df[['Q', 'S',]]


# In[29]:


#Other way of passing a column insted of a list[], we can pass dot .
df.Q


# In[30]:


# If we want to create a new column, we can use "new"
df['NEW'] = df['Q'] + df['S']


# In[31]:


df


# In[34]:


df.drop('NEW', axis=1)


# In[35]:


df.drop('Q', axis=1)


# In[36]:


df.drop('new', axis=1)


# In[38]:


# Creating a situation
# Imagine that the DataFrame that our client sent us came with duplicated columns, so how could we treat it?
df.drop('new', axis=1)


# In[39]:


df.drop('Q', axis=1)


# In[40]:


df.drop('new', axis=1, inplace=True)


# In[41]:


df


# In[42]:


df.drop('NEW', axis=1, inplace=True)


# In[43]:


df


# In[44]:


df.drop('Q', axis=1, inplace=True)


# In[45]:


df


# In[49]:


#We have to take a look a specific line, in this case we can the function df.loc, end it will bring line
df.loc['G']


# In[50]:


#Call lines and columnns specifically 
df.loc[['A', 'B'], ['T', 'U', 'V']]


# In[52]:


df.iloc[1:4,1:]


# In[ ]:




