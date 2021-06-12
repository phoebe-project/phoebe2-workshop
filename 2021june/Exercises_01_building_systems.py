#!/usr/bin/env python
# coding: utf-8

# # Exercises #1: Building Systems
# 
# These exercises are designed to be done anytime after Tutorial #2 (constraints).
# 
# Don't feel like you need to do all of these - just pick and choose which seem the most interesting to you.  Make sure to save your notebooks and/or bundles, as [tomorrow's exercise](./Exercises_02_forward_models.ipynb) will have you generate synthetic models for these same system(s).

# # \#1: Sun-Jupiter
# 
# Create a default binary Bundle, re-parameterize so that you can set both.  Now set the value of the masses and the respective radii such that you have a Jupiter around a Sun.
# 
# Hint: try using units to handle the conversion between Jupiter and Solar masses/radii.  You can always do `dir(phoebe.u)` to see a list of all available units, or `phoebe.u.solMass.find_equivalent_units()`.  For other quantities (orbital/rotation periods, sma, etc), you may need to lookup the values since they do not have units/constants available.

# In[ ]:





# # \#2: Sun-Earth
# 
# Create a Sun-Earth system.  Make sure to get the correct masses, radii, orbital period, separation, eccentricity, and rotational period.

# In[ ]:





# # \#3: Reproduce Systems from the Literature
# 
# Find (or pick your favorite) EB solution in the literature and try to map the reported values in the paper into PHOEBE.

# In[ ]:





# # \#4: Advanced: Reproduce Binaries from the CALEB Catalog
# 
# Pick a system from the [Caleb catalog of EBs](http://caleb.eastern.edu/query_stars_by_type.php), click on one of the "library sets", and then view the BM3 input file.  Try to translate as many of these parameters as you can into PHOEBE.  
# 
# Choose a detached binary first.  If you'd like to try a semi-detached or contact binary, refer to the following tutorials:
# * [Advanced: Contact Binary Hierarchy](http://phoebe-project.org/docs/2.3/tutorials/contact_binary_hierarchy)
# * [Advanced: Semidetached Systems](http://phoebe-project.org/docs/2.3/tutorials/requiv_crit_semidetached)
# 
# 
# Note that the [morphology definitions in caleb](http://caleb.eastern.edu/binary_type_definitions.php) are slightly different than PHOEBE. You may want to use the following:
# 
# * Caleb's detached -> `phoebe.default_binary()`
# * Caleb's semi-detached or near-contact -> `phoebe.default_binary()` with semi-detached constraint on one component
# * Caleb's contact -> `phoebe.default_binary()` with semi-detached constraint on both components
# * Caleb's overcontact -> `phoebe.default_binary(contact_binary=True)`
# * Caleb's double-contact -> good luck! (you can try semi-detached constraints)
# 
# For detached systems, you can try using `R1_BACK`, `R2_BACK` as the equivalent radius, but otherwise you will need to translate the equipotentials `OMEGA_1`, `OMEGA_2` using [phoebe.distortions.roche.pot_to_requiv](http://phoebe-project.org/docs/2.3/api/phoebe.distortions.roche.pot_to_requiv) with `d=1-e` (as potentials are defined at periastron) along with an estimate of the semi-major axis from the RV semi-amplitudes, inclination, and eccentricity.  If you get stuck, don't hesitate to ask for help!

# In[ ]:




