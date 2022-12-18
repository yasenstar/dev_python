#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:15:23 2019

@author: v0cn037
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 20, 250)
b = np.sin(a)

plt.plot(a, b, 'b^')
plt.grid(True)