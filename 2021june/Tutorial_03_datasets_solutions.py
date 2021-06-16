#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial Example Solutions: Datasets
# 
# These are just an example of the many possible solutions to the exercises in [Workshop Tutorial: Datasets](./Tutorial_03_datasets.ipynb)

# In[1]:


import phoebe
b = phoebe.default_binary()


# In[2]:


b.add_dataset('rv')


# In[3]:


b.add_dataset('lc')


# What choices are available for `rv_method`, `passband`, `pblum_mode`, `ld_mode`, and `intens_weighting` (refer back to the [first tutorial](./Tutorial_01_bundle_basics.ipynb) if you've forgotten how to check the choices)?

# In[4]:


print(b.filter(qualifier='rv_method'))


# In[5]:


print(b.get_parameter(qualifier='rv_method', component='primary').get_choices())


# In[6]:


print(b.filter(qualifier='passband'))


# In[7]:


print(b.get_parameter(qualifier='passband', dataset='lc01').choices)


# In[8]:


print(b.filter(qualifier='pblum_mode'))


# In[9]:


print(b.get_parameter(qualifier='pblum_mode').choices)


# In[10]:


print(b.filter(qualifier='ld_mode'))


# In[11]:


print(b.get_parameter(qualifier='ld_mode', component='primary', dataset='lc01').choices)


# In[12]:


print(b.filter(qualifier='intens_weighting'))


# In[13]:


print(b.get_parameter(qualifier='intens_weighting', dataset='lc01').choices)


# Let's say we had a single-lined binary system.  Set the times on the RV dataset such that only the primary star would be computed.

# In[14]:


# to do this from an existing RV dataset:

b.set_value('times', dataset='rv01', component='primary', value=phoebe.linspace(0,1,101))
b.set_value('times', dataset='rv01', component='secondary', value=[])

print(b.filter(qualifier='times', dataset='rv01'))


# In[15]:


# to do this while adding a dataset:

b.add_dataset('rv', times={'primary': phoebe.linspace(0,1,101)}, dataset='rv02')
print(b.filter(qualifier='times', dataset='rv02'))


# In[16]:


# or

b.add_dataset('rv', times=phoebe.linspace(0,1,101), component='primary', dataset='rv03')
print(b.filter(qualifier='times', dataset='rv03'))


# Add another RV dataset.  Set the new RV dataset to have `rv_method='dynamical'` while keeping the original 'rv01' dataset with `rv_method='flux-weighted'`.  (You'll notice there is a parameter per-component - you'll either need to set both manually or use [set_value_all](http://phoebe-project.org/docs/latest/api/phoebe.parameters.ParameterSet.set_value_all.md))

# In[17]:


print(b.filter(qualifier='rv_method'))


# In[18]:


print(b.filter(qualifier='rv_method', dataset=['rv01', 'rv02']))


# In[19]:


b.set_value_all(qualifier='rv_method', dataset=['rv01', 'rv02'], value='dynamical')


# In[20]:


print(b.filter(qualifier='rv_method'))

