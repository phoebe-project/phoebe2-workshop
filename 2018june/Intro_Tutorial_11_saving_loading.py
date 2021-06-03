#!/usr/bin/env python
# coding: utf-8

# In this tutorial we'll cover how to save and load a Bundle as well as how to import from and export to a PHOEBE 1 file.

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


# # Saving a Bundle

# Saving a bundle to a file is as simple as calling the save method and passing a filename.

# In[4]:


b.save('test.phoebe')


# We can now inspect the contents of the created file.
# 
# This file is in the JSON-format and is simply a list of dictionaries - where each dictionary represents the attributes of a single Parameter.
# 
# You could edit this file in a text-editor - but do be careful if changing any of the tags. For example: if you want to change the component tag of one of your stars, make sure to change ALL instances of the component tag to match.

# In[5]:


get_ipython().system('head -30 test.phoebe')


# # Loading a Bundle

# To reload a Bundle from a file, we'll use phoebe.load instead of default_binary

# In[6]:


b = phoebe.load('test.phoebe')


# # Exporting to PHOEBE Legacy

# PHOEBE also supports exporting the the file format required by other backends - including PHOEBE legacy.  Note that not all Parameters can directly be translated and not all physics in PHOEBE 2 is supported by legacy.

# In[7]:


b.export_legacy('test_legacy.phoebe')


# In[8]:


get_ipython().system('head -30 test_legacy.phoebe')


# # Importing from PHOEBE Legacy

# Similarly, we can import a file created in PHOEBE Legacy (including in the GUI) into a PHOEBE 2 Bundle.  Here we'll use phoebe.from_legacy instead of default_binary

# In[9]:


b = phoebe.from_legacy('test_legacy.phoebe')


# # Exercise

# If you have any PHOEBE legacy files, try to import them.

# In[ ]:





# Try to change some values in the saved Bundle and make sure you can re-load the Bundle successfully.

# In[ ]:




