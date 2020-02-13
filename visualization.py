'''
Visualisation: Here I start with visualization.

The code is at times an altered code I got from this
time series guide:
https://www.machinelearningplus.com/time-series/time-series-analysis-python/
So good tap on the sholder to Selva Prabhakaran for posting this and allowing me to learn 
from it. 

The data will has been pulled from another project I am still developing. 
'''


from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import datetime
from statsmodels.tsa.stattools import adfuller


df = pd.read_csv("AAPL.csv", parse_dates = ["Date"])

def plot_df(df, x, y, title = "", xlabel = "Date", ylabel = "Value", dpi = 100):
    '''
    This is a simple generic plot function that will plot a time series. 
    '''
    plt.figure(figsize = (16,5), dpi = dpi)
    plt.plot(x,y, color = "tab:red")
    plt.gca().set(title = title, xlabel = xlabel, ylabel = ylabel)
    plt.show()


def rollave(df, x, y, roll, title = ""):
    '''
    This function is meant to take in either a value or a list of values
    that will represent the moving average window.
    This function will add the rolling averages to the data frame. This
    is, for now, is not a problem since it can be a positive going forward.
    '''
    if isinstance(roll, list):
        plt.figure(figsize = (16,5), dpi = 100)
        plt.plot(df[x], df[y], color = "tab:red", label = y)
        plt.gca().set(title = "Moving averages", xlabel = x, ylabel = y)
        for i in (roll):
            df[f"ma{i}"] = df[y].rolling(window = i, min_periods = 0).mean()
            plt.plot(df[x], df[f"ma{i}"], label = df[f"ma{i}"].name)   
    
    else:
        df[f"ma{roll}"] = df[y].rolling(window = roll, min_periods = 0).mean()
        plt.figure(figsize = (16,5), dpi = 100)
        plt.plot(df[x], df[f"ma{roll}"], label = df[f"ma{roll}"].name)
        plt.plot(df[x], df[y], color = "tab:red", label = y)
        plt.gca().set(title = "Moving averages", xlabel = x, ylabel = y)
    plt.legend()
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

def specialyear(df, x, y, years):
    '''
    This function should plot a specific year.
    TODO. Add to the function so that its possible 
    to pass a list of years.
    '''
    df['year'] = [d.year for d in df["Date"]]
    #print(df["year"].tail())
    df2 = df.loc[df["year"] == years,:]
    plt.plot(df2[x], df2[y])
    plt.show()

def nCandlegraph(df):
    '''
    This will get a specific data frame and produces a candlestick graph.
    To make this function work you need to parse_dates for the dataframe.
    '''
    try:
        df.reset_index(inplace=True)
        df["Date"] = mdates.date2num(df["Date"].values)
        ohlc = df[["Date","Open","High", "Low", "Close", "Volume"]].copy()
        fig, ax = plt.subplots(figsize = (16,5))
        candlestick_ohlc(ax, ohlc.values, width = .8, colorup = '#77d879', colordown = '#db3f3f')
        ax.xaxis_date()

        plt.show()
    except SyntaxError:
        print("You may need to use the parse_dates command for your data frame")
    except AttributeError:
        print("You may need to use the parse_dates command for your data frame")

def nReturns (df, y):
    '''
    This function is meant to calculate the log retruns
    of a variable in the data frame given and add this
    to the same data frame. This is rather simple but,
    keeping with the theme, this will also generate a plot
    of the returns.
    '''

    df[f"{y}_pctChange"] = df[y].pct_change()
    df = df.dropna()
    results = adfuller(df[f"{y}_pctChange"])
    plt.plot(df.index, df[f"{y}_pctChange"])
    plt.title(f"The adfuller test statistic is {round(results[0], 2)} with p value of {results[1]}")
    plt.show()

nReturns(df, "Adj Close")
