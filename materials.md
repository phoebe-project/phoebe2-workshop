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

We'll also be using [ellc](https://github.com/pmaxted/ellc) as an optional alternate backend and [emcee](https://emcee.readthedocs.io/en/stable/) for fitting, so make sure you have that installed as well (both are available from pip).


### Testing Your Installation

Please test your installation well in advance of the workshop by running the [test script](https://raw.githubusercontent.com/phoebe-project/phoebe2-workshop/2021june/test_install.py) (should take 10-60 seconds to run) and make sure it completes without any errors (warning messages are not a cause for concern).  If the script does not run successfully, please reach out to us so we can debug any installation issues in advance.

# Tuesday June 22: Overview and Building Systems in PHOEBE

* [Welcome & Introduction](https://docs.google.com/presentation/d/e/2PACX-1vTPiLVRPAUJnrSyNgqpWXbuQduLDqp36RP6inq5-QdtYA0nnLTjsQN1FuyhVIgvW9fHkiz_FAEpNrjp/pub?start=false&loop=false&delayms=3000) (Kelly - **2021 - NEEDS UPDATING**)
* [Talk: PHOEBE Overview - wdgui to PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vTeR0gdxhuHt7-rEQMK5SEM3bGETEF-ItWQHsvmr8cwt1bNqJuMflTABL8vvV6jrNEdPqRaIpL8-TiJ/pub?start=false&loop=false&delayms=3000) (Andrej - **2021 - NEEDS UPDATING**)
* [Talk: Introduction to PHOEBE 2: why so complicated?](https://docs.google.com/presentation/d/e/2PACX-1vTdjGepiD4v0VvAv8DQsed_uCQ4SMYPqfUtCLzvR92PKjnSSeTZ9qWuZpVbzdNxWBE445BwigEg9Tv7/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Tutorial #1: General Concepts & Bundle Basics](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_01_bundle_basics.ipynb) (Kyle)
* [Tutorial #2: Constraints](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_02_constraints.ipynb) (Kyle)
* [Exercises #1: Building Systems](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_01_building_systems.ipynb) (Kyle)


# Wednesday June 23: Creating Forward Models

* [Tutorial #3: Datasets](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_03_datasets.ipynb) (Bert)
* [Tutorial #4: Compute](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_04_compute.ipynb) (Angela)
* [Tutorial #4b: Time and Phase](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_04b_time_and_phase.ipynb) (Bert)
* [Tutorial #5: Plotting](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_05_plotting.ipynb) (Angela)
* [Talk: Atmospheres, Limb Darkening, Intensity Weighting, Extinction, and Reflection](https://docs.google.com/presentation/d/e/2PACX-1vSrILRxT1eygipBOurKZ2trffr5KQBRbK3y1TxY0-oydV1t4SaoZAWvDLZfUCc4iIZDzaHhlkVW8meM/pub?start=false&loop=false&delayms=3000) (Dave - **NEEDS UPDATING AND ADD EXTINCTION**)
* [Tutorial: Passband Luminosity, Third Light, and Distance](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Intro_Tutorial_11_pblum_l3_distance.ipynb) (Kyle)
* [Exercises #2: Creating Forward Models](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_02_forward_models.ipynb) (Kyle)


# Thursday June 24: Advanced Physics & Features

* Talk: Scientific Introduction to PHOEBE (Andrej)
* [Tutorial #5b: Animations](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_05b_animations.ipynb) (Angela)
* [Tutorial #5c: Accessing and Plotting Meshes](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_05c_meshes.ipynb) (Kyle)
* [Tutorial #6: Features (Spots & Gaussian Processes)](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_06_features.ipynb) (Kyle - **NEEDS UPDATING WITH GPs**)
* [Exercises #3: Forward Model Animations](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_03_animations.ipynb) (Kyle)



# Friday June 25: PHOEBE Development & Upcoming Releases

* [Talk: In Development - Pulsations](https://docs.google.com/presentation/d/e/2PACX-1vR13F6t5UqxxLntwHs5_sVo8YW-xzRlq2BOm08KxRMYAETPqH8qHsmL6M8BvNNTXEzStFYcvKF-IjK5/pub?start=false&loop=false&delayms=3000) (Andrej - **NEEDS UPDATING**)
* [Tutorial #6b: Pulsations (PREVIEW)](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Intro_Tutorial_19_pulsations.ipynb) (Andrej)
* [Talk: In Development - Triple and Higher-Order Systems](https://docs.google.com/presentation/d/e/2PACX-1vSk1awjZ-mrvsSOQunNYikwGr6PjdAseIhPEnh84ABExkgAvAzZ1QF2WEMVIr04IMYPQYwEoPGDjir2/pub?start=false&loop=false&delayms=3000) (Kyle - **NEEDS UPDATING**)
* [Talk: In Development - Blended Atmosphere Tables](https://docs.google.com/presentation/d/e/2PACX-1vRMJxgdwwWs-IF1OY9ligGgNVul2z1Kk_GjRgH9-hFpkN8gJqtFcQUG4D3wzrsN998pvqt4bMNTtrfB/pub?start=false&loop=false&delayms=3000) (Andrej - **NEEDS UPDATING**)
* Exercises: finish or continue any of the previous exercises.  Next week we start fitting! (Andrej)


# Monday June 28: Inverse Problem Overview
* Talk: Introduction to the Inverse Problem (Angela - framing the inverse problem, why it isn't simple, parameterization, overview of what can be obtained given types of systems and observations)
* Talk: Inverse Problem in PHOEBE (Kyle - explaining estimators vs optimizers vs samplers and role of distributions)
* Tutorial #7: Distributions & Priors (Kyle)
* Tutorial #8a: Estimators (Angela)
* Tutorial #8b: Optimizers (Bert)
* Exercises #4: Estimators & Optimizers (Bert)

# Tuesday June 29: MCMC in PHOEBE
* Talk: MCMC Introduction (Andrej)
* Tutorial #8c: MCMC (Andrej)
* Tutorial #8d: Export Solver Runs to an External Machine (Andrej)
* Tutorial #8e: Resampling/Continuing a Previous Run (Andrej)
* Talk: Choice of Parameterization (**???**)
* Exercises #5: Setting up an MCMC Run (Andrej)

# Wednesday June 30: Advanced MCMC
* Talk: Marginalizing over Nuisance Parameters (Angela)
* Tutorial: Noise Nuisance Parameter (Angela)
* Talk: Convergence Criteria (Andrej)
* Tutorial: Accessing and Interpreting MCMC Chains (Andrej)
* Tutorial: Accessing and Propagating Posteriors (Kyle)
* Exercises #6: Getting Posteriors (Kyle)

# Thursday July 1:
* Talk: Common Pitfalls when Fitting (Angela - PHOEBE specific things like atmosphere bounds, but also q-search, choice of priors, dataset noise, etc)
* Tutorial: Using PHOEBE with AWS (Kyle)
* Fitting topics of interest
