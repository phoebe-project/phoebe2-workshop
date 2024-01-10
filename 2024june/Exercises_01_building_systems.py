#!/usr/bin/env python
# coding: utf-8

# # Exercises #1: Building Systems
# 
# These exercises are designed to be done anytime after the tutorial on constraints.
# 
# Don't feel like you need to do all of these - just pick and choose which seem the most interesting to you.  Make sure to save your notebooks and/or bundles, as [tomorrow's exercise](./Exercises_02_forward_models.ipynb) will have you generate synthetic models for these same system(s).

# # \#1: Sun-Jupiter
# 
# Create a default binary Bundle, re-parameterize so that you can set both masses.  Now set the the masses and the radii such that you have a Jupiter around a Sun.
# 
# Hint: try using units to handle the conversion between Jupiter and Solar masses/radii.  You can always do `dir(phoebe.u)` to see a list of all available units, or `phoebe.u.solMass.find_equivalent_units()`.  For other quantities (orbital/rotation periods, sma, etc), you may need to lookup the values since they do not have units/constants available.

# In[ ]:





# # \#2: Sun-Earth
# 
# Create a Sun-Earth system.  Make sure to get the correct masses, radii, orbital period, separation, eccentricity, and rotational period.

# In[ ]:





# # \#3: Advanced: Reproduce Systems from the Literature
# 
# Find (or pick your favorite) EB solution in the literature and try to map the reported values in the paper into PHOEBE.
# 
# If you'd like to try a semi-detached or contact binary, refer to the following tutorials:
# * [Advanced: Contact Binary Hierarchy](http://phoebe-project.org/docs/2.4/tutorials/contact_binary_hierarchy)
# * [Advanced: Semidetached Systems](http://phoebe-project.org/docs/2.4/tutorials/requiv_crit_semidetached)
# 
# Depending on the code used for modeling, the results may be reported using parameters not readily available in PHOEBE. For detached systems, you can use any reported point radii (polar, equatorial, back/front) as approximations for the equivalent radius. If the solution is reported in equipotentials, you can convert them to radii using [phoebe.distortions.roche.pot_to_requiv](http://phoebe-project.org/docs/2.4/api/phoebe.distortions.roche.pot_to_requiv) with `d=1-e` (as potentials are defined at periastron) along with an estimate of the semi-major axis from the RV semi-amplitudes, inclination, and eccentricity.  If you get stuck, don't hesitate to ask for help!

# In[ ]:




