#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial Example Solutions: Constraints
# 
# These are just an example of the many possible solutions to the exercises in [Workshop Tutorial: Constraints](./Tutorial_02_constraints.ipynb)

# In[1]:


import phoebe
b = phoebe.default_binary()


# **How is q defined: is it Mprimary/Msecondary or Msecondary/Mprimary?**
# 
# Hint: there are (at least) 2 ways to do this.  Try first by looking through the equations of the constraints if you feel a bit daring.  You can also change the value of q and see how the resulting constrained masses react.

# In[2]:


print(b.filter(qualifier=['q', 'mass']))


# Here we can see by comparing to Kepler's third law that it is `q = M2/M1`, but let's also show that by changing `q`.

# In[3]:


b.set_value('q', 0.9)


# In[4]:


print(b.filter(qualifier='mass', context='component'))


# **Flipping constraints could be particularly useful if you have an observational constraint on 'asini' (say from the amplitude of RVs) and want to leave asini fixed as you fit for the inclination.  Flip the constraint so it is possible to adjust the values of both 'asini' and 'incl'.**  (**NOTE** you may want to either start from a fresh bundle or re-flip the Kepler's third law constraint back to solve for mass first).

# In[5]:


b = phoebe.default_binary()


# In[6]:


print(b.filter(qualifier=['sma', 'asini', 'incl'], component='binary'))


# In[7]:


b.get_constraint('asini', component='binary')


# In[8]:


b.flip_constraint('asini', component='binary', solve_for='sma')


# **Now that you can change the value of 'asini', set it to 20 (solar radii... we'll talk about units in the next tutorial), adjust the inclination, and show that 'sma' is adjusting automatically to conserve 'asini'.**

# In[9]:


b.set_value('asini', component='binary', value=20)


# In[10]:


b.set_value('incl', component='binary', value=85)


# In[11]:


print(b.filter(qualifier=['sma', 'asini', 'incl'], component='binary'))


# In[ ]:




