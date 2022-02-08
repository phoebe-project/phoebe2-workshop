#!/usr/bin/env python
# coding: utf-8

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
# Mac users may need to turn multi-processing off
#phoebe.multiprocessing_off() 
logger = phoebe.logger('error')


# In[2]:


b = phoebe.load('synthetic/optimizers_before_exercise.bundle')


# Exercise: Combine both light and rv curves to achieve a better fit, primarily within the eclipse. Hint: It's often better to fit a small number of parameters first. 

# In[3]:


#add rv back 
b.enable_dataset('rv01')


# In[4]:



fit_params = ['t0_supconj@binary', 'teffratio@binary', 'asini@binary', 'incl@binary']
b.set_value('fit_parameters', fit_params)


# In[5]:


b.run_solver('nm_solver', solution='nm_solution', overwrite=True)


# In[6]:


print(b.adopt_solution('nm_solution', trial_run=True))


# In[7]:




b.run_compute('nm_fit', sample_from='nm_solution', sample_num=1)


# In[8]:



b.plot(kind='lc', x='phases', show=True, legend=True, marker = 'o')
b.plot(kind='lc', x='phases', y='residuals', show=True, legend=True, marker = 'o')
b.plot(kind='rv', x='phases', show=True, legend=True, marker = 'o')


# In[9]:


b.adopt_solution('nm_solution')


# In[10]:


#Different set of parameters
fit_params = ['teffratio@binary', 'requiv@primary', 'requivratio@binary']
b.set_value('fit_parameters', fit_params)


# In[11]:


b.run_solver('nm_solver', solution='nm_solution', overwrite=True)


# In[12]:


print(b.adopt_solution('nm_solution', trial_run=True))


# In[13]:


#%%timeit -r 1 -n 1

b.run_compute('nm_fit', sample_from='nm_solution', sample_num=1)


# In[14]:



b.plot(kind='lc', x='phases', xlim=[-0.08,0.08], show=True, legend=True, marker = 'o')
b.plot(kind='lc', x='phases', xlim=[-0.5,-0.45], show=True, legend=True, marker = 'o')
b.plot(kind='lc', x='phases', y='residuals', show=True, legend=True, marker = 'o')
b.plot(kind='rv', x='phases', show=True, legend=True, marker = 'o')


# In[15]:


b.adopt_solution('nm_solution')


# In[16]:


b.save('synthetic/after_optimizers.bundle')


# In[ ]:




