#!/usr/bin/env python
# coding: utf-8

# ## Breakout session: semi-detached and contact binaries in PHOEBE

# In[1]:


import phoebe
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# ### SEMI - DETACHED

# Building a semi-detached system in Phoebe is very straight-forward. All you need to do is add a 'semidetached' constraint to the desired component in the Bundle, which will fix the component's radius to the critical one.

# Let's start with the default Bundle, as usual:

# In[2]:


b = phoebe.default_binary()


# Assuming that the primary star in our binary is filling it's Roche lobe, we can add a semidetached constraint as:

# In[3]:


b.add_constraint('semidetached', 'primary')


# The above call adds a constraint on the requiv of the primary star. We can view it by accessing the constraint:

# In[4]:


b['requiv@constraint@primary']


# Now whenever any of the relevant parameters (q, ecc, syncpar, sma) are changed, the value of requiv will change to match the critical value as defined by requiv_max. Let's change some of the parameters and see how it affects the value of the constrained requiv:

# In[5]:


b['q'] = 1.3
b['requiv@constraint@primary']


# In[6]:


b['sma@binary'] = 6.
b['requiv@constraint@primary']


# Let's finally add, compute and plot the mesh of the above system.

# In[7]:


b.add_dataset('mesh', times=[0.25])


# In[8]:


b.run_compute(irrad_method='none')


# In[9]:


afig, mplfig = b.plot(show=True)


# ### CONTACT

# A contact binary Bundle is created by passing **contact_binary=True** to the default binary bundle.

# In[30]:


cb = phoebe.default_binary(contact_binary = True)


# The main difference between the detached and contact binary Bundles is in the *hierarchy* of the system. In addition to the two star components, contact binaries have an **envelope component** as well.

# In[31]:


print(cb.hierarchy)


# The parameters of the system are distributed between the star and envelope components. The stellar parameters, like mass, radius, temperature, etc. are attached to the primary and secondary star components. The overall (shared) parameters, like potential, fillout factor, metallicity, etc. are attached to the envelope component. For a full list of parameters associated with each component, we can filter on them:

# In[32]:


print(cb.filter(context='component', kind='star', component='primary'))


# In[33]:


print(cb.filter(context='component', kind='star', component='secondary'))


# As before, the parameters marked with a `C` are constrained by other parameters. If we compare the primary and secondary, we notice that the equivalent radius (requiv) of the primary is a free parameter, while the secondary requiv is constrained by the envelope potential, mass ratio and semi-major axis of the system:

# In[34]:


print(cb['requiv@secondary@constraint'])


# This is one way in which the implementation of contact binaries in PHOEBE differes from the detached systems. The relative sizes of the two stars are "linked" through the shared envelope potential and mass ratio of the system, thus only the primary requiv needs to be provided by the user.

# Let's filter on the envelope component:

# In[35]:


print(cb.filter(context='component', kind='envelope'))


# As you can see, all of the envelope parameters except the abundance are constrained. Let's check which parameters constrain the fillout factor and potential:

# In[36]:


print(cb['fillout_factor@contact_envelope@constraint'])


# In[37]:


print(cb['pot@contact_envelope@constraint'])


# From the above two calls we can see that the fillout factor is constrained by the potential of the envelope, which is in turn constrained by the primary equivalent radius. This allows for a lot of freedom in terms of which parameters are chosen to describe a contact binary system - if we're comparing to evolutionary simulations, we probably know the values of the equivalent radii or the fillout factor; if we have a phoebe-legacy model, we know the value of the potential instead. This allows for easy and accurate comparison with other codes and models.

# #### ** Note on fillout factor

# There are several different definitions of the fillout factor used in the literature. In Phoebe we use the following:
# \begin{equation}
# FF = \frac{\Omega - \Omega_{L1}}{\Omega_{L23} - \Omega_{L1}}
# \end{equation}
# where $\Omega$ is the envelope potential, and $\Omega_{L1}$ and $\Omega_{L23}$ are the inner and outer critical potentials, respectively. Thus, the fillout factor is 0 at the inner and 1 at the outer critical potential.

# To be able to set the potential, you just need to flip the constraint to solve for requiv@primary:

# In[38]:


cb.flip_constraint('pot@contact_envelope', solve_for='requiv@primary')


# The fillout factor is constrained by the potential, so to be able to set it, we need to do another constraint flip:

# In[39]:


cb.flip_constraint('fillout_factor', solve_for='pot@contact_envelope')


# #### Meshes, datasets, compute

# Everything else works the same as for detached systems, with certain contact binary - related precautions that need to be taken into account. We'll get to them in this section.

# Let's add a mesh and light curve dataset, compute and plot the model.

# In[40]:


cb.add_dataset('mesh', times=[0.125], dataset='mesh01', columns=['teffs'], overwrite=True)
cb.add_dataset('lc', times=np.linspace(0.,0.5,50), dataset='lc01', overwrite=True)


# In[41]:


cb.run_compute()


# In[42]:


_ = cb.plot('mesh01', fc='teffs', ec='face', fcmap='plasma', show=True)


# *Fun, but impractical* - since the mesh is still assigned to each component separately, we can also plot just a half of the envelope that pertains to one star:

# In[43]:


_ = cb.plot('mesh01@primary', fc='teffs', ec='face', fcmap='plasma', show=True)


# In[44]:


_ = cb.plot('lc01', show=True)


# The way the surface temperature values are assigned is also component-dependent, so the two "halves" of the envelope are treated like single, separate stars that are separated in the neck by an artifical boundary that the code introduces. This treatment was first implemented in W-D and we are working towards a better, more physical solution.

# To illustrate the component splitting in terms of temperature distribution, let's change one of the effective temperatures and the recommended values of gravity brightening and reflection coefficient for that temperature:

# In[45]:


cb.set_value('teff', component='primary', value=9000.)


# In[46]:


cb.set_value('gravb_bol', component='primary', value=1.)
cb.set_value('irrad_frac_refl_bol', component='primary', value=1.)


# In[47]:


cb.run_compute()


# In[48]:


_ = cb.plot('mesh01', facecolor='teffs', ec='face', fcmap='plasma', show=True)


# ### Failed meshes

# Because the mesh of a contact binary envelope is not convex, certain combinations of parameters (i.e. very low or very high fillout factor, very low mass ratio) can lead to failing or weird marching meshes.

# In[49]:


cb['q'] = 0.1
cb['fillout_factor'] = 0.05


# In[50]:


cb.run_compute()


# There is no direct solution to an issue like this one - in cases of small fillout factors it might work to use a detached system close to fillout instead or increase the value of the fillout factor until a mesh can be created successfully. 
# 
# In other cases it's sufficient to increase the number of triangles. For example:

# In[51]:


cb['q'] = 0.1
cb['fillout_factor'] = 0.1


# In[52]:


cb.run_compute()


# In[53]:


cb.run_compute(ntriangles=5000) # will compute successfully


# In[54]:


ax, artists = cb.plot('mesh01', show=True)

