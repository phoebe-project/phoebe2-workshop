# Installing & Setup

### Installing PHOEBE

During the workshop, we will be using the 2.4 version of PHOEBE.  `emcee`, `scikit-learn`, and `celerite2` will also be useful for any fitting.  The easiest way to install is via pip (you're welcome to install within a virtual or conda environment if you'd like, just make sure you know how to activate that environment from within Jupyter):

```
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


Please test your installation well in advance of the workshop by running the [test script](https://raw.githubusercontent.com/phoebe-project/phoebe2-workshop/2025aug/test_install.py) (should take approximately 60 seconds to run) and make sure it completes without any errors (warning messages are not a cause for concern).  If the script does not run successfully or takes significantly longer than 60 seconds, please reach out to us so we can debug any installation issues in advance.


# Week 1

### Monday August 4: Overview and Building Systems in PHOEBE

* [Welcome & Introduction](https://docs.google.com/presentation/d/e/2PACX-1vTH436zb5IPSMPoCq0AbAW0lzJrQjhRINJyoUOZxAYyaFHPyx8TM1jXeqcs2NOC-mWmXxiTh7B0cQd7/pub?start=false&loop=false&delayms=3000) (Kelly)
* Opening Ceremony and Self-Introductions (Sheng-Bang)
* Jupyter and PHOEBE Setup (Andrej | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-04_02_jupyter_and_phoebe_setup.mp4))
* Group Photo, Coffee Break, Installation Debugging
* [Talk: PHOEBE Overview - wdgui to PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vRDgAr5NEH738njEqj4LS4YtxUs6T8TA5EHe3jry454n7cRdzRBvGuxpn_5QAgjeykQnx8er97c3_VD/pub?start=false&loop=false&delayms=3000) (Andrej | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-04_03_phoebe_overview.mp4))
* [Talk: Introduction to PHOEBE 2: why so complicated?](https://docs.google.com/presentation/d/e/2PACX-1vQZF_BRCGQZEjNlLhzznY5i_T5WNj6y7RJMvqxat7aDzTq7l1qDx7CnInoiNtIFZWL2BczoHf3RWnTK/pub?start=false&loop=false&delayms=3000) (Kyle | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-04_04_introduction_to_phoebe2.mp4))
* [Tutorial: General Concepts & Bundle Basics](./Tutorial_01_bundle_basics.ipynb) (Kelly | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-04_05_general_concepts.mp4))
* [Tutorial: Constraints](./Tutorial_02_constraints.ipynb) (Kyle | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-04_06_constraints.mp4))
* [Exercises: Building Systems](./Exercises_01_building_systems.ipynb)


### Tuesday August 5: Creating Forward Models

* [Talk: Parameterization](https://docs.google.com/presentation/d/e/2PACX-1vQ_WFnIM5ZubzjF0JWQrkLNkB84m8NJokQ93kafYry8J9Nd01cCr0ib59fVrKqdHPNVFJpMacNzKjRS/pub?start=false&loop=false&delayms=3000) (Marcin | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-05_01_parametrization.mp4))
* [Tutorial: Datasets](./Tutorial_03_datasets.ipynb) (Kelly | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-05_02_datasets.mp4))
* [Tutorial: Compute](./Tutorial_04_compute.ipynb) (Michael | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-05_03_compute.mp4))
* [Tutorial: Time and Phase](./Tutorial_05_time_and_phase.ipynb) (Andrej | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-05_04_time_and_phase.mp4))
* [Talk: Atmospheres, Limb Darkening, Intensity Weighting, Extinction, and Reflection](https://docs.google.com/presentation/d/e/2PACX-1vQBFsBHcaE1ZJV4hETfCvv03D3Y_rFZEIuz5m0QhApM5mRdceEc78iGCF1FfmY-ID23jC7unqvtofNj/pub?start=false&loop=false&delayms=3000) (Dave | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-05_05_atmospheres.mp4))
* [Tutorial: Plotting](./Tutorial_06_plotting.ipynb) (Kyle | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-05_06_plotting.mp4))
* [Exercises: Creating Forward Models](./Exercises_02_forward_models.ipynb)


### Wednesday August 6: Advanced Physics & Features


* Talk: Scientific Introduction to PHOEBE (Andrej | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-06_01_scientific_intro_to_phoebe.mp4))
* [Tutorial: Animations](./Tutorial_07_animations.ipynb) (Kyle | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-06_02_animations.mp4))
* [Tutorial: Accessing and Plotting Meshes](./Tutorial_08_meshes.ipynb) (Michael | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-06_03_meshes.mp4))
* [Tutorial: Flux Scaling (Passband Luminosity, Third Light, and Distance)](./Tutorial_09_pblum_l3_distance.ipynb) (Dave | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-06_04_flux_scaling.mp4))
* [Exercises: Forward Model Animations](./Exercises_03_animations.ipynb)


### Thursday August 7: Hack Day


* [Tutorial: Optimizing PHOEBE Computations](./Tutorial_10_optimizing_computations.ipynb) (Kelly | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-07_01_optimizations.mp4))
* [Optional Breakout Session: Contact Binaries](./Tutorial_semidetached_contact.ipynb) (Michael | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-07_02_contact_binaries.mp4))
* [Optional Breakout Talk: Line Profiles with PHOEBE and SPAMMS](https://docs.google.com/presentation/d/e/2PACX-1vTw7p9Hlh0F2GOWZIFTiTIaKD20hTE_pWxsurxARzg10SU8VOVh4IbqtctM0J6tpd6xO7NU25GHY6aR/pub?start=false&loop=false&delayms=3000) (Michael | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-07_03_spamms.mp4))
* [Tutorial: Features (Spots & Gaussian Processes)](./Tutorial_11_features.ipynb) (Kyle | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-07_04_features.mp4))
* [Optional Breakout Session: In-depth look at fluxes and magnitudes](./Tutorial_flux_calibration.ipynb) (Andrej | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-07_06_fluxes_vs_mags.mp4))
* [Optional Breakout Talk: In Development - Pulsations](https://docs.google.com/presentation/d/e/2PACX-1vT1itS6W6Z0FOOnPGFud2TWg-sIxdLXYLX-GquIB-lssk2aiD33VL1TSSsBBs4bwwxOMC3M4jwQuadS/pub?start=false&loop=false&delayms=3000) (Andrej | [recording](https://phoebe-project.org/static/workshops/2025aug/2025-08-07_05_pulsations.mp4))
* [Exercises: Forward Model Animations](./Exercises_03_animations.ipynb)
* [Exercises: Hack Day](./Exercises_04_hack_day.ipynb)


# Week 2

### Monday August 11: Inverse Problem Overview

* [Talk: Introduction to the Inverse Problem](https://docs.google.com/presentation/d/e/2PACX-1vQJUYYl3Y9zxWceapJ9cjbgRyHjkb8xw9qmdZ1Ve4-q4MorCS2OgjpAVYDkyfLQLm7mb_zbnvBMEI-h/pub?start=false&loop=false&delayms=3000) (Kelly)
* [Talk: Inverse Problem in PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vQnOikYGaIVd1O6Aj4jp6_A26T41h-pid6IOh-qwQdafZIGvSWNo89SvRHz-6JVtUoKXlin0g_KdguZ/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Optional Breakout Tutorial: Detrending](./Tutorial_detrending.ipynb) (Andrej)
* [Tutorial: Estimators](./Tutorial_12_estimators.ipynb) (Marcin)
* [Tutorial: Optimizers](./Tutorial_13_optimizers.ipynb) (Kelly)
* [Exercises: Optimizers](./Exercises_06_estimators_optimizers.ipynb) 


### Tuesday August 12: Optimizers

* [Tutorial: Distributions & Priors](./Tutorial_16_distributions.ipynb) (Kyle)
* [Tutorial: Degeneracies](./Tutorial_14_degeneracy.ipynb) (Marcin)
* [Tutorial: Running Jobs on External Compute Resources](./Tutorial_15_server.ipynb) (Kyle)
* [Exercises: Optimizers](./Exercises_06_estimators_optimizers.ipynb) 


### Wednesday August 13: MCMC in PHOEBE

* [Tutoritalk: MCMC Introduction](./mcmc_generic.ipynb) (Andrej)
* [Tutorial: MCMC Basics in PHOEBE](./Tutorial_17_mcmc.ipynb) (Marcin)
* [Tutorial: Continuing/Resampling in MCMC](./Tutorial_18_mcmc_continued.ipynb) (Kelly)
* [Exercises: Setting up an MCMC Run](./Exercises_07_mcmc.ipynb)
* [Optional Breakout Session: Fitting Contact Binaries](https://docs.google.com/presentation/d/e/2PACX-1vT_Cx34ifFzE_vM_75IRGXVFcIplju_VOsUNK0w-FjPJ9mlNI9riUZk5nb0iUzwrwQ4oGYnEYNzDiJK/pub?start=false&loop=false&delayms=3000) (Michael)


### Thursday August 14: Advanced MCMC

* [Talk: Common Pitfalls when Fitting](https://docs.google.com/presentation/d/e/2PACX-1vTwak5SRgicPcFJMHosg6AC1gnHqiEkVLiPT1H97bgJ40W1r39rtsgmf4eJitHb02rMtKKUtTW-PtkK/pub?start=false&loop=false&delayms=3000) (Dave)
* [Optional Breakout Tutorial: Interpreting Chains and Convergence in MCMC](./Tutorial_19_convergence.ipynb) (Andrej)
* [Talk: PHOEBAI](https://docs.google.com/presentation/d/e/2PACX-1vRLvSKCzA_BTZN7vl_tTXxKe6Y3wIKMCAuuZhwh0LIkfoZKiDCOzZBSuHwyhe7tu4o_lm0aANAOFv7o/pub?start=false&loop=false&delayms=3000) (Marcin)
* [Optional Breakout Tutorial: Posteriors and Parameter Uncertainties](./Tutorial_20_posteriors.ipynb) (Kelly)
* [Optional Breakout Tutorial: Choice of Parameterization](./Tutorial_21_parameterization.ipynb) (Kyle)
* [Exercises: Getting Posteriors](./Exercises_08_posteriors.ipynb)
* Wrap Up: volunteer wrap-up contributions and discussion (Kelly)
