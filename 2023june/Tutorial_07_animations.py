#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Animations
# 
# In this tutorial, we'll see how to make simple animations within PHOEBE
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Advanced: Animations](http://phoebe-project.org/docs/latest/tutorials/animations.ipynb)

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# # Animating

# Let's first re-add some simple datasets and run the models

# In[4]:


b.add_dataset('lc', compute_times=phoebe.linspace(0,1,51), dataset='lc01')


# In[5]:


b.add_dataset('rv', compute_times=phoebe.linspace(0,1,21), dataset='rv01')


# In[6]:


b.run_compute()


# By passing `animate=True` and a list of times to b.plot, we can build an animation.  Here we'll save to a gif and then display that gif in the next line (seems to be the most compatible across different versions of Jupyter notebooks).. but you could also try passing `show=True` instead and/or including `%matplotlib notebook` at the top of your notebook.

# In[7]:


afig, mplanim = b.plot(animate=True, times=phoebe.linspace(0,1,21), 
                       save='Tutorial_05b_1.gif', 
                       # save_kwargs={'writer': 'imagemagick'}
                      )


# ![animation](Tutorial_05b_1.gif)

# If we don't want to plot EVERYTHING, we can filter either before or within the plot command

# In[8]:


afig, mplanim = b.plot(dataset='lc01', animate=True, times=phoebe.linspace(0,1,101),
                       save='Tutorial_05b_2.gif', 
                       # save_kwargs={'writer': 'imagemagick'}
                      )


# ![animation](Tutorial_05b_2.gif)

# ### Other Options

# The [animations tutorial](http://phoebe-project.org/docs/latest/tutorials/animations/) in the docs gives many more options.

# In[9]:


afig, mplanim = b.plot(animate=True, times=phoebe.linspace(0,1,51), uncover=True,
                       save='Tutorial_05b_3.gif', 
                       # save_kwargs={'writer': 'imagemagick'}
                      )


# ![animation](Intro_Tutorial_09_3.gif)

# # Exercise

# Turn some of the plots you made in the last tutorial into animations.

# In[ ]:




