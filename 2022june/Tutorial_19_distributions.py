#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Distributions
# 
# In this tutorial we'll cover how to create, attach, and manipulate distribution objects.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Distributions](http://phoebe-project.org/docs/2.4/tutorials/distributions.ipynb)
# * [Advanced: Distribution Types](http://phoebe-project.org/docs/2.4/tutorials/distribution_propagation.ipynb)
# * [Advanced: Distribution Propagation](http://phoebe-project.org/docs/2.4/tutorials/distribution_propagation.ipynb)
# * [Advanced: Latex Representations in Distribution Plots](http://phoebe-project.org/docs/2.4/tutorials/latex_repr.ipynb)

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101))


# # Adding Distributions
# 
# Distributions can be attached to most any FloatParameter in the Bundle. To see a list of these available parameters, we can call [b.get_adjustable_parameters](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.get_adjustable_parameters.md). Note the `exclude_constrained` option which defaults to `True`: we can set distributions on constrained parameters (for priors, for example), but those will not be able to be sampled from in the forward model or while fitting. We'll come back to this in the next tutorial when looking at priors.

# In[4]:


print(b.get_adjustable_parameters())


# The values of the [DistributionParameters](http://phoebe-project.org/docs/2.4/api/phoebe.parameters.DistributionParameter.md) are [distl](https://distl.readthedocs.io) distribution objects -- the most common of which are conveniently available at the top-level of PHOEBE:
# 
# * [phoebe.gaussian](http://phoebe-project.org/docs/2.4/api/phoebe.gaussian.md)
# * [phoebe.gaussian_around](http://phoebe-project.org/docs/2.4/api/phoebe.gaussian_around.md)
# * [phoebe.uniform](http://phoebe-project.org/docs/2.4/api/phoebe.uniform.md)
# * [phoebe.uniform_around](http://phoebe-project.org/docs/2.4/api/phoebe.uniform_around.md)
# 
# For an overview of the different available types as they apply in PHOEBE, see [Advanced: Distribution Types](http://phoebe-project.org/docs/2.4/tutorials/distribution_types.ipynb).
# 
# Now let's attach a gaussian distribution on the temperature of the primary star.

# In[5]:


b.add_distribution(qualifier='teff', component='primary', 
                   value=phoebe.gaussian(6000,100), 
                   distribution='mydist')


# We can now add additional distributions (to other parameters) with this same distribution label.  In addition to the single-distribution syntax above, multiple distributions can be attached in a single call as follows:

# In[6]:


b.add_distribution({'requiv@primary': phoebe.gaussian(1, 0.2),
                    'requiv@secondary': phoebe.gaussian(1.2, 0.25),
                    'incl@binary': phoebe.uniform(88,90)},
                   distribution='mydist')


# # Accesing & Plotting Distributions
# 
# The parameters we've created and attached are [DistributionParameters](http://phoebe-project.org/docs/2.4/api/phoebe.parameters.DistributionParameter.md) and live in `context='distribution'`, with all other tags matching the parameter they're referencing. For example, let's filter and look at the distributions we've added.

# In[7]:


print(b.filter(context='distribution'))


# In[8]:


print(b.get_parameter(context='distribution', qualifier='teff'))


# The "value" of the parameter, is the [distl](https://distl.readthedocs.io/) distributon object itself.

# In[9]:


b.get_value(context='distribution', qualifier='teff')


# And because of that, we can call any method on the distl object, including plotting the distribution.

# In[10]:


_ = b.get_value(context='distribution', qualifier='teff').plot(show=True)


# If we want to see how multiple individual distributions interact and are correlated with each other via a corner plot, we can access the combined "distribution collection" from any number of `distribution` tags. This may not be terribly useful now, but is very useful when trying to create multivariate priors.
# 
# * [b.get_distribution_collection](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
# * [b.plot_distribution_collection](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.plot_distribution_collection.md)

# In[11]:


_ = b.plot_distribution_collection(distribution='mydist', show=True)


# # Using Distributions as Priors
# 
# Most solvers that include the forward model (optimizers & samplers) have a `priors` parameter which accepts a list of distribution tags which will then be used as priors in the merit function.
# 
# `lnprobability = lnlikelihood + lnpriors`
# 
# for more information see [this slide from Andrej's talk](https://docs.google.com/presentation/d/e/2PACX-1vT_GwcoD_0Tz-5V1dEolYYFCMp2qxrfKqfySOCI9QU3rpMuR7ANGY_rDiLRZbXnrvTN57x6qndroC0Z/pub?start=false&loop=false&delayms=3000&slide=id.g1257bc21d63_0_13) and the API docs for [b.calculate_residuals](http://phoebe-project.org/docs/2.4/api/phoebe.parameters.ParameterSet.calculate_residuals.md), [b.calculate_chi2](http://phoebe-project.org/docs/2.4/api/phoebe.parameters.ParameterSet.calculate_chi2.md), [b.calculate_lnlikelihood](http://phoebe-project.org/docs/2.4/api/phoebe.parameters.ParameterSet.calculate_lnlikelihood.md).
# 
# `lnpriors` is the probability of drawing the _current parameter face-values_ from the distributions assigned as priors.  We can expose the probability of drawing the current values from our `'mydist'` distribution with [b.calculate_lnp](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.calculate_lnp.md).  But note that this _only_ becomes the `lnpriors` when `'mydist'` is included within the `priors` parameter of a given solver.

# In[12]:


b.calculate_lnp(distribution='mydist')


# In[13]:


b.add_solver('optimizer.nelder_mead', solver='nm_solver')


# In[14]:


print(b.get_parameter('priors', solver='nm_solver'))


# In[15]:


b.set_value('priors', value=['mydist'])


# In[16]:


print(b.filter(qualifier='priors*'))


# As a shortcut, we can pass a pointer to the `priors` parameter itself.  This will automatically account for combining multiple distributions as defined by `priors_combine` and will ensure that constrained parameters are included (`include_constrained=True`, which is the default for `calculate_lnp`):

# In[17]:


b.calculate_lnp('priors@nm_solver')


# Now if we change a face-value of one of the parameters within this distribution, we'll see the probability change.

# In[18]:


b.set_value('teff', component='primary', context='component', value=5500)


# In[19]:


b.calculate_lnp('priors@nm_solver')


# If we do the same of an _uninformative_ (uniform) distribution, we'll get -inf returned if the value is outside the bounds of the boxcar distribution, which within an optimizer or sampler would immediately reject that step before even running the forward model

# In[20]:


b.set_value('incl', component='binary', context='component', value=87)


# In[21]:


b.calculate_lnp('priors@nm_solver')


# This allows using _uninformative_ (uniform) distributions as priors to set artificial limits on parameters - but should _only_ be done for good reason!

# # Propagating Distributions through Constraints
# 
# We can pass a list of parameters (as twigs) to the `parameters` keyword argument to only plot a subset of the available parameters, but also to propagate distributions through constraints linking parameters together.

# In[22]:


_ = b.plot_distribution_collection(distribution='mydist', 
                                   parameters=['incl@binary', 'asini@binary'],
                                   show=True)


# # Propagating Distributions through Forward Model
# 
# Lastly, we can have PHOEBE automatically draw from a "distribution collection" multiple times and expose the distribution of the model itself.

# In[23]:


print(b.get_parameter(qualifier='sample_from', context='compute'))


# Once `sample_from` is set, `sample_num` and `sample_mode` are exposed as visible parameters

# In[24]:


b.set_value('sample_from', value='mydist')


# In[25]:


print(b.filter(qualifier='sample*'))


# Now when we call [run_compute](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.run_compute.md), 10 different instances of the forward model will be computed from 10 random draws from the "distribution collection" but only the median and 1-sigma uncertainties will be exposed in the model.

# In[26]:


b.run_compute(irrad_method='none')


# In[27]:


_ = b.plot(show=True)


# # Exercises
# 
# Start from scratch, add constraints on both `sma@binary` and `incl@binary` and see how those propagate through to `asini@binary`.

# In[ ]:





# Try setting distributions on parameters in Kepler's third law, flip constraints as necessary, and propagate the distributions through the Kepler's third law constraint.

# In[ ]:





# Try adding multiple distributions (with different `distribution` labels), set as priors, and play with the different options for `priors_combine`.

# In[ ]:




