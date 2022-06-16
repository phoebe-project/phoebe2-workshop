#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial Example Solutions: Animations
# 
# These are just an example of the many possible solutions to the exercises in [Workshop Tutorial: Animations](./Tutorial_05b_animations.ipynb)

# In[5]:


import phoebe
b = phoebe.default_binary()


# **Turn some of the plots you made in the last tutorial into animations.**

# In[6]:


b.add_dataset('orb', compute_phases=phoebe.linspace(0,1,501))
b.set_value('q', 0.8) # just so the orbits don't always overlap
b.run_compute()


# In[7]:


_ = b.plot(x='ws', y='us', animate=True, times=phoebe.linspace(0,1,21), 
           save='Tutorial_05b_solutions.gif', 
           # save_kwargs={'writer': 'imagemagick'}
          )


# ![animation](Tutorial_05b_solutions.gif)

# In[ ]:




