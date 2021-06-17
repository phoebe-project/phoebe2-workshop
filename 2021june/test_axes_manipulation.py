#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic(u'matplotlib inline')

import phoebe
import matplotlib.pyplot as plt

b = phoebe.default_binary()
b.add_dataset('lc', compute_phases=phoebe.linspace(0,1,101))
b.add_dataset('mesh', compute_phases=[0, 0.1, 0.2])

b.run_compute()


# In[2]:


afig, mplfig = b.plot(kind='lc', x='phases', axpos=212, rasterized=True)
afig, mplfig = b.plot(kind='mesh', time=0, axpos=231, rasterized=True)
afig, mplfig = b.plot(kind='mesh', time=0.1, axpos=232, rasterized=True)
afig, mplfig = b.plot(kind='mesh', time=0.2, axpos=233, rasterized=True)


# In[3]:


mplfig = plt.figure(figsize=(8,10))
mplfig = afig.draw(fig=mplfig)


# In[4]:


mplfig.axes


# In[5]:


mplfig.axes[1].axis('off')
mplfig.axes[2].axis('off')
mplfig.axes[3].axis('off')

mplfig.savefig('test_axes_manipulation.png')


# In[ ]:




