#!/usr/bin/env python
# coding: utf-8

# In this tutorial we'll cover how to handle passband luminosities, third light, and distance.

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# In[4]:


b.add_dataset('lc', times=phoebe.linspace(0,1,101))


# # Passband Luminosities
# 
# For more details, see the [pblum tutorial](http://phoebe-project.org/docs/devel/tutorials/pblum).

# In[5]:


print(b.get_parameter(qualifier='pblum_mode'))


# In[6]:


print(b.get_parameter(qualifier='pblum_mode').choices)


# * **component-coupled** (default): provide the passband luminosity of *one* of the stars, the other is scaled automatically. See `pblum_component` and `pblum` parameters.
# * **decoupled**: provide the passband luminosity of each star individually.  See `pblum` parameters.
# * **dataset-coupled**: scale this dataset according to the scaling of another (accounting for passbands). See `pblum_dataset` parameter.
# * **dataset-scaled**: scale the light curve to the provided observational data (NOTE: cannot access luminosities or intensities in this mode)
# * **pbflux**: provide the passband luminosity of the *system* in flux units (under a bunch of assumptions).  See `pbflux` parameter.
# * **absolute**: don't provide passband luminosities - fluxes/luminosities will be in absolute units.

# For all modes (except dataset-scaled), we can compute the relative and absolute luminosities outside of `run_compute` by calling [compute_pblums](http://phoebe-project.org/docs/devel/api/phoebe.frontend.bundle.Bundle.compute_pblums.md).  Note that this is a completely option step to expose these quantities and doesn't need to be called.

# In[7]:


print(b.compute_pblums())


# Third Light
# -----------------
# 
# See the [third light tutorial](http://phoebe-project.org/docs/devel/tutorials/l3) for more details.

# In[8]:


print(b.get_parameter(qualifier='l3_mode'))


# In[9]:


print(b.get_parameter(qualifier='l3_mode').choices)


# * **flux** (default): provide third light in units of flux.  See `l3` parameter.
# * **fraction**: provide third light as a fraction of the total flux.  See `l3_frac` parameter.

# Similarly to compute_pblums, we can compute and expose the translation between `l3` and `l3_frac` via [compute_l3s](http://phoebe-project.org/docs/devel/api/phoebe.frontend.bundle.Bundle.compute_l3s.md).

# In[10]:


print(b.compute_l3s())


# Distance 
# ---------------
# 
# See the [distance tutorial](http://phoebe-project.org/docs/devel/tutorials/distance) for more details.

# The 'distance' parameter lives in the 'system' context and is simply the distance between the center of the coordinate system and the observer (at t0).

# In[11]:


print(b.get_parameter(qualifier='distance', context='system'))


# # Exercises

# Make a plot of multiple light curves in different passbands.  Have one passband be set so that the out-of-eclipse flux is approximately one (either using 'component-coupled' or 'pbflux'), and the others all coupled relative to that.  Try naming the datasets appropriately and include labels on the plot.

# In[ ]:





# Set `pblum_mode` to 'component-coupled' or 'absolute' and show how third light (either in flux or fractional units) affects a light curve and the luminosities.  You can also try passing `pbflux=True, pbflux_ext=True` to `compute_pblums` to see how the estimated flux-levels are also affected.
# 
# Now set `pblum_mode` to 'pbflux' and see that the flux-levels now remain (essentially) fixed, with luminosities automatically changing to account for the change in third light.
# 
# **WARNING**: be careful - if you set the `l3` >= `pbflux`, this can give weird results, including negative luminosities.  This behavior is subject to change before the 2.2 release.

# In[ ]:





# Do the same for `distance` as you just did for third light: set `pblum_mode` to 'component-coupled' or 'absolute' and show how changing the distance affects the flux-levels in a light curve.  Then try setting `pblum_mode` to 'pbflux' and show that the flux-levels remain fixed.

# In[ ]:





# Combine non-zero `l3` and non-unity `distance` and see how the output from `compute_pblums` changes.  
# 
# **IMPORTANT**: this can be confusing and this exact behavior is subject to change before the 2.2 release.

# In[ ]:




