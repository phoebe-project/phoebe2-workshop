#!/usr/bin/env python
# coding: utf-8

# # Exercises #4: Estimators and Optimizers
# 
# These exercises are designed to be done any time after the tutorial on optimizers.
# 
# Try to find a decent fit to the observations by running **estimators** and **optimizers** .  Later, we will use the optimized solution as a starting point for the sampler (MCMC) - so try to get the residuals as flat as possible and make sure to save your progress.
# 
# * [lc.B.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2023june/data/dataset_exercises/lc.B.data) (times, fluxes, sigmas - Johnson B passband)
# * [lc.V.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2023june/data/dataset_exercises/lc.V.data) (times, fluxes, sigmas - Johnson V passband)
# * [rv1.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2023june/data/dataset_exercises/rv1.data) (times, rvs, sigmas for primary star)
# * [rv2.data](https://github.com/phoebe-project/phoebe2-workshop/raw/2023june/data/dataset_exercises/rv2.data) (times, rvs, sigmas for secondary star - same times as `rv1.data`, so feel free to merge into a single PHOEBE dataset)
# 
# 
# This case is more complicated than the one used in the tutorials and requires more parameter tweaking and back and forth to get a good estimate!  There are several different general approaches you can take, with increased levels of "difficulty", so choose whichever sounds most interesting but manageable to you:
# 
# 1. Only use one of the two provided light curves, _assume_ a fixed temperature of one of the components, and fit for the temperature ratio (you can either fit for the secondary temperature and translate that to the ratio or use the built-in optional constraint via `b.add_constraint('teffratio')`).  You likely won't be able to get absolute temperatures out as only the limb-darkening contains any temperature information.
# 2. Only use one of the two provided light curves, but use the "known" spectral type of the _primary star_ of F8 as a _prior_ (you'll need to decide how to translate that into a distribution on temperature).  In real life, this case would require careful spectral disentangling or an extreme luminosity ratio (not the case here) in order to have separated the primary from secondary component, but will make your job easier for this exercise.
# 3. Only use one of the two provided light curves, but use the "known" spectral type of the _entire system_ of F9 as a _prior_.  You'll need to create a [custom parameter and constraint](http://phoebe-project.org/docs/2.4/tutorials/constraints_custom) to represent the system temperature and then decide how to set the spectral type as a distribution on that temperature.  This is a much more realistic case where the spectral type came from a combined spectrum or color temperature, but does require some manual setup and careful consideration of approximations.
# 4. Use both of the provided light curves and use them to extract absolute temperatures.  You'll need to make sure that the light curve datasets are coupled together so that only a _single pblum_ parameter (along with both temperatures or the temperature sum and ratio) is fitted.  Although simpler to setup than option \#3, this may require more time to converge and (in real life) requires calibrated photometry. PHOEBE refers to this as [color constraining](https://ui.adsabs.harvard.edu/abs/2006Ap%26SS.304..347P/abstract).
# 
# Refer to the [solver API docs](http://phoebe-project.org/docs/2.4/api/phoebe.parameters.solver) if you need to tweak additional parameters that haven't been covered in the tutorials.  If you have any questions - feel free to ask!
# 
# For optimization runs, feel free to submit the jobs remotely and make use of `progress_every_niters` and `b.load_job_progress`.  Once you get somewhat close to a good solution, make sure to determine if any of the expensive effects can safely be disabled (see [optimizing computations](./Tutorial_11_optimizing_computations.ipynb)) before adding a bunch of extra free parameters or running for extended iterations overnight.  For any approximations you do take, make sure to re-evaluate their validity as you go!

# In[ ]:




