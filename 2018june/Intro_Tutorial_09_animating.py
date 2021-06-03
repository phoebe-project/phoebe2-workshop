#!/usr/bin/env python
# coding: utf-8

# In this tutorial, we'll see how to make simple animations within PHOEBE

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


# # Animating

# Let's first re-add some simple datasets and run the models

# In[4]:


b.add_dataset('lc', times=np.linspace(0,1,51), dataset='lc01')


# In[5]:


b.add_dataset('rv', times=np.linspace(0,1,21), dataset='rv01')


# In[6]:


b.run_compute()


# b.animate takes essentially the same arguments as b.plot, except it also requires a list of times (one time will be used per-frame of the animation).

# In[7]:


b.animate(times=np.linspace(0,1,21))


# If we don't want to plot EVERYTHING, we can filter either before or within the plot command

# In[8]:


b.filter(dataset='lc01').animate(times=np.linspace(0,1,101))


# ### Other Options

# The [animations tutorial](http://phoebe-project.org/docs/2.0/tutorials/animations/) in the docs gives many more options.

# In[9]:


b.animate(times=np.linspace(0,1,51), uncover=True)


# # Exercise

# Turn some of the plots you made in the last tutorial into animations.

# In[ ]:




