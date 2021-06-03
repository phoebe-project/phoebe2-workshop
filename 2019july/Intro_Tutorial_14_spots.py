#!/usr/bin/env python
# coding: utf-8

# In this tutorial we'll learn how to add spots on a star

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# # Spots

# Multiple spots can be attached to any given Star in the system.  Because of this, they live in the "feature" context (along with future features such as pulsations).  Adding a spot follows the same syntax as datasets or compute options:

# In[4]:


b.add_feature('spot', component='primary', feature='spot01')


# In[5]:


print(b.filter(feature='spot01'))


# As a shortcut, you can call b.add_spot:

# In[6]:


b.add_spot(component='secondary', feature='spot02')


# The spot is parameterized by the colatitude (where 0 is defined as the North (spin) Pole) and longitude (where 0 is defined as pointing towards the other star for a binary, or to the observer for a single star) of its center, its angular radius, and the ratio of temperature of the spot to the local intrinsic value.

# # Exercise

# Plot a light curve with and without a spot.

# In[ ]:





# Make a mesh plot that shows the presence of a spot and get comfortable with how the coordinate system is defined.  Try for both binary systems and single stars.

# In[ ]:




