

# Create Correlation Plots of Data

# library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# DataSet
df = pd.read_csv("Lahman_Batting_Combined.csv")

df =  df[df['yearID']>2014]
df =  df[df['AB']>100]
df = df[['H', 'HR', 'SB', 'RBI', 'Team_W', 'teamID']]
print(df.head())
print(df.shape)

print("Dataset: Success")
# Create Plot
fig1 = sns.pairplot(df, kind="reg", diag_kind="hist", hue="teamID", palette="Set2")
# plt.show()

print("Successful Plot")

fig1.savefig('images/batting_correlation_plot_2015-2020.png')

print("Plot Saved Successful")

print("File Complete")




# DataSet
df = pd.read_csv("Lahman_Pitching_Combined.csv")

df =  df[df['yearID']>2014]
df =  df[df['IPouts']>120]
df = df[['GS', 'IPouts', 'ER', 'BB', 'SO', 'ERA', 'teamID']]
print(df.head())
print(df.shape)

print("Dataset: Success")
# Create Plot
fig2 = sns.pairplot(df, kind="reg", diag_kind="hist", hue="teamID", palette="Set2")
# plt.show()

print("Successful Plot")

fig2.savefig('images/pitching_correlation_plot_2015-2020.png')

print("Plot Saved Successful")

print("File Complete")