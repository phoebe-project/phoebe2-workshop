#!/usr/bin/env python
# coding: utf-8

# # \#1: Sun-Jupiter Example Solution

# # Data we will need
# mass of Jupiter = 1.898 × 10^27 kg
# 
# dist Jupiter to the Sun 778600627.2km
# 
# orbital period 12 years
# 
# sun rotation period = 25 days
# 
# jupiter rotation period = 10 hours
# 

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# In[4]:


# we are going to need to set 3 periods.  1 orbital and 2 rotation


# In[5]:


print( b.filter(qualifier='period') )


# In[6]:


b.flip_constraint(qualifier='period', component='secondary', solve_for='syncpar@secondary')


# In[7]:


b.flip_constraint(qualifier='period', component='primary', solve_for='syncpar@primary')


# In[8]:


b.set_value('period@primary', 25)
b.set_value('period@secondary', 10, unit=u.hr)
b.set_value('period@binary', 12, unit=u.yr)


# In[9]:


# now let's flip the constraints on the primary and secondary mass


# In[10]:


b.flip_constraint(qualifier='mass', component='primary', solve_for='sma')


# In[11]:


b.flip_constraint(qualifier='mass', component='secondary', solve_for='q')


# In[12]:


b.set_value('mass@primary', 1.0)
b.set_value('mass@secondary', 1.898e27, unit=u.kg)


# In[13]:


# let's get the value of the sma for this orbit to see how close it is to Jupiter's orbital radius


# In[14]:


b.get_value('sma@component@binary',  unit=u.km)


# In[15]:


b.get_value('sma@component@secondary',  unit=u.km)


# In[16]:


# very useful function


# In[17]:


u.solMass.find_equivalent_units()


# In[18]:


#so we could have used Jupiter mass for setting the mass!

