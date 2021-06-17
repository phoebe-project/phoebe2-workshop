#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Flux Scaling (pblum, third light, and distance)
# 
# In this tutorial we'll cover how to handle passband luminosities, third light, and distance.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Atmospheres & Passbands](http://phoebe-project.org/docs/2.3/tutorials/atm_passbands)
# * [Passband Luminosity](http://phoebe-project.org/docs/2.3/tutorials/pblum)
# * [Third Light](http://phoebe-project.org/docs/2.3/tutorials/l3)
# * [Distance](http://phoebe-project.org/docs/2.3/tutorials/distance)

# # Setup

# In[ ]:


import phoebe
from phoebe import u,c


# In[ ]:


logger = phoebe.logger(clevel='WARNING')


# In[ ]:


b = phoebe.default_binary()


# In[ ]:


b.add_dataset('lc', compute_times=phoebe.linspace(0,1,101))


# # Passband Luminosities
# 
# For more details, see the [pblum tutorial](http://phoebe-project.org/docs/2.3/tutorials/pblum).

# In[ ]:


print(b.get_parameter(qualifier='pblum_mode'))


# In[ ]:


print(b.get_parameter(qualifier='pblum_mode').choices)


# * **component-coupled** (default): provide the passband luminosity of *one* of the stars, the other is scaled automatically. See `pblum_component` and `pblum` parameters.
# * **decoupled**: provide the passband luminosity of each star individually.  See `pblum` parameters.
# * **dataset-coupled**: scale this dataset according to the scaling of another (accounting for passbands). See `pblum_dataset` parameter.  Note: `pblum` parameters will be hidden.
# * **dataset-scaled**: scale the light curve to the provided observational data (NOTE: cannot access luminosities or intensities in this mode).  Note: `pblum` parameters will be hidden.
# * **absolute**: don't provide passband luminosities - fluxes/luminosities will be in absolute units.  Note: `pblum` parameters will be hidden.

# For all modes (except dataset-scaled), we can compute the relative and absolute luminosities outside of `run_compute` by calling [compute_pblums](http://phoebe-project.org/docs/devel/api/phoebe.frontend.bundle.Bundle.compute_pblums.md).  Note that this is a completely optional step to expose these quantities and doesn't need to be called.

# In[ ]:


print(b.compute_pblums())


# Third Light
# -----------------
# 
# See the [third light tutorial](http://phoebe-project.org/docs/2.3/tutorials/l3) for more details.

# In[ ]:


print(b.get_parameter(qualifier='l3_mode'))


# In[ ]:


print(b.get_parameter(qualifier='l3_mode').choices)


# * **flux** (default): provide third light in units of flux.  See `l3` parameter.
# * **fraction**: provide third light as a fraction of the total flux.  See `l3_frac` parameter.

# Similarly to `compute_pblums`, we can compute and expose the translation between `l3` and `l3_frac` via [compute_l3s](http://phoebe-project.org/docs/2.3/api/phoebe.frontend.bundle.Bundle.compute_l3s.md).

# In[ ]:


print(b.compute_l3s())


# Distance 
# ---------------
# 
# See the [distance tutorial](http://phoebe-project.org/docs/2.3/tutorials/distance) for more details.

# The `distance` parameter lives in the 'system' context and is simply the distance between the center of the coordinate system and the observer (at t0).

# In[ ]:


print(b.get_parameter(qualifier='distance', context='system'))


# # Exercises

# **NOTE**: this tutorial is a bit of a tangent and will not be used directly in the following tutorials, so don't feel that it is necessary to complete all the exercises below. For any that do seem interesting to you, you may need to dig a little deeper into the explanations in the linked online docs for details about how each option works and feel free to ask questions!
# 
# 
# Make a plot of multiple light curves in different passbands.  Have one passband be set so that the out-of-eclipse flux is approximately one (using `pblum_mode='component-coupled'` and manually adjusting `pblum` and calling `run_compute` or `compute_pblums(pbflux=True)`) and the other light curves all coupled relative to that (using `'dataset-coupled'` and setting the `pblum_dataset` parameter).  Try naming the datasets appropriately and include labels on the plot.
# 
# You can find the [compute_pblums API docs here](http://phoebe-project.org/docs/2.3/api/phoebe.frontend.bundle.Bundle.compute_pblums).

# In[ ]:





# Set `pblum_mode` to `'component-coupled'` or `'absolute'` and show how third light (either in flux or fractional units) affects a light curve and the luminosities.  (**NOTE**: `pbflux=True` is _intrinsic_ only and so does not account for third light)

# In[ ]:





# Do the same for `distance` as you just did for third light: set `pblum_mode` to `'component-coupled'` or `'absolute'` and show how changing the distance affects the flux-levels in a light curve. (**NOTE**: `pbflux=True` is _intrinsic_ only and so does not account for distance)

# In[ ]:





# Combine non-zero `l3` and non-unity `distance` and see how the output from `compute_pblums` changes.  

# In[ ]:




