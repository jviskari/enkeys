#!/bin/python3
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/jviskari/enkeys/master/data/enkeys.csv')

fig = px.line(df, x = 'ENK_x', y = 'ENK_y', title='Amount of exposure notification keys checked over time (2020-)')
fig.show()
