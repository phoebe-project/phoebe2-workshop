# Installing & Setup

### Installing PHOEBE

During the workshop, we will be using the 2.4 version of PHOEBE.  `emcee`, `scikit-learn`, and `celerite2` will also be useful for any fitting.  The easiest way to install is via pip (you're welcome to install within a virtual or conda environment if you'd like, just make sure you know how to activate that environment from within Jupyter):

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


Please test your installation well in advance of the workshop by running the [test script](https://raw.githubusercontent.com/phoebe-project/phoebe2-workshop/2024june/test_install.py) (should take approximately 60 seconds to run) and make sure it completes without any errors (warning messages are not a cause for concern).  If the script does not run successfully or takes significantly longer than 60 seconds, please reach out to us so we can debug any installation issues in advance.

### Prerequsite Comfort with PHOEBE

Unlike previous PHOEBE Workshops, where participants were taught the basics of PHOEBE, the purpose of this workshop is to improve on existing models, generate publishable results, and for participants to become advanced PHOEBE users. For this reason, workshop participants are expected to have either already attended a PHOEBE Workshop or to be actively using PHOEBE. Prior to the workshop, participants should be familiar with concepts including: setting parameter values, manipulating constraints, running forward models, and using estimators, optimizers, and samplers.  If you are not regularly using PHOEBE, please consider running through the online tutorials or videos from last year's workshop before arrival.

