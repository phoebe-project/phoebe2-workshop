#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Constraints
# 
# In this tutorial we will learn about constraints between Parameters and the default parameterization of a binary system.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Constraints](http://phoebe-project.org/docs/latest/tutorials/constraints.ipynb)
# * [Advanced: Constraints and Changing Hierarchies](http://phoebe-project.org/docs/latest/tutorials/constraints_hierarchies.ipynb)
# * [Advanced: Built-In Constraints](http://phoebe-project.org/docs/latest/tutorials/constraints_builtin.ipynb)

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary(force_build=True)


# # Constraints

# As we saw in the last exercise, there are 5 Parameters with a qualifier of `incl`.

# In[4]:


print(b.filter(qualifier='incl'))


# Note that here the previously-mentioned twig-syntax is shown to show as much information as possible about the Parameters.

# Three of these are because there are inclinations defined for the orbit as well as each of the two stars ('primary' and 'secondary').  These three Parameters all have `context='component'`.

# In[5]:


print(b.filter(qualifier='incl', context='component'))


# The other inclinations of the stars are (by default) *constrained* to be the same as the inclination of the orbit (i.e., an aligned system).  We can see this by the `C` in the output (to the left of the twigs) above as well as by accessing the `constrained_by` attribute of the Parameter (attempting to call `set_value` will also raise an error).

# In[6]:


b.get_parameter(qualifier='incl', context='component', component='primary').constrained_by


# The other two Parameters with `qualifier='incl'` are the constraints themselves and have `context='constraint'`

# In[7]:


print(b.filter(qualifier='incl', context='constraint'))


# In[8]:


b.get_parameter(qualifier='incl', context='constraint', component='primary')


# Here we see that this is a simple constraint: the inclination of the primary star is being *constrained* to be exactly that of the inclination of the binary orbit (since the `pitch` is set to zero).  If we change the inclination of the orbit, the inclinations of the 'primary' and 'secondary' stars will immediately update to reflect that change.

# In[9]:


b.set_value(qualifier='incl', component='binary', value=80)


# In[10]:


print(b.filter(qualifier='incl', context='component'))


# Other constraints are a little more complicated.

# In[11]:


b.get_parameter(qualifier='asini', component='binary', context='constraint')


# In[12]:


print("asini: {}, sma: {}, incl: {}".format(
    b.get_value(qualifier='asini', component='binary', context='component'),
    b.get_value(qualifier='sma', component='binary', context='component'),
    b.get_value(qualifier='incl', component='binary', context='component')))


# In[13]:


b.set_value(qualifier='sma', component='binary', context='component', value=10.0)


# In[14]:


print("asini: {}, sma: {}, incl: {}".format(
    b.get_value(qualifier='asini', component='binary', context='component'),
    b.get_value(qualifier='sma', component='binary', context='component'),
    b.get_value(qualifier='incl', component='binary', context='component')))


# # Re-Parameterizing or "Flipping" Constraints

# In the default binary, there are a significant number of constrained Parameters.

# In[15]:


print(b.filter(context='constraint').qualifiers)


# Let's look at mass, which is _constrained_ by default according to Kepler's third law.

# In[16]:


print(b.get_parameter('mass', component='primary', context='component'))


# In[17]:


print(b.get_parameter('mass', component='primary', context='constraint'))


# Here we see the 4 parameters that are involved in Kepler's third law. PHOEBE allows you to freely set 3 of these 4 (sma, period, q) and automatically uses these values to compute that mass.
# 
# However, let's say that you wanted to set the mass (perhaps you know the mass, but don't know the semi-major axis as well). This can be done via the `flip_constraint` method. The easiest way to use this correctly is to make sure our keywords return the correct Constraint Parameter via `get_constraint` and then use `flip_constraint`.

# In[18]:


b.get_constraint(qualifier='mass', component='primary')


# Now we just add `solve_for='sma'` to "flip" this constraint to solve for 'sma' instead of 'mass'.

# In[19]:


b.flip_constraint(qualifier='mass', component='primary', solve_for='sma')


# Now we're allowed to set the mass and we'll see that the value of sma is automatically computed.

# In[20]:


b.set_value('mass', component='primary', value=1.2)


# In[21]:


b.get_value('sma', component='binary', context='component')


# # Exercise

# How is q defined: is it Mprimary/Msecondary or Msecondary/Mprimary?
# 
# Hint: there are (at least) 2 ways to do this.  Try first by looking through the equations of the constraints if you feel a bit daring.  You can also change the value of q and see how the resulting constrained masses react.

# In[ ]:





# Flipping constraints could be particularly useful if you have an observational constraint on 'asini' (say from the amplitude of RVs) and want to leave asini fixed as you fit for the inclination.  Flip the constraint so it is possible to adjust the values of both 'asini' and 'incl'.  (**NOTE** you may want to either start from a fresh bundle or re-flip the Kepler's third law constraint back to solve for mass first).

# In[ ]:





# Now that you can change the value of 'asini', set it to 20 (solar radii... we'll talk about units in the next tutorial), adjust the inclination, and show that 'sma' is adjusting automatically to conserve 'asini'.

# In[ ]:




