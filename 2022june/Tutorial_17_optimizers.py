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
# * [Advanced: Nelder-Mead Optimizer](http://phoebe-project.org/docs/2.4/tutorials/nelder_mead)
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


# It's useful to remind ourselves what models and compute options we have in the bundle:

# In[5]:


print(b.models, b.computes)


# Now let's take a quick look at our final fit from the previous bundle:

# In[10]:


b.run_compute('phoebe01', model='after_estimators', overwrite=True)
b.plot(model='after_estimators', x='phases', show=True)


# This looks close enough for the optimizer run. We will first initialize a new compute parameter-set and tweak a few optimization options for faster runtime:

# In[12]:


b.add_compute(
    compute='nm_fit',
    irrad_method='none',
    rv_method='dynamical',
    distortion_method='sphere'
)


# To save even more time, we can run the optimizer in phase space instead of time space; for that, we need to provide an array of phases in which the model should be computed and optimized:

# In[15]:


b.flip_constraint('compute_phases@rv01', solve_for='compute_times@rv01')
comp_phases = np.linspace(0,1,25)
b.set_value_all('compute_phases', dataset='rv01', value=comp_phases)


# Phoebe has three optimizer methods: 
# 
# * conjugate gradient (`optimizer.cg`)
# * powell (`optimizer.powell`) 
# * nelder_mead (`optimizer.nelder_mead`) 
# 
# In most cases, `nelder_mead` is the most efficient so this is the one we will use moving forward. However, the logic is essentially identical if you would like to try a different one.
# 
# We start by adding an optimizer and attaching compute options to it:

# In[16]:


b.add_solver('optimizer.nelder_mead',  solver='nm_solver', compute='nm_fit')


# Let's take a look at the parameters:

# In[17]:


print(b['nm_solver'])


# For the tutorial we will reduce the maximum number of iterations to 20; let us also disable light curve data for now, in order to get radial velocity parameters figured out:

# In[18]:


b.set_value('maxiter', solver='nm_solver', value=20)
b.disable_dataset('lc01')


# Now we need to inform the optimizer which parameters should be adjusted:

# In[19]:


b['fit_parameters@nm_solver'] = ['vgamma@system', 't0_supconj@binary', 'q@binary', 'asini@binary']


# With everything set, we can now run the solver. This will take a little bit of time because of the non-zero eccentricity but not enough for a coffee run:

# In[20]:


b.run_solver('nm_solver', solution='nm_solution', overwrite=True)


# New (fit) values for adjusted parameters are stored in the `fitted_values` parameter:

# In[21]:


print(b['nm_solution'])


# Alternatively, we can call the `adopt_solution()` method by passing `trial_run=True`:

# In[22]:


print(b.adopt_solution('nm_solution', trial_run=True))


# We can now run the model with these proposed parameters and inspect the solution visually:

# In[25]:


b.run_compute('nm_fit', solution='nm_solution', model='after_nm', overwrite=True)

b.plot(kind='rv', model='after_nm', x='phases', show=True, legend=True, marker = 'o')
b.plot( kind='rv', model='after_nm', x='phases', y='residuals', show=True, legend=True, marker = 'o')


# This improves the initial fit, so we can adopt this solution, thus copying proposed solution values to the bundle's face values:

# In[26]:


b.adopt_solution('nm_solution')


# Now let's return to light curve data; enable them, and disable RVs:

# In[27]:


b.disable_dataset('rv01')
b.enable_dataset('lc01')


# Depending on the number of data points, computing the forward model can take a long time. That means that _optimizing_ the model can take a _very_ long time. When light curve data do not exhibit significant out-of-eclipse variability, we can limit the optimizer to eclipse regions, thus saving us appreciable time. We will use our previous `lcgeom_solution` to mask out everything else. Eclipse regions are stored in the `eclipse_edges` parameter:

# In[29]:


print(b['eclipse_edges@lcgeom_solution'])


# The masking parameter is associated with the datasets:

# In[38]:


print(b['mask_phases'])


# To automatically populate these arrays, we will set `mask_phases` as a parameter to be adopted from the `lcgeom_solution` and then adopt the solution:

# In[39]:


b.set_value(solution = 'lcgeom_solution', qualifier='adopt_parameters', value=['mask_phases'])
b.adopt_solution('lcgeom_solution')


# Now the masked phases are populated by taking `eclipse_edges` and padding 30% of the eclipse width to ascertain adequate eclipse coverage:

# In[41]:


print(b['mask_phases'])


# The easiest way to see this in action is to visualize it:

# In[42]:


b.plot(kind='lc', model='after_estimators', x='phases', show='True')


# Recall that, for estimators, we used $R_2/R_1$ and $R_1+R_2$ to parametrize the model. As we will run the actual forward model, it serves our purpose better to use $R_1$ and $R_2$ as independent parameters. Let us flip the constraint and mark relevant parameters for adjustment:

# In[43]:


b.flip_constraint('requiv@primary', solve_for='requivsumfrac@binary')

b['fit_parameters'] = [
    'teffratio@binary',
    't0_supconj@binary',
    'incl@binary'
]


# As we set all solver parameters already, we can now simply run it:

# In[44]:


b.run_solver('nm_solver', solution='nm_solution', overwrite=True)


# As before, we can inspect the adjusted values either by looking at `fitted_values` or by running `adopt_solution()` with `trial_run=True`:

# In[45]:


print(b.adopt_solution('nm_solution', trial_run=True))


# What did that do to our light curve fit?

# In[46]:


b.run_compute('nm_fit', solution='nm_solution', model='after_nmlc')

b.plot(kind='lc', model='after_nmlc', x='phases', show=True, legend=True, marker = 'o')
b.plot(kind='lc', model='after_nmlc', x='phases', y='residuals', show=True, legend=True, marker = 'o')


# As before, this looks reasonable, so we can adopt the solution:

# In[47]:


b.adopt_solution('nm_solution')


# We can take a closer look at the primary eclipse:

# In[48]:


b.plot(kind='lc', x='phases', model='after_nmlc', xlim=[-0.2,0.2], show=True, legend=True, marker = 'o')
b.plot(kind='lc', x='phases', model='after_nmlc', xlim=[-0.2,0.2], y='residuals', show=True, legend=True, marker = 'o')


# # Exercise
# 
# Combine both light and rv curves to achieve a better fit, primarily within the eclipse. Hint: It's often better to fit a small number of parameters first. 

# In[ ]:




