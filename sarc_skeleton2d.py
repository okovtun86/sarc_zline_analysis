# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:29:00 2025

@author: okovt
"""

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


setA = pd.read_csv('Branch Information A.csv')
setB = pd.read_csv('Branch Information B.csv')
setC = pd.read_csv('Branch Information C.csv')

branch_lengths_A = setA.groupby('Skeleton ID')['Branch length'].sum()
branch_lengths_B = setB.groupby('Skeleton ID')['Branch length'].sum()
branch_lengths_C = setC.groupby('Skeleton ID')['Branch length'].sum()

bin_width = 1
bins = range(0, 300, bin_width)

plt.figure(figsize=(12, 8))
sns.histplot(branch_lengths_A, bins=bins, kde=True, color="blue", label="Image A", alpha=0.6)
sns.histplot(branch_lengths_B, bins=bins, kde=True, color="orange", label="Image B", alpha=0.6)
sns.histplot(branch_lengths_C, bins=bins, kde=True, color="magenta", label="Image C", alpha=0.6)

plt.xlabel("Branch Length", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xlim(0,20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=18)
plt.show()


