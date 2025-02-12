#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Estimators

# In this tutorial, we'll cover the first stages of fitting a data set with PHOEBE, using the built-in estimator methods:
# 
# - lc_periodogram
# - rv_periodogram
# - ebai
# - lc_geometry
# - rv_geometry
# 
# These methods are meant to offer a kick-start to optimizing and bypass any significant amount of manual tweaking typically required for the user to get to an approximate solution.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Solving the Inverse Problem](http://phoebe-project.org/docs/latest/tutorials/solver.ipynb)
# * [Advanced: LC Estimators](http://phoebe-project.org/docs/latest/tutorials/LC_estimators.ipynb)
# * [Advanced: RV Geometry Estimator](http://phoebe-project.org/docs/latest/tutorials/RV_estimators.ipynb)

# ## Setup

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import phoebe
logger = phoebe.logger('WARNING')
get_ipython().run_line_magic('matplotlib', 'inline')


# For this tutorial and the upcoming fitting tutorials, we'll use a synthetic data set comprised of one light curve and radial velocity curves of the primary and secondary component. 
# 
# You can find the data files in the workshop github repository, or download them from the following links (just note you may need to adjust the paths below when loading):
# * [lc.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2023june/data/synthetic/lc.data)
# * [rv1.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2023june/data/synthetic/rv1.data)
# * [rv2.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2023june/data/synthetic/rv2.data)
# 
# Recall from the Datasets tutorial (Tutorial_3) that when we add a dataset, we have the option of providing observables.  While this can be done after `add_dataset` is called, we can also do it directly in the initial call by assigning the appropriate values to the corresponding observables. Let's load the data in our bundle and plot them first!

# In[2]:


b = phoebe.default_binary(force_build=True)
lc = np.loadtxt('data/synthetic/lc.data')
rv1 = np.loadtxt('data/synthetic/rv1.data')
rv2 = np.loadtxt('data/synthetic/rv2.data')

b.add_dataset('lc', times = lc[:,0], fluxes=lc[:,1], sigmas=lc[:,2], passband='Johnson:V')
b.add_dataset('rv')
b['times@rv@primary'], b['rvs@rv@primary'], b['sigmas@rv@primary'] = rv1[:,0], rv1[:,1], rv1[:,2]
b['times@rv@secondary'], b['rvs@rv@secondary'], b['sigmas@rv@secondary'] = rv2[:,0], rv2[:,1], rv2[:,2]
_ = b.plot(x='times', show=True)


# PHOEBE currently offers 5 estimator methods and these all fall under the umbrella of solvers.  Later we will learn about optimizers and samplers which are other types of solvers offered by PHOEBE.  In order to use any of these solvers, we will call the `add_solver` method.  Lets go over the estimators that are available and how to use them

# ## Periodograms

# PHOEBE offers both light curve and radial velocity curve periodograms. The light curve periodogram supports the box least-squares (BLS) algorithm, which is more suitable for "boxy" eclipses of detached stars, and Lomb-Scargle (LS), which is more suitable for stars with strong ellipsoidal variations. The radial velocity periodogram only supports the LS algorithm.

# ### rv_periodogram

# Let's start with the rv_periodogram first:

# In[3]:


b.add_solver('estimator.rv_periodogram', solver='rvperiod')
print(b['rvperiod'])


# We'll leave all the options to their default values for the time being and see what the output of the solver is.

# In[6]:


b.run_solver('rvperiod', solution='rvperiod_solution')
print(b['rvperiod_solution'])


# The first two lines of the output are the periods and respective powers that the automatic sampling mode has generated. We see that the chosen periods are in the range of 0.4~40, which may not be ideal for our case, where we can roughly estimate from the data that out period is 1-2 days. 
# 
# The period_factor can be adjusted by the user and determines if a multiple of the period is to be adopted, since the periodogram may land on a harmonic.
# 
# The rest of the output parameters refer to the solution and we can see that the fitted value of ~0.6 is not ideal. So let's instead provide manual samples in a narrower range.

# In[7]:


b.set_value('sample_mode', context='solver', solver='rvperiod', value='manual')
b.set_value('sample_periods', context='solver', solver='rvperiod', value=np.linspace(0.5,5,1000))
b.run_solver('rvperiod', solution='rvperiod_solution_2')
print(b['rvperiod_solution_2'])


# The new value of the period ~1.67 looks much better now! Let's adopt it and plot our data in phase space to see the result.

# In[8]:


b.adopt_solution('rvperiod_solution_2')
b.plot(x='phase', show=True)


# ### lc_periodogram

# The light curve periodogram follows a similar workflow as the rv_periodogram. Let's add two different ones and assign one of the two algorithm options to each.

# In[9]:


b.add_solver('estimator.lc_periodogram', solver='lcperiod_bls', algorithm='bls')
b.add_solver('estimator.lc_periodogram', solver='lcperiod_ls', algorithm='ls')


# Not all parameters are applicable for both algorithms. For more details check: http://phoebe-project.org/docs/2.4/api/phoebe.parameters.solver.estimator.lc_periodogram

# In[10]:


b.run_solver('lcperiod_bls', solution='lcperiod_bls_solution', overwrite=True)
print(b['fitted_values@lcperiod_bls_solution'])
b.run_solver('lcperiod_ls', solution='lcperiod_ls_solution', overwrite=True)
print(b['fitted_values@lcperiod_ls_solution'])


# As expected, the bls algorithm performed better in our case, yielding half the period returned from the rv_periodogram. We can easily adopt the correct period by passing the period_factor in .adopt_solution():

# In[11]:


b.adopt_solution('lcperiod_bls_solution', period_factor=2)
b.plot(x='phase', show=True)


# And now we have a period for our system straight from PHOEBE! 

# ## Parameter estimates from geometry

# Before running the solvers, let's flip the required constraints and tweak some of the compute options, so that our computations run faster after adopting the solutions.

# In[12]:


# ensures the model light curve is scaled to the data
b.set_value('pblum_mode', 'dataset-scaled')
# speeds up run_compute
b.set_value_all('distortion_method', 'sphere')
# avoids errors from atmospheres
b.set_value_all('atm', 'blackbody')
b.set_value_all('ld_mode', 'manual')
b.set_value_all('ld_mode_bol', 'manual')

# constraints that needs to be flipped
# for lc_geometry
b.flip_constraint('requivratio', solve_for='requiv@secondary')
b.flip_constraint('requivsumfrac', solve_for='requiv@primary')
b.flip_constraint('teffratio', solve_for='teff@secondary')

# for rv_geometry
b.flip_constraint('asini@binary', solve_for='sma@binary')


# ### rv_geometry

# The rv_geometry solver provides simple estimates for several parameters that can be obtained from the radial velocity curves.

# In[13]:


b.add_solver('estimator.rv_geometry', solver='rvgeom', overwrite=True)
b.run_solver('rvgeom', solution='rvgeom_solution')


# In[14]:


for param, value, unit in zip(b.get_value('fitted_twigs', solution='rvgeom_solution'),
                       b.get_value('fitted_values', solution='rvgeom_solution'),
                        b.get_value('fitted_units', solution='rvgeom_solution')):
     print('%s = %.2f %s' % (param,value,unit))


# In[15]:


b.adopt_solution('rvgeom_solution')
b.run_compute(model='rvgeom_model')
b.plot(x='phase', legend=True, show=True)


# ### EBAI

# The EBAI (Eclipsing Binaries Aritifical Intelligence) estimator relies on machine learning methods to return estimates of the sum of radii, inclination, temperature ratio, esinw and ecosw from the light curve. There are two methods available in EBAI as of PHOEBE 2.4: 'mlp', which uses a trained neural network, and 'knn', which uses a k-Nearest Neighbors regressor.

# Now we're ready to add and run EBAI:

# In[16]:


b.add_solver('estimator.ebai', ebai_method='mlp', solver='ebai_mlp_est')
b.run_solver('ebai_mlp_est', solution='ebai_mlp_solution')


# In[17]:


for param, value, unit in zip(b.get_value('fitted_twigs', solution='ebai_mlp_solution'),
                       b.get_value('fitted_values', solution='ebai_mlp_solution'),
                        b.get_value('fitted_units', solution='ebai_mlp_solution')):
     print('%s = %.2f %s' % (param,value,unit))


# In[18]:


# flip the esinw/ecosw constraints so we can adopt the solution
b.flip_constraint('esinw', solve_for='ecc')
b.flip_constraint('ecosw', solve_for='per0')

# adopt solution and compute the model
b.adopt_solution('ebai_mlp_solution')
b.run_compute(model='ebai_mlp_model')
b.plot(x='phase', legend=True, show=True)


# We can see that EBAI with the 'mlp' method is not particularly good at estimating esinw and ecosw. Let's try the same with the 'knn' method:

# In[19]:


b.add_solver('estimator.ebai', ebai_method='knn', solver='ebai_knn_est')
b.run_solver('ebai_knn_est', solution='ebai_knn_solution')


# In[20]:


for param, value, unit in zip(b.get_value('fitted_twigs', solution='ebai_knn_solution'),
                       b.get_value('fitted_values', solution='ebai_knn_solution'),
                        b.get_value('fitted_units', solution='ebai_knn_solution')):
     print('%s = %.2f %s' % (param,value,unit))


# In[21]:


b.adopt_solution('ebai_knn_solution')
b.run_compute(model='ebai_knn_model')
b.plot(x='phase', legend=True, show=True)


# We can see that the 'knn' estimator does a better job at estimating esinw and ecosw! Let's finally compare the results of these two machine learning models with a model based on the light curve geometry (lc_geometry), which estimates all of the parameters that EBAI does, with the exception of inclination:

# In[22]:


b.add_solver('estimator.lc_geometry', solver='lcgeom')
b.run_solver('lcgeom', solution='lcgeom_solution')


# In[23]:


for param, value, unit in zip(b.get_value('fitted_twigs', solution='lcgeom_solution')[:5],
                       b.get_value('fitted_values', solution='lcgeom_solution')[:5],
                        b.get_value('fitted_units', solution='lcgeom_solution')[:5]):
     print('%s = %.2f %s' % (param,value,unit))


# In[24]:


# lc_geometry returns ecc and per0, so we need to flip the constraints back before adopting the solution
b.flip_constraint('ecc', solve_for='esinw')
b.flip_constraint('per0', solve_for='ecosw')

b.adopt_solution('lcgeom_solution')
b.run_compute(model='lcgeom_model')
b.plot(x='phase', legend=True, show=True)


# That looks great! lc_geometry further improved on the eclipse fits and we now have a good starting position for optimizers.

# Finally, let's return the atmosphere parameters to their default PHOEBE values and ensure that our solution is within the atmosphere table bounds. (Moving forward to optimiziers and samplers, we want to make sure that we're starting from a somewhat physical solution!)

# In[25]:


b.set_value_all('atm', 'ck2004')
b.set_value_all('ld_mode', 'interp')
b.set_value_all('ld_mode_bol', 'lookup')
b.run_compute()
b.plot(['dataset', 'latest'], x='phase', show=True)


# In[26]:


b.save('data/synthetic/after_estimators.bundle')


# # Exercises

# 1. Initialize a new bundle and load the synthetic light curve used in the tutorial. Add a light curve periodogram and try to tweak the parameter values, such that the periodogram will yield the true period, instead of the half-value harmonic.

# In[ ]:





# 2. Initialize a new bundle. Load only the primary radial velocity data. Set the period to 1.67 and t0 to 1.23. Add an rv_geometry estimatator and examine how the output is different compared to the output in the tutorial, where we had both RVs.

# In[ ]:





# 3. (Optional) The lc_geometry estimator offers two analytical models that can be fitted to the light curve to estimate the eclipse parameters (and from that, the parameters of interest). In the same bundle used in the example above, add a new lc_geometry estimator and change the analytical model from 'two-gaussian' to 'polyfit'. Plot the resulting light curves from both and try to determine if one model performs better than the other for this case!

# In[ ]:




