#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial Example Solutions: Flux Scaling
# 
# These are just an example of the many possible solutions to the exercises in [Workshop Tutorial: Flux Scaling](./Tutorial_09_pblum_l3_distance.ipynb)

# In[1]:


import phoebe
import numpy as np


# **NOTE**: this tutorial is a bit of a tangent and will not be used directly in the following tutorials, so don't feel that it is necessary to complete all the exercises below. For any that do seem interesting to you, you may need to dig a little deeper into the explanations in the linked online docs for details about how each option works and feel free to ask questions!
# 
# 
# **Make a plot of multiple light curves in different passbands.  Have one passband be set so that the out-of-eclipse flux is approximately one (using `pblum_mode='component-coupled'` and manually adjusting `pblum` and calling `run_compute` or `compute_pblums(pbflux=True)`) and the other light curves all coupled relative to that (using `'dataset-coupled'` and setting the `pblum_dataset` parameter).  Try naming the datasets appropriately and include labels on the plot.**

# In[2]:


b = phoebe.default_binary()
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101), passband='Johnson:V', dataset='lcV')
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101), passband='Johnson:B', dataset='lcB')


# In[3]:


print(b.filter(qualifier='pblum*', dataset='lcV'))


# In[4]:


print(b.compute_pblums(dataset='lcV', pbflux=True))


# In[5]:


b.set_value('pblum', component='primary', dataset='lcV', value=2*np.pi)


# In[6]:


print(b.compute_pblums(dataset='lcV', pbflux=True))


# In[7]:


print(b.filter(qualifier='pblum*', dataset='lcB'))


# In[8]:


b.set_value('pblum_mode', dataset='lcB', value='dataset-coupled')


# In[9]:


print(b.filter(qualifier='pblum*', dataset='lcB'))


# In[10]:


b.run_compute()


# In[11]:


_ = b.plot(show=True, legend=True)


# **Set `pblum_mode` to `'component-coupled'` or `'absolute'` and show how third light (either in flux or fractional units) affects a light curve and the luminosities.**  (**NOTE**: `pbflux=True` is _intrinsic_ only and so does not account for third light)**

# In[12]:


b = phoebe.default_binary()
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101), pblum_mode='absolute')


# In[13]:


print(b.compute_pblums(pbflux=True))


# In[14]:


b.run_compute(model='l3off')


# In[15]:


print(b.filter(qualifier='l3*'))


# In[16]:


b.set_value('l3', 1e24)


# In[18]:


b.run_compute(model='l3_flux')


# In[19]:


_ = b.plot(show=True, legend=True)


# In[20]:


print(b.get_parameter('l3_mode').choices)


# In[21]:


b.set_value('l3_mode', 'fraction')


# In[22]:


print(b.filter(qualifier='l3*'))


# In[23]:


b.set_value('l3_frac', 0.1)


# In[25]:


b.run_compute(model='l3_fraction')


# In[26]:


_ = b.plot(show=True, legend=True)


# **Do the same for `distance` as you just did for third light: set `pblum_mode` to `'component-coupled'` or `'absolute'` and show how changing the distance affects the flux-levels in a light curve.** (**NOTE**: `pbflux=True` is _intrinsic_ only and so does not account for distance)

# In[27]:


b = phoebe.default_binary()

b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101))


# In[28]:


print(b.filter(qualifier='distance'))


# In[30]:


b.run_compute(model='original')


# In[31]:


b.set_value('distance', value=2)


# In[33]:


b.run_compute(model='distance_halved')


# In[34]:


_ = b.plot(show=True, legend=True)


# **Combine non-zero `l3` and non-unity `distance` and see how the output from `compute_pblums` changes.**

# In[ ]:




