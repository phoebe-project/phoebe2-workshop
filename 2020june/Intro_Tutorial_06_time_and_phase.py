#!/usr/bin/env python
# coding: utf-8

# In this tutorial, we'll learn about manually translating between time- and phase-space.

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# # Times and Phase

# As you may have noticed while adding datasets, PHOEBE 2 works entirely in time (not phase) space.  This has its advantages (allowing time-dependent changes to the system) but can be a bit of a pain if you have old data stored only in phase-space or if you want to add a synthetic dataset covering a full orbital period, but don't remember the exact period of your system.  For this reason, we provide a few useful ways to help translate between the time-space used within PHOEBE and phase.
# 
# Converting between time and phase depends on a few parameters
# * orbital period
# * dpdt (change in orbital period in time)
# * t0
# 
# The value of t0 could be interpreted from several different standards, all of which are defined in the Bundle:
# * t0_supconj: time of superior conjunction
# * t0_perpass: time of periastron passage
# * t0_ref: time of the "reference point" (to adopt the usage in PHOEBE legacy)
# 
# t0_supconj, t0_perpass, and t0_ref are all defined within the orbit (so context='component', component='binary' for our default binary).  By default, t0_supconj is the free Parameter, with t0_perpass and t0_ref being constrained by a multiple other parameters.

# In[4]:


b.get_parameter(qualifier='t0_supconj', context='component')


# In[5]:


b.get_parameter(qualifier='t0_perpass', context='component')


# In[6]:


b.get_parameter(qualifier='t0_ref', context='component')


# We can access the current ephemeris of our system using any of these t0s or a custom-time.

# In[7]:


b.get_ephemeris(t0='t0_supconj')


# In[8]:


b.get_ephemeris(t0='t0_perpass')


# In[9]:


b.get_ephemeris(t0=5)


# Similarly, we can transform any time (float or list/array) to phase using any of these ephemerides

# In[10]:


b.to_phase([0,0.1], t0='t0_supconj')


# In[11]:


b.to_phase([0,0.1], t0='t0_perpass')


# We can also translate from phase to time (where the returned time will be the first instance of that phase after the provided t0)

# In[12]:


b.to_time(0.5, t0='t0_supconj')


# In[13]:


b.to_time(0.5, t0=2455000)


# Compute Phases
# ----------------------
# 
# As mentioned in the previous tutorial, datasets also have a 'compute_phases' parameter, with a constraint between 'compute_times' and 'compute_phases'.  If you'd like to compute your model evenly in phase-space, this can be used *instead* of 'compute_times'... but note that the phase-to-time translation is not nearly as "complete" as to_time or to_phase.
# 
# If you have observational data in phases, you should **not** use this to convert.  Rather you should convert your observational data to times using the best information you have on the ephemeris that was originally used on the dataset to convert to phases.

# In[14]:


b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101), dataset='lc01')


# In[17]:


print(b.filter(qualifier=['compute_times', 'compute_phases'], context='dataset'))


# In[18]:


b.set_value('period', component='binary', value=3.14)


# In[19]:


print(b.filter(qualifier=['compute_times', 'compute_phases'], context='dataset'))


# # Exercise

# Find and print the constraints between the various t0s.

# In[ ]:





# Change the orbital period of the system to something other than 1 day and t0_supconj to something other than 0.0.  Then add a light curve dataset such that the times sample 1-orbital period with 100 points.

# In[ ]:





# compute_phases and compute_times are related through a constraint... how is this constraint less complex than to_time/to_phase?

# In[ ]:




