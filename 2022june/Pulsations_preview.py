#!/usr/bin/env python
# coding: utf-8

# ### Preview: pulsations in PHOEBE -- coming soon to a computer near you
# 
# Pulsations in spherical stars can be described by a set of three wavenumbers: radial order $n$, non-radial degree $l$, and longitudinal order $m$. Radial order $n$ gives the number of nodes between the center and the surface of
# the star; non-radial degree $l$ gives the number of all (longitudinal and latitudinal) node lines; and longitudinal order $m$ gives the number of longitudinal node lines (Aerts, Christensen-Dalsgaard, and Kurtz, 2010). Longitudinal order $m$ can assume values from $-l$ to $l$, where $\pm m$ modes correspond to mode chirality and are indistinguishable for spherically symmetric stars because there is no preferred axis, but different for non-symmetric (i.e. rotating, distorted) stars where axial asymmetry breaks the degeneracy. Thus, $l = 0$ modes are radial pulsations, $l = 1$ modes are dipole modes, $l = 2$ are quadrupole modes, etc.

# *PHOEBE support for pulsations has not yet been released. Thus, this is just a preview of the functionality to come in the near future.*

# As usual, let's import phoebe. Note that this is an *unreleased* and *unsupported* version from a development branch.

# In[1]:


import phoebe


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# To demonstrate pulsations, we will use a single star as it keeps things simple. Let's initialize a default star:

# In[3]:


s = phoebe.default_star(starA='pulsator')


# Pulsations in PHOEBE are *features*, similar to spots and gaussian processes covered in [Tutorial 6](Tutorial_06_features.ipynb). They are characterized by radial amplitude (`radamp`), frequency (`freq`), phase (`phase`) and pulsation modes `l` and `m`. For a start let's initialize a radial pulsator ($l=m=0$):

# In[4]:


s.add_feature('pulsation', component='pulsator', feature='puls01', freq=10, phase=0.5, l=0, m=0)


# Let's take a closer look at the pulsation ParameterSet:

# In[5]:


print(s['puls01'])


# One parameter that might have caught your eye is `teffext`; PHOEBE currently modifies the temperature map by following the gravity darkening law, i.e. the local temperature change is caused by the change in $\log g$ as driven by the radial amplitude `radamp`. This is not an accurate physical description of the surface brightness variability (see the talk by Rich Townsend that follows this) -- that is why PHOEBE *will* support external temperature mapping to be provided.

# Now that we have a pulsation on our star, let's compute a mesh in, say, 50 points, and see how it changes:

# In[6]:


s.add_dataset('mesh', times=phoebe.linspace(0, 0.1, 50), passband='Johnson:V', dataset='mesh01')


# Recall from the [meshing tutorial](http://phoebe-project.org/workshops/2021june/Tutorial_05c_meshes.ipynb) that by default the mesh only contains surface element coordinates. That's why we need to add the columns that we are interested in. Let's remind ourselves what our options are:

# In[7]:


print(s['columns@mesh01'].choices)


# Let's add `teffs` for now:

# In[8]:


s['columns@mesh01'] = ['teffs',]


# Now we can compute this model and animate it:

# In[9]:


s.run_compute(model='l0m0')


# In[ ]:


afig, mplfig = s['mesh01@l0m0'].plot(animate=True, save='l0m0.gif', save_kwargs={'writer': 'imagemagick'})


# ![l0m0.gif](attachment:l0m0.gif)

# Now let's color-code this by temperature:

# In[ ]:


afig, mplfig = s['mesh01@l0m0'].plot(animate=True, fc='teffs', ec='gray', save='l0m0_color.gif', save_kwargs={'writer': 'imagemagick'})


# ![l0m0_color.gif](attachment:l0m0_color.gif)

# How about adding a light curve over 10 pulsational cycles? Let's add the dataset and recompute the model:

# In[10]:


s.add_dataset('lc', times=phoebe.linspace(0, 1, 501), passband='Johnson:V', dataset='lc01')


# In[11]:


s.run_compute(model='l0m0', overwrite=True)


# In[12]:


afig, mplfig = s['lc01'].plot(show=True)


# Now let's try something more complicated. Let's change pulsation parameters to, say, $l=5$, $m=-2$, and color-code by temperature:

# In[13]:


s['l@puls01'] = 5
s['m@puls01'] = -2


# In[14]:


s.run_compute(model='l5mn2')


# In[15]:


s['lc01@l5mn2'].plot(show=True)


# In[ ]:


afig, mplfig = s['mesh01@l5mn2'].plot(animate=True, fc='teffs', ec='gray', save='l5mn2.gif', save_kwargs={'writer': 'imagemagick'})


# ![l5mn2.gif](attachment:l5mn2.gif)

# As one last demonstration, let's tilt the star by, say, 15 degrees and let's color-code it by intensities. For that to happen, we need to add intensity to the `columns` array:

# In[16]:


s['columns@mesh01'] += ['intensities@lc01']


# In[17]:


s['incl@pulsator'] = 75


# In[18]:


s.run_compute(model='final')


# Finally, let's animate the mesh:

# In[ ]:


afig, mplfig = s['mesh01@final'].plot(animate=True, show=True, save='puls_final.gif', fc='intensities@lc01', ec='gray', save_kwargs={'writer': 'imagemagick'})


# ![puls_final.gif](attachment:puls_final.gif)

# In[ ]:




