#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 00:53:25 2024

@author: eaydin
"""

import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv("PEP.csv",)
fiyatlar = veri[['Open','Close']]
veri["YEARS"]= pd.to_datetime(veri['Date'])
plt.plot( veri["YEARS"],fiyatlar)
plt.xlabel("Years")
plt.ylabel("Dollars")
plt.title("Opens and Closes of Pepsico")
plt.show()

