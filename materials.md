# Installing & Setup

### Jupyter Notebooks

The tutorials at the workshop will make heavy use of [Jupyter notebooks](https://jupyter.org/install).  If you'd prefer, you can copy and paste from the files into an interactive Python or IPython session, but if you'd like to follow along directly in Jupyter, please make sure that you have Jupyter up and running and can import PHOEBE (more on that next).

The Jupyter notebooks (and talks) will all be linked below so that you can pull them up to view in the browser, or download and run locally on your own machine as we go through them.  We're still making changes to these between now and the workshop, so there should be no need to download them in advance.

### Installing PHOEBE

During the workshop, we will be using a custom development branch based the recently-released 2.3 version of PHOEBE, but with the inclusion of a few features that won't officially be released until the upcoming 2.4 version.  The easiest way to install is via pip (you're welcome to install within a virtual or conda environment if you'd like, just make sure you know how to activate that environment from within Jupyter):

```
pip install numpy
pip install https://github.com/phoebe-project/phoebe2/archive/refs/heads/workshop2021.zip --ignore-installed
```

Note that PHOEBE only supports Python 3.6+, so you may need to replace `pip` with `pip3` or even `python3 -m pip` depending on your system.  Also a "PEP 440 version" warning isn't a concern - this is just python complaining that "workshop2021" doesn't follow the standard version formatting.

If you're on a newer mac system and PHOEBE fails to build, you may need to first install a supported compiler.  The easiest way to do this is to install PHOEBE within a conda environment where you first install a compiler (`conda install clangxx_osx-64`).  See the [mac install instructions for 2.3](http://phoebe-project.org/install/latest/mac/auto) for more details (and just swap out the `pip install phoebe` with the line above to install the workshop version).

Similarly, if you are on a Linux system without `g++` or `python3-dev` installed by default, you may need to manually install a few dependencies.  See the [Linux install instructions for 2.3](http://phoebe-project.org/install/latest/linux/auto) and swap out the `pip install phoebe` with the line above to install the workshop version.

You can check to make sure the correct version is installed in a Python console (or Jupyter if you plan to use that at the workshop):

* `import phoebe`
* `print(phoebe.__version__)`

(must say 'workshop2021').

If you have any troubles before the meeting, please reach out to us for assistance.


### Other Dependencies

We'll also be using [ellc](https://github.com/pmaxted/ellc) as an optional alternate backend and [emcee](https://emcee.readthedocs.io/en/stable/) for fitting, so make sure you have those installed as well (both are available from pip).


### Testing Your Installation

Please test your installation well in advance of the workshop by running the [test script](https://raw.githubusercontent.com/phoebe-project/phoebe2-workshop/2021june/test_install.py) (should take 10-60 seconds to run) and make sure it completes without any errors (warning messages are not a cause for concern).  If the script does not run successfully, please reach out to us so we can debug any installation issues in advance.

# Tuesday June 15: Overview and Building Systems in PHOEBE

* [Welcome & Introduction](https://docs.google.com/presentation/d/e/2PACX-1vTPiLVRPAUJnrSyNgqpWXbuQduLDqp36RP6inq5-QdtYA0nnLTjsQN1FuyhVIgvW9fHkiz_FAEpNrjp/pub?start=false&loop=false&delayms=3000) (Kelly - **2021 - NEEDS UPDATING**)
* [Talk: PHOEBE Overview - wdgui to PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vTeR0gdxhuHt7-rEQMK5SEM3bGETEF-ItWQHsvmr8cwt1bNqJuMflTABL8vvV6jrNEdPqRaIpL8-TiJ/pub?start=false&loop=false&delayms=3000) (Andrej - **2021 - NEEDS UPDATING**)
* [Talk: Introduction to PHOEBE 2: why so complicated?](https://docs.google.com/presentation/d/e/2PACX-1vTdjGepiD4v0VvAv8DQsed_uCQ4SMYPqfUtCLzvR92PKjnSSeTZ9qWuZpVbzdNxWBE445BwigEg9Tv7/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Tutorial: General Concepts & Bundle Basics](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_01_bundle_basics.ipynb) (Kyle)
* [Tutorial: Constraints](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_02_constraints.ipynb) (Kyle)
* [Exercises: Building Systems](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_01_building_systems.ipynb) (Kyle)


# Wednesday June 16: Creating Forward Models

* [Tutorial: Datasets](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_03_datasets.ipynb) (Bert)
* [Talk: Atmospheres, Limb Darkening, Intensity Weighting, Extinction, and Reflection](https://docs.google.com/presentation/d/e/2PACX-1vSrILRxT1eygipBOurKZ2trffr5KQBRbK3y1TxY0-oydV1t4SaoZAWvDLZfUCc4iIZDzaHhlkVW8meM/pub?start=false&loop=false&delayms=3000) (Dave)
* [Tutorial: Compute](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_04_compute.ipynb) (Angela)
* [Tutorial: Time and Phase](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_04b_time_and_phase.ipynb) (Bert)
* [Tutorial: Plotting](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_05_plotting.ipynb) (Angela)
* [Tutorial: Flux Scaling - Passband Luminosity, Third Light, and Distance](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_pblum_l3_distance.ipynb) (Kyle)
* [Exercises: Creating Forward Models](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_02_forward_models.ipynb) (Kyle)


# Thursday June 17: Animations & Features

* Talk: Scientific Introduction to PHOEBE (Andrej)
* [Tutorial: Animations](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_05b_animations.ipynb) (Angela)
* [Tutorial: Accessing and Plotting Meshes](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_05c_meshes.ipynb) (Kyle)
* [Tutorial: Features (Spots & Gaussian Processes)](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_06_features.ipynb) (Kyle - **NEEDS UPDATING WITH GPs**)
* [Exercises: Forward Model Animations](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_03_animations.ipynb) (Kyle)



# Friday June 18: PHOEBE Development & Upcoming Releases

* [Talk: In Development - Pulsations](https://docs.google.com/presentation/d/e/2PACX-1vR13F6t5UqxxLntwHs5_sVo8YW-xzRlq2BOm08KxRMYAETPqH8qHsmL6M8BvNNTXEzStFYcvKF-IjK5/pub?start=false&loop=false&delayms=3000) (Andrej - **NEEDS UPDATING**)
* [Talk: In Development - Triple and Higher-Order Systems](https://docs.google.com/presentation/d/e/2PACX-1vSk1awjZ-mrvsSOQunNYikwGr6PjdAseIhPEnh84ABExkgAvAzZ1QF2WEMVIr04IMYPQYwEoPGDjir2/pub?start=false&loop=false&delayms=3000) (Kyle - **NEEDS UPDATING**)
* [Talk: In Development - Blended Atmosphere Tables](https://docs.google.com/presentation/d/e/2PACX-1vRMJxgdwwWs-IF1OY9ligGgNVul2z1Kk_GjRgH9-hFpkN8gJqtFcQUG4D3wzrsN998pvqt4bMNTtrfB/pub?start=false&loop=false&delayms=3000) (Andrej - **NEEDS UPDATING**)
* Exercises: finish or continue any of the previous exercises.  Next week we start fitting! (Andrej)


# Monday June 22/29: Inverse Problem Overview
* [Talk: Introduction to the Inverse Problem](https://docs.google.com/presentation/d/e/2PACX-1vTtiioAwAllKi9rycyklKPGbbji2cS9sf2wp9nvkccKtb7T_RaYHL7ByFUXy8fhvaM7MlOLi2eCYdtV/pub?start=false&loop=false&delayms=3000) (Angela - **NEEDS WRITING**: framing the inverse problem, why it isn't simple, parameterization, overview of what can be obtained given types of systems and observations)
* [Talk: Inverse Problem in PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vQsVUENU9QuQSFu2f5qvfJy9HJfgn3EqodG1nxuHXR4gukbt5J39aXmI8XDXo40RMJ93omsTix826z5/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Tutorial: Distributions & Priors](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_07_distributions.ipynb) (Kyle)
* [Tutorial: Estimators](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_08a_estimators.ipynb) (Angela)
* [Tutorial: Optimizers](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_08b_optimizers.ipynb) (Bert)
* [Tutorial: Running Jobs on External Compute Resources](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_09_server.ipynb) (Kyle)
* [Exercises: Estimators & Optimizers](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Exercises_05_estimators_optimizers.ipynb) (Kyle)

# Tuesday June 23/30: MCMC in PHOEBE
* Talk: MCMC Introduction (Andrej)
* [Tutorial: MCMC Basics in PHOEBE](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2021june/Tutorial_10_mcmc.ipynb) (Andrej)
* Tutorial: Resampling/Continuing an MCMC Run (Andrej)
* Talk: Choice of Parameterization (Angela)
* Exercises: Setting up an MCMC Run (Andrej)

# Wednesday June 24/31: Advanced MCMC
* Talk: Marginalizing over Nuisance Parameters (Angela)
* Tutorial: Noise Nuisance Parameter (Angela)
* Talk: Convergence Criteria and Interpreting Parameter Uncertainties (Andrej)
* Tutorial: Accessing and Interpreting MCMC Chains (Andrej)
* Tutorial: Accessing and Propagating Posteriors (Kyle)
* Exercises: Getting Posteriors (Kyle)

# Thursday June 25/July 1:
* Talk: Common Pitfalls when Fitting (Angela - PHOEBE specific things like atmosphere bounds, but also q-search, choice of priors, dataset noise, etc)
* Tutorial: Using PHOEBE with AWS (Kyle)
* Fitting topics of interest
