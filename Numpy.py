#!/usr/bin/env python
# coding: utf-8

# In[126]:


import numpy as np


# In[127]:


np.array([3,3,4])


# In[128]:


b=np.array([[5,3,4],[7,5,3]])


# In[129]:


b


# In[130]:


b.shape


# In[131]:


b.dtype


# In[132]:


b.ndim


# In[133]:


type(b)


# In[134]:


np.arange(100)


# In[135]:


c=range(10000)


# In[136]:


get_ipython().run_line_magic('timeit', '[i**3 for i in c]')


# In[137]:


d=np.arange(10000)


# In[138]:


get_ipython().run_line_magic('timeit', '[i**3 for i in d]')


# In[139]:


np.ones((2,3))


# In[140]:


np.zeros((2,3))


# In[141]:


np.eye(3)


# In[142]:


np.full((3,3),2)


# In[143]:


np.full((3,3),2.2,dtype=int)


# In[144]:


np.diag((3,4,5,2))


# In[145]:


v=np.array([4,5,3])


# In[146]:


np.tile(v,(3,2))


# In[147]:


np.random.random()   # 0 to 1


# In[148]:


np.random.random() * 50   # 0 to 50


# In[149]:


2+np.random.random() * 50  # from 2


# In[150]:


np.random.random([3,4])


# In[151]:


a=np.linspace(1,50,10)


# In[152]:


a


# In[153]:


a.itemsize  # it took 8 bytes of size


# In[154]:


np.arange(9).reshape(3,3)


# In[155]:


a=np.arange(1,11)
a[4]


# In[156]:


a[:]


# In[157]:


a[3:]


# In[158]:


a[3:4]


# In[159]:


a[0::2]  # it will jump (skip 1)


# In[160]:


s=np.matrix([[2,3,4],[7,3,6],[8,9,9]])


# In[161]:


s


# In[162]:


s[1,2]


# In[163]:


s>3


# In[164]:


s[(s>2) & (s<5)]


# In[165]:


b=a


# In[166]:


print(b)


# In[167]:


print(a)


# In[168]:


b[0]=3


# In[169]:


b


# In[170]:


a                      # it is pointing to same location .so it if we change 1 then automatically other also will be changed


# In[171]:


np.shares_memory(a,b)


# In[172]:


b=a.copy()


# In[173]:


b


# In[174]:


a


# In[175]:


b[0]=55


# In[176]:


b


# In[177]:


a


# In[178]:


np.shares_memory(a,b)


# In[179]:


a=np.array([[2,3,4],[2,3,4]])


# In[180]:


a


# In[181]:


a.T


# In[182]:


b=np.array([[2,5,3],[3,5,3]])


# In[183]:


a==b


# In[184]:


a


# In[185]:


b


# In[186]:


np.vstack((a,b))


# In[187]:


np.hstack((a,b))


# In[188]:


np.sin(b)


# In[189]:


np.sum(b)


# In[190]:


np.exp(b)


# In[191]:


np.median(b)


# In[192]:


np.mean(b)


# In[193]:


np.std(b)


# In[194]:


c=np.array([[2,3],[9,9]])


# In[195]:


np.linalg.det(c)


# In[196]:


np.linalg.inv(c)


# In[197]:


np.linalg.eig(c)


# In[198]:


a=np.array([[1,1,0],[1,1,1]])


# In[199]:


b=np.array([[1,1,0],[0,0,0]])


# In[200]:


np.logical_and(a,b)


# In[201]:


np.logical_or(a,b)


# In[202]:


a=np.array([[2,3],[4,3]])


# In[203]:


a.sum()


# In[204]:


a.sum(axis=0)


# In[205]:


sum(a)


# In[206]:


a.sum(axis=1)


# In[207]:


a.max()


# In[208]:


a.shape


# In[209]:


np.sort(a)


# In[ ]:




