#!/usr/bin/env python
# coding: utf-8

# In[1]:


import phoebe
import numpy as np

b = phoebe.default_binary()
b.add_dataset('lc', times=np.linspace(0,1,11), fluxes=np.ones(11), sigmas=np.ones(11))

b.add_compute('phoebe', compute='compute2')


# In[2]:


b.add_solver('optimizer.differential_corrections', fit_parameters=['incl@binary'], compute='compute2')


# In[3]:


b.run_solver()


# In[ ]:




