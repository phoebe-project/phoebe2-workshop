#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Flux Scaling (pblum, third light, and distance)
# 
# In this tutorial we cover how to handle passband luminosities, third light, and distance.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Atmospheres & Passbands](http://phoebe-project.org/docs/2.4/tutorials/atm_passbands)
# * [Passband Luminosity](http://phoebe-project.org/docs/2.4/tutorials/pblum)
# * [Third Light](http://phoebe-project.org/docs/2.4/tutorials/l3)
# * [Distance](http://phoebe-project.org/docs/2.4/tutorials/distance)

# # Setup
# 
# As usual, let us import phoebe, constants, units, initialize logging and load the default binary:

# In[2]:


import phoebe
from phoebe import u, c
logger = phoebe.logger(clevel='WARNING')
b = phoebe.default_binary()


# Add a light curve:

# In[3]:


b.add_dataset('lc', compute_times=phoebe.linspace(0,1,101))


# ## Passband Luminosities
# 
# Passband luminosity, by definition, is a star's luminosity in a specific passband. Most PHOEBE newcomers are surprised to learn that *luminosity*, being an aspect-independent quantity that measures the power output of the star and thus depends on its surface area and effective temperature, is an input parameter. After all, if we prescribe `requiv` and `teff` for a star, should that not suffice for determining luminosity?
# 
# Indeed it does: `requiv` and `teff` determine *bolometric* luminosity under the assumption of isotropic radiation. If we provide a passband, they also determine *passband* luminosity; the actual relationship between `requiv` and `teff` on one side, and `pblum` on the other is described by the Stefan-Boltzmann law for blackbody radiation, or suitable model atmospheres (along with `logg` and `abun` parameters) for a more realistic approximation.
# 
# The reason why PHOEBE needs to parametrize passband luminosity *in addition* to stellar size and atmospheric parameters is two-fold: (1) the measured quantity is *flux*, not luminosity, and (2) the relationship between `requiv`, `teff` and `pblum` might not be correct. Let us take a closer look at both scenarios.
# 
# ### Flux vs. luminosity
# 
# Luminosity -- the power of the star -- is measured in watts (W). It tells us how many Joules per second flow from the surface of the star into space irrespective of the direction. Now we point our telescope-mounted CCD to that star. We *count photons* that strike the CCD; during this process, we inevitably lose some photons to interstellar travel, to Earth's atmosphere, to telescope optics, to CCD's non-perfect quantum efficiency, and then there is an inherent Poissonian counting noise. This photon count is *instrumental flux*, measured in photons per second per meter squared of distance between the star and our telescope. In SI units, this would be W/m^2. In order to relate luminosity of the star and measured flux, we thus need to know both how far the source is, and everything that happens to the photon stream between there and here.
# 
# While theorists love to ponder on all these effects, observers usually settle for *differential* flux measurements. Reported fluxes are *arbitrarily* scaled, possibly also converted to magnitudes. That implies that the relationship between luminosity and flux is *lost*, or heavily obfuscated at best. Thus, PHOEBE provides `pblum` as a parameter to bridge this: it sets the luminosity of the star to correspond to the units of measured flux. This will now be independent of the distance, of the atmosphere, of the instrument, and of any other effects that affect our flux measurement. Simply put: if `pblum` increases by a factor of 2, so will the synthetic flux of that star. Colloquially, `pblum` sets the radiation scale units for the given dataset.
# 
# ### Inadequate atmosphere models
# 
# The other option is that we do know all intricate details that manifest the star's luminosity into measured flux; there may still be a problem with that if the used model atmosphere is not suitable for the type of star being observed. For example, if we have a hot O-type star with pronounced non-LTE effects, we probably do not want to impose luminosity based on a plane-parallel, LTE model. Likewise, if we have a cool red supergiant, model atmospheres that do not account for a plethora of molecular lines might not be the right choice. So instead of prescribing luminosity based on these models, we can decouple it and use it to scale the flux appropriately. If we *really* know the response of our system and the distance to the star, we could even use decoupled luminosities to calibrate model atmospheres.
# 
# ## Passband luminosity mode
# 
# The mode of operation regarding passband luminosity is set by using the `pblum_mode` parameter. Let us take a closer look:

# In[4]:


print(b.get_parameter(qualifier='pblum_mode'))


# Having two stars instead of one implies making further decisions. The choices for passband luminosity treatment are:
# * **decoupled**: provide the passband luminosity of each star individually;
# * **component-coupled** (default): provide the passband luminosity for *one* of the stars, the other is scaled automatically using model atmospheres;
# * **dataset-coupled**: scale this dataset according to the scaling of another dataset (accounting for passbands);
# * **dataset-scaled**: scale the light curve to the provided dataset;
# * **absolute**: compute luminosities from absolute parameters; fluxes/luminosities will be in absolute units.

