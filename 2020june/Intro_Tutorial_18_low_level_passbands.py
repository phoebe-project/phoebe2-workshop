#!/usr/bin/env python
# coding: utf-8

# # Low-level passband interface

# In this short tutorial we will show you how to access low-level functions for interacting with passband tables.

# In[1]:


import phoebe
import numpy as np
import matplotlib.pyplot as plt


# Loading passband tables can be done by either providing the passband file itself (via the `load()` method), or by providing the passband name and set delimited by the colon:

# In[2]:


pb = phoebe.get_passband('Kepler:mean')


# Once the passband is loaded, we can inspect the basic structure:

# In[3]:


print(pb)


# In[4]:


pb.content


# Low-level functions exist to access the tables and interpolate the values automatically:

# In[5]:


pb.Inorm(Teff=5772., logg=4.43, abun=0.0, atm='blackbody')


# In[6]:


pb.Imu(Teff=5772., logg=4.43, abun=0.0, mu=1.0, atm='ck2004')


# In[7]:


pb.interpolate_ldcoeffs(Teff=5772., logg=4.43, abun=0.0, ldatm='ck2004', ld_func='power')


# These functions take arrays, so we could create quick plots:

# In[8]:


teffs = phoebe.arange(3500., 6001., 250)
loggs = np.ones_like(teffs)*4.43
abuns = np.zeros_like(teffs)


# In[9]:


plt.xlabel('Teff [K]')
plt.ylabel('Normal intensity [W/m^3]')
plt.plot(teffs, pb.Inorm(teffs, loggs, abuns, atm='blackbody'), 'b-', label='blackbody')
plt.plot(teffs, pb.Inorm(teffs, loggs, abuns, atm='ck2004'), 'r-', label='ck2004')
plt.legend(loc='lower right')
plt.show()


# If you are interested in the underlying structures, you can take a look at those too:

# In[10]:


pb._ck2004_axes


# In[11]:


pb._ck2004_energy_grid.shape


# In[12]:


pb._ck2004_photon_grid.shape


# In[13]:


pb._ck2004_photon_grid[:,9,3,0]


# In[14]:


plt.xlabel('Teff [K]')
plt.ylabel('Normal intensity [W/m^3]')
plt.plot(pb._ck2004_axes[0], 10**pb._ck2004_photon_grid[:,9,3,0], 'b-')
plt.show()

