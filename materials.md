# Installing & Setup

### Jupyter Notebooks

The tutorials at the workshop will make heavy use of [Jupyter notebooks](https://jupyter.org/install).  If you'd prefer, you can copy and paste from the files into an interactive Python or IPython session, but if you'd like to follow along directly in Jupyter, please make sure that you have Jupyter up and running and can import PHOEBE (more on that next).

The Jupyter notebooks (and talks) will all be linked below so that you can pull them up to view in the browser, or download and run locally on your own machine as we go through them (see the links to download on the top left of each tutorial).  We're still making changes to these between now and the workshop, so there should be no need to download them in advance.

### Installing PHOEBE

During the workshop, we will be using a custom development branch based on the recently-released 2.3 version of PHOEBE, but with the inclusion of a few features that won't officially be released until the upcoming 2.4 version.  We'll also be using `emcee` in the second week (feel free to remove emcee below if you're only attending the first week).  The easiest way to install is via pip (you're welcome to install within a virtual or conda environment if you'd like, just make sure you know how to activate that environment from within Jupyter):

```
pip install numpy
pip install https://github.com/phoebe-project/phoebe2/archive/refs/heads/workshop2021.zip --ignore-installed
pip install emcee
```

Note that PHOEBE only supports Python 3.6+, so you may need to replace `pip` with `pip3` or even `python3 -m pip` depending on your system.  Also a "PEP 440 version" warning isn't a concern - this is just python complaining that "workshop2021" doesn't follow the standard version formatting.

If you're on a newer mac system and PHOEBE fails to build, you may need to first install a supported compiler.  The easiest way to do this is to install PHOEBE within a conda environment where you first install a compiler (`conda install clangxx_osx-64`).  See the [mac install instructions for 2.3](http://phoebe-project.org/install/latest/mac/auto) for more details (and just swap out the `pip install phoebe` with the line above to install the workshop version).

Similarly, if you are on a Linux system without `g++` or `python3-dev` installed by default, you may need to manually install a few dependencies.  See the [Linux install instructions for 2.3](http://phoebe-project.org/install/latest/linux/auto) and swap out the `pip install phoebe` with the line above to install the workshop version.

You can check to make sure the correct version is installed in a Python console (or Jupyter if you plan to use that at the workshop):

* `import phoebe`
* `print(phoebe.__version__)`

(must say 'workshop2021').

If you have any troubles before the meeting, please reach out to us for assistance.


### Testing Your Installation

Please test your installation well in advance of the workshop by running the [test script](https://raw.githubusercontent.com/phoebe-project/phoebe2-workshop/2021june/test_install.py) (should take 10-60 seconds to run) and make sure it completes without any errors (warning messages are not a cause for concern).  If the script does not run successfully, please reach out to us so we can debug any installation issues in advance.

# Tuesday June 15: Overview and Building Systems in PHOEBE

Session Chair: Angela

* [Welcome & Introduction](https://docs.google.com/presentation/d/e/2PACX-1vTPiLVRPAUJnrSyNgqpWXbuQduLDqp36RP6inq5-QdtYA0nnLTjsQN1FuyhVIgvW9fHkiz_FAEpNrjp/pub?start=false&loop=false&delayms=3000) (Kelly - **2021 - NEEDS UPDATING**)
* [Talk: PHOEBE Overview - wdgui to PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vTeR0gdxhuHt7-rEQMK5SEM3bGETEF-ItWQHsvmr8cwt1bNqJuMflTABL8vvV6jrNEdPqRaIpL8-TiJ/pub?start=false&loop=false&delayms=3000) (Andrej)
* [Talk: Introduction to PHOEBE 2: why so complicated?](https://docs.google.com/presentation/d/e/2PACX-1vTdjGepiD4v0VvAv8DQsed_uCQ4SMYPqfUtCLzvR92PKjnSSeTZ9qWuZpVbzdNxWBE445BwigEg9Tv7/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Tutorial: General Concepts & Bundle Basics](./Tutorial_01_bundle_basics.ipynb) (Kyle)
* [Tutorial: Constraints](./Tutorial_02_constraints.ipynb) (Kyle)
* [Exercises: Building Systems](./Exercises_01_building_systems.ipynb) (Kyle)


# Wednesday June 16: Creating Forward Models

Session Chair: Kelly

* [Tutorial: Datasets](./Tutorial_03_datasets.ipynb) (Bert)
* [Talk: Atmospheres, Limb Darkening, Intensity Weighting, Extinction, and Reflection](https://docs.google.com/presentation/d/e/2PACX-1vSrILRxT1eygipBOurKZ2trffr5KQBRbK3y1TxY0-oydV1t4SaoZAWvDLZfUCc4iIZDzaHhlkVW8meM/pub?start=false&loop=false&delayms=3000) (Dave)
* [Tutorial: Compute](./Tutorial_04_compute.ipynb) (Angela)
* [Tutorial: Time and Phase](./Tutorial_04b_time_and_phase.ipynb) (Bert)
* [Tutorial: Plotting](./Tutorial_05_plotting.ipynb) (Angela)
* [Tutorial: Flux Scaling - Passband Luminosity, Third Light, and Distance](./Tutorial_pblum_l3_distance.ipynb) (Kyle)
* [Exercises: Creating Forward Models](./Exercises_02_forward_models.ipynb) (Kyle)


# Thursday June 17: Animations & Features

Session Chair: Kelly

* Talk: Scientific Introduction to PHOEBE (Andrej)
* [Tutorial: Animations](./Tutorial_05b_animations.ipynb) (Angela)
* [Tutorial: Accessing and Plotting Meshes](./Tutorial_05c_meshes.ipynb) (Kyle)
* [Tutorial: Features (Spots & Gaussian Processes)](./Tutorial_06_features.ipynb) (Kyle)
* [Tutorial: Optimizing PHOEBE Computations](./Tutorial_optimizing_computations.ipynb) (Kyle)
* [Exercises: Forward Model Animations](./Exercises_03_animations.ipynb) (Kyle)



# Friday June 18: PHOEBE Development & Upcoming Releases

Session Chair: Michael

* Group Photo/Screenshot
* [Talk: In Development - Pulsations](https://docs.google.com/presentation/d/e/2PACX-1vR13F6t5UqxxLntwHs5_sVo8YW-xzRlq2BOm08KxRMYAETPqH8qHsmL6M8BvNNTXEzStFYcvKF-IjK5/pub?start=false&loop=false&delayms=3000) (Andrej - **NEEDS UPDATING**)
* [Talk: In Development - Triple and Higher-Order Systems](https://docs.google.com/presentation/d/e/2PACX-1vSk1awjZ-mrvsSOQunNYikwGr6PjdAseIhPEnh84ABExkgAvAzZ1QF2WEMVIr04IMYPQYwEoPGDjir2/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Talk: In Development - Blended Atmosphere Tables](https://docs.google.com/presentation/d/e/2PACX-1vRMJxgdwwWs-IF1OY9ligGgNVul2z1Kk_GjRgH9-hFpkN8gJqtFcQUG4D3wzrsN998pvqt4bMNTtrfB/pub?start=false&loop=false&delayms=3000) (Andrej - **NEEDS UPDATING**)
* Wrap Up: volunteer wrap-up contributions and discussion
* Exercises: finish or continue any of the previous exercises.  Next week we start fitting! (Andrej)


# Monday June 21/28: Inverse Problem Overview
* [Talk: Introduction to the Inverse Problem](https://docs.google.com/presentation/d/e/2PACX-1vTtiioAwAllKi9rycyklKPGbbji2cS9sf2wp9nvkccKtb7T_RaYHL7ByFUXy8fhvaM7MlOLi2eCYdtV/pub?start=false&loop=false&delayms=3000) (Angela - **NEEDS WRITING**: framing the inverse problem, why it isn't simple, parameterization, overview of what can be obtained given types of systems and observations)
* [Talk: Inverse Problem in PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vQsVUENU9QuQSFu2f5qvfJy9HJfgn3EqodG1nxuHXR4gukbt5J39aXmI8XDXo40RMJ93omsTix826z5/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Tutorial: Distributions & Priors](./Tutorial_07_distributions.ipynb) (Kyle)
* [Tutorial: Estimators](./Tutorial_08a_estimators.ipynb) (Angela)
* [Tutorial: Optimizers](./Tutorial_08b_optimizers.ipynb) (Bert)
* [Tutorial: Running Jobs on External Compute Resources](./Tutorial_09_server.ipynb) (Kyle)
* [Exercises: Estimators & Optimizers](./Exercises_05_estimators_optimizers.ipynb) (Kyle)

# Tuesday June 22/29: MCMC in PHOEBE
* [Talk: MCMC Introduction](https://docs.google.com/presentation/d/e/2PACX-1vTJlHTQlJFSTIcGhvfQHoNWOS8q6xlOVFX3uYOytQxvJKwePgg0m5mWbXA20WvtH0YlOhniKeM6-U2l/pub?start=false&loop=false&delayms=3000) (Andrej - **NEEDS WRITING**)
* [Tutorial: MCMC Basics in PHOEBE](./Tutorial_10_mcmc.ipynb) (Andrej)
* [Tutorial: Continuing/Resampling in MCMC](./Tutorial_11_mcmc_continued.ipynb) (Andrej)
* [Tutorial: Choice of Parameterization](./Tutorial_parametrization.ipynb) (Angela)
* [Exercises: Setting up an MCMC Run](./Exercises_06_mcmc.ipynb) (Andrej)

# Wednesday June 23/30: Advanced MCMC
* Tutoritalk: Convergence Criteria and Interpreting Parameter Uncertainties (Andrej)
* [Tutorial: Interpreting Chains and Convergence in MCMC](./Tutorial_12_convergence.ipynb) (Andrej)
* Tutorial: Posteriors and Parameter Uncertainties (Andrej)
* Tutorial: Propagating Posteriors (Kyle)
* [Tutorial: Marginalizing over Additional Parameters](./Tutorial_marginalization.ipynb) (Angela)
* [Exercises: Getting Posteriors](./Exercises_07_posteriors.ipynb) (Angela)

# Thursday June 24/July 1:
* [Talk: Common Pitfalls when Fitting](https://docs.google.com/presentation/d/e/2PACX-1vQ7tNOfVPpBuOn49D0jChGsKALZpgCbYUHGRYVbO4EV8kYo_eQbIaOwzOu7pDP0-5A7bjrsxvUphKIk/pub?start=false&loop=false&delayms=3000) (Angela - **NEEDS WRITING** PHOEBE specific things like atmosphere bounds, data far from t0, but also q-search, choice of priors, dataset noise, etc)
* Tutorial: Using PHOEBE with AWS (Kyle)
* Wrap Up: volunteer wrap-up contributions and discussion
