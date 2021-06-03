#!/usr/bin/env python
# coding: utf-8

# In this tutorial we'll expose and plot the mesh that PHOEBE uses to compute the model and learn how to create plots/animations of the mesh quantities.

# # Setup

# Uncomment the line below if necessary to see inline plots

# In[1]:


#%matplotlib inline


# In[2]:


import phoebe
from phoebe import u,c


# In[3]:


logger = phoebe.logger(clevel='WARNING')


# In[4]:


b = phoebe.default_binary()


# # Meshes

# We already covered adding a mesh dataset, but now let's look at what gets returned by the model and how to plot meshes.

# In[5]:


b.add_dataset('lc', compute_times=phoebe.linspace(0,1,101), dataset='lc01')


# In[6]:


b.add_dataset('mesh', compute_times=[0, 0.25, 0.5, 0.75], dataset='mesh01')


# In[7]:


print(b.get_parameter('columns', dataset='mesh01').choices)


# In[8]:


b.set_value('columns', value=['teffs', 'loggs', '*intensities*'])


# In[9]:


b.get_value('columns')


# In[10]:


b.get_value('columns', expand=True)


# In[11]:


b.run_compute()


# Let's look at the Parameters in the model that have been tagged with our mesh dataset.

# In[12]:


b.filter(context='model', dataset='mesh01').qualifiers


# Here we see that we have each of our requested columns along with a few default that are required for the geometry of the mesh itself.
# 
# Let's look at the default mesh plot.  Since we have meshes stored at several times, we should provide a single time at which we want the meshes drawn.  Let's choose quarter-phase so that we can see both stars.

# In[13]:


afig, mplfig = b.filter(dataset='mesh01').plot(time=0.25, show=True)


# Now if we want to, we can choose separate columns for facecolor and edgecolor (or pass "None" **as a string** to turn off edges, or "face" to color the same as the faces).

# In[14]:


afig, mplfig = b.filter(dataset='mesh01').plot(time=0.25, fc='teffs', ec="face", show=True)


# If we wanted, we can even override the default "mesh" plot and plot any two columns against each other in a scatter plot.
# 
# **NOTE** if you get a `KeyError: 'z'` error here, this was just fixed on Saturday, so either update or pass `z=0` below.

# In[15]:


afig, mplfig = b.filter(dataset='mesh01').plot(time=0.25, x='loggs', y='teffs', show=True)


# All the Parameters tagged in the model with dataset='mesh01' are passband-*independent*.  Passband-*dependent* Parameters are exposed as well, but they are tagged with the lc/rv dataset instead (but still with kind='mesh' instead of kind='lc' or 'rv').  To see all of these, let's filter on kind='mesh' instead of dataset='mesh01'.  These will only be available for times that occur in **both** the lc and mesh datasets.

# In[16]:


b.filter(context='model', kind='mesh').datasets


# In[17]:


b.filter(context='model', kind='mesh', dataset='lc01').qualifiers


# Here we see the Parameters for our light curve.  These are the local quantities needed to obtain the final integrated flux at this single time.  We can use these as facecolor/edgecolor as well, but need to change our filter a bit so that they're included.

# In[18]:


afig, mplfig = b.filter(kind='mesh').plot(time=0.25, fc='abs_normal_intensities', 
                                          ec="face", show=True)


# # Exercise

# Make a mesh plot (at any single time) to show the limb-darkening across the surface of the star.  Play with changing the underlying limb-darkening model and re-plotting.

# In[ ]:





# Try making an animation with the meshes.

# In[ ]:




