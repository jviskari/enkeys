#!/bin/python3
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/jviskari/enkeys/master/data/enkeys.csv')

fig1=px.scatter(df, y='ENK_y', trendline_color_override='crimson', trendline='lowess')
fig2=px.bar(df, y='ENK_y')
fig1.add_traces(fig2.data[0])


fig1.show()
