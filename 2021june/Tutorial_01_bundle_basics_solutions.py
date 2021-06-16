#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial Example Solutions: General Concepts & Bundle Basics
# 
# These are just an example of the many possible solutions to the exercises in [Workshop Tutorial: General Concepts & Bundle Basics](./Tutorial_01_bundle_basics.ipynb)

# In[1]:


import phoebe
b = phoebe.default_binary()


# Find and access the value of the effective temperature of the primary star via filtering and twig access.

# In[2]:


print(b.filter(component='primary'))


# In[3]:


print(b.get_parameter(qualifier='teff', component='primary'))


# Find the choices for the `atm` Parameter

# In[4]:


b.filter(qualifier='atm')


# In[5]:


print(b.get_parameter(qualifier='atm', component='primary').choices)


# Find what the `ltte` Parameter stands for.  Does it have choices?

# In[6]:


b.filter(qualifier='ltte')


# In[7]:


print(b.get_parameter(qualifier='ltte').get_description())


# In[8]:


#print(b.get_parameter(qualifier='ltte').get_choices())


# In[9]:


type(b.get_parameter(qualifier='ltte'))


# Change the default unit of the argument of periastron from degrees to radians and print the result with the new units.

# In[10]:


print(b.filter(component='binary'))


# In[11]:


print(b.filter(component='binary').info)


# In[12]:


print(b.get_parameter(qualifier='per0'))


# In[13]:


b.get_parameter(qualifier='per0').set_default_unit(phoebe.u.rad)


# In[14]:


print(b.get_quantity(qualifier='per0'))


# Set the default_unit for all radii and smas of all components to AU and then show their values. (Hint: you can also call set_default_unit_all to act on a ParameterSet instead of a Parameter)

# In[15]:


print(b.filter(context='component').info)


# In[16]:


print(b.filter(qualifier=['sma', 'requiv'], context='component'))


# In[17]:


b.filter(qualifier=['sma', 'requiv'], context='component').set_default_unit_all('AU')


# In[18]:


print(b.filter(qualifier=['sma', 'requiv'], context='component'))


# Find and set the following Parameters:
# * effective temperature of the secondary star to 5500 K
# * inclination of the binary to 86 degrees

# In[19]:


print(b.filter(qualifier='teff'))


# In[20]:


b.set_value(qualifier='teff', component='secondary', value=5500)


# In[21]:


print(b.filter(qualifier='incl'))


# In[22]:


b.set_value(qualifier='incl', component='binary', value=86)


# You likely noticed that there are several (5!) Parameters in the Bundle for inclination.  This is because there is an inclination for the orbit as well as for each of the two stars in the binary system.  The other 2 are called Constraints which relate these Parameters to each other... which will be the topic of the next tutorial.
