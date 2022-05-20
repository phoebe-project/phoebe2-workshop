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


# In[19]:


b['fit_parameters@nms'] = ['teff@primary', 'teff@secondary', 'pblum@primary@mock']


# In[13]:


b.run_solver('nms', solution='adjust_teffs')


# In[16]:


print(b['adjust_teffs'])


# In[17]:


print(b['enabled'])


# In[15]:


b.calculate_chi2()


# NMS is demonstrably too slow, so we'll implement DC instead.

# In[ ]:





# In[17]:


def run_dc(steps):
    obs = b['value@fluxes@mock@dataset']
    sigs = b['value@sigmas@mock@dataset']
    fit_params = b['value@fit_parameters@nms']
    orig_values = [b[f'value@{param}'] for param in fit_params]

    A = np.empty(shape=(len(obs), len(fit_params)))
    V = np.diag(1/sigs)

    b.run_compute(irrad_method='none', model='baseline', overwrite=True)
    xi = obs-b['value@fluxes@baseline@model']

    for k, param in enumerate(fit_params):
        if 'pblum' in param:
            A[:,k] = 1
            continue
        b[param] = orig_values[k] + steps[k]/2
        b.run_compute(irrad_method='none', model='upper', overwrite=True)
        b[param] = orig_values[k] - steps[k]/2
        b.run_compute(irrad_method='none', model='lower', overwrite=True)
        b[param] = orig_values[k]

        A[:,k] = (b['value@fluxes@upper']-b['value@fluxes@lower'])/steps[k]

    return np.linalg.lstsq(V@A, V@xi, rcond=None)


# In[18]:


b['teff@secondary'] = 5880
b['fit_parameters@nms'] = ['teff@secondary', 'pblum@primary@mock', 'requiv@primary', 'requiv@secondary']
steps = [50, 0.01, 0.05, 0.05]
corrections = run_dc(steps)


# In[19]:


corrections


# In[48]:


b['teff@primary']


# In[ ]:




