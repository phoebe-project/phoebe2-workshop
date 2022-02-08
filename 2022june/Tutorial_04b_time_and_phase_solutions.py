#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial Example Solutions: Computing in Time or Phase
# 
# These are just an example of the many possible solutions to the exercises in [Workshop Tutorial: Computing in Time or Phase](./Tutorial_04b_time_and_phase.ipynb)

# In[2]:


import phoebe
b = phoebe.default_binary()


# **Find and print the constraints between the various t0s.**

# In[3]:


print(b.filter(qualifier='t0*', context='constraint'))


# **Set the orbital period of the system to something other than 1 day and `t0_supconj` to something other than 0.0.  Then add a light curve dataset such that the times sample 1-orbital period with 100 points.**

# In[4]:


b.set_value('period', component='binary', value=1.6)
b.set_value('t0_supconj', component='binary', value=0.123)


# In[5]:


b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,100))


# In[6]:


print(b.filter(qualifier='compute_*'))

