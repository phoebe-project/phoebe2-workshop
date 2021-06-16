#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial Example Solutions: Compute (Creating the Forward Model)
# 
# These are just an example of the many possible solutions to the exercises in [Workshop Tutorial: Compute (Creating the Forward Model](./Tutorial_04_compute.ipynb)

# In[1]:


import phoebe
b = phoebe.default_binary()

b.add_dataset('lc', compute_times=phoebe.linspace(0,1,51), dataset='lc01')
b.add_dataset('rv', compute_times=phoebe.linspace(0,1,21), dataset='rv01')


# # Exercise

# Add another set of compute options (called, say, 'robust') and set whatever values you think might be necessary.  Run a model and see how much longer it takes to run.

# In[2]:


b.add_compute(compute='robust')


# In[3]:


print(b.filter(compute='robust'))


# In[4]:


b.set_value('ltte', compute='robust', value=True)
b.set_value_all('ntriangles', compute='robust', value=10000)


# In[5]:


print(b.computes)


# In[6]:


b.run_compute(compute='phoebe01', model='default_options')


# In[7]:


b.run_compute(compute='robust', model='custom_options')

