#!/usr/bin/env python
# coding: utf-8

# In this tutorial we will learn about how units are handled in the frontend and how to translate between different units.

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# # Units

# As you probably noticed in the last exercise when setting asini=20, the default units were in solar radii.  However, the default units are not always the most convenient, so let's discuss PHOEBE's handling of unit conversions.
# 
# Instead of flipping the constraint over again, let's look at the sma (semi-major axis) Parameter.

# In[4]:


b.get_parameter(qualifier='sma', component='binary', context='component')


# From the representation above, we can already see that the units are in solar radii.  We can access the units directly via the key in the Parameter.

# In[5]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_default_unit()


# Calling get_value returns only the float of the value in these units.

# In[6]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value()


# Alternatively, you can access an [astropy quantity](http://docs.astropy.org/en/stable/units/) object that contains the value and unit by calling get_quantity

# In[7]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# Both get_value and get_quantity also accept a unit argument which will return the value or quantity in the requested units (if able to convert).  This unit argument takes either a unit object (we imported a forked version of astropy units from within PHOEBE) or a string representation that can be parsed.

# In[8]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value(unit=u.km)


# In[9]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity(unit='km')


# Similarly when setting the value, you can provide either a Quantity object or a value and unit.  These will still be stored within PHOEBE according to the default_unit of the Parameter object.

# In[10]:


b.get_parameter(qualifier='sma', component='binary', context='component').set_value(3800000*u.km)


# In[11]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# In[12]:


b.get_parameter(qualifier='sma', component='binary', context='component').set_value(3900000, unit='km')


# In[13]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# If for some reason you want to change the default units, you can, but just be careful that this could cause some float-point precision issues.

# In[14]:


b.get_parameter(qualifier='sma', component='binary', context='component').set_default_unit('mm')


# In[15]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# In[16]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity(unit='solRad')


# # Exercise

# Change the default parameter of the argument of periastron from degrees to radians and print the result with the new units.

# In[ ]:





# Set the default_unit for all radii and smas of all components to AU and then show their values.  (Hint: you can also call set_default_unit_all to act on a ParameterSet instead of a Parameter)

# In[ ]:




