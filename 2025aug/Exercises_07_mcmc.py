#!/usr/bin/env python
# coding: utf-8

# # Exercises #5: MCMC / Hack Day
# 
# # MCMC
# 
# These exercises are designed to be done anytime after the tutorials introducing MCMC.
# 
# Starting with your solution from [estimators and optimizers](./Exercises_06_estimators_optimizers.ipynb), setup and submit an MCMC job to sample the local parameter space.  
# 
# Run the job remotely. Make sure to set `progress_every_niters` so that you can monitor the results and kill/restart the job if necessary, and to save your bundle if you detatch it.  If you haven't done so already, make sure to determine if any of the expensive effects can safely be disabled (see [optimizing computations](./Tutorial_10_optimizing_computations.ipynb)) first, so that you can get a reasonable number of iterations.
# 
# Once you have a reasonable number of iterations. Plot the light and/or radial velocity curve, the trace plot and the corner plot.

# # Systems from the literature

# ## Kepler systems
# 
# Detached circular system (KIC10661783 https://ui.adsabs.harvard.edu/abs/2021MNRAS.505.3206M/abstract)
# 
# Detached system with apsidal motion (KIC3749404 https://academic.oup.com/mnras/article/463/2/1199/2892176?login=false )
# 
# Tidally induced pulsations, eccentric, only secondary eclipse (KIC3230227 https://ui.adsabs.harvard.edu/abs/2017ApJ...834...59G/abstract)
# 
# EB with pulsations (GPs) (KIC11285625 https://www.aanda.org/articles/aa/full_html/2013/08/aa21702-13/aa21702-13.html)

# ## Other interesting systems
# 
# Alpha Draconis https://ui.adsabs.harvard.edu/abs/2022MNRAS.511.2648H/abstract
# 
# NGC 1850 BH1 https://ui.adsabs.harvard.edu/abs/2022MNRAS.511.2914S/abstract

# # Additional data
# 
# https://www.astro.keele.ac.uk/jkt/debcat/ (detached benchmark stars)
# 
# http://keplerebs.villanova.edu (when searching, check "Require Publication"

# # Development projects (ultra advanced!)
# 
# ## New tutorials
# 
# dataset-coupled example
# 
# synchronicity tutorial/example
# 
# callbacks within animations
# 
# custom constraint for vsini (if not as built-in), create synthetic line profile, measure vsini using standard methods, compare to input
# 
# ## Code implementation:
# 
# new built-in constraints
# 
# new compute backends (batman, elisa, lcurve, BM3, elc, starry, WD, Beer, Ebop, Lightcurve factory, nightfall, pytransit, allesfitter)
# 
# support for plotting stars on HR diagram/evolution tracks
# 
# ability to set total luminosity
# 
# ability to provide observations for orbits (and include in fitting)
# 
# 

# In[ ]:





# In[ ]:




