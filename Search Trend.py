# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:26:00 2021

@author: Nihal
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

covid_search = pd.read_csv("SearchTrend.csv")

covid_search['date']=pd.to_datetime(covid_search['date'])
covid_search = covid_search[covid_search['date'].dt.strftime('%Y')=='2020']

plt.figure(figsize=(15,10))

x1 = covid_search["cold"]
y1 = covid_search["date"]

plt.tick_params(axis="x", rotation=70)
plt.plot(y1,x1)

x2 = covid_search["flu"]
y2 = covid_search["date"]

plt.tick_params(axis="x", rotation=70)

x3 = covid_search["pneumonia"]
y3 = covid_search["date"]

plt.tick_params(axis="x", rotation=70)
plt.plot(y3,x3)

x4 = covid_search["coronavirus"]
y4 = covid_search["date"]

plt.tick_params(axis="x", rotation=70)
plt.plot(y4,x4)

blue_patch = mpatches.Patch(color=(0,0.5,0.8,1), label="Cold")
orange_patch = mpatches.Patch(color=(1,0.3,0,1), label="Flu")
red_patch = mpatches.Patch(color=(1,0,0,1), label="Coronavirus")
green_patch = mpatches.Patch(color=(0.3,1,0.4,1), label="Pneumonia")
plt.legend(handles=[red_patch, green_patch, blue_patch, orange_patch])
plt.title("Internet Search Ratio of Diseases")
plt.ylabel("Search Ratio")
plt.xlabel("Date")






