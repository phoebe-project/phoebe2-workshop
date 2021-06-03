#!/usr/bin/env python
# coding: utf-8

# In this tutorial, we'll see how to plot the resulting models from within PHOEBE using matplotlib.

# # Setup

# Uncomment the line below if your Jupyter version requires matplotlib inline.

# In[ ]:


#%matplotlib inline


# In[1]:


import phoebe
from phoebe import u,c

import numpy as np
import matplotlib.pyplot as plt


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# # Plotting

# Let's first re-add some simple datasets and run the models

# In[4]:


b.add_dataset('lc', times=np.linspace(0,1,51), dataset='lc01')


# In[5]:


b.add_dataset('rv', times=np.linspace(0,1,21), dataset='rv01')


# In[6]:


b.run_compute()


# Calling plot will attempt to plot all datasets and models in the Bundle, splitting into subplots when needed

# In[7]:


axs, artists = b.plot()


# If we don't want to plot EVERYTHING, we can filter either before or within the plot command

# In[8]:


axs, artists = b.filter(dataset='lc01').plot()


# ### Custom Columns

# By default, PHOEBE will plot flux vs time for light curves and RV vs time for radial velocity datasets.  To override this, we can send the name of the column to x or y.  In addition to the Parameter names, we can also request 'phase'.  This will use the ephemeris of the system and will use t0_supconj by default.

# In[10]:


axs, artists = b.filter(dataset='rv01').plot(x='phase')


# In[11]:


axs, artists = b.filter(dataset='rv01').plot(x='phase', t0='t0_perpass')


# ### Highlighting at a given time

# If you pass a time to the plot call, that time will be highlighted in all datasets.

# In[12]:


axs, artists = b.plot(time=0.65)


# ### And much more...

# The [plotting tutorial](http://phoebe-project.org/docs/2.0/tutorials/plotting/) in the docs has a very thorough explanation of other advanced features in plotting.
# 
# NOTE: plotting in PHOEBE is currently planned to get a major overhaul in one of the upcoming releases.  This will allow for much smarter defaults and more powerful options, but may require some changes to the syntax.

# # Exercise

# Add an orbit dataset and plot different projections of the orbit (z vs x, y vs x, z vs y).  Try changing orbital Parameters (q, incl, long_an), rerun compute, and see the changes to the plots.

# In[ ]:





# Play with plotting.  If you want to try more advanced options, feel free to look at the [plotting tutorial](http://phoebe-project.org/docs/2.0/tutorials/plotting/) in the official docs.

# In[ ]:




