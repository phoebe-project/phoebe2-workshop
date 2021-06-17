#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: General Concepts & Bundle Basics
# 
# In this first tutorial, we'll learn about the basics of the Bundle - which is the container of all Parameters within PHOEBE.  We'll see how to access individual Parameter and view and set their values.
# 
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [The PHOEBE Bundle](http://phoebe-project.org/docs/2.3/tutorials/general_concepts.ipynb)
# * [Advanced: Parameter Types](http://phoebe-project.org/docs/2.3/tutorials/parameters.ipynb)
# * [Advanced: Parameter Units](http://phoebe-project.org/docs/2.3/tutorials/units.ipynb)
# * [Advanced: Building a System](http://phoebe-project.org/docs/2.3/tutorials/contact_binary_hierarchy.ipynb)
# * [Advanced: Contact Binary Hierarchy](http://phoebe-project.org/docs/2.3/tutorials/contact_binary_hierarchy.ipynb)
# * [Advanced: Semi-Detached Systems](http://phoebe-project.org/docs/2.3/tutorials/requiv_crit_semidetached.ipynb)
# * [Advanced: Saving, Loading, and Exporting](http://phoebe-project.org/docs/2.3/tutorials/saving_and_loading.ipynb)

# # Setup

# In[ ]:


import phoebe
from phoebe import u,c


# In[ ]:


logger = phoebe.logger(clevel='WARNING')


# # Default Binary Bundle

# Everything for our system will be stored in a single Python object that we call the "Bundle".  Let's start just by creating the default binary system and store it in a Bundle-object which we'll call "b" (short for bundle).

# In[ ]:


b = phoebe.default_binary()


# The Bundle is just a collection of Parameter objects along with some callable methods.  Here we can see that the default binary Bundle consists of over 100 individual parameters.

# In[ ]:


b


# If we want to view or edit a Parameter in the Bundle, we first need to know how to access it.  Each Parameter object has a number of tags which can be used to filter (similar to a database query).  When filtering the Bundle, a ParameterSet is returned - this is essentially just a subset of the Parameters in the Bundle and can be further filtered until eventually accessing a single Parameter.

# In[ ]:


b.filter(context='compute')


# Here we filtered on the context tag for all Parameters with context='compute' (i.e. the options for computing a model).  If we want to see all the available options for this tag in the Bundle, we can use the plural form of the tag.

# In[ ]:


b.contexts


# Although there is no strict hierarchy to the tags, it can be helpful to think of the context tag as the top-level tag and is often very helpful to filter by the appropriate context first.
# 
# Other tags currently include:
# * kind
# * component
# * dataset
# * model
# * time
# * qualifier

# Accessing the plural form of the tag as an attribute also works on a filtered ParameterSet

# In[ ]:


b.filter(context='compute').components


# This then tells us what can be used to filter further.

# In[ ]:


b.filter(context='compute').filter(component='primary')


# The qualifier tag is the shorthand name of the Parameter itself.  If you don't know what you're looking for, it is often useful to list all the qualifiers of the Bundle or a given ParameterSet.

# In[ ]:


b.filter(context='compute', component='primary').qualifiers


# Now that we know the options for qualifier within this filter, we can choose to filter on one of those.  Let's filter by the `ntriangles` qualifier.

# In[ ]:


b.filter(context='compute', component='primary', qualifier='ntriangles')


# Once we filter far enough to get to a single Parameter, we can use get_parameter to return the Parameter object itself (instead of a ParameterSet).

# In[ ]:


b.filter(context='compute', component='primary', qualifier='ntriangles').get_parameter()


# As a shortcut, get_parameter also takes filtering keywords.  So the above line is also equivalent to the following:

# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles')


# Each Parameter object contains several keys that provide information about that Parameter.  The keys "description" and "value" are always included, with additional keys available depending on the type of Parameter.

# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_value()


# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_description()


# Since the Parameter for `ntriangles` is an IntegerParameter, it also includes a key for the allowable limits.

# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').get_limits()


# In this case, we're looking at the Parameter called `ntriangles` with the component tag set to 'primary'.  This Parameter therefore defines how many triangles should be created when creating the mesh for the star named 'primary'.  By default, this is set to 1500 triangles, with allowable values above 100.
# 
# If we wanted a finer mesh, we could change the value.

# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles').set_value(2000)


# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='ntriangles')


# If we choose the `distortion_method` qualifier from that same ParameterSet, we'll see that it has a few different keys in addition to description and value.

# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method')


# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_value()


# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_description()


# Since the `distortion_method` Parameter is a ChoiceParameter, it contains a key for the allowable choices.

# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_choices()


# We can only set a value if it is contained within this list - if you attempt to set a non-valid value, an error will be raised.

# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').set_value('rotstar')


# In[ ]:


b.get_parameter(context='compute', component='primary', qualifier='distortion_method').get_value()


# Parameter types include:
# * String Parameter
# * Choice Parameter
# * Select Parameter
# * Float Parameter
# * Integer Parameter
# * Boolean Parameter
# * FloatArray Parameter
# 
# these Parameter types and their available options are all described in great detail in [Advanced: Parameter Types](http://phoebe-project.org/docs/2.3/tutorials/parameters.ipynb)

# ## Twigs

# As a shortcut to needing to filter by all these tags, the Bundle and ParameterSets can be filtered through what we call "twigs" (as in a Bundle of twigs).  These are essentially a single string-representation of the tags, separated by @ symbols.
# 
# This is very useful as a shorthand when working in an interactive Python console, but somewhat obfuscates the names of the tags and can make it difficult if you use them in a script and make changes earlier in the script.
# 
# For example, the following lines give identical results:

# In[ ]:


b.filter(context='compute', component='primary')


# In[ ]:


b['primary@compute']


# In[ ]:


b['compute@primary']


# However, this dictionary-style twig access will never return a ParameterSet with a single Parameter, instead it will return the Parameter itself.  This can be seen in the different output between the following two lines:

# In[ ]:


b.filter(context='compute', component='primary', qualifier='distortion_method')


# In[ ]:


b['distortion_method@primary@compute']


# This dictionary-style access can also set the value directly:

# In[ ]:


b['distortion_method@primary@compute'] = 'roche'


# In[ ]:


print(b['distortion_method@primary@compute'])


# And can even provide direct access to the keys/attributes of the Parameter (value, description, limits, etc)

# In[ ]:


print(b['value@distortion_method@primary@compute'])


# In[ ]:


print(b['description@distortion_method@primary@compute'])


# As with the tags, you can call .twigs on any ParameterSet to see the "smallest unique twigs" of the contained Parameters

# In[ ]:


b['compute'].twigs


# Since the more verbose method without twigs is a bit clearer to read, most of the tutorials will show that syntax, but feel free to use twigs if they make more sense to you

# To see a nice representation of the names (twigs or qualifier) of all the parameters and their descriptions, we can call `info` on any bundle or ParameterSet.

# In[ ]:


print(b.info)


# In[ ]:


print(b.filter(context='component').info)


# ## Units
# 
# Each FloatParameter has an associated unit. Let's look at the 'sma' Parameter for the binary orbit.

# In[ ]:


b.get_parameter(qualifier='sma', component='binary', context='component')


# From the representation above, we can already see that the units are in solar radii. We can access the units directly via get_default_unit.

# In[ ]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_default_unit()


# Calling get_value returns only the float of the value in these units.

# In[ ]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value()


# Alternatively, you can access an astropy quantity object that contains the value and unit by calling get_quantity.

# In[ ]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# Both get_value and get_quantity also accept a unit argument which will return the value or quantity in the requested units (if able to convert). This unit argument takes either a unit object (we imported a forked version of astropy units from within PHOEBE) or a string representation that can be parsed.

# In[ ]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value(unit=u.km)


# If for some reason you want to change the default units, you can, but just be careful that this could cause some float-point precision issue

# In[ ]:


b.get_parameter(qualifier='sma', component='binary', context='component').set_default_unit('mm')


# In[ ]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# In[ ]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity(unit='solRad')


# ## Saving & Loading

# The entire bundle object can be saved to (and reloaded from) and ASCII file.

# In[ ]:


b.save('test.phoebe')


# In[ ]:


b = phoebe.load('test.phoebe')


# # Exercise

# Find and access the value of the effective temperature of the primary star via filtering and twig access.

# In[ ]:





# Find the choices for the `atm` Parameter

# In[ ]:





# Find what the `ltte` Parameter stands for.  Does it have choices?

# In[ ]:





# Change the default unit of the argument of periastron from degrees to radians and print the result with the new units.

# In[ ]:





# Set the default_unit for all radii and smas of all components to AU and then show their values. (Hint: you can also call set_default_unit_all to act on a ParameterSet instead of a Parameter)

# In[ ]:





# Find and set the following Parameters:
# * effective temperature of the secondary star to 5500 K
# * inclination of the binary to 86 degrees

# In[ ]:





# You likely noticed that there are several (5!) Parameters in the Bundle for inclination.  This is because there is an inclination for the orbit as well as for each of the two stars in the binary system.  The other 2 are called Constraints which relate these Parameters to each other... which will be the topic of the next tutorial.
