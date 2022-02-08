#!/usr/bin/env python
# coding: utf-8

# Workshop Tutorial: Running Jobs on External Compute Resources
# ============================
# 
# **IMPORTANT NOTE**: this entire tutorial covers new capabilities _since_ the 2.3 release.  These are planned to be included in the 2.4 release, but may require some syntax change based on any feedback received during the workshop.
# 
# 
# In this tutorial we'll cover how to setup external compute resources on terra, submit, and manage jobs.
# 
# This interactive workshop tutorial covers many of the same topics as the corresponding online tutorials:
# 
# * [Servers](http://phoebe-project.org/docs/development/tutorials/server.ipynb)
# 

# Setup
# -----------------------------
# 
# We'll load our bunde from the previous tutorial to show examples of running both a forward-model and solver remotely on terra.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np

logger = phoebe.logger('error')

b = phoebe.open('data/synthetic/after_optimizers.bundle')


# Server Configuration
# -----------------------------
# 
# PHOEBE makes use of [crimpl](http://crimpl.readthedocs.io) as a built-in depedency to manage submitting and monitoring jobs on external compute resources.  In order to make use of one of these server, you must first configure the server within [crimpl](http://crimpl.readthedocs.io) (this only needs to be done once, after which the name of the crimpl server can be referenced from within PHOEBE on your local machine).
# 
# The available server types include:
# * [LocalThread](https://crimpl.readthedocs.io/en/latest/LocalThread/)
# * [RemoteSlurm](https://crimpl.readthedocs.io/en/latest/RemoteSlurm/)
# * [AWSEC2](https://crimpl.readthedocs.io/en/latest/AWSEC2/)
# 
# For the workshop, you've already created a temporary account with passwordless ssh to terra, so we'll configure that server within crimpl now.

# In[2]:


from phoebe.dependencies import crimpl


# Note that whatever you put as `host` needs to be ssh-able without a password.  If you don't have `terra` as an alias in your ssh config, you may need `host="username@terra.villanova.edu"` instead.

# In[3]:


s = crimpl.RemoteSlurmServer(host='terra')


# In[4]:


print(s)


# We'll be using conda on the remote server to manage installing any necessary dependencies.  You can manually install and configure conda, or let `crimpl` do it for you (if conda is already detected as installed, this won't do any harm to call again).

# In[5]:


s.install_conda()


# We will have PHOEBE manage installing the dependencies for us at each job submission.  This does add some minimal overhead to check the existing installation, but will fairly quickly see all dependencies met and move on.
# 
# If running this in the `development` branch instead of the `workshop2021` branch, then PHOEBE will force a re-install to the latest `development` version for each job.  In that case or when you want to install a dependency manually, you could do something like the following, reference the same `conda_env` from within PHOEBE, and set `install_deps=False` to skip having PHOEBE check and install dependencies.
# 
# The `workshop2021` branch however will not force a re-install.  If we have to make any bugfixes to the branch during the workshop, then you can either force a re-install by using a new `conda_env`, deleting the conda environment remotely, or by running something like the following manually.
# 
# Note that once 2.4 is relased, PHOEBE will make sure that the version number on the remote machine is the same as that on the local installation.
# 
# You can always call [b.dependencies](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.dependencies.md) to see the required pip dependencies for a given bundle.
# 
# **NOTE**: this line will take a few minutes to run, but only needs to be run once to setup the conda environment on the remote server.

# In[6]:


#s.run_script(['pip install https://github.com/phoebe-project/phoebe2/archive/refs/heads/workshop2021.zip mpi4py emcee --ignore-installed'], 
#             conda_env='phoebe_workshop')


# In[7]:


s.save('terra', overwrite=True)


# The name provided when saving the crimpl configuration is the same name that we will reference later in PHOEBE as `crimpl_name`.  This keeps all the server configuration and potential sensitive information out of the bundle so that the bundle (or notebook) can safely be saved and shared, while also not requiring the servers to be re-configured in each case.  If `crimpl_name` is not available from `crimpl` on the local machine, an error will be raised and the server can easily be configured or swapped.

# Servers in the Bundle
# -------------------------------
# 
# Servers in the bundle are added and managed as any other set of options via [b.add_server](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.add_server.md) and with "kinds" for each of the supported crimpl server types listed above:
# 
# * [localthread](http://phoebe-project.org/docs/development/api/phoebe.parameters.server.localthread.md)
# * [remoteslurm](http://phoebe-project.org/docs/development/api/phoebe.parameters.server.remoteslurm.md)
# * [awsec2](http://phoebe-project.org/docs/development/api/phoebe.parameters.server.awsec2.md)

# In[8]:


b.add_server('remoteslurm', crimpl_name='terra',
             conda_env='phoebe_workshop',
             nprocs=48,
             server='terra', overwrite=True)


# Note that there are a few other useful options here, including `walltime`.  We'll leave that at the default 30 minutes for now, but for longer jobs, you'll likely want to extend this to a reasonable value (terra allows up to 48 hours walltime per-job).

# In[9]:


print(b.get_server('terra'))


# use_server parameters
# --------------------------
# 
# compute and solver options both have `use_server` parameters that will then dictate how [b.run_compute](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.run_compute.md) and [b.run_solver](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.run_solver.md) should handle running on external resources.  
# 
# If 'none' (as by default), the job is run in the current thread.  `use_server` in solver options are set to 'compute' by default, which means they will fallback on the `use_server` parameter in the referenced compute options.

# In[10]:


print(b.filter(qualifier='use_server'))


# So in this case, if running the `nm_solver`, PHOEBE will use the solver options for the `nm_fit` compute options.

# In[11]:


print(b.filter(qualifier='compute'))


# As with any other parameter in compute or solver options, these can either be set or overridden as keyword arguments when calling [b.run_compute](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.run_compute.md) and [b.run_solver](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.run_solver.md), respectively.

# Running External Jobs with crimpl
# --------------------------------
# 
# There are several different use-cases for running compute or solver jobs on external servers
# 
# ### 1. wait and load results automatically
# 
# As always, we can send kwargs to `run_compute` or `run_solver` to override any compute/solver options.  Here we can pass the server tag (note: this is the PHOEBE server tag, not the crimpl server name) to `run_compute` overriding the `use_server` parameter, which then looks up the server options, loads the corresponding crimpl object, and passes the job to the remote machine.
# 
# Once the job is submitted, PHOEBE will poll to check its status, and retrieve the results once complete (or failed).

# In[14]:


b.run_compute(compute='phoebe01', use_server='terra', model='terra_model')


# In[15]:


_ = b.plot(model='terra_model', x='phases', show=True)


# ### 2. detach and monitor/retrieve results 
# 
# For long jobs, we can submit the job and immediately detach from `run_compute` or `run_solver`.  This results in a "Job Parameter" in the model or solution holding the necessary information to check the progress and retrieve the results at any time in the future. 
# 
# This is particularly useful for long solver runs as it allows you to monitor their progress *as* they're running, killing the job early if necessary.  In order to do that, we need to set `progress_every_niters` in the solver options (not available for all solvers).  This tells the solver to dump the progress to a file every set number of iterations, which can then be retrieved, loaded, and inspected.  Note that this does come with some overhead, so you don't want to necessarily set this to 1.

# In[16]:


print(b.get_solver('nm_solver'))


# In[17]:


print(b.get_parameter(qualifier='progress_every_niters', solver='nm_solver'))


# Here we'll set `progress_every_niters=10`, `maxiter=1e6`, and `fatol=xatol=1e-12`... essentially telling the optimizer to continue running until its manually terminated or exceeds the walltime.

# In[18]:


b.set_value('progress_every_niters', solver='nm_solver', value=10)
b.set_value('maxiter', solver='nm_solver', value=1e6)
b.set_value('xatol', solver='nm_solver', value=1e-12)
b.set_value('fatol', solver='nm_solver', value=1e-12)


# In[19]:


b.run_solver(solver='nm_solver', use_server='terra', 
             solution='nm_solution_progress', detach=True)


# In[20]:


print(b.get_solution('nm_solution_progress'))


# We can now (optionally) save the bundle, turn off our local machine, start a new python session, load the bundle, and all necessary information to check the job's status and retrieve results are handled automatically (with job information in the detached_job parameter and server setup/credentials in the crimpl configuration to avoid any security concerns when sharing bundles).

# In[21]:


b.save('running_job.phoebe')

import phoebe
b = phoebe.open('running_job.phoebe')


# Depending on how long we expect the job to take, we have a number of available methods we can call to act on this detached job parameter:
# 
# * [b.get_job_status](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.get_job_status.md)
# * [b.get_job_crimpl_object](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.get_job_crimpl_object.md)
# * [b.attach_job](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.attach_job.md)
# * [b.load_job_progress](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.load_job_progress.md)
# * [b.kill_job](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.kill_job.md)
# * [b.resubmit_job](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.resubmit_job.md)
# 
# Here we'll call [b.get_job_status](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.get_job_status.md) to confirm that the job has started running.

# In[22]:


b.get_job_status(solution='nm_solution_progress')


# Calling [b.load_job_progress](http://phoebe-project.org/docs/development/api/phoebe.frontend.bundle.Bundle.load_job_progress.md) will fail until the first progress file is written, so just for the sake of letting the notebook run by executing all cells, we'll force sleeping for 2 minutes.  Once it does succeed, it will download the latest dumped progress file and import it into the solution.

# In[23]:


from time import sleep
sleep(120)


# In[24]:


b.load_job_progress(solution='nm_solution_progress')


# In[25]:


print(b.filter(qualifier=['fitted_twigs', '*_values', '*_lnprobability', 'niter', 'message'], 
               solution='nm_solution_progress'))


# In[26]:


b.run_compute(compute='nm_fit', solution='nm_solution_progress', model='progress_model')


# In[27]:


_ = b.plot(model='progress_model', x='phases', show=True)


# We can essentially keep running this loop of code blocks to re-load the latest progress file from the server (automatically overwriting the previous progress), compare results, and decide whether to keep it running or terminate the job.
# 
# If we're happy with the results before `maxiter`, `xatol`, `fatol` or the server's `walltime` have been reached, we can kill the job.  

# In[28]:


b.kill_job(solution='nm_solution_progress')


# ### 3. export script
# 
# See the [online servers tutorial](http://phoebe-project.org/docs/development/tutorials/server.ipynb) for more use-cases, including exporting a script capable of submitting the job externally or a script to copy and submit manually.
