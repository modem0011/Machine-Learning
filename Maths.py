#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a=np.array([2,3,4])


# In[3]:


b=np.array([4,5,6])


# In[4]:


print(np.dot(a,b))


# In[5]:


x=np.matrix([[3,4,5],[3,5,6],[2,8,6]])


# In[6]:


y=np.matrix([[3,5,6],[3,5,6],[3,5,6]])


# In[7]:


x*y


# In[8]:


x+y


# In[9]:


x=np.matrix([[3,4,5],[3,5,6],[2,8,6]])


# In[10]:


from numpy import linalg as la


# In[11]:


la.matrix_rank(x)


# In[ ]:




