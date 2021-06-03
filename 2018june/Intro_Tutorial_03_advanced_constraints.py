#!/usr/bin/env python
# coding: utf-8

# Here we will learn how to change the Parameterization such that you can set the value of constrained Parameters (by having the constraint solve for a different Parameter instead).

# # Setup

# In[2]:


import phoebe
from phoebe import u,c

import numpy as np
import matplotlib.pyplot as plt


# In[3]:


logger = phoebe.logger(clevel='WARNING')


# In[4]:


b = phoebe.default_binary()


# # Advanced Constraints

# In the default binary, there are a significant number of constrained Parameters.

# In[7]:


print b.filter(context='constraint').qualifiers


# One that may standout for anyone who has used PHOEBE Legacy in the past is the 'pot' (potential) Parameter.
# 
# PHOEBE 2 does not (by default) allow for setting the potential, but rather *constrains* the potential via the 'rpole' (polar radius) and other Roche values (the mass-ratio 'q', eccentricity 'ecc', synchronicity parameter 'syncpar', and semi-major axis 'sma').

# In[14]:


b.get_parameter(qualifier='pot', component='primary', context='constraint')


# This was the chosen parameterization for PHOEBE 2 as the polar radius is more physically meaningful and to avoid degeneracies between the potential and other Roche parameters.

# In[16]:


print "pot: {} rpole: {}".format(
    b.get_value(qualifier='pot', component='primary', context='component'),
    b.get_value(qualifier='rpole', component='primary', context='component'))


# In[17]:


b.set_value(qualifier='rpole', component='primary', context='component', value=0.8)


# In[18]:


print "pot: {} rpole: {}".format(
    b.get_value(qualifier='pot', component='primary', context='component'),
    b.get_value(qualifier='rpole', component='primary', context='component'))


# However, let's say that for some reason you wanted to instead constraint 'rpole' via 'pot'.  In most cases, you can *flip* the constraint to solve for some other Parameter (not all parameterizations are supported, especially when they result in infinite loops).
# 
# This is done via the 'flip_constraint' method.  First, let's make sure our filter keywords return the correct Constraint Parameter.

# In[19]:


b.get_constraint(qualifier='pot', component='primary')


# Now we call 'flip_constraint' while passing one of the Parameter qualifiers to 'solve_for'.

# In[20]:


b.flip_constraint(qualifier='pot', component='primary', solve_for='rpole')


# Now we're allowed to set the potential (without an error) and the polar radius adjusts automatically.

# In[21]:


print "pot: {} rpole: {}".format(
    b.get_value(qualifier='pot', component='primary', context='component'),
    b.get_value(qualifier='rpole', component='primary', context='component'))


# In[25]:


b.set_value(qualifier='pot', component='primary', context='component', value=6.3)


# In[26]:


print "pot: {} rpole: {}".format(
    b.get_value(qualifier='pot', component='primary', context='component'),
    b.get_value(qualifier='rpole', component='primary', context='component'))


# # Exercise

# Flipping constraints could be particularly useful if you have an observational constraint on 'asini' (say from the amplitude of RVs) and want to leave asini fixed as you fit for the inclination.  Flip the constraint so it is possible to adjust the values of both 'asini' and 'incl'.

# In[ ]:





# Now that you can change the value of 'asini', set it to 20 (solar radii... we'll talk about units in the next tutorial), adjust the inclination, and show that 'sma' is adjusting automatically to conserve 'asini'.

# In[ ]:




