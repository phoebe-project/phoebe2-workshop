#!/usr/bin/env python
# coding: utf-8

# # Minimal example of a Caleb dataset - RT And(B) a detached system
# Exercise Exercises_02_forward_models #2
# we could set more parameters, we jsut set what we need.  We also ignore the spots
# but we run the forward model here

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np


# In[2]:


logger = phoebe.logger(clevel='INFO')
Period = 0.6289294 #days
MASS_RATIO = 0.740000
TEMPERATURE_1 = 6150.000000 #K
TEMPERATURE_2 = 4920.000000 #K
INCLINATION = 82.00000 #deg
ECCENTRICITY = 0.0
OMEGA_1 = 3.918202
OMEGA_2 = 3.898896
ROTATION_F1 = 1
ROTATION_F2 = 1


# from Caleb radial velocity data for this system we have K1 and K2 and can determin that the sma of the binary is 3.8671 SolRad

# In[3]:


sma = 3.8671


# In[4]:


b = phoebe.Bundle.default_binary()


# In[5]:


d = 1 - ECCENTRICITY
requiv_1Dist = phoebe.distortions.roche.pot_to_requiv(OMEGA_1, sma, MASS_RATIO, ROTATION_F1, d, component=1)
requiv_2Dist = phoebe.distortions.roche.pot_to_requiv(OMEGA_2, sma, MASS_RATIO, ROTATION_F2, d, component=2)
b.set_value('requiv@primary', requiv_1Dist)
b.set_value('requiv@secondary', requiv_2Dist)


# In[6]:


b.set_value('incl@orbit', INCLINATION)
b.set_value('period@binary', Period)
b.set_value('q@binary@component',MASS_RATIO)
b.set_value('teff@primary', TEMPERATURE_1)
b.set_value('teff@secondary', TEMPERATURE_2)
b.set_value('ecc@binary@orbit', ECCENTRICITY )
b.set_value('sma@binary', sma )


# Just to see how close r_back*sma is to requiv

# In[7]:


b.get_value('requiv@primary')


# In[8]:


b.get_value('requiv@secondary')


# In[9]:


b.add_dataset('lc', compute_times=phoebe.linspace(0,10,101), dataset='lc01')
b.add_dataset('rv', compute_times=phoebe.linspace(0,10,101), dataset='rv01')


# In[10]:


b.run_compute()


# In[11]:


requiv_1Dist


# In[12]:


_ = b.plot(show=True)


# In[13]:


_ = b.plot(x = 'phase', show=True)


# In[ ]:




