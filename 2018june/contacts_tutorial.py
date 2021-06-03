#!/usr/bin/env python
# coding: utf-8

# In[1]:


import phoebe
from phoebe import u,c

import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='WARNING')


# A contact binary Bundle is created by passing contact_binary=True to the default binary bundle.

# In[2]:


cb = phoebe.default_binary(contact_binary = True)


# The main difference between the detached and contact binary Bundles comes in the hierarchy of the system. In addition to the two star components, contact binaries have an envelope component as well.

# In[3]:


print cb.hierarchy


# The envelope component stores parameters that pertain to the overall system and are in principle shared by the two stars or equal.

# In[4]:


print cb.filter(component='contact_envelope', kind='envelope', context='component')


# The star components hold parameters that can still be attributed to the indivudal stars in the contact binary:

# In[5]:


print cb.filter(component='primary', kind = 'star', context='component')


# In[6]:


cb.add_dataset('mesh', times=[0.25], dataset='mesh01')


# In[7]:


cb.add_dataset('lc', times=np.linspace(0.,1.,50), dataset='lc01')


# In[8]:


cb.run_compute()


# In[9]:


cb.plot('mesh01', facecolor='teffs')


# In[10]:


cb.plot('lc01')


# In[11]:


cb['teff@primary'] = 8000.


# In[12]:


cb.run_compute()


# In[13]:


cb.plot('mesh01', facecolor='teffs')


# In[14]:


cb.plot('lc01')


# In[15]:


def pot_to_ff(cb):
    crit_pots = cb.compute_critical_pots('contact_envelope')
    L1, L2 = crit_pots['L1'], np.max((crit_pots['L2'], crit_pots['L3']))
    return (cb['pot@contact_envelope'] - L1)/(L2-L1)


# In[16]:


def ff_to_pot(cb, FF):
    crit_pots = cb.compute_critical_pots('contact_envelope')
    L1, L2 = crit_pots['L1'], np.max((crit_pots['L2'], crit_pots['L3']))
    return L1 + FF*(L2-L1)


# In[17]:


ff = 0.08
q = 0.2
cb['q'] = q
cb['pot@contact_envelope@component'] = ff_to_pot(cb, ff)


# In[18]:


cb.run_compute()


# In[19]:


cb.plot('mesh01')


# ### Exercises

# 1. Find the lowest (to +/- 0.05) value of the fillout parameter that produces a reasonable mesh for the above system.

# 2. Plot the surface temperatures of the contact envelope as a function of the mesh $x$ coordinates.

# In[ ]:




