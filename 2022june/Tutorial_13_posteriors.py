#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Posteriors & Parameter Uncertainties
# 
# In this tutorial we will focus on posterior probability density functions (pdfs), also known as posteriors. These inform us of the parameter distributions that underlie the topology of the parameter space.
# 
# We will not be doing any new computations. Instead, we will use the results from our final round of sampling and interpret them in the context of posterior pdfs.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorial(s):
# 
# * [Advanced: EMCEE Sampler](http://phoebe-project.org/docs/latest/tutorials/emcee.ipynb)
# * [Advanced: Convert Posterior Distributions from EMCEE](http://phoebe-project.org/docs/latest/tutorials/emcee_distributions_convert.ipynb)
# 
# As usual, we do the imports first.

# In[1]:


import phoebe
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st


# And load the [bundle from the previous tutorial](https://github.com/phoebe-project/phoebe2-workshop/raw/2021june/data/synthetic/after_final_round.bundle):

# In[2]:


b = phoebe.load('./data/synthetic/after_final_round.bundle')


# Let's make sure that this final round looks okay by plotting the trace plots of the parameters and the logprobaility function.

# In[3]:


_ = b.plot(solution='final_round', show=True)


# This looks good (and converged, which we already know from the convergence analysis of the previous tutorial!) so let's first adopt the final round, including the distributions, which will give us easier access to the parameter posteriors and uncertainties.

# In[4]:


b.adopt_solution(solution='final_round',
                 adopt_values=False,
                 adopt_distributions=True,
                 distributions_convert='mvsamples',
                 distribution='ndg_final_mvsamples')


# Note that we convert the distributions here to 'mvsamples', meaning we are storing the samples directly. Just for reference, let's look at the other options for this parameter:

# In[5]:


b['final_round@distributions_convert'].choices


# The description has information on what each one of these does. The 'mvhistogram' and 'mvgaussian' options are especially useful for simplified storing of the chains:

# In[6]:


b['final_round@distributions_convert'].description


# Let's adopt the solution with a different choice of distributions_convert:

# In[7]:


b.adopt_solution(solution='final_round',
                 adopt_values=False,
                 adopt_distributions=True,
                 distributions_convert='mvgaussian',
                 distribution='ndg_final_mvgaussian')


# Now let's take a closer look at one of the parameters in the adopted distributions, so that we can follow the logic built into phoebe for these different options:

# In[8]:


b['value@ecc@binary@distribution@ndg_final_mvsamples']


# In[9]:


b['value@ecc@binary@distribution@ndg_final_mvgaussian']


# These structures are inherited from the distl module and you can get even more intimately familiar with them to understand the inner workings of the posterior methods supported in PHOEBE:

# In[10]:


help(b['value@ecc@ndg_final_mvsamples@distribution'])


# In[11]:


help(b['value@ecc@ndg_final_mvgaussian@distribution'])


# Now, let's see how we can use these distributions to plot the posterior of a single parameter:

# In[12]:


ecc_posterior_samples = b['value@ecc@binary@distribution@ndg_final_mvsamples']
ecc_posterior_mvg = b['value@ecc@binary@distribution@ndg_final_mvgaussian']


# In[13]:


_ = ecc_posterior_samples.plot_sample(bins=50, alpha=0.5)
_ = ecc_posterior_mvg.plot_sample(bins=50, alpha=0.5)


# We can see that the posterior with the 'mvsamples' option (blue) is truer to the actual samples distribution, while the 'mvgaussian' one (ornage) is, as expected, more gaussian. Ultimately, we would like to plot a gaussian to either option and we can see that they don't differ significantly for our case (which is good news!)

# In[14]:


_ = ecc_posterior_samples.plot_gaussian()
_ = ecc_posterior_mvg.plot_gaussian()


# We can also use a single `plot()` method to combine the plots and make them even nicer:

# In[15]:


_ = ecc_posterior_samples.plot(plot_pdf=True)


# And even update the number of bins in the sample and overplot the Gaussian fit:

# In[16]:


_ = ecc_posterior_samples.plot(plot_sample=True, plot_sample_kwargs={'bins': 50}, plot_gaussian=True, plot_uncertainties=True)


# In addition to individual parameter posteriors, it's useful to also look at the corner plot of the entire final sample, which unveils more information on the parameter correlations (the more skewed a 2D posterior is, the more correlated the two parameters are). Let's see the diffrence in the corner plots with the two distributions we adopted:

# In[17]:


_ = b.plot_distribution_collection('ndg_final_mvsamples')


# In[18]:


_ = b.plot_distribution_collection('ndg_final_mvgaussian')


# We see that the 'mvgaussian' distribution look much nicer than the 'mvsamples' one and that comes directly from the fact that the samples were fitted with Gaussians before we adopted them. This may seem tempting for producing nice plots, but it is considered "tricking/cheating" your results into looking nicer than they actually are, especially if your posteriors are nowhere near Gaussian!

# Therefore, to avoid falling into these distribution conversion traps, while keeping the plots nice and smooth, we recommend plotting the corner plot of the solution directly and potentially using smoothing to avoid the choppy look of individual samples:

# In[19]:


_ = b.plot('final_round', style='corner', smooth=True)


# Finally, to view the mean values with their uncertainties outside of a plot, we can call:

# In[20]:


b.uncertainties_from_distribution_collection('ndg_final_mvsamples', tex=True)


# ## Posterior propagation

# The one major benefit of running MCMC with PHOEBE distributions is the option to propagate them through constraints (as we saw in the [distributions tutorial](./Tutorial_07_distributions.ipynb)), which allows us to get posteriors on parameters beyond the ones directly sampled. To achieve this, we can pass `parameters` to propagate this set of distributions through the constraint to any other parameter(s).  
# For example, let's see how eccentricity and argument of periastron look in `esinw` and `ecosw` instead.

# In[21]:


_ = b.plot_distribution_collection(solution='final_round', parameters=['ecc', 'per0'], show=True)


# In[22]:


_ = b.plot_distribution_collection(solution='final_round', parameters=['esinw', 'ecosw'], show=True)


# And we can also do the same thing as an argument to [uncertainties_from_distribution_collection](http://phoebe-project.org/docs/2.3/api/phoebe.frontend.bundle.Bundle.uncertainties_from_distribution_collection):

# In[23]:


b.uncertainties_from_distribution_collection(solution='final_round', parameters=['ecc', 'per0'], tex=True)


# In[24]:


b.uncertainties_from_distribution_collection(solution='final_round', parameters=['esinw', 'ecosw'], tex=True)


# As we've already seen several times, we can also sample from the posteriors to propagate through the forward model.

# In[25]:


b.run_compute(compute='nm_fit', solution='final_round', sample_num=20, model='post_prop')


# In[26]:


_ = b.plot(model='post_prop', kind='rv', x='phases', show=True)


# In[27]:


_ = b.plot(model='post_prop', kind='rv', x='phases', y='residuals', show=True)


# # Exercises
# 
# **Exercise 1**: We used the posterior on eccentricity to discuss what phoebe can do for us. Now run the same type of analysis on other parameters.

# In[ ]:




