#!/usr/bin/env python
# coding: utf-8

# In this tutorial we will use the basic functionallity of EMCEE (the MCMC software) to fit a synthetic binary that we make using phoebe.

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import emcee
import matplotlib.pyplot as pl
import phoebe
import matplotlib.mlab as mlab
from matplotlib.pyplot import cm 


# First we make our synthetic data, this time we will make a binary star using PHOEBE and add noise:

# In[ ]:


logger = phoebe.logger(clevel='WARNING')


# In[ ]:


b = phoebe.default_binary()


# First we will add a light curve data set so that we cam make our synthetic data model:

# In[ ]:


times = np.linspace(0,1,51)
b.add_dataset('lc', times=times, dataset='lc01')


# We will set the irradiation method to "none" (for the purpose of the tutorial) as that requires significant computational time:

# In[ ]:


b.get_parameter(context='compute', qualifier='irrad_method').set_value("none")


# We will also significantly reduce the number of triangles to speed up computations:

# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').set_value(300)


# In[ ]:


b.get_parameter(context='compute', component='secondary', qualifier='ntriangles').set_value(300)


# We will set the parameters that we plan to fit to specific values:

# In[ ]:


b['incl@binary@orbit@component'] = 86.5
b['rpole@primary@star@component'] = 1.2
b['rpole@secondary@star@component'] = 0.8
b['q@binary@orbit@component'] = 0.7
b['pblum@primary@dataset'] = 2.9*np.pi


# Now we will compute our phoebe model, add noise and plot the results:

# In[ ]:


b.run_compute()


# In[ ]:


flux = b['fluxes@latest@model'].get_value()
sigma = 0.01
mean = 0.0
noise = np.random.normal(mean, sigma, flux.shape)
noisy = flux + noise


# In[ ]:


pl.plot(times, noisy, "b.-")
pl.xlabel("Times")
pl.ylabel("Flux")
pl.show()


# Now we have our data, we need to set the hyperparamters required to run emcee. Here the prior boxes provide the lower and upper limits for the phoebe parameter values. We will select the order to be incl, rpole1, rpole2, mass ratio, luminosity:

# In[ ]:


nwalkers = 12
niter = 10
prior_boxes = [(85.,87.),(1.1,1.3),(0.7,0.9),(0.65,0.75),(2.8*np.pi,3.0*np.pi)]
sigma = 0.01


# Now we will set up a new bundle, which we will call "mod", to compute the model to fit the synthetic data we just generated:

# In[ ]:


mod = phoebe.default_binary()


# We will need to generate the model at the same times as our data (or make it at equidistant points and interpolate). Also, if you have a large observed data set and your phased light curve does not change in time (due to effects such as apsidal motion or a third body), I recommend only computing one orbital cycle of the model and extrapolating to the whole data set before computing the merit function.

# In[ ]:


times = np.linspace(0,1,51)
mod.add_dataset('lc', times=times, dataset='lc01')


# Again, for the purpose of speeding up computations we will set the number of triangles to a (ridiciously) low value and turn off reflection:

# In[ ]:


mod.get_parameter(context='compute', qualifier='irrad_method').set_value("none")
mod.get_parameter(context='compute', component='primary', qualifier='ntriangles').set_value(300)
mod.get_parameter(context='compute', component='secondary', qualifier='ntriangles').set_value(300)


# Generate an initial guess for all the parameters:

# In[ ]:


def rpars(prior_boxes):
    return [np.random.rand() * (p[1]-p[0]) + p[0] for p in prior_boxes]


# Here the priors are flat (meaning they are just linearly distributed between two numbers). If we wish to specify Gaussian priors, we could set our prior boxes to specify the mean and sigma values, and use the following function to determine our priors:

# return [random.gauss(p[0],p[1]) for p in pars]

# Now we will specify our log probability function, which will include our figure of merit computation. Here, z will be the array of values returned by the mcmc algorithm. We will update the parameter values with the new values given by the mcmc fitter in this function and then recompute the model:

# In[ ]:


def lnprob(z):

    mod['incl@binary@orbit@component'] = z[0]
    mod['rpole@primary@star@component'] = z[1]
    mod['rpole@secondary@star@component'] = z[2]
    mod['q@binary@orbit@component'] = z[3]
    mod['pblum@primary@dataset'] = z[4]
    
    mod.run_compute()
        
    model = mod['fluxes@latest@model'].get_value()

    # use chi^2 to compare the model to the data:
    chi2 = 0.
    for i in range (len(times)):
            chi2+=((noisy[i]-model[i])**2)/(sigma**2)

    # calculate lnp
    lnp = -0.5*chi2

    return lnp


# Now we will set the run function which will combine all our computations:

# In[ ]:


def run(prior_boxes, nwalkers, niter):
    # Specify the number of dimensions for mcmc
    ndim = len(prior_boxes)

    # Generate initial guesses for all parameters for all chains
    p0 = np.array([rpars(prior_boxes) for i in xrange(nwalkers)])

    # Generate the emcee sampler. Here the inputs provided include the lnprob function. With this setup, the value z
    # in the lnprob function, is the output from the sampler.
    sampler = emcee.EnsembleSampler(nwalkers,ndim,lnprob)
    
    pos, prob, state = sampler.run_mcmc(p0, niter)
    
    for i in range(ndim):
        pl.figure()
        y = sampler.flatchain[:,i]
        n, bins, patches = pl.hist(y, 200, normed=1, color="b", alpha=0.45)#, histtype="step")
        pl.title("Dimension {0:d}".format(i))
        
        mu = np.average(y)
        sigma = np.std(y)
        
        print "mu = ", mu
        print "sigma = ",sigma

        bf = mlab.normpdf(bins, mu, sigma)
        l = pl.plot(bins, bf, 'k--', linewidth=2.0)
    pl.show()
    return pos


# In[ ]:


pos = run(prior_boxes, nwalkers, niter)


# If we wish to see how good our last fit was, we can overplot the final models and the synthetic data. To do this, we will need to update the model with the last parameter values from our fit, and then overplot each one:

# In[ ]:


color=cm.rainbow(np.linspace(0,1,nwalkers))
for i,c in zip(range(nwalkers),color):
  
    #pl.figure()
    
    # Set all the parameter values
    mod['incl@binary@orbit@component'] = pos[-1-i,0]
    mod['rpole@primary@star@component'] = pos[-1-i,1]
    mod['rpole@secondary@star@component'] = pos[-1-i,2]
    mod['q@binary@orbit@component'] = pos[-1-i,3]
    mod['pblum@primary@dataset'] = pos[-1-i,4]
        
    mod.run_compute()
    
    model = mod['fluxes@latest@model'].get_value()
    
    pl.plot(times,model,c=c)

pl.xlabel("Times")
pl.ylabel("Flux")
pl.plot(times,noisy,"k.")
pl.show()


# As you can see there is still a large spread of models. The key here is that we need to do lots of iterations. 
