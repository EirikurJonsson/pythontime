'''
FORECASTING IN PYTHON

This file is reserved for forecasting methods in python. I will use a variety of methods,
trying my best to generalize them into functions as best I can.
'''

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot as acp
from pandas.plotting import lag_plot as lp
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.ar_model import AR

df = pd.read_csv("AAPL.csv", parse_dates = ["Date"])
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace = True)


lp(df["Adj Close"])
#plt.show()

acp(df["Adj Close"])
#plt.show()

#print(df["Adj Close"].corr(df["Adj Close"].shift(26)))

decomposed = seasonal_decompose(df["Close"].values, model = 'additive', freq = 26)
decomposed.plot()
#plt.show()

df["stationary"] = df["Adj Close"].diff()
df["stationary"].plot()
#plt.show()
stationary_decomposed = seasonal_decompose(df["stationary"].dropna(), model = "additive", freq = 26)

stationary_decomposed = seasonal_decompose(df["stationary"].dropna(), model = "additive", freq = 26)
stationary_decomposed.plot()
#plt.show()



nX = df["stationary"].dropna()

train = nX[1:len(nX)-503]
test = nX[nX[len(nX)-503:]]

model = AR(train)
model_fit = model.fit()

# print("The lag value is: %s" % model_fit.k_ar)

# print("The coefficients of the model are: \n %s" % model_fit.params)
# print(df["2018":])

pred = model_fit.predict(start = len(train), end = len(train)+len(test)-1, dynamic = False)

compare_df = pd.concat([df["stationary"].tail(503), pred], axis = 1)

print(compare_df.tail())

#compare_df.plot()
#plt.show()