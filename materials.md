# Installing & Setup

## Jupyter Notebooks

The tutorials at the workshop will make heavy use of [Jupyter notebooks](https://jupyter.org/install).  If you'd prefer, you can copy and paste from the files into an interactive Python or IPython session, but if you'd like to follow along directly in Jupyter, please make sure that you have Jupyter up and running and can import phoebe (more on that next).

The Jupyter notebooks (and talks) will all be linked below so that you can pull them up to view in the browser, or download and run locally on your own machine as we go through them.  We're still making changes to these between now and the workshop, so there should be no need to download them in advance.

## Installing PHOEBE

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
* `python setup.py install --user` for a user-install or `sudo python setup.py install` for a global installation.

Now check the following in a Python console (or Jupyter if you plan to use that at the workshop):

* `import phoebe`
* `print(phoebe.__version__)` should print '2.2-prerelease-workshop'

If you have any troubles before the meeting, please email us for assistance.  We'll also have some time during the first morning/coffee break to deal with last-minute debugging.





# Introductory Talks

* Welcome & Introduction
* PHOEBE Overview: wdgui to PHOEBE
* Scientific Introduction to PHOEBE
* [Introduction to PHOEBE 2: why so complicated?](https://docs.google.com/presentation/d/e/2PACX-1vT5d5bzuzABHvERmmMfe_aq7fN2w9Q3ctcFib0KM1e8bD_gUpyVCDBk7d28OWgKBNlNYSK6CI5xK2VD/pub?start=false&loop=false&delayms=3000)

# Tutorials and Exercises

Day 1:
* [Tutorial #0: Overview](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_00_overview.ipynb)
* [Tutorial #1: Bundle Basics](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_01_bundle_basics.ipynb)
* [Tutorial #2: Constraints](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_02_constraints.ipynb)
* [Tutorial #3: Advanced Constraints](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_03_advanced_constraints.ipynb)
* [Tutorial #4: Units](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_04_units.ipynb)
* [Exercises #1: Building Systems](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Exercises_01.ipynb)


Day 2:
* [Tutorial #5: Datasets](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_05_datasets.ipynb)
* [Tutorial #6: Time and Phase](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_06_time_and_phase.ipynb)
* [Tutorial #7: Compute](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_07_compute.ipynb)
* [Tutorial #8: Plotting](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_08_plotting.ipynb)
* [Tutorial #9: Animating](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_09_animating.ipynb)
* [Tutorial #10: Meshes](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_10_meshes.ipynb)
* [Tutorial #11: Saving and Loading](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_11_saving_loading.ipynb)
* [Tutorial #12: Hierarchies](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_12_hierarchies.ipynb)
* [Tutorial #13: Spots](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Intro_Tutorial_13_spots.ipynb)
* [Exercises #2: Rossiter-McLaughlin](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/Exercises_02.ipynb)


# Science Topics

* Passband Luminosity, Third Light, and Distance
* Current State of Contacts | [tutorial](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/contacts_tutorial.ipynb)
* Atmospheres, Limb Darkening, Intensity Weighting, and Reflection | [tutorial](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/atm_ld_tutorial.ipynb)

# Fitting

* Introduction to Fitting
* Fitting in PHOEBE with emcee | [tutorial #1](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/phoebe_fitting_1.ipynb), [tutorial #2](https://nbviewer.jupyter.org/github/phoebe-project/phoebe2-workshop/blob/2019july/phoebe_fitting_2.ipynb)

# Coming Soon in Future Releases

* Upcoming Changes in PHOEBE 2.2 (if not yet released)
* Extinction (if not yet released)
* Pulsations
* Triple and Higher-Order Systems
* Contact Binaries
* GUI
* Misc
* Discussion
