#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Datasets
# 
# In this tutorial, we'll learn about PHOEBE datasets, how to add them to the Bundle, and which options are available for light curve, radial velocity curves, orbits, and meshes.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Datasets](http://phoebe-project.org/docs/2.3/tutorials/datasets.ipynb)
# * [Advanced: Datasets (passband options, dealing with phases, removing datasets)](http://phoebe-project.org/docs/2.3/tutorials/datasets_advanced.ipynb)

# # Setup

# In[ ]:


import phoebe
from phoebe import u,c


# In[ ]:


logger = phoebe.logger(clevel='WARNING')


# In[ ]:


b = phoebe.default_binary()


# # Datasets

# PHOEBE creates synthetic models of our binary system at the times and options provided by datasets (which do not necessarily need to contain observations, but can just be a list of times).  PHOEBE currently supports several different dataset kinds:
# 
# * lc (light curves)
# * rv (radial velocitiy curves)
# * lp (line profiles)
# * orb (orbits)
# * mesh (meshes)
# 
# In order to get the synthetic model, we must first add a dataset to the Bundle via [add_dataset](http://phoebe-project.org/docs/dev/api/phoebe.frontend.bundle.Bundle.add_dataset.md).  The first argument is the shorthand-notation for the kind (listed above).  Although this is the only *required* argument, you will usually also want to provide a list of times at which you want that dataset computed as well as a label for the dataset (if you don't provide a label, one will be created for you using the convention 'dataset_type' followed by a two digit integer, e.g. lc01).
# 
# If you're unfamiliar with numpy, we will use two helpful functions: [linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html) and [arange](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html).  You could call np.linspace and np.arange directly, but PHOEBE also provides a shortcut to these which will save on the memory requirements within the Bundle.

# ## Light Curves

# In[ ]:


b.add_dataset('lc', times=phoebe.linspace(0,1,51), dataset='lc01')


# This attaches a set of new Parameters to the Bundle.  Most have the context='dataset', but a few have context='compute', 'figure', 'constraint', etc.  The 'times' Parameter is set with the provided array, and all Parameters are tagged with dataset='lc01'.

# In[ ]:


b.filter(dataset='lc01').contexts


# Let's look at the new Parameters (for our light curve) with context='dataset'.

# In[ ]:


b.filter(dataset='lc01', context='dataset').qualifiers


# These Parameters describe the *observational* data (`times`, `fluxes`, `sigmas`), the passband information (`passband`, `pblum_mode`, `pblum_component`), limb-darkening (`ld_mode`), telescope/observational information (`exptime`, `l3_mode`, `l3`, `intens_weighting`), and if/how to phase and mask the data (`mask_enabled`, `mask_phases`, `phases_t0`).
# 
# You may also notice the `compute_times` and `compute_phases` parameters.  `compute_times` (or `compute_phases` - but more on that in the next tutorial) allows for overriding the values provided in `times`.  Think of `times` as the observational times that correspond to your actual data (if you have them) - and must have the same length as `fluxes`, if provided.  `compute_times` are the times that you want your model computed.

# Now let's quickly look at the Parameters with `context='compute'`

# In[ ]:


b.filter(dataset='lc01', context='compute').qualifiers


# These set whether this dataset should be computed or ignored (`enabled`), as well as methods for how to handle [finite exposure times](http://phoebe-project.org/docs/2.3/tutorials/fti) (`fti_method`).

# ## Radial Velocities

# Now let's do the same for a [radial velocity (rv) dataset](http://phoebe-project.org/docs/2.3/tutorials/RV.ipynb).

# In[ ]:


b.add_dataset('rv', times=phoebe.linspace(0,1,11), dataset='rv01')


# Let's look at the Parameters for a radial velocity dataset with `context='dataset'`

# In[ ]:


b.filter(dataset='rv01', context='dataset').qualifiers


# Here we see again Parameters describing the *observational* data (`times`, `rvs`, `sigmas`), the passband information (`passband`), limb-darkening (`ld_mode`) and telescope/observational information (`intens_weighting`).  Some of the Parameters we saw in the lc dataset are not applicable when computing rvs, so are not included (`l3_mode`, `pblum_mode`, etc).
# 
# Currently, finite exposure times are not supported for radial velocities in PHOEBE, so there is no exptime Parameter.
# 
# Note that there are actually **2** `times` Parameters - one for each star.  When sending `times=np.linspace(...)` to `b.add_dataset`, both times Parameters received that value.  But, we could set separate times for the two components after by setting the values of the individual Parameters.
# 
# Note: You can also send a dictionary when creating the dataset: `b.add_dataset('rv', times={'primary': [0,1,2], 'secondary': [1,2,3]})` to send values to individual parameters.

# In[ ]:


b.filter(dataset='rv01', context='dataset', qualifier='times').components


# And now look at the added Parameters with context='compute'.

# In[ ]:


b.filter(dataset='rv01', context='compute').qualifiers


# Here again we see the `enabled` Parameter, the method for computing radial velocities (`rv_method`), and an option to enable/disable gravitational redshift when computing RVs (`rv_grav`).

# ## Orbits

# Although you're unlikely to have observational data on an orbit, the [orb dataset](http://phoebe-project.org/docs/2.3/tutorials/ORB.ipynb) allows you to expose the orbital information of the stars in a system at any given time, which can be useful for visualization or debugging purposes.

# In[ ]:


b.add_dataset('orb', compute_times=phoebe.linspace(0,1,101), dataset='orb01')


# There are no options for orbits besides providing the compute times/phases and enabling/disabling.  Note that there is no `times` parameter, as there are no observations.  However, if you pass `times` to `add_dataset`, they will be adopted automatically as `compute_times`.

# In[ ]:


b.filter(dataset='orb01', context='dataset').qualifiers


# In[ ]:


b.filter(dataset='orb01', context='compute').qualifiers


# ## Line Profiles

# [Line profiles](http://phoebe-project.org/docs/2.3/tutorials/LP) are time *and* wavelength dependent.  Note that the times cannot be changed after the dataset is created and attached to the bundle (although the wavelengths can).  **However**, `compute_times` can be changed.  Because of this, the distinction between `times` and `compute_times` is a bit more important for line profiles - you probably only want to provide `times` if you want to attach your actual observations, otherwise just provide `compute_times`.

# In[ ]:


b.add_dataset('lp', 
              times=phoebe.linspace(0,1,11), 
              wavelengths=phoebe.linspace(549,551,101), 
              dataset='lp01')


# Let's look at the Parameters for a line profile dataset with `context='dataset'`

# In[ ]:


b.filter(dataset='lp01', context='dataset').qualifiers


# In[ ]:


print(b.filter(dataset='lp01', context='dataset'))


# If we instead provide `compute_times`, we won't have all these extra per-time "observational" parameters.

# In[ ]:


b.add_dataset('lp', 
              compute_times=phoebe.linspace(0,1,11), 
              wavelengths=phoebe.linspace(549,551,101), 
              dataset='lp01',
              overwrite=True)


# In[ ]:


print(b.filter(dataset='lp01', context='dataset'))


# And now look at the added Parameters with `context='compute'`.

# In[ ]:


b.filter(dataset='lp01', context='compute').qualifiers


# ## Meshes

# Similarly, the [mesh dataset](http://phoebe-project.org/docs/2.3/tutorials/MESH.ipynb) is unlikely to be compared to data, but is very useful for visualization of the system.  This dataset only allows you to define a list of times, columns, and coordinates at which you'd like the meshes used within PHOEBE exposed.
# 
# Meshes can't have observational data, so *only* have a `compute_times`.  But if you try to pass `times`, it will accept those as `compute_times` with a warning in the logger.

# In[ ]:


b.add_dataset('mesh', 
              compute_times=[0, 0.5, 1], 
              dataset='mesh01')


# In[ ]:


b.filter(dataset='mesh01', context='dataset').qualifiers


# In[ ]:


b.filter(dataset='mesh01', context='compute').qualifiers


# # Exercise

# What choices are available for `rv_method`, `passband`, `pblum_mode`, `ld_mode`, and `intens_weighting` (refer back to the [first tutorial](./Tutorial_01_bundle_basics.ipynb) if you've forgotten how to check the choices)?

# In[ ]:





# Let's say we had a single-lined binary system.  Set the times on the RV dataset such that only the primary star would be computed.

# In[ ]:





# Add another RV dataset.  Set the new RV dataset to have `rv_method='dynamical'` while keeping the original 'rv01' dataset with `rv_method='flux-weighted'`.  (You'll notice there is a parameter per-component - you'll either need to set both manually or use [set_value_all](http://phoebe-project.org/docs/latest/api/phoebe.parameters.ParameterSet.set_value_all.md))

# In[ ]:




