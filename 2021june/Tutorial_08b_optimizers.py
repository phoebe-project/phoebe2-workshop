#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Optimizers
# 
# In this tutorial we will continue the fitting process by optimizing our results from the previous tutorial. 
# 
# Specifically we will cover:
# 
# - optimizer.nelder_mead
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Advanced: Nelder-Mead Optimizer](http://phoebe-project.org/docs/2.3/tutorials/nelder_mead)
# 
# 

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
# Mac users may need to turn multi-processing off
#phoebe.multiprocessing_off() 
logger = phoebe.logger('error')


# You may need to update the path below to where you saved the bundle from the previous tutorial, or you can download [after_estimators.bundle](https://github.com/phoebe-project/phoebe2-workshop/raw/2021june/data/synthetic/after_estimators.bundle).

# In[2]:


#Load Previous Bundle
b = phoebe.open('data/synthetic/after_estimators.bundle')


# In[3]:


#First let's look at our final fit from the previous bundle
b.run_compute('phoebe01', model='after_estimators')


# In[4]:


b.plot(model='after_estimators', x='phases', show=True)


# In[5]:


#Create a new compute parameter set 
b.add_compute(compute='nm_fit')


# In[6]:


# Change fitting options for faster model computation
b.set_value('irrad_method', compute='nm_fit', value='none')
b.set_value_all('rv_method', compute='nm_fit', value='dynamical')
b.set_value_all('distortion_method', compute='nm_fit', value='sphere')


# In[7]:


# Add compute phases and reduce model computation speed
b.flip_constraint('compute_phases@rv01', solve_for='compute_times@rv01')
comp_phases = np.linspace(0,1,25)
b.set_value_all('compute_phases', dataset='rv01', value=comp_phases)


# Phoebe has three optimizer methods: 
# 
# conjugate gradient (optimizer.cg)
# 
# powell (optimizer.powell) 
# 
# nelder_mead (optimizer.nelder_mead) 
# 
# In most cases nelder_mead is the most efficient and useful so this is the one we will use moving forward. However, the logic is almost identical if you would like to try a different one. 

# In[8]:


#Add optimizer
b.add_solver('optimizer.nelder_mead',  solver='nm_solver', compute='nm_fit')


# In[9]:



#change max iterations
b.set_value('maxiter', solver='nm_solver', value=20)


# In[10]:


#disable lc and fit rvs
b.disable_dataset('lc01')


# In[11]:


#check rv values and adjust
print(b.filter('ecc@binary'))


# In[12]:


#set ecc to 0
b.set_value('ecc', component='binary', value=0.)


# In[13]:


#set fit parameters
fit_params = ['vgamma@system', 't0_supconj@binary', 'q@binary', 'asini@binary']
b.set_value('fit_parameters', fit_params)


# In[14]:


#run solver
b.run_solver('nm_solver', solution='nm_solution', overwrite=True)


# We can check on the reasonableness of the fit with the keyword trial_run = True. This let's us see what the new values are without having to adopt them first. 

# In[15]:


#check updated fitted parameters
print(b.adopt_solution('nm_solution', trial_run=True))


# In[16]:


#compute model and check fit
b.run_compute('nm_fit', solution='nm_solution', model='after_nm', sample_num=1)


# You'll notice a new parameter in run computer "sample_num". When you are computing values from a solution it will generally compute multiple times, which is useful when the parameters have an associated distribution.  This will be useful for mcmc, but for now we will just set it to 1.

# In[17]:


b.plot(kind='rv', model='after_nm', x='phases', show=True, legend=True, marker = 'o')
b.plot( kind='rv', model='after_nm', x='phases', y='residuals', show=True, legend=True, marker = 'o')


# In[18]:


b.adopt_solution('nm_solution')


# In[19]:


#fit lc
b.disable_dataset('rv01')
b.enable_dataset('lc01')


# Now we want to reduce the number of points that we need to compute. One easy way to do this is to only fit the eclipses. So let's  use our previous lc geometry solution to mask everything else. 

# In[20]:


print(b.filter('lcgeom_solution'))


# In[21]:


adopt_parameters = ['mask_phases']
b.set_value(solution = 'lcgeom_solution', qualifier='adopt_parameters', 
            value=adopt_parameters)
b.adopt_solution('lcgeom_solution')


# In[22]:


b.plot(kind='lc', model='after_estimators', x='phases', show='True')


# In[23]:


#switch back from requivsumfrac to a primary radius
b.flip_constraint('requiv@primary', solve_for='requivsumfrac@binary')


# In[24]:


fit_params = ['teffratio@binary', 't0_supconj@binary', 'incl@binary']
b.set_value('fit_parameters', fit_params)


# In[25]:


#change max iterations
b.set_value('maxiter', solver='nm_solver', value=15)


# In[26]:


b.run_solver('nm_solver', solution='nm_solution', overwrite=True)


# In[27]:


print(b.adopt_solution('nm_solution', trial_run=True))


# In[28]:


b.run_compute('nm_fit', solution='nm_solution', model='after_nmlc', sample_num=1)

b.plot(kind='lc', model='after_nmlc', x='phases', show=True, legend=True, marker = 'o')
b.plot(kind='lc', model='after_nmlc', x='phases', y='residuals', show=True, legend=True, marker = 'o')


# In[29]:


b.adopt_solution('nm_solution')


# In[30]:


#look more closely at the primary eclipse
b.plot(kind='lc', x='phases', model='after_nmlc', xlim=[-0.2,0.2], show=True, legend=True, marker = 'o')
b.plot(kind='lc', x='phases', model='after_nmlc', xlim=[-0.2,0.2], y='residuals', show=True, legend=True, marker = 'o')


# # Exercise
# 
# Combine both light and rv curves to achieve a better fit, primarily within the eclipse. Hint: It's often better to fit a small number of parameters first. 

# In[ ]:




