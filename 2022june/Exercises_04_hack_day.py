#!/usr/bin/env python
# coding: utf-8

# # Exercises #4: Hack Day
# 
# These exercises are designed to be done anytime after feeling comfortable building forward models.

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




