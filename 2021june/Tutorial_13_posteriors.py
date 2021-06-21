#!/usr/bin/env python
# coding: utf-8

# In[30]:


import phoebe
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st


# In[2]:


b = phoebe.load('./data/synthetic/after_final_round.bundle')


# In[4]:


print(b['ecc@binary@distribution'])


# In[5]:


b.solutions


# In[6]:


b.adopt_solution(solution='final_round',
                 adopt_values=False,
                 adopt_distributions=True,
                 distributions_convert='mvsamples',
                 distribution='ndg_final')


# In[19]:


print(b['value@ecc@binary@distribution@ndg_final'].samples)


# In[16]:


help(b['value@ecc@ndg_final@distribution'])


# In[20]:


plt.hist(b['value@ecc@binary@distribution@ndg_final'].samples, bins=50)
plt.show()


# In[26]:


mean = b['value@ecc@binary@distribution@ndg_final'].mean()
stdev = b['value@ecc@binary@distribution@ndg_final'].std()
print('Mean: ', mean)
print('Stdev:', stdev)


# In[48]:


vals, bins, _ = plt.hist(b['value@ecc@binary@distribution@ndg_final'].samples, bins=50, density=True)
uvg = st.norm.pdf(bins, mean, stdev)
plt.plot(bins, uvg, 'r-')
plt.show()


# In[37]:


dir(b['value@ecc@binary@distribution@ndg_final'])


# In[38]:


ecc_posterior = b['value@ecc@binary@distribution@ndg_final']


# In[44]:


_ = ecc_posterior.plot_sample(bins=50)


# In[45]:


_ = ecc_posterior.plot_gaussian()


# In[49]:


help(ecc_posterior.plot)


# In[54]:


_ = ecc_posterior.plot(plot_pdf=True)


# In[57]:


_ = ecc_posterior.plot(plot_sample=True, plot_sample_kwargs={'bins': 50}, plot_gaussian=True, plot_uncertainties=True)


# In[59]:


_ = b.plot_distribution_collection('ndg_final')


# In[61]:


_ = b.plot('final_round', style='corner', distributions_convert='mvgaussian')


# In[ ]:




