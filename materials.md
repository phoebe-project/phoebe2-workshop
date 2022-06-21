
# Installing & Setup

### Jupyter Notebooks

The tutorials at the workshop will make heavy use of [Jupyter notebooks](https://jupyter.org/install).  If you'd prefer, you can copy and paste from the files into an interactive Python or IPython session, but if you'd like to follow along directly in Jupyter, please make sure that you have Jupyter up and running and can import PHOEBE (more on that next).

The Jupyter notebooks (and talks) will all be linked below so that you can pull them up to view in the browser, or download and run locally on your own machine as we go through them. Please note, these will not be avilable until we solidify the program.

### Installing PHOEBE

During the workshop, we will be using the recently-released 2.4 version of PHOEBE.  We'll also be using `emcee`, `scikit-learn`, and `celerite2` for the second on-line component of the workshop (feel free to skip the last line below if you're only attending the first week).  The easiest way to install is via pip (you're welcome to install within a virtual or conda environment if you'd like, just make sure you know how to activate that environment from within Jupyter):

```
pip install numpy
pip install phoebe
pip install emcee scikit-learn celerite2
```

Note that PHOEBE only supports Python 3.6+, so you may need to replace `pip` with `pip3` or even `python3 -m pip` depending on your system.

If you're on a newer mac system and PHOEBE fails to build, you may need to first install a supported compiler.  The easiest way to do this is to install PHOEBE within a conda environment where you first install a compiler (`conda install clangxx_osx-64`).  See the [mac install instructions](http://phoebe-project.org/install/latest/mac/auto) for more details.

Similarly, if you are on a Linux system without `g++` or `python3-dev` installed by default, you may need to manually install a few dependencies.  See the [Linux install instructions](http://phoebe-project.org/install/latest/linux/auto) for more details.

You can check to make sure the correct version is installed in a Python console (or Jupyter if you plan to use that at the workshop):

* `import phoebe`
* `print(phoebe.__version__)`

If you have any troubles before the meeting, please reach out to us for assistance.


### Testing Your Installation


Please test your installation well in advance of the workshop by running the [test script](https://raw.githubusercontent.com/phoebe-project/phoebe2-workshop/2022june/test_install.py) (should take approximately 60 seconds to run) and make sure it completes without any errors (warning messages are not a cause for concern).  If the script does not run successfully or takes significantly longer than 60 seconds, please reach out to us so we can debug any installation issues in advance.

# Part 1

### Monday June 20: Overview and Building Systems in PHOEBE

* [Welcome & Introduction](https://docs.google.com/presentation/d/e/2PACX-1vRMXSVmy3BlJDXqQnmC_PPvuO-kQ1-NAPWEz-gk5laHL0w7kSC75EcXInDY6ZHMPsTJopfPCAfX5z-g/pub?start=false&loop=false&delayms=3000) (Kelly)
* [Talk: PHOEBE Overview - wdgui to PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vTcg5sbS9wdqg5b5g1fwe_VoyMG1THPX6mQx4VDbvZOUfKMS6FAd8pYcBl0HeyN5prpDzi54nNZfVB7/pub?start=false&loop=false&delayms=3000) (Andrej)
* [Talk: Introduction to PHOEBE 2: why so complicated?](https://docs.google.com/presentation/d/e/2PACX-1vQJKn6aqRFU6eJ34TZRJqllb7fOm6f-vaiBnXMkdaqV2MNGtjCSLM_iVDEP49naPiWH36yjbq1ugbLj/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Tutorial: General Concepts & Bundle Basics](./Tutorial_01_bundle_basics.ipynb) (Andrej)
* [Tutorial: Constraints](./Tutorial_02_constraints.ipynb) (Angela)
* [Exercises: Building Systems](./Exercises_01_building_systems.ipynb)


### Tuesday June 21: Creating Forward Models

* [Talk: Atmospheres, Limb Darkening, Intensity Weighting, Extinction, and Reflection](https://docs.google.com/presentation/d/e/2PACX-1vTX__cTcowjUGuJ18jYY85tWX9VjjYEu7ISEkLgMMFKSFUNNFPHRreGW_LaUjSsQF62-M5od-J37LAu/pub?start=false&loop=false&delayms=3000) (Dave)
* [Tutorial: Datasets](./Tutorial_03_datasets.ipynb) (Andrej)
* [Tutorial: Compute](./Tutorial_04_compute.ipynb) (Angela)
* [Tutorial: Time and Phase](./Tutorial_05_time_and_phase.ipynb) (Andrej)
* [Tutorial: Plotting](./Tutorial_06_plotting.ipynb) (Angela)
* [Exercises: Creating Forward Models](./Exercises_02_forward_models.ipynb)


### Wednesday June 22: Advanced Physics & Features


* Talk: Scientific Introduction to PHOEBE (Andrej)
* [Tutorial: Animations](./Tutorial_07_animations.ipynb) (Angela)
* [Tutorial: Accessing and Plotting Meshes](./Tutorial_08_meshes.ipynb) (Kyle)
* [Tutorial: Flux Scaling (Passband Luminosity, Third Light, and Distance)](./Tutorial_09_pblum_l3_distance.ipynb) (Andrej)
* [Tutorial: Features (Spots & Gaussian Processes)](./Tutorial_10_features.ipynb) (Angela)
* [Tutorial: Optimizing PHOEBE Computations](./Tutorial_11_optimizing_computations.ipynb) (Andrej)
* [Exercises: Forward Model Animations](./Exercises_03_animations.ipynb)
* Excursion into Philadelphia and Workshop Dinner.


### Thursday June 23: Hack Day


* [Exercises: Hack Day](./Exercises_04_hack_day.ipynb)


[Optional Breakout Session: Contact Binaries](./Tutorial_12_semidetached_contact.ipynb) (Angela) <br>
[Optional Breakout Session: In-depth look at fluxes and magnitudes](./Tutorial_13_flux_calibration.ipynb) (Andrej)


### Friday June 24: PHOEBE Development & Upcoming Releases


* Group Photo/Screenshot
* [Talk: In Development - Pulsations](https://docs.google.com/presentation/d/e/2PACX-1vTY9f-XjDgw5knxFRDKpwNzNp8OMFMsH0nC9zYN1_TBxndnFuRSoKejpuDK34JJ_b0wrkfTlu5hy1Ki/pub?start=false&loop=false&delayms=3000) (Andrej)
* [Talk: Line Profiles with PHOEBE and SPAMMS](https://docs.google.com/presentation/d/e/2PACX-1vRT4EwgIf7ocn8JJFyULGhaVJvi7c4zZT36ttaXJ8qN4krQ7uaX1QMUmlTpMcyBo_GhNRIVjlzHmAIM/pub?start=false&loop=false&delayms=3000) (Michael)
* [Talk: In Development - Blended Atmosphere Tables](https://docs.google.com/presentation/d/e/2PACX-1vStqWOOdGpaQcGbvKVU3uwPxfc70Dr1K_w3dHSas7dv3s48ZeBkWI4gjd0pqffJDc5Gjk9Z1CrCojY2/pub?start=false&loop=false&delayms=3000) (Andrej)
* Wrap Up: volunteer wrap-up contributions and discussion
* Exercises: finish or continue any of the previous exercises.

# Part 2

### Tuesday June 28: Inverse Problem Overview 

* [Talk: Introduction to the Inverse Problem](https://docs.google.com/presentation/d/e/2PACX-1vR-fRxNcn5PEMQ6Rvq5dEHALVIDs62OqGDDaWr2liCNMrtcP-h6u4WztVxUhGoGvKQTh9DXyN9xXLYh/pub?start=false&loop=false&delayms=3000) (Angela)
* [Talk: Inverse Problem in PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vT_GwcoD_0Tz-5V1dEolYYFCMp2qxrfKqfySOCI9QU3rpMuR7ANGY_rDiLRZbXnrvTN57x6qndroC0Z/pub?start=false&loop=false&delayms=3000) (Andrej)
* [Tutorial: Detrending](./Tutorial_14_detrending.ipynb) (Andrej)
* [Tutorial: Estimators](./Tutorial_15_estimators.ipynb) (Angela)
* [Tutorial: Degeneracies](./Tutorial_16_degeneracy.ipynb) (Andrej)
* [Exercises: Estimators](./Exercises_06_estimators.ipynb) (Angela)


### Tuesday July 5: Optimizers

* [Tutorial: Optimizers](./Tutorial_17_optimizers.ipynb) (Andrej)
* [Tutorial: Running Jobs on External Compute Resources](./Tutorial_18_server.ipynb) (Andrej)
* [Tutorial: Distributions & Priors](./Tutorial_19_distributions.ipynb) (Kyle)
* [Exercises: Optimizers](./Exercises_07_optimizers.ipynb) (Andrej)


### Tuesday July 12: MCMC in PHOEBE

* [Tutoritalk: MCMC Introduction](./mcmc_generic.ipynb)
* [Tutorial: MCMC Basics in PHOEBE](./Tutorial_20_mcmc.ipynb) (Andrej)
* [Tutorial: Continuing/Resampling in MCMC](./Tutorial_21_mcmc_continued.ipynb) (Andrej)
* [Exercises: Setting up an MCMC Run](./Exercises_08_mcmc.ipynb) (Andrej)

### Tuesday July 19: Advanced MCMC

[Optional Breakout Session: Fitting Contact Binaries](https://docs.google.com/presentation/d/e/2PACX-1vRrcYeotz37WyqXCmBQqwqH7dkHBUi-D6SMvAiZketoqlkGCmZ7vWhPgD46dx_pl_SCs3nPrNB4bOgV/pub?start=false&loop=false&delayms=3000) (Angela)


* [Tutorial: Interpreting Chains and Convergence in MCMC](./Tutorial_22_convergence.ipynb) (Andrej)
* [Tutorial: Posteriors and Parameter Uncertainties](./Tutorial_23_posteriors.ipynb) (Angela)
* [Tutorial: Choice of Parameterization](./Tutorial_24_parameterization.ipynb) (Angela)
* [Tutorial: Marginalizing over Additional Parameters](./Tutorial_25_marginalization.ipynb) (Angela)
* [Exercises: Getting Posteriors](./Exercises_07_posteriors.ipynb) (Angela)


### Tuesday July 26: Gaussian Processes


* [Tutorial: Gaussian Processes](./Tutorial_26_gaussian_processes.ipynb) (Angela)
* Group Photo/Screenshot
* [Tutorial: Running on OTHER Compute Resources](./Tutorial_27_server_other.ipynb) (Kyle)
* [Talk: Common Pitfalls when Fitting](https://docs.google.com/presentation/d/e/2PACX-1vTI2tTM7K307S8KRn_agtd_4IoXfwgA2_e4yfH47UzlwEdn0sl59tKSibZxHlfgbF43KPfWCgxgA1Fx/pub?start=false&loop=false&delayms=3000)
* Wrap Up: volunteer wrap-up contributions and discussion
