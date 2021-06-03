#!/usr/bin/env python
# coding: utf-8

# In this tutorial we'll introduce the Hierarchy Parameter and see how to create other default systems: both single stars and contact binaries.

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


# # Hierarchy Parameter

# PHOEBE supports more than just detached binary systems, and will eventually support generic hierarchies (triples, quadruples, etc).  The hierarchy for a system is stored as a single Parameter in the Bundle with qualifier='hierarchy' and context='system'.

# In[4]:


b.get_parameter('hierarchy')


# As a shortcut, the hierarchy attribute on the Bundle leads to this same Parameter.

# In[5]:


b.hierarchy


# In[6]:


b.hierarchy.get_value()


# This Parameter simply holds a string, but is parsed to tell the backend the configuration of all the stars and how to connect the different component tags when building the model.  In this default_binary system, this says that we have a binary with two stars, labeled 'primary' and 'secondary' orbiting each other by the orbital parameters defined by component='binary'.
# 
# If you want to change the name of a component, you can do that and all tags and the hierarchy Parameter will update.

# In[7]:


b.change_component('primary', 'starA')


# In[8]:


b.filter(context='component').components


# In[9]:


b.hierarchy.get_value()


# # Single Stars

# In addition to default_binary, PHOEBE also supports other default configurations.  Including a single star via default_star

# In[10]:


b = phoebe.default_star()


# In[11]:


b.hierarchy.get_value()


# # Contact Binaries

# As well as simple support for contact binaries by passing contact_binary=True to default_binary

# In[12]:


b = phoebe.default_binary(contact_binary=True)


# In[13]:


b.hierarchy.get_value()


# Here we actually have an additional component with kind='envelope' and component='contact_envelope' that encompasses the two stars.

# In[14]:


b.filter(component='contact_envelope', context='component').qualifiers


# And some of the Parameters in the individual stars are no longer available

# In[15]:


b.filter(component='primary', context='component').qualifiers


# # Exercise

# What star Parameters are hidden for a contact binary compared to a detached binary?

# In[ ]:




