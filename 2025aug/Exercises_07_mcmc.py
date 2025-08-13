#!/usr/bin/env python
# coding: utf-8

# # Exercises #5: MCMC / Hack Day
# 
# # MCMC
# 
# These exercises are designed to be done anytime after the tutorials introducing MCMC.
# 
# Starting with your solution from [estimators and optimizers](./Exercises_04_estimators_optimizers.ipynb), setup and submit an MCMC job to sample the local parameter space.  
# 
# You will very likely need to run these jobs remotely, so make sure to set `progress_every_niters` so that you can monitor the results and kill/restart the job if necessary.  If you haven't done so already, make sure to determine if any of the expensive effects can safely be disabled (see [optimizing computations](./Tutorial_11_optimizing_computations.ipynb)) first so that you can get a reasonable number of iterations.

# # Systems from the literature

# ## Kepler systems
# 
# detached circular system (KIC10661783 https://ui.adsabs.harvard.edu/abs/2021MNRAS.505.3206M/abstract)
# 
# detached eccentric system (KIC4862625 https://iopscience.iop.org/article/10.1088/0004-637X/768/2/127/pdf)
# 
# *detached system with apsidal motion (KIC3749404 https://academic.oup.com/mnras/article/463/2/1199/2892176?login=false )
# 
# *tidally induced pulsations, eccentric, only secondary eclipse (KIC3230227 https://ui.adsabs.harvard.edu/abs/2017ApJ...834...59G/abstract)
# 
# *EB with pulsations (GPs) (KIC11285625 https://www.aanda.org/articles/aa/full_html/2013/08/aa21702-13/aa21702-13.html)

# ## Other interesting systems
# (interesting because Angela has modeled them and can help with the intricacies :D)
# 
# Alpha Draconis https://ui.adsabs.harvard.edu/abs/2022MNRAS.511.2648H/abstract
# 
# NGC 1850 BH1 https://ui.adsabs.harvard.edu/abs/2022MNRAS.511.2914S/abstract

# # Advanced: data with Gaia distances 
# ### (mag to flux, and normalized to absolute flux conversions!)
# 
# https://ui.adsabs.harvard.edu/abs/2013Natur.495...76P/abstract 
# 
# https://ui.adsabs.harvard.edu/abs/2022ApJ...926...46O/abstract

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
# ## Bug fixes:
# 
# improve remeshing logic
# 
# autofig: ec='face' avoid "assuming named color" warning
# 
# autofig: support for linewidths in mesh plots

# In[ ]:





# In[ ]:




