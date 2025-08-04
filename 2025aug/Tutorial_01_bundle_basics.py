#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: General Concepts & Bundle Basics
# 
# In this first tutorial, we will learn the basics of the "Bundle" - the container for all parameters within PHOEBE.  We will cover access to individual parameters and learn how to get and set their values.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [The PHOEBE Bundle](http://phoebe-project.org/docs/2.4/tutorials/general_concepts.ipynb)
# * [Advanced: Parameter Types](http://phoebe-project.org/docs/2.4/tutorials/parameters.ipynb)
# * [Advanced: Parameter Units](http://phoebe-project.org/docs/2.4/tutorials/units.ipynb)
# * [Advanced: Building a System](http://phoebe-project.org/docs/2.4/tutorials/building_a_system.ipynb)
# * [Advanced: Contact Binary Hierarchy](http://phoebe-project.org/docs/2.4/tutorials/contact_binary_hierarchy.ipynb)
# * [Advanced: Semi-Detached Systems](http://phoebe-project.org/docs/2.4/tutorials/requiv_crit_semidetached.ipynb)
# * [Advanced: Saving, Loading, and Exporting](http://phoebe-project.org/docs/2.4/tutorials/saving_and_loading.ipynb)

# # Setup

# In[55]:


import phoebe
from phoebe import u


# In[56]:


logger = phoebe.logger(clevel='WARNING')


# # The Bundle

# Everything for our system will be stored in a single Python object that we call the "Bundle". Let us create a default binary system and store it in a Bundle object variable `b` (short for bundle).

# In[57]:


b = phoebe.default_binary()


# The Bundle is a collection of parameters along with some callable methods. Each parameter is also a python object. Here we can see that the Bundle consists of over 140 individual parameters:

# In[58]:


b


# If we want to know what see a list of parameters, we just need to print the bundle:

# In[59]:


print(b)


# If we think of the bundle as a database/dataframe, each parameter in the database has several tags that uniquely identify it. The qualifier, which is the shorthand for the name of the parameter is a tag. To access the list of qualifiers, we type the plural of the tag name (we type it as an attribute, without brackets after):

# In[60]:


b.qualifiers


# We further classify parameters with additional tags, for example, the "component" tag and the "context" tag. To see all the possible tags, type:

# In[61]:


b.tags.keys()


# To get a list of possible values for the `component` tag, we type the plural of the tag name (as an attribute on the bundle, no brackets needed):

# In[62]:


b.components


# The component tag tells me if the parameter is associated with the primary, the secondary or with the binary. To get a list of the values for the `context` tag, we do the same:

# In[63]:


b.contexts


# The context tag tells me more about the type of parameter. E.g., parameters with the tag of context=system include distance, ra and dec.

# ## Filtering Parameter Sets

# As we already saw, each `Parameter` object has a number of tags which are used to uniquely identify it. We can use the tags to filter parameters, akin to a database query. When filtering, a `ParameterSet` is returned - a python object that holds a set of `Parameter` objects. We can keep filtering using multiple tags until they obtain a single `Parameter`.

# In[64]:


b.filter(context='compute')


# To get an actual list of parameters, you can print the corresponding `ParameterSet`:

# In[65]:


print(b.filter(context='compute'))


# Here we filtered on the "context" tag for all parameters where context='compute'. This tag refers to parameters that determine how a forward model is computed. 

# Although technically there is no hierarchy to the tags, it can be helpful to think of the "context" tag as the top-level tag and we should filter by the appropriate context first. We will discuss other tags in detail today and tomorrow.

# Now that I have a `ParameterSet` that contains all the `Parameters` that all fall under the context "compute", if I want to then filter on the component tag, we can look at the options available for the component tag by specifying the plural for the tag name as an attribute to the filter:

# In[66]:


b.filter(context='compute').components


# This then tells us what can be used to filter further.

# In[67]:


b.filter(context='compute').filter(component='primary')


# You can also filter in a single call to `filter()`, by naming keyword arguments appropriately:

# In[68]:


b.filter(context='compute', component='primary')


# As already mentioned, the "qualifier" tag is the shorthand name of the parameter itself.  If you do not know the name of the parameter you need, it is often useful to list all the qualifiers of the `Bundle` or a given `ParameterSet`:

# In[69]:


b.filter(context='compute', component='primary').qualifiers


# If we want to know more information about the parameters in our `ParameterSet`, we can use the "info" attribute. Note that we must print the output:

# In[70]:


print(b.filter(context='compute', component='primary').info)


# Now that we know the options for qualifiers within this `filter`, we can choose to filter on one qualifier to look at in more detail. For example, let us filter on the `ntriangles` qualifier.

# In[71]:


b.filter(context='compute', component='primary', qualifier='ntriangles')


# Now we have one parameter in our parameter set. We can also print the results of our filter to find out more information:

# In[72]:


print(b.filter(context='compute', component='primary', qualifier='ntriangles'))


# Once we filter to a single `Parameter`, we can use `get_parameter()` instead of `filter()` to return the `Parameter` object itself (instead of a `ParameterSet`). Important: `get_parameter()` only works on single parameters. If you have more than one `Parameter` in your `ParameterSet`, `get_parameter()` will return an error.

# In[73]:


b.filter(context='compute', component='primary', qualifier='ntriangles').get_parameter()


# Again, the difference between `filter()` and `get_parameter()` is that `filter()` returns a `ParameterSet` whereas `get_parameter()` returns a single `Parameter` object.
# Note that `get_parameter()` also takes filtering keywords. The above line is thus equivalent to the following:

# In[74]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles')


# To see all the information about our parameter, we can print the `Parameter`:

# In[75]:


print(b.get_parameter(context='compute', component='primary', qualifier='ntriangles'))


# This gives us more information than just printing the filter, since we are printing the `Parameter`, which contains one parameter, instead of the `ParameterSet`.

# In[76]:


print(b.filter(context='compute', component='primary', qualifier='ntriangles'))


# An alternative way to access parameters is by concatenating the tag names together using "@" as the separator. We refer to these constructs as "twigs" (nomenclature was inspired by "a bundle of twigs"). We already saw some twigs when we were printing the bundle and the `ParameterSets`. Twigs can both return a `Parameter` or a `ParameterSet`:

# In[77]:


b['ntriangles@primary@compute']


# There are some minor limitations to using twigs that we will address as the workshop progresses, so for the time being we will use the more verbose, but also more explicit methods of accessing parameters. In general, though, the ways to access parameters are by-and-large interchangeable.

# ## Interacting with Parameters

# Each `Parameter` object contains several keys that provide information about that parameter.  These include `get_value()` and `get_description()` and some others, depending on the type of `Parameter`. 

# In[78]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_value()


# In[79]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_description()


# These methods also work on the bundle (not just on `Parameters`). For example:

# In[80]:


b.get_value(context='compute', component='primary', qualifier='ntriangles')


# Finally, adding a key to the twig will also provide access to it:

# In[81]:


b['ntriangles@primary@compute'].get_description()


# As the `ntriangles` parameter is an integer parameter, it also includes a key for the allowable limits.

# In[82]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_limits()


# In this case, we're looking at the Parameter called `ntriangles` with the component tag set to 'primary'.  This Parameter therefore defines how many triangles should be created when creating the mesh for the star named 'primary'.  By default, this is set to 1500 triangles, with allowable values above 100.
# 
# If we wanted a finer mesh, we would change the value using `.set_value()`:

# In[83]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').set_value(2000)


# We can also apply the `set_value()` method directly to the bundle:

# In[84]:


b.set_value(context='compute', component='primary', qualifier='ntriangles', value=2100)


# Now let's check the parameter to ensure that we have updated the value:

# In[85]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles')


# Twig access attempts to simplify the interface even more, so it is not necessary to explicitly provide `value` as part of the twig; it is also not necessary to provide *all* tags, just the ones that uniquely qualify the parameter:

# In[86]:


b['ntriangles@primary'] = 1500


# Now to see the `Parameter` value we simply state:

# In[87]:


b['ntriangles@primary']


# Importantly, when using twigs, if your twigs do not return a unique parmeter, the twigs act like a `filter()` and return a `ParameterSet` object. If your twigs uniqely qualify an individual parmaeter, the twigs will act like `get_parameter()` and return a `Parameter` object.

# As with the tags, you can call `.twigs` on any `ParameterSet` to see the "smallest unique twigs" of the contained parameters:

# In[88]:


b['compute'].twigs


# Now let us take a look at another parameter, say the `distortion_method` qualifier from that same `ParameterSet`. It has an added key, `choices`:

# In[89]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method')


# In[90]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_choices()


# We can only set a value if it is contained within this list - if you attempt to set a non-valid value, an error will be raised.

# In[91]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').set_value('rotstar')


# In[92]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_value()


# Parameter types include:
# 
# * String Parameter
# * Choice Parameter
# * Select Parameter
# * Float Parameter
# * Integer Parameter
# * Boolean Parameter
# * FloatArray Parameter
# 
# These parameter types and their available options are all described in detail in [Advanced: Parameter Types](http://phoebe-project.org/docs/2.4/tutorials/parameters.ipynb).

# To see a convenient representation of the names (twigs or qualifiers) of all parameters and their descriptions, we can look at the `info` attribute for any `Bundle` or `ParameterSet`:

# In[93]:


print(b.info)


# In[94]:


print(b.filter(context='component').info)


# ## Units
# 
# Each float parameter has an associated unit. Let us take a look at the semi-major axis ('sma') parameter for the binary orbit.

# In[95]:


b.get_parameter(qualifier='sma', component='binary', context='component')


# From the representation above, we can already see that the units are in solar radii. We can access the units directly via get_default_unit:

# In[96]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_default_unit()


# Calling get_value returns only the float of the value in these units:

# In[97]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value()


# Alternatively, you can access an actual "quantity" object that contains the value and unit by calling `get_quantity()`:

# In[98]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# Of course, recall from above that the entire family of get_*() methods can be used dierctly on the bundle:

# In[99]:


b.get_quantity(qualifier='sma', component='binary')


# Both `get_value()` and `get_quantity()` also accept a unit argument which will return the value or quantity in the requested units (if possible to convert). This unit argument takes either a unit object or a string representation that can be parsed:

# In[100]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value(unit=u.km)


# Note, here we are not changing the units in the bundle, we are just outputting the value in the specified units.

# If we want to change the default units, we can use `set_default_unit()`. Be careful when changing the units as this can affect the float-point precision.

# In[101]:


b.get_parameter(qualifier='sma', component='binary', context='component').set_default_unit('mm')


# In[102]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# In[103]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity(unit='solRad')


# ## Saving & Loading

# Finally, the entire bundle object can be saved to (and reloaded from) and ASCII file:

# In[104]:


b.save('test.phoebe')


# And loaded again:

# In[105]:


b = phoebe.load('test.phoebe')


# # Exercise

# Find and access the value of the effective temperature of the primary star via filtering and twig access.

# In[ ]:





# Find the choices for the `atm` parameter.

# In[ ]:





# Find what the `ltte` Parameter stands for.  Does it have choices?

# In[ ]:





# Change the default unit of the argument of periastron from degrees to radians and print the result with the new units.

# In[ ]:





# Set the default unit for all radii and the semi-major axes of all components to AU and then show their values. (Hint: you can also use `set_default_unit()` to act on a `Parameter` or `set_default_unit_all()` to act on a `ParameterSet`).

# In[ ]:





# Find and set the following Parameters:
# * Effective temperature of the secondary star to 5500 K;
# * Inclination of the binary to 86 degrees.

# In[ ]:





# You likely noticed that there are several (5!) Parameters in the Bundle for inclination.  This is because there is an inclination for the orbit as well as for each of the two stars in the binary system.  The other 2 are called Constraints which relate these Parameters to each other. That will be the topic of the next tutorial.

# 

# 
