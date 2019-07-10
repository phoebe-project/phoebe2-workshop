# Installing & Setup

### Jupyter Notebooks

The tutorials at the workshop will make heavy use of [Jupyter notebooks](https://jupyter.org/install).  If you'd prefer, you can copy and paste from the files into an interactive Python or IPython session, but if you'd like to follow along directly in Jupyter, please make sure that you have Jupyter up and running and can import phoebe (more on that next).

The Jupyter notebooks (and talks) will all be linked below so that you can pull them up to view in the browser, or download and run locally on your own machine as we go through them.  We're still making changes to these between now and the workshop, so there should be no need to download them in advance.

### Installing PHOEBE

PHOEBE 2.2 (which will include multiple improvements, optimizations, and support for python 3) is almost, but not quite, ready to be released.  Instead of using PHOEBE 2.1 at the workshop and missing out on all these soon-to-be-released features, we will be using a pre-release development version of 2.2.  If you already have the latest version of 2.1 installed and would rather use the stable release version, we will try our best to point out the relevant changes and what won't work for you.

Note about Python versions:

* PHOEBE 2.2 adds support for Python 3, so feel free to use either 2.7+ or 3.6+ for the workshop.  If you'd rather use PHOEBE 2.1, you'll have to use Python 2.
* Note for mac users: be careful not to use the *system* version of Python as that usually results in problems.

Dependencies:

* in whatever version of python you'd like to install PHOEBE (either python 2 or 3), make sure you have numpy, astropy, and matplotlib installed.

To download the pre-release workshop version of PHOEBE 2.2:

* using git (which will allow you to easily update for any bugfixes *during* the meeting via `git pull`, but you may need to install git if you don't already have it): `git clone --depth=1 --single-branch -b workshop https://github.com/phoebe-project/phoebe2.git`
* alternatively, download and extract the zip file: [PHOEBE workshop zip](https://github.com/phoebe-project/phoebe2/archive/workshop.zip)


To install PHOEBE (replace `python` with whatever is necessary to point to the version of Python you'd like to use):

* make sure you're in the 'phoebe2' directory which contains 'setup.py'
* `python setup.py build`
* `python setup.py install --user` for a user-install or `sudo python setup.py install` for a global installation. Note that the --user flag may not be necessary for a local installation on a mac.

Now check the following in a Python console (or Jupyter if you plan to use that at the workshop):

* `import phoebe`
* `print(phoebe.__version__)` should print 'workshop'

If you have any troubles before the meeting, please email us for assistance.  We'll also have some time during the first morning/coffee break to deal with last-minute debugging.


### Other Dependencies

We'll also be using [emcee](https://emcee.readthedocs.io/en/stable/) for fitting, so make sure you have that installed in the version of Python you'll be using.


# Monday

### Introduction Talks
* [Welcome & Introduction](https://docs.google.com/presentation/d/e/2PACX-1vRjK8iEVZbdZkDBpW0d7XvfqUNq4_waFI9doIx_DAXQvgIYgendKSSeuWIZuUK59w2IN_hEoCm4lZtL/pub?start=false&loop=false&delayms=3000) (Kelly)
* [PHOEBE Overview: wdgui to PHOEBE](https://docs.google.com/presentation/d/e/2PACX-1vRemPIyKkMmWOe_YAQlH3oKfaSBNt5MhNc0MyTfygJrIEBGhlGrki138KljRymM6sobkCayD2LkYfGw/pub?start=false&loop=false&delayms=3000) (Andrej)
* [Introduction to PHOEBE 2: why so complicated?](https://docs.google.com/presentation/d/e/2PACX-1vT5d5bzuzABHvERmmMfe_aq7fN2w9Q3ctcFib0KM1e8bD_gUpyVCDBk7d28OWgKBNlNYSK6CI5xK2VD/pub?start=false&loop=false&delayms=3000) (Kyle)

### Tutorials
* [Tutorial #1: Bundle Basics](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_01_bundle_basics.ipynb) (Kyle)
* [Tutorial #2: Constraints](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_02_constraints.ipynb) (Kyle)
* [Tutorial #3: Advanced Constraints](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_03_advanced_constraints.ipynb) (Kyle)
* [Tutorial #4: Units](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_04_units.ipynb) (Kyle)
* [Exercises #1: Building Systems](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Exercises_01.ipynb) (Kyle)

# Tuesday

### Introduction Talks
* Scientific Introduction to PHOEBE (Andrej)

### Tutorials
* [Tutorial #5: Datasets](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_05_datasets.ipynb) (Bert)
* [Tutorial #6: Time and Phase](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_06_time_and_phase.ipynb) (Bert)
* [Tutorial #7: Compute](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_07_compute.ipynb) (Angela)
* [Tutorial #8: Plotting](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_08_plotting.ipynb) (Angela)
* [Tutorial #9: Animating](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_09_animating.ipynb) (Angela)
* [Tutorial #10: Meshes](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_10_meshes.ipynb) (Kyle)
* [Exercises #2: Animations](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Exercises_02.ipynb) (Kyle)

### Downtown Outing


# Wednesday


### Advanced Physics & Features
* [Atmospheres, Limb Darkening, Intensity Weighting, and Reflection](https://docs.google.com/presentation/d/e/2PACX-1vQ3LFDQrKAbEhieM3hUDyFgg-W9ozacQYAPmyBlmsb180qqjChf2kNsLonvDCE0iKAF5RdEFdxlC7Pr/pub?start=false&loop=false&delayms=3000) (Dave)


### Tutorials
* [Tutorial #11: Passband Luminosity, Third Light, and Distance](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_11_pblum_l3_distance.ipynb) (Kyle)
* [Tutorial #12: Saving and Loading](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_12_saving_loading.ipynb) (Bert) 
* [Tutorial #13: Hierarchies](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_13_hierarchies.ipynb) (Angela)
* [Tutorial #14: Spots](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_14_spots.ipynb) (Bert)
* [Tutorial #15: Semi-Detached Binaries](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_15_semidetached.ipynb) (Angela)
* [Tutorial #16: Contact Binaries](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_16_contact_binaries.ipynb) (Angela)
* [Tutorial #17: Optimizing PHOEBE](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_17_optimizing.ipynb) (Kyle)
* [Tutorial #18: Low-level access to passbands](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_18_low_level_passbands.ipynb) (Andrej)



### Building Systems & Forward Models

The rest of the day is set aside to work on writing scripts to build your own systems (or to continue working on the [animations exercises](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Exercises_02.ipynb), if you'd rather).  If you don't have any specific systems you'd like to try, you can choose any from the literature or from the [Caleb catalog of EBs](http://caleb.eastern.edu/query_stars_by_type.php).

Note that the [morphology definitions in caleb](http://caleb.eastern.edu/binary_type_definitions.php) are slightly different than PHOEBE.  You may want to use the following:

* Caleb's detached -> phoebe.default_binary()
* Caleb's semi-detached or near-contact -> phoebe.default_binary() with semi-detached constraint on one component
* Caleb's contact -> phoebe.default_binary() with semi-detached constraint on *both* components
* Caleb's overcontact -> phoebe.default_binary(contact_binary=True)
* Caleb's double-contact -> good luck! (you can try semi-detached constraints)




# Thursday

### Fitting
* [Introduction to Fitting](https://docs.google.com/presentation/d/e/2PACX-1vRPMs4qfUborTwJUcBMDy393d7sOVsTT2jsiUFGZAzcWGhEl53cuzSSEpxhE1HDsTnceS6EAek24zfe/pub?start=false&loop=false&delayms=3000) (Andrej)
* [Fitting in PHOEBE with emcee](https://docs.google.com/presentation/d/e/2PACX-1vQyUigkK0EwzbLmAOsdu8t1tgKMC-lyt5dGKUYACWqXFWNNa7N6DnJnauocY1cEBXvF2pdTo28psCvV/pub?start=false&loop=false&delayms=3000) (Kelly)
* [MCMC Tips & Tricks](https://docs.google.com/presentation/d/e/2PACX-1vRoGy9U53Lnko-v7OKBsD1fIxa3-RYyo3wMwRle1xFekZNpBtSWAOvl9wKZ3oLAsvgkEpd2B3TxNrS1/pub?start=false&loop=false&delayms=3000) (Angela)
* [Fitting Tutorial #1: fitting a line](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/phoebe_fitting_1.ipynb) (Kelly)
* [Fitting Tutorial #2: fitting with PHOEBE](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/phoebe_fitting_2.ipynb) (Kelly)

### Fitting to Fake (or Real) Data

The rest of the day is set aside to work on writing script to fit your own data/systems.  If you don't have your own data or want to get some easier practive first you can try the [Fitting Exercise](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Exercises_03_Fitting.ipynb).


### Workshop Dinner @ Dave & Busters


# Friday

### Future Features
* [Extinction (2.2 feature release)](https://docs.google.com/presentation/d/e/2PACX-1vTjWPSGagcIpOb-_ZJDE7AicGKnZqm5c81U_sAOpB-5CWe6xbUPzkeNB7pk1AkxS_t7xDBEas_AhH7O/pub?start=false&loop=false&delayms=3000) (Dave)
* [Blended Atmosphere Tables (2.2 feature release)](https://docs.google.com/presentation/d/e/2PACX-1vRWc9Fdaeg6aSyV53D_--ebKS4aeHIMtAthozA6J-XVeYtQV8zA9DyBlf6j-Lp7rTDhkQiUiELFX654/pub?start=false&loop=false&delayms=3000) (Andrej)
* [Pulsations](https://docs.google.com/presentation/d/e/2PACX-1vRjBQKKqGBy7pojNo3I3y1JzqEmweKpAUBVNW27glySsiuMWnaHrAdDLXskscu4Wh3g0irqQ3X7PgfU/pub?start=false&loop=false&delayms=3000) (Andrej)
* [Triple and Higher-Order Systems](https://docs.google.com/presentation/d/e/2PACX-1vTfc9rEUzGDbvQ7E4GEa38m-JG6CgS67rPBHuCAABpTWJE9CQlAhXrUSqfApEHVwLR-it8Cs3SsYb8w/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Contact Binaries](https://docs.google.com/presentation/d/e/2PACX-1vR3Qz7TC-77pMzrqc-U57WNS_ec83A0fgxtV2JZ_Em34CbLvbcaCw87VOzW5dNlV3KUnR-nu6u6nZy3/pub?start=false&loop=false&delayms=3000) (Angela)
* [GUI](https://docs.google.com/presentation/d/e/2PACX-1vTJITJ26XNAlyvU6K656k9D9MCIaR6b3HpQ4yLNQSJptpOpSlf8vtz9FNFK6fg-ZVihS34VTS4e4yqj/pub?start=false&loop=false&delayms=3000) (Kyle)
* [Misc](https://docs.google.com/presentation/d/e/2PACX-1vT8op_EoU1CZiemxhZ2XRixSc1SFZxVzKwUPrEAFGMCAoJJSUPeKxebukTC9bZk2JIFZNoJB0BPnCxf/pub?start=false&loop=false&delayms=3000) (Kyle)
* Discussion (Kelly)
