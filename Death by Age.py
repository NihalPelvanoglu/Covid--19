# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:10:31 2020

@author: nihal
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

covid = pd.read_csv("TimeAge.csv")

covid["date"]= pd.to_datetime(covid["date"])

covid19 = covid[covid["date"].dt.strftime("%Y-%m-%d") == "2020-04-20"]

Dead = covid[["age", "deceased"]].copy()

plt.figure(figsize=(15,10))

plt.title("DEATH BY AGE")

plt.xlabel("Groups of Age")

plt.ylabel("Death Toll")

x= Dead["age"]

y= Dead["deceased"]

plt.bar(x,y)

