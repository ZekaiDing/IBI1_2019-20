# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:26:04 2020

@author: lenovo
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


T=[]
newcases=[]
world=[]
spain=[]
covid_data = pd.read_csv("full_data.csv")
#read the 'csv' file


print(covid_data.iloc[0:15:3,:])


for i in range (0,int(covid_data.describe().iloc[0,0])):
    if covid_data.iloc[i,1]=='Afghanistan':       
        T.append(True)
        
    else:
        T.append(False)
    if covid_data.iloc[i,1]=='World':       
        world.append(True)
        
    else:
        world.append(False)
    if covid_data.iloc[i,1]=='Spain':       
        spain.append(True)
        
    else:
        spain.append(False)
#use the boolean to confirm the location of some specific concties
      


print(covid_data.loc[T,'total_cases'])
print('The mean of new cases: ', (covid_data.describe().iloc[1,0]))
print('The median of new cases: ', (covid_data.describe().iloc[5,0]))
#use the discribe() to get the mean and median

newcases=covid_data.loc[world,'new_cases']

#draw the boxplot
plt.boxplot(newcases,patch_artist = True,meanline = False,showbox = True,notch = False)
plt.title('Worldwide New Cases ')
plt.show()

world_dates=covid_data.loc[world , 'date']
world_new_cases=covid_data.loc[world ,'new_cases']
world_new_deaths=covid_data.loc[world,'new_deaths']

plt.plot(world_dates, world_new_cases, 'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.ylabel('Number Of Cases')
plt.title('New Cases')
plt.show()

plt.plot(world_dates,world_new_deaths,'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.ylabel('Number Of Deaths')
plt.title('New Deaths')
plt.show()

spain_dates=covid_data.loc[spain,'date']
spain_new_cases=covid_data.loc[spain ,'new_cases']
spain_total_cases=covid_data.loc[spain ,'total_cases']

spain_new_cases=covid_data.loc[spain,'new_cases']
plt.plot(spain_dates,spain_new_cases,'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.ylabel('Number Of New cases')
plt.title('Spainish Tendency')
plt.show()

spain_total_cases=covid_data.loc[spain,'total_cases']
plt.plot(spain_dates,spain_total_cases,'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.ylabel('Number Of Total cases')
plt.title('Spainish Tendency')
plt.show()