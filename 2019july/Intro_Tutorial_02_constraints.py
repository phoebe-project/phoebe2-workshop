#!/usr/bin/env python
# coding: utf-8

# In this tutorial we will learn about constraints between Parameters and the default parameterization of a binary system.

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# # Constraints

# As we saw in the last exercise, there are 5 Parameters with a qualifier of 'incl'.

# In[5]:


print(b.filter(qualifier='incl'))


# Note that here the previously-mentioned twig-syntax is shown to show as much information as possible about the Parameters.

# Three of these are because there are inclinations defined for the orbit as well as each of the two stars ('primary' and 'secondary').  These three Parameters all have context='component'.

# In[6]:


print(b.filter(qualifier='incl', context='component'))


# The other inclinations of the stars are (by default) *constrained* to be the same as the inclination of the orbit (i.e., an aligned system).  We can see this by the \*s in the output (to the left of the twigs) above as well as by accessing the 'constrained_by' attribute of the Parameter (attempting to call set_value will also raise an error).

# In[7]:


b.get_parameter(qualifier='incl', context='component', component='primary').constrained_by


# The other two Parameters with qualifier='incl' are the constraints themselves and have context='constraint'

# In[8]:


print(b.filter(qualifier='incl', context='constraint'))


# In[9]:


b.get_parameter(qualifier='incl', context='constraint', component='primary')


# Here we see that this is a simple constraint: the inclination of the primary star is being *constrained* to be exactly that of the inclination of the binary orbit.  If we change the inclination of the orbit, the inclinations of the 'primary' and 'secondary' stars will immediately update to reflect that change.

# In[10]:


b.set_value(qualifier='incl', component='binary', value=80)


# In[11]:


print(b.filter(qualifier='incl', context='component'))


# Other constraints are a little more complicated.

# In[12]:


b.get_parameter(qualifier='asini', context='constraint')


# In[13]:


print("asini: {}, sma: {}, incl: {}".format(
    b.get_value(qualifier='asini', component='binary', context='component'),
    b.get_value(qualifier='sma', component='binary', context='component'),
    b.get_value(qualifier='incl', component='binary', context='component')))


# In[14]:


b.set_value(qualifier='sma', component='binary', context='component', value=10.0)


# In[15]:


print("asini: {}, sma: {}, incl: {}".format(
    b.get_value(qualifier='asini', component='binary', context='component'),
    b.get_value(qualifier='sma', component='binary', context='component'),
    b.get_value(qualifier='incl', component='binary', context='component')))


# # Exercise

# Find and list all constraints in the default_binary Bundle

# In[ ]:





# The mass of each star is a constrained Parameter.  Try setting the value of the mass (you should get an error, do **not** try to change the value of the constraint itself).  Then find what it depends on, vary those Parameters, and print the resulting value of the mass.

# In[ ]:





# How q is defined: is it Mprimary/Msecondary or Msecondary/Mprimary?
# 
# Hint: there are (at least) 2 ways to do this.  Try first by looking through the equations of the constraints if you feel a bit daring.  You can also change the value of q and see how the resulting constrained masses react.

# In[ ]:




