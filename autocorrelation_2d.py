# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:57:13 2024

@author: okovt
"""

#%%

import numpy as np
import matplotlib.pyplot as plt
import diplib as dip

def radial_average(data):
    """
    Calculate the radial average of a 2D array.
    
    Parameters:
    - data: 2D numpy array (i.e., an autocorrelation map)
    
    Returns:
    - radial_profile: Radial average as a 1D array
    """
    y, x = np.indices(data.shape)
    center = np.array([data.shape[0] // 2, data.shape[1] // 2])
    r = np.sqrt((x - center[1])**2 + (y - center[0])**2)
    r = r.astype(int)

    radial_mean = np.bincount(r.ravel(), weights=data.ravel()) / np.bincount(r.ravel())
    return radial_mean

img_A = dip.ImageRead('A.tif')
img_B = dip.ImageRead('B.tif')
img_C = dip.ImageRead('C.tif')

auto_A = dip.AutoCorrelationFT(img_A)
auto_B = dip.AutoCorrelationFT(img_B)
auto_C = dip.AutoCorrelationFT(img_C)

fig, axes = plt.subplots(1, 3, figsize=(15, 5), dpi=300)
fig.suptitle('2D Autocorrelation Maps', fontsize=16)

images = [auto_A, auto_B, auto_C]
titles = ['A', 'B', 'C']
for i, ax in enumerate(axes):
    ax.imshow(images[i], cmap='turbo')
    ax.set_title(f"Image {titles[i]}")
    ax.set_xlabel('x (pixels)')
    ax.set_ylabel('y (pixels)')

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()

radial_profile_A = radial_average(np.array(auto_A))
radial_profile_B = radial_average(np.array(auto_B))
radial_profile_C = radial_average(np.array(auto_C))

plt.figure(figsize=(10, 6),dpi=300)
plt.plot(radial_profile_A, label='A')
plt.plot(radial_profile_B, label='B')
plt.plot(radial_profile_C, label='C')
plt.title("Radial Autocorrelation Profiles")
plt.xlabel("Radial Distance (pixels)")
plt.ylabel("Correlation")
plt.legend()
plt.show()

