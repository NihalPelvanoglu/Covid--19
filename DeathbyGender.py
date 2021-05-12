# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:37:12 2020

@author: nihal
"""

import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

covid = pd.read_csv("TimeGender.csv")
deathbygender = covid[["date", "sex", "deceased"]].copy()

male = deathbygender[deathbygender.loc[:,"sex"]=="male"]

female = deathbygender[deathbygender.loc[:, "sex"]=="female"]

plt.figure(figsize=(15,10))

x1=male["deceased"]
y1=male["date"]

plt.tick_params(axis = "x", rotation=70)
plt.bar(y1,x1, edgecolor="black")

x2=female["deceased"]
y2=female["date"]

plt.tick_params(axis="x", rotation=70)
plt.bar(y2,x2, edgecolor="black")

blue_patch = mpatches.Patch(color=(0,0.5,0.8,1), label="Male")
orange_patch = mpatches.Patch(color=(0.9,0.3,0,1), label="Female")
plt.legend(handles=[blue_patch,orange_patch])
plt.title("DEATH BY GENDER")
plt.ylabel("Death Toll")
plt.xlabel("Days")

