#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial Example Solutions: Plotting
# 
# These are just an example of the many possible solutions to the exercises in [Workshop Tutorial: Plotting](./Tutorial_05_plotting.ipynb)

# In[1]:


import phoebe
b = phoebe.default_binary()


# Add an orbit dataset and plot different projections of the orbit (u vs w, u vs v, w vs v).  Try changing orbital Parameters (q, incl, long_an), rerun compute, and see the changes to the plots.

# In[2]:


b.add_dataset('orb', compute_phases=phoebe.linspace(0,1,501))
b.set_value('q', 0.8) # just so the orbits don't always overlap
b.run_compute()


# In[3]:


_ = b.plot(x='ws', y='us', show=True)


# In[4]:


_ = b.plot(x='us', y='vs', show=True)


# In[5]:


b.set_value('incl', component='binary', value=85)
b.run_compute(model='changed_incl')


# In[6]:


_ = b.plot(x='us', y='vs', legend=True, show=True)


# Play with plotting.  If you want to try more advanced options, feel free to look at the [plotting tutorial](http://phoebe-project.org/docs/2.3/tutorials/plotting/) in the official docs.
