'''
Visualisation: Here I start with visualization.

The code is at times an altered code I got from this
time series guide:
https://www.machinelearningplus.com/time-series/time-series-analysis-python/
So good tap on the sholder to Selva Prabhakaran for posting this and allowing me to learn 
from it. I rely hevily on this guide and this is just for my own education.

The data will has been pulled from another source, so I wont be utilizing the data in the guide
'''


from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("AAPL.csv", parse_dates = ["Date"])

def plot_df(df, x, y, title = "", xlabel = "Date", ylabel = "Value", dpi = 100):
    plt.figure(figsize = (16,5), dpi = dpi)
    plt.plot(x,y, color = "tab:red")
    plt.gca().set(title = title, xlabel = xlabel, ylabel = ylabel)
    plt.show()

#plot_df(df, y = df["Adj Close"], x = df["Date"], title = "Adj Close")


def rollave(df, x, y, roll, title = ""):
    '''
    This function is meant to take in either a value or a list of values
    that will represent the moving average window. Still does not work
    TODO. Make sure that the if else statements work
    TODO. Should use a for loop to plot the new values created
    '''
    if isinstance(roll, list):
        for i in roll:
            df[f"ma{i}"] = df[x].rolling(window = i, min_periods = 0).mean()
    else:
        df[f"ma{roll}"] = df[x].rolling(window = i, min_periods = 0).mean()
    plt.figure(figsize = (16,5), dpi = 100)
    plt.plot(x, y, color = "tab:red")
    plt.plot(x,df[f"ma{roll}"], color = "blue")
    plt.gca().set(title = "Moving averages", xlabel = x, ylabel = y)
    plt.show()

def roll250(df, x, y):
    '''
    This function plots the 50 and 200 day moving average
    This can take in any csv file that contain the right
    column names.
    '''
    ma50 = df[y].rolling(window = 50, min_periods = 0).mean()
    ma200 = df[y].rolling(window = 200, min_periods = 0).mean()
    plt.plot(df[x],df[y], color = "tab:red")
    plt.plot(df[x], ma50, color = "tab:green")
    plt.plot(df[x], ma200, color = "tab:blue")
    plt.title("50/200 moving averages")
    plt.show()
    del ma50
    del ma200

