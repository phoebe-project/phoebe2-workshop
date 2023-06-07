# Installing & Setup

### Jupyter Notebooks

The tutorials at the workshop will make heavy use of [Jupyter notebooks](https://jupyter.org/install).  If you'd prefer, you can copy and paste from the files into an interactive Python or IPython session, but if you'd like to follow along directly in Jupyter, please make sure that you have Jupyter up and running and can import PHOEBE (more on that next).

The Jupyter notebooks (and talks) will all be linked below so that you can pull them up to view in the browser, or download and run locally on your own machine as we go through them. Please note, these will not be avilable until we solidify the program.

### Installing PHOEBE

During the workshop, we will be using the 2.4 version of PHOEBE.  We'll also be using `emcee`, `scikit-learn`, and `celerite2` for some fitting exercises.  The easiest way to install is via pip (you're welcome to install within a virtual or conda environment if you'd like, just make sure you know how to activate that environment from within Jupyter):

```
pip install numpy
pip install phoebe
pip install emcee scikit-learn celerite2
```

Note that PHOEBE only supports Python 3.6+, so you may need to replace `pip` with `pip3` or even `python3 -m pip` depending on your system.

If you're on a newer mac system and PHOEBE fails to build, you may need to first install a supported compiler.  The easiest way to do this is to install PHOEBE within a conda environment where you first install a compiler (`conda install clangxx_osx-64`).  See the [mac install instructions](http://phoebe-project.org/install/latest/mac/auto) for more details.

Similarly, if you are on a Linux system without `g++` or `python3-dev` installed by default, you may need to manually install a few dependencies.  See the [Linux install instructions](http://phoebe-project.org/install/latest/linux/auto) for more details.  If you're using a conda environment, `conda install -c conda-forge gxx` should install a compatible compiler.

You can check to make sure the correct version is installed in a Python console (or Jupyter if you plan to use that at the workshop):

* `import phoebe`
* `print(phoebe.__version__)`

If you have any troubles before the meeting, please reach out to us for assistance.


### Testing Your Installation


Please test your installation well in advance of the workshop by running the [test script](https://raw.githubusercontent.com/phoebe-project/phoebe2-workshop/2022june/test_install.py) (should take approximately 60 seconds to run) and make sure it completes without any errors (warning messages are not a cause for concern).  If the script does not run successfully or takes significantly longer than 60 seconds, please reach out to us so we can debug any installation issues in advance.

# Workshop Talks & Tutorials

### Monday June 19: Overview and Building Systems in PHOEBE

* [Welcome & Introduction](https://docs.google.com/presentation/d/e/2PACX-1vS8VXgvYJV4cXrnwF8XMLbZoKJqiTRQJcFv_GXnJrLOcn6QyU7JHJJ7ZH5totNOQIPSu1yawF1kL1m1/pub?start=false&loop=false&delayms=3000) (Kelly | needs updating for 2023)
* [Talk: PHOEBE Overview - wdgui to PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vT1no8csPNugrLUarxISYj_jtFidp6vMzzNj3jUkqTsUTw9ozOQ1wqh79kSaL-xLXZcSWKQ8UyNI_RE/pub?start=false&loop=false&delayms=3000) (Andrej)
* [Talk: Introduction to PHOEBE 2: why so complicated?](https://docs.google.com/presentation/d/e/2PACX-1vR_okhrCOKLqCW_d_cBiq5CwaIBWREYbIXPwB-AnndvYA8g9Xxs91rlZBjHLpEzzCp622i19hbsaxLh/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Tutorial: General Concepts & Bundle Basics](./Tutorial_01_bundle_basics.ipynb) (Andrej)
* [Tutorial: Constraints](./Tutorial_02_constraints.ipynb) (Michael)
* [Exercises: Building Systems](./Exercises_01_building_systems.ipynb)
* Optional Breakout Session: Preview of lcviz (Kyle | needs updating for 2023)


### Tuesday June 20: Creating Forward Models

* [Talk: Atmospheres, Limb Darkening, Intensity Weighting, Extinction, and Reflection](https://docs.google.com/presentation/d/e/2PACX-1vQ9ba54aHX5cwTNN2eJfRdG5nLXFqoOKLLUl9I0_sGwVYX2BEVLQDjQh1po8xti6bzbDAzD7sIT3ACH/pub?start=false&loop=false&delayms=3000) (Dave | needs updating for 2023)
* [Tutorial: Datasets](./Tutorial_03_datasets.ipynb) (Andrej)
* [Tutorial: Compute](./Tutorial_04_compute.ipynb) (Michael)
* [Tutorial: Time and Phase](./Tutorial_05_time_and_phase.ipynb) (Andrej)
* [Tutorial: Plotting](./Tutorial_06_plotting.ipynb) (Kyle)
* [Exercises: Creating Forward Models](./Exercises_02_forward_models.ipynb) (needs updating for 2023)
* [Optional Breakout Session: Line Profiles with PHOEBE and SPAMMS](https://docs.google.com/presentation/d/e/2PACX-1vTnWRdVfhC4bbrzGyP7kzhoMbZCOzyBbjJaRFJiMIUkpeSitL5Eqd_Dt1Ip3RZhPLhUvlKS1-iqnC0h/pub?start=false&loop=false&delayms=3000) (Michael)
* [Optional Breakout Session: In Development - Blended Atmosphere Tables](https://docs.google.com/presentation/d/e/2PACX-1vSI-dNQSiGfNqttEuOzEd-iD2HIFfrvPVtFhk__I4YCwqOAo9cy047Tbkk74MkYgiRgO4iePvYf2Ss3/pub?start=false&loop=false&delayms=3000) (Andrej | needs updating for 2023)


### Wednesday June 21: Advanced Physics & Features

* Group Photo
* Talk: Scientific Introduction to PHOEBE (Andrej | needs updating for 2023)
* [Tutorial: Animations](./Tutorial_07_animations.ipynb) (Michael | needs updating for 2023)
* [Tutorial: Accessing and Plotting Meshes](./Tutorial_08_meshes.ipynb) (Kyle)
* [Tutorial: Flux Scaling (Passband Luminosity, Third Light, and Distance)](./Tutorial_09_pblum_l3_distance.ipynb) (Andrej)
* [Tutorial: Features (Spots & Gaussian Processes)](./Tutorial_10_features.ipynb) (Kyle)
* [Tutorial: Optimizing PHOEBE Computations](./Tutorial_11_optimizing_computations.ipynb) (Kyle)
* [Exercises: Forward Model Animations](./Exercises_03_animations.ipynb) (needs updating for 2023)
* [Optional Breakout Session: In Development - Pulsations](https://docs.google.com/presentation/d/e/2PACX-1vR54syXqzX9MiGxsHdus7A7xDjS3_4ka3TyQiXpoBzCduwAiEymK0zxn40zSrBaNDQ3SodwxlY3p6mm/pub?start=false&loop=false&delayms=3000) (Andrej | needs updating for 2023)


### Thursday June 22: Introduction to Fitting

* [Talk: Inverse Problem in PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vSZxGLuuJAf2_imhVVhGAW_xoeOgmEI-0YWbnfES2XaUz8YO1jGdHe8652c8flxiSGotJQQF1eGp16R/pub?start=false&loop=false&delayms=3000) (Andrej | needs updating for 2023)
* [Tutorial: Estimators](./Tutorial_12_estimators.ipynb) (Michael | needs updating for 2023 - mention need for detrending and link to prev tutorial/resources)
* [Tutorial: Optimizers](./Tutorial_13_optimizers.ipynb) (Kyle | needs updating for 2023)
* [Exercises: Estimators & Optimizers](./Exercises_04_estimators_optimizers.ipynb) (needs updating for 2023)
* [Optional Breakout Session: In-depth look at fluxes and magnitudes](./Tutorial_flux_calibration.ipynb) (Andrej)
* [Optional Breakout Session: Detrending](./Tutorial_detrending.ipynb) (Kelly | needs updating for 2023)


### Friday June 23: Advanced Fitting

* [Tutorial: Distributions & Priors](./Tutorial_14_distributions.ipynb) (Kyle)
* [Tutorial: MCMC Basics in PHOEBE](./Tutorial_15_mcmc.ipynb) (Andrej | needs updating for 2023)
* [Tutorial: Continuing/Resampling in MCMC](./Tutorial_16_mcmc_continued.ipynb) (Andrej | needs updating for 2023)
* [Exercises: Setting up an MCMC Run](./Exercises_08_mcmc.ipynb) (needs updating for 2023)
* [Optional Breakout Session: Contact Binaries](./Tutorial_semidetached_contact.ipynb) (Michael | needs updating for 2023)
* Optional Breakout Session: PHOEBE Backend Under-the-Hood (Martin | needs updating for 2023)
* [Exercises: Hack Day](./Exercises_05_mcmc_hack_day.ipynb) (needs updating for 2023)
