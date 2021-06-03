#!/usr/bin/env python
# coding: utf-8

# In this tutorial, we'll learn about PHOEBE datasets, how to add them to the Bundle, and which options are available for light curve, radial velocity curves, orbits, and meshes.

# # Setup

# In[1]:


import phoebe
from phoebe import u,c

import numpy as np
import matplotlib.pyplot as plt


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# # Datasets

# PHOEBE creates synthetic models of our binary system at the times and options provided by datasets (which do not necessarily need to contain observations, but can just be a list of times).  PHOEBE currently supports several different dataset kinds:
# 
# * lc (light curves)
# * rv (radial velocitiy curves)
# * orb (orbits)
# * mesh (meshes)
# 
# In order to get the synthetic model, we must first add a dataset to the Bundle via add_dataset.  The first argument is the shorthand-notation for the kind (listed above).  Although this is the only *required* argument, you will usually also want to provide a list of times at which you want that dataset computed as well as a label for the dataset (if you don't provide a label, one will be created for you).
# 
# PHOEBE currently only supports forward-models (not fitting), so including fluxes and uncertainties is really only useful for the sake of plotting the model over your data.
# 
# If you're unfamiliar with numpy, we will use two helpful functions: [linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html) and [arange](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html).

# ### Light Curves

# In[4]:


b.add_dataset('lc', times=np.linspace(0,1,51), dataset='lc01')


# This attaches a set of 15 new Parameters to the Bundle.  Most have context='dataset', but a few have context='compute'.  The 'times' Parameter is set with the provided array, and all Parameters are tagged with dataset='lc01'.

# In[5]:


b.filter(dataset='lc01').contexts


# Let's look at the new Parameters (for our light curve) with context='dataset'.

# In[6]:


b.filter(dataset='lc01', context='dataset').qualifiers


# These Parameters describe the *observational* data (times, fluxes, sigmas), the passband information (passband, pblum, pblum_ref), limb-darkening (ld_func), and telescope/observational information (exptime, l3, intens_weighting).

# Now let's quickly look at the Parameters with context='compute'

# In[7]:


b.filter(dataset='lc01', context='compute').qualifiers


# These set whether this dataset should be computed or ignored (enabled), as well as methods for computing the light curve (lc_method) and how to handle finite exposure times (fti_method).

# ### Radial Velocities

# Now let's do the same for a radial velocity (rv) dataset

# In[8]:


b.add_dataset('rv', times=np.linspace(0,1,11), dataset='rv01')


# Let's look at the Parameters for a radial velocity dataset with context='dataset'

# In[9]:


b.filter(dataset='rv01', context='dataset').qualifiers


# Here we see again Parameters describing the *observational* data (times, rvs, sigmas), the passband information (passband), limb-darkening (ld_func) and telescope/observational information (intens_weighting).  Some of the Parameters we saw in the lc dataset are not applicable when computing rvs, so are not included (l3, pblum).
# 
# Currently, finite exposure times are not supported for radial velocities in PHOEBE, so there is no exptime Parameter.
# 
# Not that there are actually **2** 'times' Parameters - one for each star.  When sending times=np.linspace(...) to b.add_dataset, both times Parameters received that value.  But, we could set separate times for the two components after by setting the values of the individual Parameters.
# 
# Note: Technically you can also send a dictionary to when creating the dataset: b.add_dataset('rv', times={'primary': [0,1,2], 'secondary': [1,2,3]})

# In[10]:


b.filter(dataset='rv01', context='dataset', qualifier='times').components


# And now look at the added Parameters with context='compute'.

# In[11]:


b.filter(dataset='rv01', context='compute').qualifiers


# Here again we see the enabled Parameter, the method for computing radial velocities (rv_method), and an option to enable/disable gravitational redshift when computing RVs (rv_grav).

# ### Orbits

# Although you're unlikely to have observational data on an orbit, the 'orb' dataset allows for exposing the orbital information of the stars in a system at any given time, which can be useful for visualization or debugging purposes.

# In[12]:


b.add_dataset('orb', times=np.linspace(0,1,101), dataset='orb01')


# There are no options for orbits besides providing the times and enabling/disabling.

# In[13]:


b.filter(dataset='orb01', context='dataset').qualifiers


# In[14]:


b.filter(dataset='orb01', context='compute').qualifiers


# ### Meshes

# Similarly, the mesh dataset is unlikely to be compared to data, but is very useful for visualization of the system.  Again, the mesh only allows for defining the times at which you'd like the meshes used within PHOEBE exposed.

# In[15]:


b.add_dataset('mesh', times=[0, 0.5, 1], dataset='mesh01')


# In[16]:


b.filter(dataset='mesh01', context='dataset').qualifiers


# In[17]:


b.filter(dataset='mesh01', context='compute').qualifiers


# # Exercise

# What choices are available for rv_method, lc_method, passband, and intens_weighting?

# In[ ]:





# Let's say we had a single-lined binary system.  Set the times on the RV dataset such that only the primary star would be computed.

# In[ ]:





# Add another RV dataset.  Set the new RV dataset to have rv_method='dynamical' while keeping the original 'rv01' dataset with rv_method='flux-weighted'.

# In[ ]:




