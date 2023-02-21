#!/usr/bin/env python
# coding: utf-8

# # Exercises #8: MCMC
# 
# These exercises are designed to be done anytime after the tutorials introducing MCMC.
# 
# Starting with your solution from [estimators](./Exercises_06_estimators.ipynb) and [optimizers](./Exercises_07_optimizers.ipynb), setup and submit an MCMC job to sample the local parameter space.  
# 
# You will very likely need to run these jobs remotely, so make sure to set `progress_every_niters` so that you can monitor the results and kill/restart the job if necessary.  If you haven't done so already, make sure to determine if any of the expensive effects can safely be disabled (see [optimizing computations](./Tutorial_11_optimizing_computations.ipynb) from the first week) first so that you can get a reasonable number of iterations.
