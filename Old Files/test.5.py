


import pandas as pd
import numpy as np


df = pd.read_csv("Lahman_Batting_Combined.csv")

print(df.head())

Positions_Checkbox = 'G_as_OF'
input_pos_appear = 20
dff = []


if Positions_Checkbox == []:
    dff = dff
else:

    dff = df[df[Positions_Checkbox] >= input_pos_appear]
   # dff = df[df[Positions_Checkbox].apply(lambda x: any(item for item in Positions_Checkbox if item is x >= input_pos_appear))]







print(dff.head())