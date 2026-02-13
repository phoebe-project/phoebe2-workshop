#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Computing in Time or Phase
# 
# This tutorial covers the concepts of time and phase, and transforming between the two quantities.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Advanced: Compute Times & Phases](http://phoebe-project.org/docs/2.4/tutorials/compute_times_phases.ipynb)
# * [Apsidal motion (dperdt, period vs period_anom)](http://phoebe-project.org/docs/2.4/tutorials/apsidal_motion)

# # Setup
# 
# We start with the usual imports, defining the logging level, and instantiating a default binary star bundle.

# In[1]:


import phoebe
from phoebe import u, c
logger = phoebe.logger(clevel='WARNING')
b = phoebe.default_binary()


# # Reference time

# You may have noticed while adding datasets that PHOEBE works entirely in time space. This is done to allow proper parametrization of time-dependent quantities in the system but can cause difficulties if our data are given in phase-space or if we wanted to inspect a phased light curve. For this reason, PHOEBE provides several methods to help translate between the time space and phase space.
# 
# Converting between time and phase depends on a few parameters:
# 
# * `period` (orbital period of the binary at time `t0`)
# * `dpdt` (change in orbital period in time)
# * `t0` (reference time-point)
# 
# The value of `t0` can follow several conventions, all of which are defined in the bundle:
# 
# * `t0_supconj`: time of superior conjunction
# * `t0_perpass`: time of periastron passage
# * `t0_ref`: time of the reference point w.r.t. the sky (useful for apsidal motion)
# 
# The `t0_supconj`, `t0_perpass`, and `t0_ref` parameters are defined at the orbit level rather than system level.  By default, `t0_supconj` is the free parameter, with `t0_perpass` and `t0_ref` being constrained:

# In[7]:


print(b.filter(qualifier='t0*'))


# For eclipsing systems, `t0_supconj` is the handy choice because the ephemerides typically provide the time of deepest minimum as the reference point, i.e. the time of superior conjunction. For non-eclipsing systems, most frequently in astrometric solutions, orbital elements provide the periastron passage time as the reference point, so in those cases we would benefit from `t0_perpass` being independent and `t0_supconj` to be constrained. Finally, for systems with eccentric orbits and apsidal motion (`dperdt` != 0), `t0_ref` defines the reference point with respect to a fixed point in the sky rather than the orbit.
# 
# Note that, when `dperdt` != 0, the role of the orbital period also becomes ambiguous: one full revolution w.r.t. orbit (the sidereal period) is different from one full revolution w.r.t. the background stars (the anomalistic period). In particular, when `dperdt`==0:

# In[8]:


print(b.filter(qualifier='period*'))


# Here we see that there is only one period, _sidereal_; but if we introduce apsidal motion:

# In[15]:


b.set_value(qualifier='dperdt', component='binary', value=(1, 'deg/day'))
print(b.filter(qualifier='period*'))


# Now the distinction between the sidereal and anomalistic orbital periods is important and the anomalistic period, `period_anom`, is now an exposed parameter. By default it is constrained, and the sidereal period is used as a free parameter.

# # Phase-folding
# 
# For demonstration purposes let us change the orbital period so that the times and phases are not identical:

# In[16]:


b.set_value(qualifier='period', component='binary', value=2.5)


# The first helper method related to times and phases is `get_ephemeris()`. We can access the current ephemeris of our system using any of the predefined `t0`s, or any custom time:

# In[17]:


b.get_ephemeris(t0='t0_supconj')


# In[18]:


b.get_ephemeris(t0='t0_perpass')


# In[19]:


b.get_ephemeris(t0=5)


# The next helper method is `to_phase()`. It transforms any time (float or list/array) to phase using any of these ephemerides:

# In[20]:


b.to_phase([0, 0.1], t0='t0_supconj')


# In[21]:


b.to_phase([0, 0.1], t0='t0_perpass')


# Finally, there is a `to_time()` method. It converts phases to times (where the returned time will be the first instance of that phase after the provided `t0`):

# In[22]:


b.to_time(0.5, t0='t0_supconj')


# In[23]:


b.to_time(0.5, t0=2455000)


# Compute Phases
# ----------------------
# 
# As we have seen in the previous tutorial, datasets have a `compute_phases` parameter, with a constraint between `compute_times` and `compute_phases`. If we wanted to compute a model in phase-space, we can achieve this by passing `compute_phases`:

# In[24]:


b.add_dataset('lc', compute_phases=phoebe.linspace(0, 1, 101), dataset='lc01')


# In[25]:


print(b.filter(qualifier=['compute_times', 'compute_phases'], context='dataset'))


# If we were to change the orbital period, that would not affect the phases:

# In[26]:


b.set_value('period', component='binary', value=3.14)


# In[27]:


print(b.filter(qualifier=['compute_times', 'compute_phases'], context='dataset'))


# Important: if your data are phase-folded, you should **not** use this to convert times and phases (and PHOEBE will raise an error as the `times` array is required if `fluxes` or `rvs` are provided). You will need to convert your phases to times (say, by using `to_time()`):

# In[17]:


phases = phoebe.linspace(0, 1, 101)
times = b.to_time(phases, t0=2459752.18750)
b.add_dataset('lc', times=times, fluxes=phoebe.linspace(1, 1, 101))


# # Exercise

# Explore the effects of `dperdt` on the anomalistic period. So far we kept our orbit circular; what happens to the times and phases if you introduce eccentricity and retain apsidal motion?

# In[ ]:





# Set the orbital period of the system to something other than 1 day and `t0_supconj` to something other than 0.0.  Then add a light curve dataset such that the times sample one orbital period with 100 points.

# In[ ]:




