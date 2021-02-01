#Lahman Dashboard

# This dashboard is a simple Batting Statistical investigation




import pandas as pd

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px #(need to pip install plotly==4.4.1)

df = pd.read_csv("baseballdatabank-master/core/Batting.csv")

# Add Player Information
people = pd.read_csv('baseballdatabank-master/core/People.csv')
df = pd.merge(df, people, left_on=['playerID'], right_on=['playerID'], how='left', suffixes=('', '_x'))
 
# Add Poisition Appearances
appearances = pd.read_csv('baseballdatabank-master/core/Appearances.csv')
df = pd.merge(df, appearances, left_on=['playerID'], right_on=['playerID'], how='left', suffixes=('', '_y'))
 

for col in df.columns: 
    print(col) 