# For all modes (except dataset-scaled), we can compute the relative and absolute luminosities outside of `run_compute` by calling [compute_pblums](http://phoebe-project.org/docs/devel/api/phoebe.frontend.bundle.Bundle.compute_pblums.md):

# In[5]:


print(b.compute_pblums())


# The units of 'W' here are "just for show": we assume that fluxes are measured in $\mathrm{W}/\mathrm{m}^2$, so passband luminosity needs to be in watts. Now let us change the mode to `absolute` and compute the flux from the Sun at Earth's distance in Johnson V passband:

# In[6]:


s = phoebe.default_star()
s.add_dataset('lc', times=[0.0], passband='Johnson:V')
s.set_value(qualifier='pblum_mode', value='absolute')
s.set_value(qualifier='teff', value=5772*u.K)
s.set_value(qualifier='requiv', value=1*u.solRad)
s.set_value(qualifier='ntriangles', value=10000)
s.set_value(qualifier='distance', value=1*u.AU)


# In[7]:


s.compute_pblums()


# In[8]:


s.run_compute()


# In[9]:


s.get_value(context='model', dataset='lc01', qualifier='fluxes')


# Compare this to the (quasi)-bolometric flux:

# In[10]:


s.add_dataset('lc', times=[0.0], passband='Bolometric:900-40000', dataset='bolo')
s.set_value(dataset='bolo', qualifier='pblum_mode', value='absolute')
s.run_compute()
s.get_value(context='model', dataset='bolo', qualifier='fluxes')


# # Third Light
# 
# Third light is a catch-all parameter for all extraneous light that comprises the passband flux but does not originate from the modeled system. Third light is *additive*: it parametrizes excess photons that are not coming from the system. The most common circumstance is a triple stellar system where the third companion light contaminates the observations of the inner binary.
# 
# Third light can either be provided in flux units or in fractional amount:

# In[11]:


print(s.get_parameter(qualifier='l3_mode', dataset='lc01'))


# * **flux** (default): provide third light in units of flux.  See `l3` parameter;
# * **fraction**: provide third light as a fraction of the total flux.  See `l3_frac` parameter.

# Similarly to `compute_pblums`, we can compute and expose the translation between `l3` and `l3_frac` via [compute_l3s](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.compute_l3s.md). For example, going back to our binary star bundle:

# In[12]:


b['pblum_mode@lc01'] = 'component-coupled'
b['l3@lc01'] = 1.0
print(b.compute_l3s())


# Alternatively, we can switch `l3_mode` to `fraction`; `compute_l3s()` will then compute third light fluxes:

# In[13]:


b['l3_mode'] = 'fraction'
b['l3_frac@lc01'] = 0.5
print(b.compute_l3s())


# Distance 
# ---------------
# 
# Finally, the `distance` parameter impacts flux attenuation by way of the inverse square law. By default the distance is set to a canonical 1m, which sets the relationship between luminosity per steradian and flux: `pblum`=4pi corresponds to unity flux.

# In[18]:


b['l3_frac@lc01'] = 0
print(b.compute_pblums())
b.run_compute()
print(b['fluxes@lc01@model'])


# Thus, if we increase the distance by a factor of 2, the flux will go down by a factor of 4:

# In[20]:


b['distance'] = 2*u.m
b.run_compute()
print(b['fluxes@lc01@model'])


# # Exercises

# Make a plot of multiple light curves in different passbands.  Have one passband be set so that the out-of-eclipse flux is approximately one (using `pblum_mode='component-coupled'` and manually adjusting `pblum` and calling `run_compute` or `compute_pblums(pbflux=True)`) and the other light curves all coupled relative to that (using `'dataset-coupled'` and setting the `pblum_dataset` parameter).  Try naming the datasets appropriately and include labels on the plot.
# 
# You can find the [compute_pblums API docs here](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.compute_pblums).

# In[ ]:





# Set `pblum_mode` to `'component-coupled'` or `'absolute'` and show how third light (either in flux or fractional units) affects a light curve and the luminosities.  (**NOTE**: `pbflux=True` is _intrinsic_ only and so does not account for third light)

# In[ ]:





# Do the same for `distance` as you just did for third light: set `pblum_mode` to `'component-coupled'` or `'absolute'` and show how changing the distance affects the flux-levels in a light curve. (**NOTE**: `pbflux=True` is _intrinsic_ only and so does not account for distance)

# In[ ]:





# Combine non-zero `l3` and non-unity `distance` and see how the output from `compute_pblums` changes.  

# In[ ]:




