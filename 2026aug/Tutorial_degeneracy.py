#!/usr/bin/env python
# coding: utf-8

# # Degeneracy woes
# 
# One of the most fundamental stumbling blocks for newcomers into the field of eclipsing binary stars is the realization that a _good-looking_ fit is not necessarily _unique_ nor _correct_. In other words, a _right_ combination of the _wrong_ parameters can fool you into thinking that the model is correct. In this tutorial we will generate our own dataset (so that we know what the actual true answer is). First things first, though, the usual imports.

# In[1]:


import phoebe
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='WARNING')


# Next up, we generate our model. Two main-sequence stars in a close orbit, no frills.

# In[2]:


b = phoebe.default_binary()
b['requiv@primary'] = 1.35
b['requiv@secondary'] = 0.80
b['teff@primary'] = 6150
b['teff@secondary'] = 5680
b['q@orbit'] = 0.78
b['incl@orbit'] = 83.5


# Let's generate a single lightcurve in Johnson V passband, and oversample it a little so that we gain full grasp of its topological beauty:

# In[3]:


b.add_dataset('lc', times=phoebe.linspace(-0.6, 0.6, 241), passband='Johnson:V', dataset='ideal_lc', overwrite=True)
b.run_compute(irrad_method='none')
b.plot(show=True)


# This is arguably quite a feature*ful* lightcurve, which makes us expect that parameters will be reasonably well constrained. We will use this lightcurve as a generative model for the data:

# In[4]:


times = b['value@times@model@ideal_lc']
fluxes = b['value@fluxes@model@ideal_lc'] + np.random.normal(0, 0.01, size=241)
sigmas = np.ones_like(times)*0.01


# Let's add another dataset (called `mock`) that will provide the data we just generated:

# In[5]:


b.add_dataset('lc', passband='Johnson:V', times=times, fluxes=fluxes, sigmas=sigmas, dataset='mock')


# We no longer need the original dataset so we will remove it:

# In[6]:


b.remove_dataset('ideal_lc')


# We now make sure that everything is up to snuff and looks good:

# In[7]:


b.run_compute(irrad_method='none')
b.plot(show=True)


# So far we did not modify any parameter values, so the chi2 value will be near-minimal (we say "near" because any stochastic non-gaussianity might affect the chi2 value slightly):

# In[8]:


b.calculate_chi2()


# This is the chi2 value that the minimizer should gravitate to. Typically, the Nelder & Mead optimizer is favored because it is globally convergent as it depends only on function evaluations, but this pro comes at a cost of prolonged computation time. Instead, we will use the _locally_ convergent differential corrections (DC) algorithm instead.

# In[9]:


b.add_solver('optimizer.differential_corrections', solver='dc')


# In a nutshell, DC minimizes the residuals between the data and the model by evaluating numerical derivatives of the residuals w.r.t. each adjusted parameter. By doing that, it finds the corrections for each adjusted parameter that reduce the overall residuals. In order for DC to work well, the starting point needs to be close to the optimum, steps for numerical derivation need to be chosen reasonably well, and data noise needs to be normally distributed, homoskedastic and uncorrelated. Even a casual reader will have noticed the use of "close" and "reasonably well" that are largely meaningless -- both depend on many aspects of data fitting: from dynamical space spun by the parameters to data noise and adjusted parameter correlations. Trial and error is the only fool-proof way of attributing the quantitative meaning to "close" and "reasonably well".

# Now let's see how parameters react to being modified, and if we can trust DC to drive them back to their initial value. We start with displacing a single parameter (secondary star's effective temperature):

# In[10]:


print(f"original T2: {b['value@teff@secondary']}")
b['teff@secondary'] = 5880
print(f"modified T2: {b['value@teff@secondary']}")
b['fit_parameters@dc'] = 'teff@secondary'
b['steps@dc@solver'] = {
    'teff@secondary': 50
}

b.run_solver(solver='dc', solution='dcsol', progressbar=False, overwrite=True)
print(f"adjusted T2: {b['value@fitted_values@dcsol'][0]}")


# Unlike other optimizers, DC steps one iteration of the time. We can run another couple of iterations to get to a converged solution:

# In[11]:


b.adopt_solution('dcsol')

for iter in range(2, 4):
    b.run_solver(solver='dc', solution='dcsol', progressbar=False, overwrite=True)
    print(f"adjusted T2: {b['value@fitted_values@dcsol'][0]} (iter {iter})")
    b.adopt_solution(solution='dcsol')


# Next, let's try to vary more parameters than just the one we displaced; the obvious choices are passband luminosity (to account for flux scaling) and equivalent radii. We will also leave steps at their defaults, which is 1% of the parameter value.

# In[12]:


print(f"original T2: {b['value@teff@secondary']}")
b['teff@secondary'] = 5880
print(f"modified T2: {b['value@teff@secondary']}")
b['fit_parameters@dc'] = ['teff@secondary', 'pblum@primary@mock', 'requiv@primary', 'requiv@secondary']

for iter in range(1, 4):
    b.run_solver('dc', solution='dcsol', progressbar=False, overwrite=True)
    print(f"adjusted T2: {b['value@fitted_values@dcsol'][0]} (it {iter})")
    b.adopt_solution('dcsol')


# In[13]:


print(b['dcsol'])


# So far this looks quite reasonable; now let's add the primary temperature to the mix, and increase the number of iterations. Let's also track the chi2 value for each iteration:

# In[14]:


b['fit_parameters@dc'] = ['teff@primary', 'teff@secondary', 'pblum@primary@mock']
b['steps@dc@solver'] = {
    'teff@primary': 50,
    'teff@secondary': 50,
    'pblum@primary@mock': 0.05
}

for iter in range(1, 5):
    b.run_solver('dc', solution='dcsol', progressbar=False, overwrite=True)
    b.adopt_solution('dcsol')
    print(f"iteration {iter:02d}: {b['value@fitted_values@dcsol']}, chi2={b['value@fitted_chi2@dcsol']}")


# Now _that_ looks surprising: both temperatures change by a few hundred K each iteration, yet chi2 does not move much; how is that possible? We should plot the lightcurve to see if chi-by-eye is equally good:

# In[15]:


b.run_compute(irrad_method='none', model='baseline', overwrite=True)
b['mock'].plot(show=True, legend=True)


# You guessed it: as flux scaling is prescribed by the parametrized luminosity (`pblum`), absolute temperatures have little impact on a single lightcurve. It is their _ratio_ that exacts a significant influence by modifying eclipse depth ratios. Their absolute values, on the other hand, only marginally influence the light curve, mostly through limb darkening and, to an even lesser extent, through reflection (which we turned off anyway). The situation where different parameters yield indistinguishable values of the cost function is called a _degeneracy_.
# 
# Another significant degeneracy arises between stellar sizes (equivalent radii) and orbital inclination: a slightly larger star at a slightly lower inclination will have a lightcurve indistinguishable from a slightly smaller star at a slightly higher inclination. Let's take a closer look at that! First, reset parameter values:

# In[16]:


b['requiv@primary'] = 1.35
b['requiv@secondary'] = 0.80
b['teff@primary'] = 6150
b['teff@secondary'] = 5680


# Now we loop over nearby inclinations and adjust other relevant parameters:

# In[17]:


b['fit_parameters@dc'] = ['requiv@primary', 'requiv@secondary', 'pblum@primary@mock']
b['steps@dc@solver'] = {
    'requiv@primary':0.03,
    'requiv@secondary': 0.03,
    'pblum@primary@mock': 0.03
}
req1s, req2s = [], []

for incl in np.linspace(81.5, 85.5, 9):
    for iter in range(1, 4):
        b.run_solver('dc', solution='dcsol', progressbar=False, overwrite=True)
        b.adopt_solution(solution='dcsol')
        print(f"incl: {incl:4.1f}, solution: {b['value@fitted_values@dcsol']}, chi2: {b['value@fitted_chi2@dcsol']} (it {iter})")
        if iter == 3:
            req1s.append(b['value@requiv@primary'])
            req2s.append(b['value@requiv@secondary'])


# The mere fact that all these chi2 values are in the same ballpark is already alarming and it should help you appreciate that formal errors computed from the covariance matrix (which we deliberately omit from this tutorial because they are largely meaningless) are grossly underestimated. On the flip side, we will show you how to sample the parameter space heuristically and obtain more realistic error estimates. For now, let us see how the equivalent radii correlate with inclination:

# In[18]:


plt.xlabel('Inclination')
plt.ylabel('R2/R1')
plt.plot(np.linspace(81.5, 85.5, 9), np.array(req2s)/np.array(req1s), 'bo')


# This tutorial only scratched the surface of a very complicated issue. Chances are that, provided you stay in the field, _everything_ you do over the course of your career will be plagued by degeneracy.

# ### Exercises
# 
# 1. Thinking about geometry and radiation, what other parameters would you expect to exhibit a large degree of correlation, and in consequence lead to degeneracy? Write them out here and justify your reasoning.

# 

# 2. Explore the correlation between equivalent radii, and the correlation between the mass ratio and secondary star's equivalent radius.

# In[ ]:




