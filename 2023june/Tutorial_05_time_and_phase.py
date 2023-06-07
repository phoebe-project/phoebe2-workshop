#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Computing in Time or Phase
# 
# This tutorial covers the concepts of time and phase, and transforming between the two quantities.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Advanced: Compute Times & Phases](http://phoebe-project.org/docs/2.4/tutorials/compute_times_phases.ipynb)
# 

# # Setup
# 
# We start with the usual imports, defining the logging level, and instantiating a default binary star bundle.

# In[1]:


import phoebe
from phoebe import u, c
logger = phoebe.logger(clevel='WARNING')
b = phoebe.default_binary()


# # Times and phases

# You may have noticed while adding datasets that PHOEBE works entirely in time space. This is done to allow proper parametrization of time-dependent quantities in the system but can cause difficulties if our data are given in phase-space or if we wanted to inspect a phased light curve. For this reason, PHOEBE provides several methods to help translate between the time space and phase space.
# 
# Converting between time and phase depends on a few parameters:
# 
# * `period` (orbital period of the binary at time `t0`)
# * `dpdt` (change in orbital period in time)
# * `t0` (reference time-point)
# 
# The value of `t0` could follow several conventions, all of which are defined in the bundle:
# 
# * `t0_supconj`: time of superior conjunction
# * `t0_perpass`: time of periastron passage
# * `t0_ref`: time of the reference point w.r.t. apsidal motion
# 
# The `t0_supconj`, `t0_perpass`, and `t0_ref` parameters are defined for the orbit (so `context='component', component='binary'` for our default binary).  By default, `t0_supconj` is the free parameter, with `t0_perpass` and `t0_ref` being constrained by a other parameters. We will look at changing that in an upcoming tutorial.

# In[2]:


b.get_parameter(qualifier='t0_supconj', context='component')


# In[3]:


b.get_parameter(qualifier='t0_perpass', context='component')


# In[4]:


b.get_parameter(qualifier='t0_ref', context='component')


# For demonstration purposes let us change the orbital period so that the times and phases are not identical:

# In[5]:


b.set_value(qualifier='period', component='binary', value=2.5)


# The first helper method related to times and phases is `get_ephemeris()`. We can access the current ephemeris of our system using any of the predefined `t0`s, or any custom time:

# In[6]:


b.get_ephemeris(t0='t0_supconj')


# In[7]:


b.get_ephemeris(t0='t0_perpass')


# In[8]:


b.get_ephemeris(t0=5)


# The next helper method is `to_phase()`. It transforms any time (float or list/array) to phase using any of these ephemerides:

# In[9]:


b.to_phase([0, 0.1], t0='t0_supconj')


# In[10]:


b.to_phase([0, 0.1], t0='t0_perpass')


# Finally, there is a `to_time()` method. It converts phases to times (where the returned time will be the first instance of that phase after the provided `t0`):

# In[11]:


b.to_time(0.5, t0='t0_supconj')


# In[12]:


b.to_time(0.5, t0=2455000)


# Compute Phases
# ----------------------
# 
# As we have seen in the previous tutorial, datasets have a `compute_phases` parameter, with a constraint between `compute_times` and `compute_phases`. If we wanted to compute a model in phase-space, we can achieve this by passing `compute_phases`:

# In[13]:


b.add_dataset('lc', compute_phases=phoebe.linspace(0, 1, 101), dataset='lc01')


# In[14]:


print(b.filter(qualifier=['compute_times', 'compute_phases'], context='dataset'))


# In[15]:


b.set_value('period', component='binary', value=3.14)


# In[16]:


print(b.filter(qualifier=['compute_times', 'compute_phases'], context='dataset'))


# Important: if your data are in phases, you should **not** use this to convert times and phases (and PHOEBE will raise an error as the `times` array is required if `fluxes` or `rvs` are provided). You will need to convert your phases to times (i.e., `to_time()`) using whatever information you have on the ephemeris that was used originally for the dataset:

# In[17]:


phases = phoebe.linspace(0, 1, 101)
times = b.to_time(phases, t0=2459752.18750)
b.add_dataset('lc', times=times, fluxes=phoebe.linspace(1, 1, 101))


# # Exercise

# Find and print the constraints between the various t0s.

# In[ ]:





# Set the orbital period of the system to something other than 1 day and `t0_supconj` to something other than 0.0.  Then add a light curve dataset such that the times sample one orbital period with 100 points.

# In[ ]:




