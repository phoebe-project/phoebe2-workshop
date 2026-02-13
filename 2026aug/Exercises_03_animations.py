#!/usr/bin/env python
# coding: utf-8

# # Exercises #3: Forward Model Animations
# 
# These exercises are designed to be done anytime after the tutorials on animations and accessing meshes.

# # \# 1: Rossiter-McLaughlin
# 
# Make a figure or animation that illustrates the Rossiter-McLaughlin effect (i.e. show the RVs plotted as color on the meshes during eclipse as well as the synthetic RVs vs time).
# 
# Hints: 
# * you may be able to get a more exagerated example by changing certain Parameters of the system.
# * try only sampling from just before ingress to just after egress
# 

# ![animation](rossiter_mclaughlin.gif)

# In[ ]:





# # \# 2: Eccentric Ellipsoidal Variable (Heartbeat)
# 
# Make a figure or animation that illustrates an eccentric ellipsoidal variable.
# 
# Hints:
# * `requiv_max` will tell you the maximum value of `requiv` at which overflow will occur *at periastron*.

# ![animation](eccentric_ellipsoidal.gif)

# In[ ]:





# # \# 3: Spot Transit
# 
# Make a figure or animation that illustrates a small star (or a planet) transiting a star with a spot.
# 
# If we haven't gotten to features and spots quite yet, you can read [this spots tutorial](http://phoebe-project.org/docs/2.4/tutorials/spots) to get the basics.
# 
# Hints:
# * you may want to override the default colormap for temperature
# * if you set the temperature of your transiting body to be cool, that will drive the entire range of the colormap - try setting `fclim` to prevent that from happening.

# ![animation](spot_transit.gif)

# In[ ]:




