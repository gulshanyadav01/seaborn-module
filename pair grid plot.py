#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import all important libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn


# In[2]:


iris=sn.load_dataset('iris')


# In[3]:


x=sn.PairGrid(iris)
x=x.map(plt.scatter)


# In[5]:


x=sn.PairGrid(iris)
x=x.map_diag(plt.hist)
x=x.map_offdiag(plt.scatter)


# In[6]:


x=sn.PairGrid(iris,hue='species')
x=x.map_diag(plt.hist)
x=x.map_offdiag(plt.scatter)


# In[9]:


# legend is missig.
x=sn.PairGrid(iris,hue='species')
x=x.map_diag(plt.hist)
x=x.map_offdiag(plt.scatter)
x=x.add_legend()


# In[10]:


x=sn.PairGrid(iris,hue='species',palette="spring")
x=x.map_diag(plt.hist)
x=x.map_offdiag(plt.scatter)
x=x.add_legend()


# In[ ]:




