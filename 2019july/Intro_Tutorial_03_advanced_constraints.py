#!/usr/bin/env python
# coding: utf-8

# Here we will learn how to change the Parameterization such that you can set the value of constrained Parameters (by having the constraint solve for a different Parameter instead).

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# # Advanced Constraints

# In the default binary, there are a significant number of constrained Parameters.

# In[5]:


print(b.filter(context='constraint').qualifiers)


# Let's look at mass, which is *constrained* by default according to Kepler's third law.

# In[6]:


print(b.get_parameter('mass', component='primary', context='component'))


# In[7]:


print(b.get_parameter('mass', component='primary', context='constraint'))


# Here we see the 4 parameters that are involved in Kepler's third law.  PHOEBE allows you to freely set 3 of these 4 (sma, period, q) and automatically uses these values to compute that mass.
# 
# However, let's say that you wanted to set the mass (perhaps you know the mass, but don't know the semi-major axis as well).  This can be done via the 'flip_constraint' method.  The easiest way to use this correctly is to make sure our keywords return the correct Constraint Parameter via 'get_constraint' and then use 'flip_constraint'.

# In[8]:


b.get_constraint(qualifier='mass', component='primary')


# Now we just add `solve_for='sma'` to "flip" this constraint to solve for 'sma' instead of 'mass'.

# In[9]:


b.flip_constraint(qualifier='mass', component='primary', solve_for='sma')


# Now we're allowed to set the mass and we'll see that the value of sma is automatically computed.

# In[10]:


b.set_value('mass', component='primary', value=1.2)


# In[11]:


b.get_value('sma', component='binary', context='component')


# # Exercise

# Flipping constraints could be particularly useful if you have an observational constraint on 'asini' (say from the amplitude of RVs) and want to leave asini fixed as you fit for the inclination.  Flip the constraint so it is possible to adjust the values of both 'asini' and 'incl'.  (**NOTE** you may want to either start fresh or re-flip the Kepler's third law constraint back to solve for mass first).

# In[ ]:





# Now that you can change the value of 'asini', set it to 20 (solar radii... we'll talk about units in the next tutorial), adjust the inclination, and show that 'sma' is adjusting automatically to conserve 'asini'.

# In[ ]:




