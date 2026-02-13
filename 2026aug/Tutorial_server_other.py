#!/usr/bin/env python
# coding: utf-8

# # Workshop Tutorial: Running Jobs on OTHER Compute Resources
# 
# PHOEBE currently supports running jobs on [external compute resources running a slurm scheduler](./Tutorial_18_server.ipynb).  But until we add support for more configurations, you can always manually run jobs on an external machine.

# In[1]:


import phoebe

b = phoebe.default_binary()
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,501))


# Instead of calling `run_compute`, call [export_compute](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.export_compute.md) (or [export_solver](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.export_solver.md) instead of `run_solver`).  These take the same arguments, _except_ that the first argument is the filename of a script that will be produced.

# In[2]:


b.export_compute('export_compute.py', irrad_method='none')


# This then returns the name of the script as well as the name of the output file that will be created when running that script (you can also override this by passing `out_fname` to the export method).
# 
# Let's take a quick peak at what's in this script.

# In[3]:


get_ipython().system('cat export_compute.py')


# Now copy this script to your server of choice, make sure phoebe is installed, and run or submit to the scheduler.
# 
# For the sake of this tutorial, we'll just run it locally in the notebook (you may need to make sure this runs in the same environment or change `python3` to whatever you use on your system for phoebe).

# In[4]:


get_ipython().system('python3 export_compute.py')


# This then creates the `export_compute.py.out` file (and for solvers with `progress_every_niters`, would create `export_compute.py.out.progress` for intermediate outputs).  Just copy this file back to your local machine and then load it using [b.import_model](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.import_model.md) or [b.import_solution](http://phoebe-project.org/docs/2.4/api/phoebe.frontend.bundle.Bundle.import_solution.md).
# 
# If you already passed `model` or `solution` to the export method, that tag will be used by default.  But you can also override during import.

# In[5]:


b.import_model('export_compute.py.out', model='model_from_export')


# In[6]:


_ = b.plot(model='model_from_export', show=True)

