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
# * [Advanced: EMCEE Sampler](http://phoebe-project.org/docs/2.3/tutorials/emcee.ipynb)
# * [Advanced: Convert Posterior Distributions from EMCEE](http://phoebe-project.org/docs/2.3/tutorials/emcee_distributions_convert.ipynb)
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


# Let's take a closer look at, say, eccentricity:

# In[3]:


print(b['ecc@binary@distribution'])


# Why is the final round missing? Because we haven't adopted the solution yet:

# In[4]:


b.adopt_solution(solution='final_round',
                 adopt_values=False,
                 adopt_distributions=True,
                 distributions_convert='mvsamples',
                 distribution='ndg_final')


# If we print it again, there it is:

# In[5]:


print(b['ecc@binary@distribution'])


# Now let's take a closer look at the samples, so that we can follow the logic built into phoebe:

# In[6]:


print(b['value@ecc@binary@distribution@ndg_final'].samples)


# This particular structure is an MVSamplesSlice from the distl module. It's always a good idea to acquaint yourself with it first:

# In[7]:


help(b['value@ecc@ndg_final@distribution'])


# Now that we have the samples, we can extract them and plot a histogram:

# In[8]:


plt.hist(b['value@ecc@binary@distribution@ndg_final'].samples, bins=50)
plt.show()


# Excellent! Now let's overplot a gaussian:

# In[9]:


mean = b['value@ecc@binary@distribution@ndg_final'].mean()
stdev = b['value@ecc@binary@distribution@ndg_final'].std()
print('Mean: ', mean)
print('Stdev:', stdev)


# In[10]:


vals, bins, _ = plt.hist(b['value@ecc@binary@distribution@ndg_final'].samples, bins=50, density=True)
uvg = st.norm.pdf(bins, mean, stdev)
plt.plot(bins, uvg, 'r-')
plt.show()


# As you can imagine, this functionality is built into phoebe; to see the supported methods, run a `dir` on the sample:

# In[11]:


dir(b['value@ecc@binary@distribution@ndg_final'])


# Thus, it is straight-forward to reproduce the above two plots:

# In[12]:


ecc_posterior = b['value@ecc@binary@distribution@ndg_final']


# In[13]:


_ = ecc_posterior.plot_sample(bins=50)


# In[14]:


_ = ecc_posterior.plot_gaussian()


# We can also use a `plot()` method to combine the plots and make them even nicer:

# In[15]:


help(ecc_posterior.plot)


# In[16]:


_ = ecc_posterior.plot(plot_pdf=True)


# In[17]:


_ = ecc_posterior.plot(plot_sample=True, plot_sample_kwargs={'bins': 50}, plot_gaussian=True, plot_uncertainties=True)


# In[18]:


_ = b.plot_distribution_collection('ndg_final')


# And finally, we can convert distributions to multivariate gaussians, thus "polishing" the posteriors:

# In[19]:


_ = b.plot('final_round', style='corner', distributions_convert='mvgaussian')


# # Exercises
# 
# **Exercise 1**: We used the posterior on eccentricity to discuss what phoebe can do for us. Now run the same type of analysis on other parameters.

# In[ ]:




