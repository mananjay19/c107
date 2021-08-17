import pandas as pd
import plotly.graph_objects as go
import csv

df = pd.read_csv('data.csv')
m = df.groupby('level')['attempt'].mean()
print(m)
fig = go.Figure(go.Bar(
    x=m,
    y=['level1','level2','level3','level4'],
    orientation = 'h'
))
fig.show()