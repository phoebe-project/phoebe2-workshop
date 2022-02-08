#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Distributions
# 
# In this tutorial we'll cover how to create, attach, and manipulate distribution objects.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Distributions](http://phoebe-project.org/docs/2.3/tutorials/distributions.ipynb)
# * [Advanced: Distribution Types](http://phoebe-project.org/docs/2.3/tutorials/distribution_propagation.ipynb)
# * [Advanced: Distribution Propagation](http://phoebe-project.org/docs/2.3/tutorials/distribution_propagation.ipynb)
# * [Advanced: Latex Representations in Distribution Plots](http://phoebe-project.org/docs/2.3/tutorials/latex_repr.ipynb)

# # Setup

# In[ ]:


import phoebe
from phoebe import u,c


# In[ ]:


logger = phoebe.logger(clevel='WARNING')


# In[ ]:


b = phoebe.default_binary()
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101))


# # Adding Distributions
# 
# Distributions can be attached to most any FloatParameter in the Bundle. To see a list of these available parameters, we can call [b.get_adjustable_parameters](http://phoebe-project.org/docs/2.3/api/phoebe.frontend.bundle.Bundle.get_adjustable_parameters.md). Note the `exclude_constrained` option which defaults to `True`: we can set distributions on constrained parameters (for priors, for example), but those will not be able to be sampled from in the forward model or while fitting. We'll come back to this in the next tutorial when looking at priors.

# In[ ]:


print(b.get_adjustable_parameters())


# The values of the [DistributionParameters](http://phoebe-project.org/docs/2.3/api/phoebe.parameters.DistributionParameter.md) are [distl](https://distl.readthedocs.io) distribution objects -- the most common of which are conveniently available at the top-level of PHOEBE:
# 
# * [phoebe.gaussian](http://phoebe-project.org/docs/2.3/api/phoebe.gaussian.md)
# * [phoebe.gaussian_around](http://phoebe-project.org/docs/2.3/api/phoebe.gaussian_around.md)
# * [phoebe.uniform](http://phoebe-project.org/docs/2.3/api/phoebe.uniform.md)
# * [phoebe.uniform_around](http://phoebe-project.org/docs/2.3/api/phoebe.uniform_around.md)
# 
# For an overview of the different available types as they apply in PHOEBE, see [Advanced: Distribution Types](http://phoebe-project.org/docs/2.3/tutorials/distribution_types.ipynb).
# 
# Now let's attach a gaussian distribution on the temperature of the primary star.

# In[ ]:


b.add_distribution(qualifier='teff', component='primary', 
                   value=phoebe.gaussian(6000,100), 
                   distribution='mydist')


# We can now add additional distributions (to other parameters) with this same distribution label.  In addition to the single-distribution syntax above, multiple distributions can be attached in a single call as follows:

# In[ ]:


b.add_distribution({'requiv@primary': phoebe.gaussian(1, 0.2),
                    'requiv@secondary': phoebe.gaussian(1.2, 0.25),
                    'incl@binary': phoebe.uniform(88,90)},
                   distribution='mydist')


# # Accesing & Plotting Distributions
# 
# The parameters we've created and attached are [DistributionParameters](http://phoebe-project.org/docs/2.3/api/phoebe.parameters.DistributionParameter.md) and live in `context='distribution'`, with all other tags matching the parameter they're referencing. For example, let's filter and look at the distributions we've added.

# In[ ]:


print(b.filter(context='distribution'))


# In[ ]:


print(b.get_parameter(context='distribution', qualifier='teff'))


# The "value" of the parameter, is the [distl](https://distl.readthedocs.io/) distributon object itself.

# In[ ]:


b.get_value(context='distribution', qualifier='teff')


# And because of that, we can call any method on the distl object, including plotting the distribution.

# In[ ]:


_ = b.get_value(context='distribution', qualifier='teff').plot(show=True)


# If we want to see how multiple individual distributions interact and are correlated with each other via a corner plot, we can access the combined "distribution collection" from any number of `distribution` tags. This may not be terribly useful now, but is very useful when trying to create multivariate priors.
# 
# * [b.get_distribution_collection](http://phoebe-project.org/docs/2.3/api/phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
# * [b.plot_distribution_collection](http://phoebe-project.org/docs/2.3/api/phoebe.frontend.bundle.Bundle.plot_distribution_collection.md)

# In[ ]:


_ = b.plot_distribution_collection(distribution='mydist', show=True)


# # Propagating Distributions through Constraints
# 
# We can pass a list of parameters (as twigs) to the `parameters` keyword argument to only plot a subset of the available parameters, but also to propagate distributions through constraints linking parameters together.

# In[ ]:


_ = b.plot_distribution_collection(distribution='mydist', 
                                   parameters=['incl@binary', 'asini@binary'],
                                   show=True)


# # Propagating Distributions through Forward Model
# 
# Lastly, we can have PHOEBE automatically draw from a "distribution collection" multiple times and expose the distribution of the model itself.

# In[ ]:


print(b.get_parameter(qualifier='sample_from', context='compute'))


# Once `sample_from` is set, `sample_num` and `sample_mode` are exposed as visible parameters

# In[ ]:


b.set_value('sample_from', value='mydist')


# In[ ]:


print(b.filter(qualifier='sample*'))


# Now when we call [run_compute](http://phoebe-project.org/docs/2.3/api/phoebe.frontend.bundle.Bundle.run_compute.md), 10 different instances of the forward model will be computed from 10 random draws from the "distribution collection" but only the median and 1-sigma uncertainties will be exposed in the model.

# In[ ]:


b.run_compute(irrad_method='none')


# In[ ]:


_ = b.plot(show=True)


# # Exercises
# 
# Start from scratch, add constraints on both `sma@binary` and `incl@binary` and see how those propagate through to `asini@binary`.

# In[ ]:





# Try setting distributions on parameters in Kepler's third law, flip constraints as necessary, and propagate the distributions through the Kepler's third law constraint.

# In[ ]:




