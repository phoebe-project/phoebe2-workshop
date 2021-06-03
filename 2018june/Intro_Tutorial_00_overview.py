#!/usr/bin/env python
# coding: utf-8

# # Setup

# If running in a Jupyter/IPython notebook, depending on your version, you **may** need to use the following line in order to view plots in the notebook directly.  This is not necessary if running from a Python console or as a script.

# In[1]:


#%matplotlib inline


# Let's import phoebe, numpy, and matplotlib.  We'll also create shortcuts to units (u) and constants (c) used within phoebe.

# In[2]:


import phoebe
from phoebe import u,c

import numpy as np
import matplotlib.pyplot as plt


# Now create a logger instance.  This will print messages to the screen or to a log file.

# In[3]:


logger = phoebe.logger(clevel='WARNING')


# Let's make sure we're using the same version of PHOEBE.  If you're using a slightly different version, *some* of the outputs may be a bit different than you see here.

# In[4]:


print phoebe.__version__


# # Make a default model

# Let's first create a default binary system.

# In[5]:


b = phoebe.default_binary()


# We can then attach datasets for both light curves (lc) and radial velocity curves (rv) with provided times.

# In[6]:


b.add_dataset('lc', times=np.linspace(0,1,51))


# In[7]:


b.add_dataset('rv', times=np.linspace(0,1,21))


# To run the forward model, we call run_compute()

# In[8]:


b.run_compute()


# And to plot all the synthetic datasets in our model, we call plot()

# In[9]:


axs, artists = b.plot(show=True)


# Or to animate we can call animate() with a list of times we want included in the animation.
# 
# (ignore the extra empty figure below the animation in Jupyter notebooks)

# In[10]:


b.animate(times=np.linspace(0,1,11))


# In[ ]:




