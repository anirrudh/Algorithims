
# coding: utf-8

# In[57]:

import os
import sys
import math
import scipy.misc
import matplotlib.pyplot as plt
import numpy as np


# In[119]:

"""
Set a list of the timeframes required in the book in an array in units of increasing seconds.
"""
time = np.arange(0.1, 100.0, .05)


# In[160]:

plt.plot(time, np.log(time),'r-', time, np.sqrt(time), 'b-', time, time, 'g-', time, (time * np.log(time)), 'y-',time , np.power(time, 2), 'r--', time, np.power(time, 3), 'b--', time, np.power(2, time), 'g--', time, scipy.misc.factorial(time), 'y--')
plt.axis([0, 100, 0, 100])
plt.annotate('log(n)', 
             xy=(80, np.log(80)),  
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.annotate('n^2', 
             xy=(80, np.sqrt(80)),  
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.annotate('n', 
             xy=(40, 40),  
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.annotate('nlog(n)', 
             xy=(9.5,  9.5*np.log(9.5)),  
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.annotate('n^2', 
             xy=(7, np.power(7, 2)),  
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.annotate('n^3', 
             xy=(4.2, np.power(4.2, 3)),  
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.annotate('2^n', 
             xy=(6.15, np.power(2, 6.15)),  
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.annotate('n!', 
             xy=(4.05, scipy.misc.factorial(4.05)),  
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.show()


# In[154]:

# Get current size
fig_size = plt.rcParams["figure.figsize"]
 
# Prints: [8.0, 6.0]
print "Current size:", fig_size


# In[159]:

fig_size[0] = 15
fig_size[1] = 12
plt.rcParams["figure.figsize"] = fig_size


# In[157]:

print fig_size


# In[ ]:



