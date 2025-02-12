#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Accessing and Plotting Meshes
# 
# In this tutorial we'll expose and plot the mesh that PHOEBE uses to compute the model and learn how to create plots/animations of the mesh quantities.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Advanced: Accessing and Plotting Meshes](http://phoebe-project.org/docs/2.4/tutorials/meshes.ipynb)

# # Setup

# Uncomment the line below if necessary to see inline plots

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


import phoebe
from phoebe import u,c


# In[ ]:


logger = phoebe.logger(clevel='WARNING')


# In[ ]:


b = phoebe.default_binary()


# # Meshes

# We already covered adding a mesh dataset, but now let's look at what gets returned by the model and how to plot meshes.

# In[ ]:


b.add_dataset('lc', compute_times=phoebe.linspace(0,1,101), dataset='lc01')


# In[ ]:


b.add_dataset('mesh', compute_times=[0, 0.25, 0.5, 0.75], dataset='mesh01')


# In[ ]:


print(b.get_parameter('columns', dataset='mesh01').choices)


# To see an explanation of these various choices, see the [mesh dataset tutorial](http://phoebe-project.org/docs/2.4/tutorials/MESH).

# In[ ]:


b.set_value('columns', value=['teffs', 'loggs', '*intensities*'])


# In[ ]:


b.get_value('columns')


# In[ ]:


b.get_value('columns', expand=True)


# In[ ]:


b.run_compute()


# Let's look at the Parameters in the model that have been tagged with our mesh dataset.

# In[ ]:


b.filter(context='model', dataset='mesh01').qualifiers


# Here we see that we have each of our requested columns along with a few default that are required for the geometry of the mesh itself.
# 
# Let's look at the default mesh plot.  Since we have meshes stored at several times, we should provide a single time at which we want the meshes drawn.  Let's choose quarter-phase so that we can see both stars.

# In[ ]:


afig, mplfig = b.filter(dataset='mesh01').plot(time=0.25, show=True)


# Now if we want to, we can choose separate columns for facecolor (`fc`) and edgecolor (`ec`).  To turn off edges entirely pass `ec="None"` (as a string) or `ec="face"` to use the same color as the faces.

# In[ ]:


afig, mplfig = b.filter(dataset='mesh01').plot(time=0.25, fc='teffs', ec="face", show=True)


# If we wanted, we can even override the default "mesh" plot and plot any two columns against each other in a scatter plot.

# In[ ]:


afig, mplfig = b.filter(dataset='mesh01').plot(time=0.25, x='loggs', y='teffs', show=True)


# All the Parameters tagged in the model with `dataset='mesh01'` are passband-*independent*.  Passband-*dependent* Parameters are exposed as well, but they are tagged with the lc/rv dataset instead (but still with `kind='mesh'` instead of `kind='lc'` or `'rv'`).  To see all of these, let's filter on `kind='mesh'` instead of `dataset='mesh01'`.  These will only be available for times that occur in **both** the lc and mesh datasets.

# In[ ]:


b.filter(context='model', kind='mesh').datasets


# In[ ]:


b.filter(context='model', kind='mesh', dataset='lc01').qualifiers


# Here we see the Parameters for our light curve.  These are the local quantities needed to obtain the final integrated flux at this single time.  We can use these as facecolor/edgecolor as well, but need to change our filter a bit so that they're included.

# In[ ]:


afig, mplfig = b.filter(kind='mesh').plot(time=0.25, fc='abs_normal_intensities', 
                                          ec="face", show=True)


# You can also change the colormaps by passing `fcmap` or `ecmap` as a valid [matplotlib colormap name](https://matplotlib.org/stable/tutorials/colors/colormaps.html) and can show the scale of the colormaps by passing `draw_sidebars=True` when plotting.

# # Exercise

# Make a mesh plot (at any single time) to show the limb-darkening across the surface of the star.  Play with changing the underlying limb-darkening model and re-plotting.

# In[ ]:





# Try making an animation with the meshes.

# In[ ]:




