# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:44:15 2020

@author: nihal
"""

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
time= pd.read_csv("Time.csv")
print(time)

import matplotlib.pyplot as plt
time.plot(y="negative",color='red', linestyle="dashdot", x="test")
plt.show()
time.plot(y="confirmed",color='green', linestyle='solid', x="test")
plt.show()

x=time["negative"]
y=time["confirmed"]
plt.plot(x,color='red',linestyle='dashdot', label="Negative")
plt.plot(y,color='green',linestyle='solid' , label="Confirmed")
plt.show()