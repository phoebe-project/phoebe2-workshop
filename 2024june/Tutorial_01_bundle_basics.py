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

# In[1]:


import phoebe
from phoebe import u, c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# # The Bundle

# Everything for our system will be stored in a single Python object that we call the "Bundle". Let us create a default binary system and store it in a Bundle object variable `b` (short for bundle).

# In[3]:


b = phoebe.default_binary()


# The Bundle is a collection of parameters along with some callable methods. Each parameter is also a python object. Here we can see that the Bundle consists of over 140 individual parameters:

# In[4]:


b


# If we want to get or set a parameter value in the Bundle, we need to learn how to access it. Each `Parameter` object has a number of tags which are used to uniquely identify it; the tags are then used to filter parameters, akin to a database query. When filtering, a `ParameterSet` is returned - another python object that holds a subset of `Parameter` objects satisfying the used tags. Parameter sets can be filtered further, until they contain a single `Parameter`.

# In[5]:


b.filter(context='compute')


# To get an actual list of parameters, you can print the corresponding `ParameterSet`:

# In[6]:


print(b.filter(context='compute'))


# Here we filtered on the "context" tag for all parameters where context='compute'. This tag refers to parameters that determine how a forward model is computed. If we wanted to see all available options for the "context" tag in the Bundle, we would use the plural form of the tag:

# In[7]:


b.contexts


# All available tags are stored in the `b.tags` dictionary; to display all its keys, we would do:

# In[8]:


b.tags.keys()


# Although technically there is no hierarchy to the tags, it can be helpful to think of the "context" tag as the top-level tag and we should filter by the appropriate context first. We will discuss other tags in detail today and tomorrow.

# Using the plural form of the tag as an attribute also works on a filtered `ParameterSet`:

# In[9]:


b.filter(context='compute').components


# This then tells us what can be used to filter further.

# In[10]:


b.filter(context='compute').filter(component='primary')


# You can also filter in a single call to `filter()`, by naming keyword arguments appropriately:

# In[11]:


b.filter(context='compute', component='primary')


# The "qualifier" tag is the shorthand name of the parameter itself.  If you do not know what is the name of the parameter you need, it is often useful to list all the qualifiers of the `Bundle` or a given `ParameterSet`:

# In[12]:


b.filter(context='compute', component='primary').qualifiers


# Now that we know the options for qualifier within this filter, we can choose to filter on one of those. For example, let us filter on the `ntriangles` qualifier.

# In[13]:


b.filter(context='compute', component='primary', qualifier='ntriangles')


# Once we filter to a single Parameter, we can use `get_parameter()` to return the `Parameter` object itself (instead of the `ParameterSet`).

# In[14]:


b.filter(context='compute', component='primary', qualifier='ntriangles').get_parameter()


# Note that `get_parameter()` also takes filtering keywords. The above line is thus equivalent to the following:

# In[15]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles')


# Finally, all tags can be concatenated together, using "@" as the separator; we refer to these constructs as "twigs" (nomenclature was inspired by "a bundle of twigs"):

# In[16]:


b['ntriangles@primary@compute']


# There are some minor limitations to using twigs that we will address as the workshop progresses, so for the time being we will use the more verbose, but also more explicit methods of accessing parameters. In general, though, the ways to access parameters are by-and-large interchangeable.

# Each `Parameter` object contains several keys that provide information about that parameter.  The keys `description` and `value` are always included, with additional keys available depending on the type of parameter. While these keys exist as properties of the `Parameter` object (i.e., `p.value` and `p.description`), there are dedicated methods `get_value()` and `get_description()` that should be used instead; they take keyword arguments that can further modify the return value, for example to specify units.

# In[17]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_value()


# In[18]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_description()


# The `get_*()` family of methods works on the bundle as well, and can be filtered using keyword arguments. For example:

# In[19]:


b.get_value(context='compute', component='primary', qualifier='ntriangles')


# Finally, adding a key to the twig will also provide access to it:

# In[20]:


b['description@ntriangles@primary@compute']


# As the `ntriangles` parameter is an integer parameter, it also includes a key for the allowable limits.

# In[21]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_limits()


# In this case, we're looking at the Parameter called `ntriangles` with the component tag set to 'primary'.  This Parameter therefore defines how many triangles should be created when creating the mesh for the star named 'primary'.  By default, this is set to 1500 triangles, with allowable values above 100.
# 
# If we wanted a finer mesh, we would change the value:

# In[22]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').set_value(2000)


# In[23]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles')


# Twig access attempts to simplify the interface even more, so it is not necessary to explicitly provide `value` as part of the twig; it is also not necessary to provide *all* tags, just the ones that uniquely qualify the parameter:

# In[24]:


b['ntriangles@primary'] = 1500
b['ntriangles@primary']


# This is a very important distinction between the filtered interface and the twig interface to parameters and their values: when a set of tags uniquely identifies a parameter, the corresponding twig (via dictionary access) will *always* return a `Parameter`, whereas the `filter()` interface will *always* return a `ParameterSet`:

# In[25]:


b.filter(component='primary', qualifier='ntriangles')


# As with the tags, you can call `.twigs` on any `ParameterSet` to see the "smallest unique twigs" of the contained parameters:

# In[26]:


b['compute'].twigs


# Now let us take a look at another parameter, say the `distortion_method` qualifier from that same `ParameterSet`. It has an added key, `choices`:

# In[27]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method')


# In[28]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_choices()


# We can only set a value if it is contained within this list - if you attempt to set a non-valid value, an error will be raised.

# In[29]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').set_value('rotstar')


# In[30]:


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

# In[31]:


print(b.info)


# In[32]:


print(b.filter(context='component').info)


# ## Units
# 
# Each float parameter has an associated unit. Let us take a look at the semi-major axis ('sma') parameter for the binary orbit.

# In[33]:


b.get_parameter(qualifier='sma', component='binary', context='component')


# From the representation above, we can already see that the units are in solar radii. We can access the units directly via get_default_unit:

# In[34]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_default_unit()


# Calling get_value returns only the float of the value in these units:

# In[35]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value()


# Alternatively, you can access an actual "quantity" object that contains the value and unit by calling `get_quantity()`:

# In[36]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# Of course, recall from above that the entire family of get_*() methods can be used for filtering directly:

# In[37]:


b.get_quantity(qualifier='sma', component='binary')


# Both `get_value()` and `get_quantity()` also accept a unit argument which will return the value or quantity in the requested units (if possible to convert). This unit argument takes either a unit object or a string representation that can be parsed:

# In[38]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value(unit=u.km)


# If for some reason you want to change the default units, you can, but just be careful that this could cause some float-point precision issue

# In[39]:


b.get_parameter(qualifier='sma', component='binary', context='component').set_default_unit('mm')


# In[40]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# In[41]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity(unit='solRad')


# ## Saving & Loading

# The entire bundle object can be saved to (and reloaded from) and ASCII file:

# In[42]:


b.save('test.phoebe')


# In[43]:


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





# Set the default unit for all radii and the semi-major axes of all components to AU and then show their values. (Hint: you can also call `set_default_unit_all()` to act on a `ParameterSet` instead of a `Parameter`).

# In[ ]:





# Find and set the following Parameters:
# * effective temperature of the secondary star to 5500 K;
# * inclination of the binary to 86 degrees.

# In[ ]:





# You likely noticed that there are several (5!) Parameters in the Bundle for inclination.  This is because there is an inclination for the orbit as well as for each of the two stars in the binary system.  The other 2 are called Constraints which relate these Parameters to each other. That will be the topic of the next tutorial.

# 
