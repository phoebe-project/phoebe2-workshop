#!/usr/bin/env python
# coding: utf-8

# In tutorial we'll see different options for optimizing PHOEBE's performance.

# # Setup

# In[1]:


import phoebe
from phoebe import u,c


# In[2]:


logger = phoebe.logger(clevel='WARNING')


# In[3]:


b = phoebe.default_binary()


# # Package-level options
# 
# For more details, see the [optimizing PHOEBE tutorial](http://phoebe-project.org/docs/development/tutorials/optimizing).

# ### interactive checks
# 
# By default, interactive checks are enabled when PHOEBE is being run in an interactive session (either an interactive python, IPython, or Jupyter notebook session), but disabled when PHOEBE is run as a script directly from the console. When enabled, PHOEBE will re-run the system checks after every single change to the bundle, raising warnings via the logger as soon as they occur.
# 
# * [phoebe.interactive_checks_off](http://phoebe-project.org/docs/development/api/phoebe.interactive_checks_off)
# * [phoebe.interactive_checks_on](http://phoebe-project.org/docs/development/api/phoebe.interactive_checks_on)
# * [b.run_checks](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.run_checks)

# In[4]:


b.set_value('requiv', component='primary', value=10)


# In[5]:


b.set_value('requiv', component='primary', value=1)


# In[6]:


phoebe.interactive_checks_off()


# In[7]:


b.set_value('requiv', component='primary', value=10)


# In[8]:


print(b.run_checks())


# In[9]:


b.set_value('requiv', component='primary', value=1)


# In[10]:


print(b.run_checks())


# In[11]:


phoebe.interactive_checks_on()


# ### interactive constraints
# 
# By default, interactive constraints are always **enabled** in PHOEBE, unless explicitly disabled. Whenever a value is changed in the bundle that affects the value of a constrained value, that constraint is immediately executed and all applicable values updated. The ensures that all constrained values are "up-to-date".
# 
# If disabled, constraints are delayed and only executed when needed by PHOEBE (when calling run_compute, for example). This can save significant time, as each value that needs updating only needs to have its constraint executed once, instead of multiple times.
# 
# * [phoebe.interactive_constraints_off](http://phoebe-project.org/docs/development/api/phoebe.interactive_constraints_off)
# * [phoebe.interactive_constraints_on](http://phoebe-project.org/docs/development/api/phoebe.interactive_constraints_on)
# * [b.run_delayed_constraints](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.run_delayed_constraints)

# In[12]:


print(b.get_value('asini', context='component'))


# In[13]:


b.set_value('sma', component='binary', value=6)


# In[14]:


print(b.get_value('asini', context='component'))


# In[15]:


phoebe.interactive_constraints_off()


# In[16]:


b.set_value('sma', component='binary', value=7)


# In[17]:


print(b.get_value('asini', context='component'))


# In[18]:


b.run_delayed_constraints()


# In[19]:


print(b.get_value('asini', context='component'))


# # Environment Variables
# 
# Additionally, you can skip expensive imports by setting the following environment variables (these can't be handled with package-level options as the imports already would have happened).
# 
# Setting inline before calling python will set for that single session of PHOEBE:
# 
# ```
# PHOEBE_ENABLE_PLOTTING=FALSE python [script.py]
# ```
# 
# Setting via the os package in python before importing PHOEBE allows you to set the setting everytime you run a given script:
# 
# ```
# import os
# os.environ['PHOEBE_ENABLE_PLOTTING'] = 'FALSE'
# import phoebe
# ```
# Note for all boolean settings, the string is converted to uppercase and compared to 'TRUE'.
# 
# ### PHOEBE_ENABLE_PLOTTING
# PHOEBE_ENABLE_PLOTTING (TRUE by default) allows for disabling plotting within PHOEBE and therefore skipping the import of all plotting libraries (which take up a significant amount of the time it takes to import phoebe).
# 
# ### PHOEBE_ENABLE_ONLINE_PASSBANDS
# PHOEBE_ENABLE_ONLINE_PASSBANDS (TRUE by default) dictates whether online passbands are queried and available for on-the-fly downloading. If you are sure you have all the local passbands you need, set this to False to save some time.

# # Running in MPI
# 
# For more details, see the [MPI tutorial](http://phoebe-project.org/docs/development/tutorials/mpi).
# 
# There are several "modes of operation" depending on your settings and whether you're running your script within python or mpirun. You can enable/disable MPI within phoebe by placing [phoebe.mpi_on()](http://phoebe-project.org/docs/devel/api/phoebe.mpi_on) or [phoebe.mpi_off()]((http://phoebe-project.org/docs/devel/api/phoebe.mpi_on)) at the top of your script. If you do not do this, MPI will be enabled by default if within mpirun and disabled otherwise.
# 
# When MPI is enabled, PHOEBE will do the following:
# 
# * if within mpirun: uses PHOEBE's built-in per-dataset or per-time parallelization. The main code you write in your script is executed on a single processor, but during run_compute the task is divided among the available resources.
# * if not within mpirun (ie. in a serial python environment): will spawn a separate thread at phoebe.frontend.bundle.Bundle.run_compute, using number of processors sent to phoebe.mpi_on (for example: phoebe.mpi_on(nprocs=4)).
# 
# When MPI is disabled, PHOEBE will do the following:
# 
# * if within mpirun: PHOEBE will run equally on all processors. The user can customize parallelization with access to phoebe.mpi.nprocs, phoebe.mpi.myrank. Your script runs equally on each processor, meaning you have multiple (separate) copies of the bundle.
# * if not within mpirun (ie. in a serial python environment): PHOEBE will run on a single processor in serial-mode.
# 
# 
