#!/usr/bin/env python
# coding: utf-8

# In[1]:


import phoebe
import numpy as np
logger = phoebe.logger(clevel='WARNING')


# In[2]:


b = phoebe.default_binary()
b['requiv@primary'] = 1.35
b['requiv@secondary'] = 0.80
b['teff@primary'] = 6150
b['teff@secondary'] = 5680
b['q@orbit'] = 0.78
b['incl@orbit'] = 83.5


# In[3]:


b.add_dataset('lc', times=phoebe.linspace(-0.6, 0.6, 241), passband='Johnson:V', dataset='ideal_lc', overwrite=True)


# In[4]:


b.run_compute(irrad_method='none')


# In[5]:


b.plot(show=True)


# This is arguably quite a feature*ful* lightcurve, so let's see which parameters are well determined.

# In[6]:


times = b['value@times@model@ideal_lc']
fluxes = b['value@fluxes@model@ideal_lc'] + np.random.normal(0, 0.01, size=241)
sigmas = np.ones_like(times)*0.01


# In[7]:


b.add_dataset('lc', passband='Johnson:V', times=times, fluxes=fluxes, sigmas=sigmas, dataset='mock')


# In[8]:


b.disable_dataset('ideal_lc')


# In[9]:


b.run_compute(irrad_method='none')


# In[10]:


b.plot(show=True)


# In[11]:


b.add_solver('optimizer.nelder_mead', solver='nms', maxfev=100, fatol=0.000241, overwrite=True)


# In[12]:


b['fit_parameters@nms'] = ['teff@primary', 'teff@secondary', 'pblum@primary']


# In[13]:


b.run_solver('nms', solution='adjust_teffs')


# In[15]:


print(b['adjust_teffs'])


# In[17]:


print(b['enabled'])


# In[ ]:




