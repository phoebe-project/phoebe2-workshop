#!/usr/bin/env python
# coding: utf-8

# In this tutorial, we'll learn how to call run_compute to create a synthetic model for the attached datasets.

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


# # Compute

# Let's first re-add some simple datasets so that we can create the models.

# In[4]:


b.add_dataset('lc', times=np.linspace(0,1,51), dataset='lc01')


# In[5]:


b.add_dataset('rv', times=np.linspace(0,1,21), dataset='rv01')


# Now that we have datasets, we could compute the forward model with all the defaults by calling run_compute

# In[6]:


b.run_compute()


# This creates synthetic versions of each dataset copied into the with context='model'.  Let's filter to see what we can find in the model.

# In[7]:


b.filter(context='model').datasets


# In[8]:


b.filter(context='model', dataset='lc01')


# For light curves, the synthetic model consists of the times (copied directly from the values provided in the dataset) and the synthetic fluxes.

# In[9]:


b.get_parameter(context='model', dataset='lc01', qualifier='times')


# In[10]:


b.get_parameter(context='model', dataset='lc01', qualifier='fluxes')


# For radial velocities, the synthetic model consists again of the times, as well as the RVs for both stars in the system.  Therefore, we also need to provide the component tag in order to access a single Parameter.

# In[11]:


b.filter(context='model', dataset='rv01').qualifiers


# In[12]:


b.get_parameter(context='model', datset='rv01', component='primary', qualifier='rvs')


# In[13]:


b.get_parameter(context='model', datset='rv01', component='secondary', qualifier='rvs')


# ### Custom Compute Options

# As we mentioned earlier when adding datasets, Parameters with context='compute' control options for how the model is computed.  With a default Bundle, there is already a single set of compute options attached (these were what was used when we called run_compute above).

# In[14]:


print b.filter(context='compute').qualifiers


# These are options that tell the backend which methods to use or which advanced effects to consider.  Because of this, these options can be changed to either create a quick-and-dirty fast model, or a robust-but-slow model.
# 
# Similar to datasets, we can add additional sets of compute options.  So let's create one set of compute options for quick-and-dirty computations (and tag it compute='preview')

# In[15]:


b.add_compute(compute='preview')


# Now if we filter for any of the Parameters with context='compute', we'll see that there is a copy for each of our created set of compute options as well as the original default set.

# In[16]:


b.filter(context='compute', qualifier='ltte')


# Now let's set a few options to turn off some effects. Let's first disable all the advanced physics (ltte, rv_grav, irrad_method).

# In[17]:


b.get_parameter(context='compute', compute='preview', qualifier='ltte').set_value(False)


# If we try to do the same as above, but use qualifier='rv_grav', we'll get an error saying there are 2 results found.  This is because 'rv_grav' can be enabled/disabled for each individual star.  We can see this is the case by doing a filter.

# In[18]:


b.filter(context='compute', compute='preview', qualifier='rv_grav')


# We could either set the value for component='primary' and component='secondary' separately, or we can set them both at once by using set_value_all (this sets the value for all Parameters in a ParameterSet)
# 
# NOTE: this requires sending value as a keyword instead of an argument since set_value_all also accepts filter options

# In[19]:


b.filter(context='compute', compute='preview', qualifier='rv_grav').set_value_all(value=False)


# In[20]:


b.get_parameter(context='compute', compute='preview', qualifier='irrad_method').choices


# In[21]:


b.get_parameter(context='compute', compute='preview', qualifier='irrad_method').set_value('none')


# And let's also decrease the number of triangles used in the meshes.  Again, we can use set_value_all since there is an entry for each star.

# In[22]:


b.filter(context='compute', compute='preview', qualifier='ntriangles').set_value_all(value=800)


# Now if we want to call run_compute again, we **must** also pass which set of compute options we want to use (the default 'phoebe01', or our new 'preview' options)

# In[23]:


b.run_compute(compute='preview')


# ### Temporarily Overriding Options

# Any of these compute options can be overridden as keyword arguments to run_compute.  These won't change the Parameter values, and will only apply to that single call of run_compute.

# In[24]:


b.run_compute(compute='preview', irrad_method='horvat')


# In addition to the compute options, you can also override the times across **all** datasets

# In[25]:


b.run_compute(compute='preview', times=[0, 0.5, 1])


# In[26]:


print "dataset times: ", b.get_value('times', dataset='lc01', context='dataset')
print "model times: ", b.get_value('times', dataset='lc01', context='model')


# ### Alternate Backends

# In addition to creating separate compute options for robust vs preview, compute options also serve to run backends other than phoebe2.  Currently there are experimental wrappers for PHOEBE 1.0 (legacy), jktebop, and photodynam.
# 
# Similar to providing 'lc' or 'rv' to add_dataset, you just need to provide the name of the backend to add_compute.
# 
# NOTE: calling run_compute with one of these alternate backends will fail unless you have the necessary code installed on your machine.

# In[27]:


b.add_compute('legacy', compute='legacycompute')


# In[28]:


print b.filter(compute='legacycompute')


# # Exercise

# Add another set of compute options (called, say, 'robust') and set whatever values you think might be necessary.  Run a model and see how much longer it takes to run.

# In[ ]:




