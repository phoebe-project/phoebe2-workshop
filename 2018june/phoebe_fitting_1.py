#!/usr/bin/env python
# coding: utf-8

# In this tutorial we will use the basic functionallity of EMCEE (the MCMC software) to fit a quadratic function with some noise.

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import emcee
import matplotlib.pyplot as pl
from matplotlib.pyplot import cm 
import matplotlib.mlab as mlab


# First we make our synthetic data:

# In[ ]:


def q(a,b,c,x):
    quad = a*x**2. + b*x + c
    return quad


# In[ ]:


x = np.linspace(-1,1,101)


# In[ ]:


quad = q(1.,0.,-0.2,x)
noise = np.random.normal(0.0, 0.1, quad.shape)
noisy = quad + noise
pl.plot (x,noisy,"k.")
pl.show()


# Now we set the hyperparamters required to run emcee:

# In[ ]:


nwalkers = 20
niter = 10
prior_boxes = [(-2.,0.),(-0.5,0.5),(-0.5,0.)]
ndim = len(prior_boxes)
sigma = 0.1


# Generate an initial guess for all the parameters:

# In[ ]:


def rpars(prior_boxes):
    return [np.random.rand() * (p[1]-p[0]) + p[0] for p in prior_boxes]


# Now we will specify our log probability function, which will include our figure of merit computation. Here, z will be the array of values returned by the mcmc algorithm:

# In[ ]:


def lnprob(z):

    # make a model using the values the sampler generated
    model = q(z[0],z[1],z[2],x)

    # use chi^2 to compare the model to the data:
    chi2 = 0.
    for i in range (len(x)):
            chi2+=((noisy[i]-model[i])**2)/(sigma**2)

    # calculate lnp
    lnp = -0.5*chi2

    return lnp


# Now we will set the run function which will combine all our computations and plot histograms of the results:

# In[ ]:


def run(prior_boxes, nwalkers, niter, ndim):

    # Generate initial guesses for all parameters for all chains
    p0 = np.array([rpars(prior_boxes) for i in xrange(nwalkers)])

    # Generate the emcee sampler. Here the inputs provided include the 
    # lnprob function. With this setup, the first parameter
    # in the lnprob function is the output from the sampler (the paramter 
    # positions).
    sampler = emcee.EnsembleSampler(nwalkers,ndim,lnprob)

    pos, prob, state = sampler.run_mcmc(p0, niter)

    for i in range(ndim):
        pl.figure()
        y = sampler.flatchain[:,i]
        n, bins, patches = pl.hist(y, 200, normed=1, color="b", alpha=0.45)
        pl.title("Dimension {0:d}".format(i))
        
        mu = np.average(y)
        sigma = np.std(y)       
        print "mu = ", "sigma = ", mu, sigma

        bf = mlab.normpdf(bins, mu, sigma)
        l = pl.plot(bins, bf, 'k--', linewidth=2.0)

    pl.show()
    return pos


# In[ ]:


niter=10
pos = run(prior_boxes, nwalkers, niter, ndim)


# In[ ]:


color=cm.rainbow(np.linspace(0,1,nwalkers))
for i,c in zip(range(nwalkers),color):
    
    model = pos[-1-i,0]*x**2 + pos[-1-i,0]*x + pos[-1-i,0]
    
    pl.plot(x,model,c=c)
    
pl.plot(x,noisy,"k.")
pl.xlabel("x")
pl.ylabel("f(x)")
pl.show()


# Now lets update the number of iterations to see how this affects our parameter values (this may take a while to run):

# In[ ]:


niter = 100000

pos = run(prior_boxes, nwalkers, niter, ndim)


# In[ ]:


color=cm.rainbow(np.linspace(0,1,nwalkers))
for i,c in zip(range(nwalkers),color):
    
    model = pos[-1-i,0]*x**2 + pos[-1-i,1]*x + pos[-1-i,2]
    
    pl.plot(x,model,c=c)
    
pl.plot(x,noisy,"k.")
pl.xlabel("x")
pl.ylabel("f(x)")
pl.show()


# In[ ]:




