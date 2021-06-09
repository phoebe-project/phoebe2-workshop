#!/usr/bin/env python
# coding: utf-8

# # Exercises #5: Estimators & Optimizers
# 
# These exercises are designed to be done anytime after Tutorial #8b (optimizers).
# 
# Download the following dataset files, attach to a default binary system, and run estimators and optimizers to try to find a decent fit to the observations.  
# * [lc.B.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2021june/data/dataset_exercises/lc.B.data) (times, fluxes, sigmas - Johnson B passband)
# * [lc.V.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2021june/data/dataset_exercises/lc.V.data) (times, fluxes, sigmas - Johnson V passband)
# * [rv1.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2021june/data/testcase/rv1.data) (times, rvs, sigmas for primary star)
# * [rv2.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2021june/data/testcase/rv2.data) (times, rvs, sigmas for secondary star - same times `rv1.data`, so feel free to merge into a single PHOEBE dataset)
# 
# 
# This case is more complicated than the one used in the tutorials and requires more parameter tweaking and back and forth to get a good estimate!  
# 
# Refer to the [solver API docs](http://phoebe-project.org/docs/2.3/api/phoebe.parameters.solver) if you need to tweak additional parameters that haven't been covered in the tutorials.  If you have any questions - feel free to ask!
# 
# For optimization runs, feel free to submit the jobs remotely and make use of `progress_every_niters` and `b.load_job_progress`.  Once you get somewhat close to a good solution, make sure to determine if any of the expensive effects can safely be disabled (see [optimizing computations](./Tutorial_optimizing_computations) from week \#1) before adding a bunch of extra free parameters or running for extended iterations overnight.
