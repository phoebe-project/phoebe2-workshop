#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Plotting
# 
# In this tutorial, we'll see how to plot the resulting models from within PHOEBE using matplotlib.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Plotting](http://phoebe-project.org/docs/2.3/tutorials/plotting.ipynb)
# * [Advanced: Plotting Options](http://phoebe-project.org/docs/2.3/tutorials/plotting_advanced.ipynb)
# 

# # Setup

# Uncomment the line below if your Jupyter version requires matplotlib inline.

# In[1]:


#%matplotlib inline


# In[2]:


import phoebe
from phoebe import u,c


# In[3]:


logger = phoebe.logger(clevel='WARNING')


# In[4]:


b = phoebe.default_binary()


# # Plotting

# Let's first re-add some simple datasets and run the models

# In[5]:


b.add_dataset('lc', compute_times=phoebe.linspace(0,1,51), dataset='lc01')


# In[6]:


b.add_dataset('rv', compute_times=phoebe.linspace(0,1,21), dataset='rv01')


# In[7]:


b.run_compute()


# Calling `b.plot` will attempt to plot all datasets and models in the Bundle, splitting into subplots when needed

# In[8]:


afig, mplfig = b.plot(show=True)


# If we don't want to plot EVERYTHING, we can filter either before or within the plot command

# In[9]:


afig, mplfig = b.filter(dataset='lc01').plot(show=True)


# ### Custom Columns

# By default, PHOEBE will plot flux vs time for light curves and RV vs time for radial velocity datasets.  To override this, we can send the name of the column to `x` or `y`.  In addition to the Parameter names, we can also request `'phase'`.  This will use the ephemeris of the system and will use `t0_supconj` by default.

# In[10]:


afig, mplfig = b.filter(dataset='rv01').plot(x='phase', show=True)


# In[11]:


afig, mplfig = b.filter(dataset='rv01').plot(x='phase', t0='t0_perpass', show=True)


# ### Highlighting at a given time

# If you pass a time to the plot call, that time will be highlighted in all datasets.

# In[12]:


afig, mplfig = b.plot(time=0.65, show=True)


# ### And much more...

# The [plotting tutorial](http://phoebe-project.org/docs/2.3/tutorials/plotting/) in the docs has a very thorough explanation of other advanced features in plotting.

# # Exercise

# Add an orbit dataset and plot different projections of the orbit (u vs w, u vs v, w vs v).  Try changing orbital Parameters (q, incl, long_an), rerun compute, and see the changes to the plots.

# In[ ]:





# Play with plotting.  If you want to try more advanced options, feel free to look at the [plotting tutorial](http://phoebe-project.org/docs/2.3/tutorials/plotting/) in the official docs.

# In[ ]:




