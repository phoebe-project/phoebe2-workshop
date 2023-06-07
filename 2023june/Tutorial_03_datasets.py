#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Datasets
# 
# This tutorial covers PHOEBE datasets, adding them to the Bundle, and available options for light curves, radial velocity curves, orbits, and meshes.
# 
# This workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Datasets](http://phoebe-project.org/docs/2.4/tutorials/datasets.ipynb)
# * [Advanced: Datasets (passband options, dealing with phases, removing datasets)](http://phoebe-project.org/docs/2.4/tutorials/datasets_advanced.ipynb)

# # Setup
# 
# To begin, let us do the usual imports, set up the logger and load the default binary bundle:

# In[1]:


import phoebe
from phoebe import u, c

logger = phoebe.logger(clevel='WARNING')
b = phoebe.default_binary()


# # Datasets

# PHOEBE interfaces data through *datasets*. These datasets can contain actual observations or they can simply parametrize the forward-model observable that PHOEBE can synthesize. The following dataset kinds are currently supported:
# 
# * `lc` (light curves)
# * `rv` (radial velocitiy curves)
# * `lp` (line profiles)
# * `orb` (orbits)
# * `mesh` (meshes)
# 
# In order to compute a synthetic model, we must first add a dataset to the Bundle via the [add_dataset()](http://phoebe-project.org/docs/dev/api/phoebe.frontend.bundle.Bundle.add_dataset.md) method. The first argument is the kind (one among those listed above). Although that is the only *required* argument, we will usually want to provide a list of times at which we want that dataset computed, along with a label for the dataset. If we do not provide a label, the dataset will be labeled automatically by 'kind' + two digit integer, e.g. 'lc01', 'rv02', etc.).
# 
# For the purposes of this tutorial, we will use two array-generating functions: [linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html) and [arange](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html). These are numpy functions, but PHOEBE also provides them natively, thus saving memory by storing less within the bundle.

# ## Light Curves
# 
# Adding a single light curve with predefined times and a label is accomplished by calling the `add_dataset()` bundle method:

# In[2]:


b.add_dataset('lc', times=phoebe.linspace(0, 1, 51), dataset='lc01')


# This attaches a set of new dataset parameters to the bundle. Most have the context='dataset', but a few have context='compute', 'figure', and 'constraint'. The 'times' parameter is set with the provided array, and all parameters are tagged with dataset='lc01'.

# In[3]:


b.filter(dataset='lc01').contexts


# We can now take a closer look at the new parameters with context='dataset':

# In[4]:


b.filter(dataset='lc01', context='dataset').qualifiers


# These parameters describe *observables* (`times`, `fluxes`, `sigmas`), *passband information* (`passband`, `pblum_mode`, `pblum_component`), *limb darkening* (`ld_mode`), *instrumental information* (`exptime`, `l3_mode`, `l3`, `intens_weighting`), phasing (`phases_t0`) and masking the data (`mask_enabled`, `mask_phases`).
# 
# You may also notice the `compute_times` and `compute_phases` parameters. These parameters allow us to override the values contained in the `times` parameter. We may think of `times` as the times of observation that correspond to the actual data -- and they must have the same length as `fluxes`, if provided; `compute_times`, on the other hand, are the timestamps in which we want our model computed. Similarly, `solver_times` determine the timestamp array to be used in the inverse problem. More on that next week.

# Next, `context='compute'` parameters:

# In[5]:


b.filter(dataset='lc01', context='compute').qualifiers


# These parameters determine whether the dataset should be enabled or disabled, and how to handle [finite times of integration](http://phoebe-project.org/docs/2.4/tutorials/fti).

# ## Radial Velocities

# Now let us do the same for a [radial velocity (rv) dataset](http://phoebe-project.org/docs/2.4/tutorials/RV.ipynb):

# In[6]:


b.add_dataset('rv', times=phoebe.linspace(0, 1, 11), dataset='rv01')


# Using `dataset='rv01'` will filter on all relevant parameters for the RV dataset:

# In[7]:


b.filter(dataset='rv01', context='dataset').qualifiers


# Here we see again parameters describing observables (`times`, `rvs`, `sigmas`), passband information (`passband`), limb darkening (`ld_mode`), instrumental information (`intens_weighting`), phasing (`phases_t0`), data masking (`mask_enabled`, `mask_phases`) and custom timestamps (`compute_times`, `compute_phases`, `solver_times`). Some of the parameters we saw in the 'lc' dataset are not applicable when computing rvs, so they are not included (`l3_mode`, `pblum_mode`, etc).
# 
# Currently, finite exposure times are not supported for radial velocities in PHOEBE, hence no `exptime` parameter.
# 
# Note that there are **2** `times` parameters - one for each star.  When passing `times=np.linspace(...)` to `b.add_dataset`, both `times` parameters are set to that value.  We could have also set separate times for the two components by setting the values of `times@primary` and `times@secondary`. Alternatively, you can also pass a dictionary when creating the dataset: `b.add_dataset('rv', times={'primary': [0,1,2], 'secondary': [1,2,3]})`.

# In[8]:


b.filter(dataset='rv01', context='dataset', qualifier='times').components


# We can now take a look at the added parameters with context='compute':

# In[9]:


b.filter(dataset='rv01', context='compute').qualifiers


# Here again we see the `enabled` parameter, the method for computing radial velocities (`rv_method`), and an option to enable/disable gravitational redshift when computing RVs (`rv_grav`).

# ## Orbits

# Although it is not common to have astrometric observations of an orbit, the [orb dataset](http://phoebe-project.org/docs/2.4/tutorials/ORB.ipynb) allows you to synthesize orbits of the stars in a system at any given time, which can be useful for visualization.

# In[10]:


b.add_dataset('orb', compute_times=phoebe.linspace(0, 1, 101), dataset='orb01')


# Orbits are parametrized by providing the compute times/phases and enabling/disabling. Note that there is no `times` parameter, as there are no observations. However, if you pass `times` to `add_dataset`, they will be adopted automatically as `compute_times`.

# In[11]:


b.filter(dataset='orb01', context='dataset').qualifiers


# In[12]:


b.filter(dataset='orb01', context='compute').qualifiers


# ## Line Profiles

# [Line profiles](http://phoebe-project.org/docs/2.4/tutorials/LP) are time- *and* wavelength-dependent.  Note that the times cannot be changed after the dataset has been created and attached to the bundle while the wavelengths can. That said, `compute_times` can be changed and used to synthesize line profiles at any desired timestamp. Because of this, the distinction between `times` and `compute_times` is a bit more important for line profiles - you probably only want to provide `times` if you want to attach your actual observations, otherwise just provide `compute_times`.

# In[13]:


b.add_dataset('lp', 
              times=phoebe.linspace(0, 1, 11), 
              wavelengths=phoebe.linspace(549, 551, 101), 
              dataset='lp01')


# Now we can take a look at the parameters for a line profile dataset with `context='dataset'`:

# In[14]:


b.filter(dataset='lp01', context='dataset').qualifiers


# To reinforce the notion of the `times` vs. `compute_times` difference, let us print the entire parameter set for `lp01`:

# In[15]:


print(b.filter(dataset='lp01', context='dataset'))


# Timestamps (passed as `times`) are provided as tags, to tag each parameter that can change in time; if instead we provided `compute_times`, they would not be tagged:

# In[16]:


b.add_dataset('lp', 
              compute_times=phoebe.linspace(0, 1, 11), 
              wavelengths=phoebe.linspace(549, 551, 101), 
              dataset='lp01',
              overwrite=True)


# In[17]:


print(b.filter(dataset='lp01', context='dataset'))


# Line profiles are parametrized differently than LCs or RVs; we need to provide a generic profile function (`profile_func`) along with its rest wavelength (`profile_rest`) and subsidiary variable (`profile_sv`), defined as $sv = (p-p_0)/(0.5 \times \mathrm{FWHM})$, where $p_0$ is the rest wavelength and $\mathrm{FWHM}$ is full width at half maximum. Wavelengths are passed as arrays, either to the binary as a whole, or to individual stars.

# As far as `context='compute'` parameters are concerned, we only have the enabled/disabled switch:

# In[18]:


b.filter(dataset='lp01', context='compute').qualifiers


# ## Meshes

# Similarly to orbits, the [mesh dataset](http://phoebe-project.org/docs/2.4/tutorials/MESH.ipynb) is unlikely to be compared to data directly, but is very useful for visualization of the system. This dataset takes a list of times, columns, and coordinates at which you would like the meshes used within PHOEBE exposed.
# 
# As orbits, meshes do not have associated observables, thus they are parametrized only by `compute_times`. As before, passing `times` will automatically be converted to `compute_times` under the hood.

# In[19]:


b.add_dataset('mesh', 
              compute_times=[0, 0.5, 1], 
              dataset='mesh01')


# Let us take a look at parameters in the 'dataset' and 'compute' contexts:

# In[20]:


b.filter(dataset='mesh01', context='dataset').qualifiers


# In[21]:


b.filter(dataset='mesh01', context='compute').qualifiers


# A unique aspect of parametrizing meshes is the `columns` parameter; we will revisit that in great detail soon, but at this point let us take a quick look at the available columns. The list is quite extensive and we will not go into any details at this point, but it should be informative to glance through the names of the columns; all these are per-surface-element values that can be exposed and visualized.

# In[22]:


b.get_parameter(dataset='mesh01', context='dataset', qualifier='columns').choices


# # Exercise

# What choices are available for `rv_method`, `passband`, `pblum_mode`, `ld_mode`, and `intens_weighting`?

# In[ ]:





# Say we have a single-lined binary system. Set the RV dataset times so that only primary star observables are computed.

# In[ ]:





# Add another RV dataset.  Set the new RV dataset to have `rv_method='dynamical'` while keeping the original 'rv01' dataset with `rv_method='flux-weighted'`. This is another example of a per-component parameter: you will either need to set parameters for both components in turn, or use [set_value_all()](http://phoebe-project.org/docs/latest/api/phoebe.parameters.ParameterSet.set_value_all.md).

# In[ ]:




