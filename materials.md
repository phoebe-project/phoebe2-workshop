# Installing & Setup

### Jupyter Notebooks

The tutorials at the workshop will make heavy use of [Jupyter notebooks](https://jupyter.org/install).  If you'd prefer, you can copy and paste from the files into an interactive Python or IPython session, but if you'd like to follow along directly in Jupyter, please make sure that you have Jupyter up and running and can import phoebe (more on that next).

The Jupyter notebooks (and talks) will all be linked below so that you can pull them up to view in the browser, or download and run locally on your own machine as we go through them.  We're still making changes to these between now and the workshop, so there should be no need to download them in advance.

### Installing PHOEBE

We will be using the recently-released 2.3 version of PHOEBE during the workshop.  See the [installation instruction](http://phoebe-project.org/install/2.3) and make sure PHOEBE is successfully installed prior to the start of the workshop.

You can check to make sure the correct version is installed in a Python console (or Jupyter if you plan to use that at the workshop):

* `import phoebe`
* `print(phoebe.__version__)`

(should be at least 2.3.20).

If you have any troubles before the meeting, please email us for assistance.


### Other Dependencies

We'll also be using [emcee](https://emcee.readthedocs.io/en/stable/) for fitting, so make sure you have that installed as well.


# Tuesday June 22: Overview and Building Systems in PHOEBE

* [Welcome & Introduction](https://docs.google.com/presentation/d/e/2PACX-1vTPiLVRPAUJnrSyNgqpWXbuQduLDqp36RP6inq5-QdtYA0nnLTjsQN1FuyhVIgvW9fHkiz_FAEpNrjp/pub?start=false&loop=false&delayms=3000) (Kelly - **2021 - NEEDS UPDATING**)
* [Talk: PHOEBE Overview - wdgui to PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vTeR0gdxhuHt7-rEQMK5SEM3bGETEF-ItWQHsvmr8cwt1bNqJuMflTABL8vvV6jrNEdPqRaIpL8-TiJ/pub?start=false&loop=false&delayms=3000) (Andrej - **2021 - NEEDS UPDATING**)
* [Talk: Introduction to PHOEBE 2: why so complicated?](https://docs.google.com/presentation/d/e/2PACX-1vTdjGepiD4v0VvAv8DQsed_uCQ4SMYPqfUtCLzvR92PKjnSSeTZ9qWuZpVbzdNxWBE445BwigEg9Tv7/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Tutorial #1: General Concepts & Bundle Basics](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_01_bundle_basics.ipynb) (Kyle)
* [Tutorial #2: Constraints](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_02_constraints.ipynb) (Kyle)
* [Exercises #1: Building Systems](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_01_building_systems.ipynb) (Kyle)

* TODO: include UI overview somewhere?

# Wednesday June 23: Creating Forward Models

* [Tutorial #3: Datasets](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_03_datasets.ipynb) (Bert)
* [Tutorial #4: Compute](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/04_compute.ipynb) (Angela)
* [Tutorial #4b: Time and Phase](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_04b_time_and_phase.ipynb) (Bert)
* Tutorial #5: Plotting
* [Talk: Atmospheres, Limb Darkening, Intensity Weighting, Extinction, and Reflection](https://docs.google.com/presentation/d/e/2PACX-1vSrILRxT1eygipBOurKZ2trffr5KQBRbK3y1TxY0-oydV1t4SaoZAWvDLZfUCc4iIZDzaHhlkVW8meM/pub?start=false&loop=false&delayms=3000) (Dave - **NEEDS UPDATING AND ADD EXTINCTION**)
* [Tutorial: Passband Luminosity, Third Light, and Distance](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Intro_Tutorial_11_pblum_l3_distance.ipynb) (Kyle)
* [Exercises #2: Creating Forward Models](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_02_forward_models.ipynb)


# Thursday June 24: Advanced Physics & Features
* Tutorial #5b: Animations
* Tutorial #5c: Accessing and Plotting Meshes
* [Exercises #3: Animations](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_03.ipynb) (Kyle)
* Tutorial #6: Features (Spots & Gaussian Processes)
* [Talk: In Development - Pulsations](https://docs.google.com/presentation/d/e/2PACX-1vR13F6t5UqxxLntwHs5_sVo8YW-xzRlq2BOm08KxRMYAETPqH8qHsmL6M8BvNNTXEzStFYcvKF-IjK5/pub?start=false&loop=false&delayms=3000) (Andrej - **NEEDS UPDATING**)
* [Tutorial #6b: Pulsations (PREVIEW)](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Intro_Tutorial_19_pulsations.ipynb) (Andrej)
* [Exercises #3: Forward Model Animations](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_03_animations.ipynb)



# Friday June 25: PHOEBE Development & Upcoming Releases
* Talk: Scientific Introduction to PHOEBE (Andrej)
* [Talk: In Development - Triple and Higher-Order Systems](https://docs.google.com/presentation/d/e/2PACX-1vSk1awjZ-mrvsSOQunNYikwGr6PjdAseIhPEnh84ABExkgAvAzZ1QF2WEMVIr04IMYPQYwEoPGDjir2/pub?start=false&loop=false&delayms=3000) (Kyle - **NEEDS UPDATING**)
* [Talk: In Development - Blended Atmosphere Tables](https://docs.google.com/presentation/d/e/2PACX-1vRMJxgdwwWs-IF1OY9ligGgNVul2z1Kk_GjRgH9-hFpkN8gJqtFcQUG4D3wzrsN998pvqt4bMNTtrfB/pub?start=false&loop=false&delayms=3000) (Andrej - **NEEDS UPDATING**)
* Exercises: finish or continue any of the previous exercises.  Next week we start fitting!


# Monday June 28: Inverse Problem Overview
* Talk: Introduction to the Inverse Problem (framing the inverse problem, why it isn't simple, parameterization, overview of what can be obtained given types of systems and observations)
* Talk: Inverse Problem in PHOEBE (Kyle - explaining estimators vs optimizers vs samplers and role of distributions)
* Tutorial #7: Distributions & Priors (Kyle)
* Tutorial #8a: Estimators (Angela)
* Tutorial #8b: Optimizers
* Exercises #4: Estimators & Optimizers

# Tuesday June 29: MCMC in PHOEBE
* Talk: MCMC Introduction
* Tutorial #8c: MCMC
* Tutorial #8d: Export Solver Runs to External Machine
* Tutorial #8e: Resampling/Continuing a Previous Run
* Talk: Choice of Parameterization
* Exercises #5: Setting up an MCMC Run

# Wednesday June 30: Advanced MCMC
* Talk: Marginalizing over Nuisance Parameters
* Tutorial: Noise Nuisance Parameter
* Talk: Convergence Criteria
* Tutorial: Accessing and Interpreting MCMC Chains & Posteriors
* Exercises #6: Getting Posteriors

# Thursday July 1:
* Talk: Common Pitfalls when Fitting (Angela - PHOEBE specific things like atmosphere bounds, but also q-search, choice of priors, dataset noise, etc).
* Fitting topics of interest
