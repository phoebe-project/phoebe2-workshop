#!/usr/bin/env python
# coding: utf-8

# ## PHOTOMETRIC CALIBRATION IN PHOEBE

# ### Background.
# 
# When measuring incident light from a source, there are several radiative properties that we need to distinguish:
# 
# * Luminosity: describe luminosity
# * Flux: describe flux
# * Intensity: describe intensity
# 
# The measured physical quantity from an unresolved source is thus flux, measured in $\mathrm{W}/\mathrm{m}^2$. However, in astronomy it is customary to use magnitudes instead; to transform fluxes to magnitudes or vice versa, we need to know a reference value for flux, $f_0$, that corresponds to a reference value for magnitude, $m_0$. Once we have that, the transformation is given by:
# 
# $$ m = m_0 - \frac 52 \log_{10} \frac{f}{f_0} \quad \textrm{ and conversely } \quad f = f_0 10^{-2/5 (m - m_0)}. $$
# 
# For example, we could set $m_0 = 0$ to correspond to $f_0 = 1\,\mathrm{W}/\mathrm{m}^2$.

# In the context of PHOEBE, by ``passband'' we denote the combined photometric response of the filter, telescope optics, detector quantum efficiency, and any other systematic effects that affect the throughput. Given an input of uniform intensity across all wavelengths, a passband transmission function determines flux density ($df/d\lambda$) at each wavelength $\lambda$. Let us take a look at Johnson B and V filters.

# In[1]:


import phoebe

jB = phoebe.get_passband('Johnson:B')
jV = phoebe.get_passband('Johnson:V')


# In[4]:


import matplotlib.pyplot as plt
plt.style.use('jupyter')


# In[5]:


plt.xlabel('Wavelength [m]')
plt.ylabel('Passband transmission')
plt.plot(jB.ptf_table['wl'], jB.ptf_table['fl'], 'b-', label='Johnson B')
plt.plot(jV.ptf_table['wl'], jV.ptf_table['fl'], 'g-', label='Johnson V')
plt.legend()


# Now let's read in a theoretical spectral energy distribution (SED) of a Sun-like star (T=5750K, logg=4.5, abun=0.0) as calculated by Kurucz's model atmospheres:

# In[6]:


import numpy as np
from astropy.io import fits

with fits.open('T05750G45P00.fits') as hdul:
    ints = hdul[0].data[-1,:]*1e7  # erg/s/cm^2/A -> W/m^3
wls = np.arange(900., 39999.501, 0.5)/1e10 # AA -> m

plt.xlabel('Wavelength [m]')
plt.ylabel('$df/d\lambda \equiv I_\lambda$')
plt.plot(wls, ints, 'r-')


# Now we can zoom in on the parts covered by the Johnson B and V passbands:

# In[7]:


flt = (wls > jB.ptf_table['wl'][0]) & (wls < jV.ptf_table['wl'][-1])
wls = wls[flt]
ints = ints[flt]

plt.xlabel('Wavelength [m]')
plt.ylabel('$df/d\lambda \equiv I_\lambda$')
plt.plot(wls, ints, 'r-')
plt.plot(jB.ptf_table['wl'], max(ints)*jB.ptf_table['fl'], 'b-')
plt.plot(jV.ptf_table['wl'], max(ints)*jV.ptf_table['fl'], 'g-')


# The SED received by the detector in each passband is the product of the passband response function and the SED:

# In[8]:


flt_B = (wls >= jB.ptf_table['wl'][0]) & (wls <= jB.ptf_table['wl'][-1])
wls_B = wls[flt_B]
ints_B = ints[flt_B]*jB.ptf(wls_B)

flt_V = (wls >= jV.ptf_table['wl'][0]) & (wls <= jV.ptf_table['wl'][-1])
wls_V = wls[flt_V]
ints_V = ints[flt_V]*jV.ptf(wls_V)

plt.xlabel('Wavelength')
plt.ylabel('$I_\lambda^\mathrm{pb}$')
plt.plot(wls_B, ints_B, 'b-')
plt.plot(wls_V, ints_V, 'g-')


# Note that the y-axis here is passband intensity, measured in $\mathrm{W}/\mathrm{m}^3$. If we want to get the amount of flux received in each passband on the surface of the star, it is the integral of passband intensity over wavelength, $F = \int_\lambda I_\lambda d\lambda$:

# In[15]:


dwl = wls[1]-wls[0]
fl_B = np.sum(ints_B)*dwl
fl_V = np.sum(ints_V)*dwl
print(f'flux in B-band: {fl_B:.0f} W/m^2\nflux in V-band: {fl_V:.0f} W/m^2')


# This allows us to calculate the mean passband intensity, $\langle I \rangle = \frac{\int_\lambda P(\lambda) S(\lambda) d\lambda}{\int_\lambda P(\lambda) d\lambda}$, which is in the units of $\mathrm{W}/\mathrm{m}^3$:

# In[13]:


pbi_B = fl_B/jB.ptf_area
pbi_V = fl_V/jV.ptf_area
print(f'B-band mean intensity: {pbi_B} W/m^3\nV-band mean intensity: {pbi_V} W/m^3')


# In[11]:


plt.xlabel('Wavelength')
plt.ylabel('$I_\lambda^\mathrm{pb}$')
plt.plot(wls_B, ints[flt_B], 'b-', alpha=0.5)
plt.plot(wls_B, np.ones_like(ints_B)*pbi_B, 'k-')
plt.plot(wls_V, ints[flt_V], 'g-', alpha=0.5)
plt.plot(wls_V, np.ones_like(ints_V)*pbi_V, 'k-')


# In[12]:


jB.Inorm(atm='ck2004', Teff=5750, logg=4.5, abun=0.0)


# In[15]:


pbu_B = np.ones_like(ints_B)*pbi_B


# In[16]:


(pbu_B*jB.ptf(wls_B)).sum()


# In[17]:


ints_B.sum()


# ## Magnitudes
# 
# Magnitudes are an astronomer's way to measure *fluxes*. In general,
# 
# $$ m - m_0 = -\frac 52 \log_{10} \frac{f}{f_0}, $$
# 
# where $m_0$ is the reference magnitude that corresponds to the flux $f_0$. Fluxes are measured in $\textrm{W}/\textrm{m}^2$ while magnitudes are unitless. The ($m_0$, $f_0$) pair is usually chosen so that $m_0=0$ for a prescribed value of $f_0$. That really is all that there is to magnitudes. The rest are details, but we still need to understand them. And for that, we need context.
# 
# First, consider observations of a given star, say Vega, in two photometric passbands, say B and V. As we saw in our discussion above, the fluxes in the B band and in the V band are in general _different_. Add another photometric passband, say R, and the three fluxes will _definitely_ be different: there is no stellar spectral energy distribution function that would have the same integrals under all three passbands. Yet, as far as magnitudes are concerned, it is customary to define $m_0$ *per passband*: in other words, each passband comes with its own $m_0$. These passband-dependent $m_0$ are referred to as *photometric zero-points*. In the past people used Vega to set *all* magnitudes to 0 at all wavelengths: $m_B = m_V = \dots = 0$. Today people no longer use Vega, instead they give exact passband-dependent $f_0$ that uniquely define $m_0$ independently of any observation specifics.
# 
# In an attempt to reach magnitude independence from observatory specifics, two standards are introduced:
# 
# * **AB magnitude system**: it represents a monochromatic flux density per unit frequency, assuming a flat reference spectrum $f_\nu \equiv df/d\nu$. A light source that has $f_\nu = 3.63 \times 10^{-20}$ erg/$\textrm{cm}^2/\textrm{s}/\textrm{Hz}$ will have the corresponding ABmag=0 in all passbands. The corresponding zero-point is $m_{AB} = 48.6$.
# 
# $$ \mathrm{ABmag} = -2.5 \log_{10} f_\nu + 48.6 $$
# 
# * **ST magnitude system**: it represents a monochromatic flux density per unit wavelength, assuming a flat reference spectrum $f_\lambda \equiv df/d\lambda$. A light source that has $f_\lambda = 3.63 \times 10^{-9} \mathrm{erg}/\textrm{cm}^2/\textrm{s}/\AA$ will have the corresponding STmag=0 in all passbands. The corresponding zero-point is $m_{ST} = 21.10$.
# 
# $$ \mathrm{STmag} = -2.5 \log_{10} f_\lambda + 21.10 $$

# 
