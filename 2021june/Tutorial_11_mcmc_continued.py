#!/usr/bin/env python
# coding: utf-8

# ### Tutorial 11: Fun with MCMC continued!
# 
# In the previous tutorial we started scratching the surface of sampling the parameter space with MCMC. In this tutorial we will focus on convergence (or lack thereof) and on offloading computations to an external computing cluster.
# 
# Let's start with the usual imports.

# In[1]:


import phoebe
import numpy as np
import matplotlib.pyplot as plt


# Load the data from the previous run:

# In[2]:


b = phoebe.load('./data/synthetic/after_initial_sampling.bundle')


# When running the sampler, we focused on the depiction of the results; let us now take a more systematic look at the sampler output:

# In[3]:


print(b['round_1'].qualifiers)


# Lots to digest here. So let's get started!
# 
# `wrap_central_values`: central positions of parameters that wrap their values;
# 
# `fitted_twigs`: parameter twigs that were sampled;
# 
# `fitted_units`: the units of parameters that were sampled;
# 
# `adopt_parameters`: list of sampled parameters for which the solution should be adopted; don't choose a subset unless you have a very good reason;
# 
# `adopt_distributions`: should distributions be stored;
# 
# `distributions_convert`: should a simplified representation of the distributions be stored; we will return to this in [Tutorial 13](http://phoebe-project.org/workshops/2021june/Tutorial_13_posteriors.ipynb);
# 
# `adopt_values`: should face values be stored;
# 
# `niters`: number of iterations used to reach the solution;
# 
# `nwalkers`: number of walkers used to reach the solution;
# 
# `samples`: MCMC samples of the shape (niters, nwalkers, npars);
# 
# `failed_samples`: MCMC samples that resulted in lnp=-inf; the return value is a dictionary where keys are failure messages and values are arrays of parameter combinations that caused the failure;
# 
# `lnprobabilities`: sampled log-probabilities of the shape (niters, nwalkers);
# 
# `acceptance_fractions`: used for convergence evaluation, provided per walker;
# 
# `autocorr_times`: autocorrelation times, used for convergence evaluation, provided per parameter;
# 
# `burnin`, `thin`, `lnprob_cutoff`: sample modifiers discussed in the previous tutorial;
# 
# `nlags`: number of autocorrelation lags to use when calculating autocorrelation;
# 
# `progress`: progress meter; useful when farming out to a cluster and checking an intermediate result;
# 
# `comments`: human-readable comments about the solution, to be used for reference.

# Remember that you can always print a certain parameter to get more verbose help on its purpose; for example:

# In[4]:


print(b['distributions_convert'])


# As we ran the sampler, some combinations of parameters resulted in 0 likelihood. We refer to those as failed samples and, as seen above, they are stored as part of the solution. We can easily plot those in a corner plot:

# In[5]:


b.plot(solution='round_1', style='failed', burnin=50, show=True)


# This is clearly a severely undersampled parameter space, but it's already evident where the failed samples lie; in this particular case, all values that fail are outside of parameter limits.

# We can now compute the average RV curve from, say, 25 samples drawn from the round 1 solution:

# In[6]:


b.run_compute(compute='dyn_rv', sample_from='round_1', sample_num=25, model='from_posteriors')


# Once computed, let's plot all 25 samples in the phase plot:

# In[7]:


b.plot(model='from_posteriors', x='phase', show=True)


# Happy with this? We can *inspect* the solution by running the `adopt_solution()` method with the `trial_run` argument set to `True`:

# In[8]:


print(b.adopt_solution(solution='round_1', trial_run=True))


# Before we adopt, though, let's have another (quick) coffee break -- let's continue sampling for another 25 iterations. The solvers and solutions that we have so far are:

# In[9]:


b.solvers


# In[10]:


b.solutions


# Remember the `continue_from` parameter of the solver? That's what we want to set!

# In[11]:


print(b['continue_from@mcmc'])


# In[12]:


b['continue_from@mcmc'] = 'round_1'


# The `niters` parameter will now correspond to the number of additional iterations; note that we need to specify here that we are setting `niters@solver` and not `niters@solution` (which is read-only anyway).

# In[13]:


b['niters@mcmc@solver'] = 25


# In[14]:


b.run_solver('mcmc', solution='round_2')


# We can now compare the results from the first sample (`round_1`) and from the second sample (`round_2`):

# In[15]:


b.plot(solution='round_1', style='lnprobability', show=True)
b.plot(solution='round_2', style='lnprobability', show=True)


# Several things worthy of mention here. First, note the span of the x-axis. It starts by the determined `burnin` value for each sample run (~26 for round 1 and ~31 for round 2), and it goes to the `niters` value (100 for round 1 and 125 for round 2).
# 
# How does phoebe estimate the value of `burnin`? It looks at the autocorrelation times, which emcee returns for each parameter. It then pick the longest autocorrelation time and multiplies it by the `burnin_factor`. Thus:

# In[16]:


print('burnin iterations for round 1: %d' % 
      (int(max(b['value@autocorr_times@round_1'])*b['value@burnin_factor@mcmc'])))
print('burnin iterations for round 2: %d' % 
      (int(max(b['value@autocorr_times@round_2'])*b['value@burnin_factor@mcmc'])))


# The value of log-probability, as well as the fact that it's still rising, hints that the solution has not yet converged. So we need to run a longer chain. As running 25 iterations locally took 3 minutes, we will offload this computation to a computer cluster. We covered the server setup in [Tutorial 9](Tutorial_09_server.ipynb), so we won't recreate it here; instead, we will rely on the already saved server (named `terra`) and add the server to the bundle. As a reminder, we keep the aggregated steps to initialize a server commented out here for simpler reference.

# In[17]:


# from phoebe.dependencies import crimpl
# s = crimpl.RemoteSlurmServer(host='terra', directory='~/workshop/crimpl')
# s.install_conda()
# s.save('terra', overwrite=True)


# Let's add a server to the bundle; as always, parameters can either be added as arguments, or by editing the instantiated parameter set later on.

# In[18]:


b.add_server('remoteslurm',
             crimpl_name='terra',
             conda_env='workshop',
             nprocs=48,
             server='terra',
             walltime=(12,'h'))


# In[19]:


print(b['terra@server'])


# Once the server is initialized, we assign the `use_server` parameter to it:

# In[20]:


print(f"original server: {b['value@use_server@dyn_rv']}")
b['use_server@dyn_rv'] = 'terra'
print(f"updated server: {b['value@use_server@dyn_rv']}")


# Given that we are offloading this computation to the HPC, let's increase the number of walkers from the current  16 to, say, 24, so that the sampler can traverse the parameter space more efficiently. The parameter `nwalkers` is in the solver parameter set:

# In[21]:


print(b['mcmc@solver'])


# Wait, it disappeared? No, it hasn't disappeared, it is hidden because we have `continue_from` set to the previous run, from which any new run will inherit all sampling parameters. Thus, we first need to set `continue_from` to none:

# In[22]:


b['continue_from@mcmc@solver'] = 'None'
print(b['mcmc@solver'])


# There it is! Now we can change it!

# In[23]:


b['nwalkers@mcmc@solver'] = 24


# But now how do we continue from the previous run? We obviously cannot literally continue because we have changed the sampler properties; instead, we need to *resample* from the last run. We do that by using the `init_from` parameter. In order to have something to initialize from, we first need to adopt parameters from the last run:

# In[24]:


b.adopt_solution(solution='round_2',
                 adopt_values=False,
                 adopt_distributions=True,
                 distributions_convert='mvsamples',
                 distribution='ndg_2')


# Now we have a new distribution:

# In[25]:


b.distributions


# We can use this new distribution to set the `init_from` parameter. The sampler will then use `ndg_2` to get a new sample for all initial values and continue from there.

# In[26]:


b['init_from@mcmc@solver'] = 'ndg_2'


# We're now ready to run the sampler! If you feel like taking a lunch break, you might want to uncomment the line below and run the sampler; in the interest of time for this tutorial, though, we will load the precomputed results instead.

# In[27]:


# b.run_solver('mcmc', solution='round_3', nprocs=24, niters=500, overwrite=True)
# b.save('./data/synthetic/after_terra.bundle')


# In[28]:


b = phoebe.load('./data/synthetic/after_terra.bundle')


# Now we can explore the solution and compare it to what we had before.

# Log-probability plot:

# In[29]:


b.plot(solution='round_3', style='lnprobability', show=True)


# Corner plot:

# In[30]:


b.plot(solution='round_3', style='corner', burnin=400, show=True)


# And finally the trace plot:

# In[31]:


b.plot(solution='round_3', style='trace', show=True)


# So how do we know when to stop? Is it converged yet? We will explore that in our [next tutorial](Tutorial_12_convergence.ipynb).

# **Exercise 1**: increase the number of walkers to 48 and run 100 iterations on terra, using 48 processors. Compare the results from above to the results you obtained. What conclusions can you draw from the comparison?

# In[ ]:





# **Exercise 2**: drop dynamical RVs and use a light curve. Start from the optimized parameter set from the Nelder & Mead run and build a starting distribution around it. Use 5 parameters: inclination, temperature ratio, primary and secondary equivalent radii, and passband luminosity. Don't run any samples yet -- we will defer that to self-study exercises.

# In[ ]:




