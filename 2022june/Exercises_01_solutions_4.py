#!/usr/bin/env python
# coding: utf-8

# # \#4: Reproduce Binaries from the CALEB Catalog Example Solution

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


# from Caleb radial velocity data we have K1 and K2 and can determin that the sma of the binary is 3.8671 SolRad

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


# Just to see how close r_back*sma is to requiv

# In[7]:


b.get_value('requiv@primary')


# In[8]:


b.get_value('requiv@secondary')


# In[ ]:




