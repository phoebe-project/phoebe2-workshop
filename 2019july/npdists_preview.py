#!/usr/bin/env python
# coding: utf-8

# # npdists package (experimental, unreleased, prototype, untested)
# 
# but if you're really curious or want to help with development, this uses the 'multivariate' branch in [github.com/kecnry/npdists](http://github.com/kecnry/npdists) with some documentation at [npdists.readthedocs.io](https://npdists.readthedocs.io/en/latest/).

# In[1]:


import numpy as np
import npdists as npd
from phoebe import u


# ## Uniform / Boxcar

# In[2]:


b = npd.uniform(5,10)


# In[3]:


b.sample()


# In[4]:


b.sample(5)


# In[5]:


out = b.plot(show=True)


# ## Gaussian / Normal

# In[6]:


g = npd.gaussian(7.5, 2)


# In[7]:


out = g.plot(show=True)


# ## Accessing log probability for a given sampled value

# In[8]:


b.logp(2)


# In[9]:


b.logp(7)


# In[10]:


b.logp(8)


# In[11]:


g.logp(6)


# In[12]:


g.logp(7)


# In[13]:


g.logp(g.sample())


# In[14]:


npd.logp_from_dists((b,g), (5,7))


# ## Math with distributions

# In[28]:


sma = npd.gaussian(6, 1, unit=u.solRad, label='sma')


# In[29]:


incl = npd.gaussian(88.5, 2, unit=u.deg, label='incl')


# In[30]:


asini = sma * np.sin(incl)


# In[36]:


asini.label = 'asini'


# In[37]:


asini


# In[34]:


print(asini)


# In[33]:


out = asini.plot(show=True)


# ## Multivariate / Correlated Distributions

# In[49]:


mvg = npd.mvgaussian((10,6), np.matrix([[5, 0.8], [0.8, 1.5]]))


# In[50]:


mvg


# In[51]:


mvg.sample()


# In[52]:


out = mvg.plot(show=True)


# ## From Posteriors
# 
# Can build also build `histogram` and `mvhistogram` distributions from an array of sampled values (i.e. chains from MCMC).  When these are well-behaved, the eventual plan is to be able to convert/fit to analytic distributions... making them smooth and more portable.
# 
# The eventual plan is to allow PHOEBE to store the distributions, pass them on to MCMC as either initial distributions and/or priors, and parse the output chains into posteriors.

# In[ ]:




