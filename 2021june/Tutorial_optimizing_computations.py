#!/usr/bin/env python
# coding: utf-8

# # Optimizing Computations
# 
# In this tutorial we'll discuss which parts of PHOEBE are the most computationally expensive and how to minimize this cost for individual systems by testing which expensive effects can safely be disabled.
# 
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Eclipse Detection](http://phoebe-project.org/docs/2.3/tutorials/eclipse.ipynb)
# * [Eccentricity & Volume Conservation](http://phoebe-project.org/docs/2.3/tutorials/ecc.ipynb)
# * [Reflection & Heating (irrad_frac_refl_bol, irrad_frac_lost_bol, ld_func_bol, ld_coeffs_bol)](http://phoebe-project.org/docs/2.3/tutorials/reflection_heating.ipynb)
# * [Reflection & Heating: Lambert Scattering (irrad_method='horvat' vs 'wilson')](http://phoebe-project.org/docs/2.3/tutorials/irrad_method_horvat.ipynb)
# * [Detached Binary: Roche vs Rotstar](http://phoebe-project.org/docs/2.3/examples/detached_rotstar.ipynb)
# * [Rossiter-McLaughlin Effect (RVs)](http://phoebe-project.org/docs/2.3/examples/rossiter_mclaughlin.ipynb)
# * [Finite Time of Integration (LCs - exptime, fti_method, fti_oversample)](http://phoebe-project.org/docs/2.3/tutorials/fti.ipynb)
# 
# 
# 
# In addition, see the following document on optimizing the performance of the PHOEBE frontend itself in scripts (this will _not_ affect the speed within `run_compute` or `run_solver`):
# 
# * [Advanced: Optimizing Performance with PHOEBE](http://phoebe-project.org/docs/2.3/tutorials/optimizing.ipynb)

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
b.add_dataset('rv', compute_times=phoebe.linspace(0,1,26))


# # Compute Times/Phases
# 
# With the exception of dynamics (dynamical RVs and orbits), PHOEBE computations scale with the number of data points (roughly linearly after some up-front costs).  As discussed in previous tutorials (see [Tutorial: Datasets](./Tutorial_03_datasets.ipynb) and [Tutorial: Time and Phase](./Tutorial_04b_time_and_phase.ipynb)), the model can be computed at different times than the input observations.  
# 
# For systems without time-dependence (no apsidal motion, etc), it can therefore be quite advantageous to compute the forward model sampled in phase-space and interpolate when comparing to the observations (PHOEBE will handle this interpolation for you).  Just check to make sure that you sample sufficiently in phase that the linear interpolation won't introduce artifacts.

# # Eclipse Detection
# 
# For more details, see [Eclipse Detection](http://phoebe-project.org/docs/2.3/tutorials/eclipse.ipynb).
# 
# By default, at each time point, PHOEBE will check to see if the maximum radius of all meshes would overlap at all on the sky-projection.  If so, the complete eclipse algorithm is called to determine the visibility of each triangle, and if not, triangles are only checked to determine if facing towards or away from the observer (horizon detection).  In cases where you _know_ eclipses will never occur (ellipsoidal variables, for example), this can be optimized slightly by telling PHOEBE to skip this check and only use horizon detection. 

# In[ ]:


print(b.get_parameter(qualifier='eclipse_method'))


# # Eccentricity
# 
# For more details, see [Eccentricity & Volume Conservation](http://phoebe-project.org/docs/2.3/tutorials/ecc.ipynb).
# 
# Eccentricity on its own does not add significant expense - however, it does when in combination with irradiation or distorted stars (both of which are enabled by default).  Whenever an orbit has a non-zero eccentricity, the stars must be re-meshed at each time point and irradiation must be re-computed.
# 
# Although it is usually a good idea to at least marginalize over eccentricity for the final parameter uncertainties (more on this in the second week), if a system can be assumed to be circular or shows no signs of significant eccentricity, setting the eccentricity to be exactly zero can minimize costs significantly.

# In[ ]:


print(b.get_parameter(qualifier='ecc'))


# # Reflection & Heating (irrad_method)
# 
# For more details, see [Reflection & Heating (irrad_frac_refl_bol, irrad_frac_lost_bol, ld_func_bol, ld_coeffs_bol)](http://phoebe-project.org/docs/2.3/tutorials/reflection_heating.ipynb) and [Reflection & Heating: Lambert Scattering (irrad_method='horvat' vs 'wilson')](http://phoebe-project.org/docs/2.3/tutorials/irrad_method_horvat.ipynb).
# 
# In addition to meshing and eclipse detection, irradiation is the next most common culprit in computation expense. In cases where irradiation can safely be ignored, it can be disabled entirely by setting `irrad_method='none'`.  This will only result in marginal gains for circular synchronous systems, but can result in significant savings for eccentric and/or asynchronous systems.

# In[ ]:


print(b.get_parameter(qualifier='irrad_method'))


# # Stellar Distortion (distortion_method)
# 
# For more details, see [Detached Binary: Roche vs Rotstar](http://phoebe-project.org/docs/2.3/examples/detached_rotstar.ipynb)
# 
# In cases where stellar distortion is negligible, stars can be meshed with either a rotating star or spherical star equipotential in place of the full roche treatment.  Similarly to irradiation, this can result in significant savings for eccentric systems as otherwise the instantaneous equipotential needs to be determined at each time point to conserve volume and the stars need to be re-meshed.
# 
# Note: there is a `distortion_method` parameter per-component.

# In[ ]:


print(b.get_parameter(qualifier='distortion_method', component='primary'))


# # Dynamical RVs
# 
# For more details, see [Rossiter-McLaughlin Effect (RVs)](http://phoebe-project.org/docs/2.3/examples/rossiter_mclaughlin.ipynb).
# 
# By default, PHOEBE will compute RVs by populating velocities at each surface element and doing an intensity-weighted average over the visible elements.  This allows for Rossiter-McLaughlin effect to be synthesized.  However, in cases where Rossiter-McLaughlin is not important, dynamical RVs can be used instead which use the center of mass velocities instead.
# 
# If the mesh is already being created and populated for an LC _at the same time_, then flux-weighted RVs do not add significant additional overhead.
# 
# Note: there is an `rv_method` parameter per-component.  However, as the mesh will need to be populated if any are set to flux-weighted, little is to be gained from an optimization perspective by not setting all to 'dynamical'.

# In[ ]:


print(b.get_parameter(qualifier='rv_method', component='primary'))


# # Integration Time
# 
# For more details, see [Finite Time of Integration (LCs - exptime, fti_method, fti_oversample)](http://phoebe-project.org/docs/2.3/tutorials/fti.ipynb)
# 
# Although we have not discussed this during the workshop, PHOEBE allows for oversampling each synthetic time over the observational exposure time (where the number of samples that will be averaged is provided in `fti_oversample`).
# 
# If the exposure time is short relative to the orbital period, accounting for this in the synthetic model will have very little affect on the model light curves and likely is not worth the increased expense (which will scale linearly with `fti_oversample`).
# 
# Note that oversampling will only occur if the `exptime` is set in the dataset.
# 
# 

# In[ ]:


print(b.get_parameter(qualifier='fti_method'))


# In[ ]:


b.set_value(qualifier='fti_method', value='oversample')


# In[ ]:


print(b.get_parameter(qualifier='fti_oversample'))


# # Determining Safe Approximations
# 
# In order to set any of these approximations, we first want to make sure that the influence of that choice will have no detrimental impact on the resulting model.  In any real case, there will be some impact, of course.  But we can compute forward models both with and without the effect and compare the magnitude of the difference to either the amplitude of the signal or of the observational uncertainties.

# In[ ]:


b.run_compute(model='full')


# In[ ]:


b.run_compute(irrad_method='none', model='irrad_off')


# In[ ]:


b.run_compute(distortion_method='sphere', model='distortion_off')


# In[ ]:


_ = b.plot(kind='lc', legend=True, show=True)


# Currently there is no built-in ability to compare two models quantitatively, and there are many different ways you might imagine doing this (relative to the amplitude of the eclipse signal, relative to the uncertainties in observations, etc), but here we'll just quickly plot the relative residuals and check the maximum relative differences.

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

times = b.get_value('times', dataset='lc01', model='full')
fluxes_full = b.get_value('fluxes', model='full')
fluxes_irrad_off = b.get_value('fluxes', model='irrad_off')
fluxes_distortion_off = b.get_value('fluxes', model='distortion_off')

fluxes_irrad_rel = (fluxes_irrad_off - fluxes_full)/fluxes_full
fluxes_distortion_rel = (fluxes_distortion_off - fluxes_full)/fluxes_full


# In[ ]:


_ = plt.plot(times, fluxes_irrad_rel, 'r.')
_ = plt.plot(times, fluxes_distortion_rel, 'b.')


# In[ ]:


np.max(abs(fluxes_irrad_rel))


# **IMPORTANT**: if you're fitting a system and applying any of these approximations, it is important to check the validity throughout the process (and particularly on the final solution - and then of course be transparent in any publications).  

# # Exercise
# 
# Take any of the systems you've built and determine which (if any) expensive effects can safely be ignored.

# In[ ]:




