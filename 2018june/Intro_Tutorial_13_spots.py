#!/usr/bin/env python
# coding: utf-8

# In this tutorial we'll learn how to add spots on a star

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


# # Spots

# Multiple spots can be attached to any given Star in the system.  Because of this, they live in the "feature" context (along with future features such as pulsations).  Adding a spot follows the same syntax as datasets or compute options:

# In[5]:


b.add_feature('spot', component='primary', feature='spot01')


# In[6]:


print b.filter(feature='spot01')


# Note that in 2.0, there is a constraint to constrain the 'colon' (terribly named) Parameter which has been updated in favor of the more accurate 'long'.  In 2.1+, 'colon' will be dropped entirely and is only kept until 2.1 for backwards compatibility reasons.

# As a shortcut, you can call b.add_spot:

# In[7]:


b.add_spot(component='secondary', feature='spot02')


# The spot is parameterized by its location on the star (colat, long), its angular radius, and the relative temperature.

# # Exercise

# Plot a light curve with and without a spot.

# In[ ]:





# Make a mesh plot that shows the presence of a spot.

# In[ ]:




