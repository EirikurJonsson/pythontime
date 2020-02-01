# Time Series

This is my repository working with time series data. I will focus on visualizations and forecasting methods, start off with simple moving averages, drif and other methods to forecast.

## Visualization

### 50/200 moving average
I have implemented a 50/200 day moving average function that works very well. I did use sendtex finance guide since I rememberd he used the rolling function. Here is an example picture

![50/200 day average](https://github.com/EirikurJonsson/pythontime/blob/master/fig.png)

### General moving average visualization

So I am creating a moving average function that is general enough that I can give it a list of windows I want to average over, instead of plotting each plot individually. I am almost done with it. My TODO right now is to combine the lines into the same plot, since my function returns two plots, one with the actual data, the other with the moving averages.

**Update** So I just finished it. The function can now take a list or a single value to represent a rolling average. Pic below

![Rollave fun with list](https://github.com/EirikurJonsson/pythontime/blob/master/fig2.png)
