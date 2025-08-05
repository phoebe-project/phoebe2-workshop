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
logger = phoebe.logger(clevel='WARNING')
b = phoebe.default_binary()


# # Reference time and ephemeral times

# You may have noticed while adding datasets that PHOEBE works entirely in time space. This is done to allow proper parametrization of time-dependent quantities in the system but can cause difficulties if our data are given in phase-space or if we wanted to inspect a phased light curve. For this reason, PHOEBE provides several methods to help translate between the time space and phase space.
# 
# There is an important distinction that we need to make when considering reference times. One reference time pertains to parameter values: it is the specific point in time at which all parameters assume a given face value. Non-time-varying parameters of course retain their value for all times, but time-varying parameters, such as P or ω, change according to their rates of change, dP/dt or dω/dt, *from reference time*. PHOEBE refers to this time as the **systemic reference time** or simply **reference time**.
# 
# On the other hand, we need to associate a position of a celestial body in its orbit with a reference time. This time is related with the orbit and, depending on the convention, we can provide the time of superior conjunction, periastron passage, or any other referential point. PHOEBE refers to these times as **ephemeral times**.
# 
# The defined ephemeral times are:
# 
# * `t0_supconj`: time of superior conjunction
# * `t0_perpass`: time of periastron passage
# * `t0_ref`: time of the reference point w.r.t. the sky (useful when a system exhibits apsidal motion)
# 
# Unlike `t0`, the `t0_supconj`, `t0_perpass`, and `t0_ref` are all *orbital* parameters rather than system parameters, one per each orbit in a multi-body system. By default, `t0_supconj` is the free parameter, with `t0_perpass` and `t0_ref` being constrained.
# 
# In addition to ephemeral times, PHOEBE uses the following parameters that determine data phasing:
# 
# * `period` (orbital period of the binary at reference time)
# * `dpdt` (temporal change in orbital period, in days/day, w.r.t. reference time)

# In[2]:


print(b.filter(qualifier='t0*'))


# For eclipsing systems, `t0_supconj` is the typical choice because the ephemerides provide the time of primary minimum as the reference point, i.e. the time of superior conjunction. For non-eclipsing systems, most frequently in astrometric solutions, orbital elements provide the periastron passage time as the reference point, so in those cases we would benefit from `t0_perpass` being independent and `t0_supconj` to be constrained. Finally, for systems with eccentric orbits and apsidal motion (`dperdt` != 0), `t0_ref` defines the reference point with respect to a fixed point in the sky (for example, due east or due north) rather than the orbit.
# 
# Note that, when `dperdt` != 0, the role of the orbital period also becomes ambiguous: one full revolution w.r.t. the orbit (the sidereal period) is different from one full revolution w.r.t. the background stars (the anomalistic period). In particular, when `dperdt`=0:

# In[3]:


print(b.filter(qualifier='period*'))


# Here we see that there is only one period, _sidereal_; but if we introduce apsidal motion:

# In[4]:


b.set_value(qualifier='dperdt', component='binary', value=(1, 'deg/day'))
print(b.filter(qualifier='period*'))


# Now the distinction between the sidereal and anomalistic orbital periods is important and the anomalistic period, `period_anom`, is now an exposed parameter. By default it is constrained, and the sidereal period is used as a free parameter.

# # Phase-folding
# 
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


# If we were to change the orbital period, that would not affect the phases:

# In[15]:


b.set_value('period', component='binary', value=3.14)


# In[16]:


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




