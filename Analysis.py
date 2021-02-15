

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
columns = ['playerID', 'stint', 'birthCity', 'deathYear', 'deathMonth', 'deathDay', 'deathCountry', 'deathState', 'deathCity', 'nameFirst', 'nameLast', 'nameGiven', 'debut', 'finalGame', 'retroID', 'bbrefID', 'name', 'park', 'BPF', 'PPF', 'teamIDBR', 'teamIDlahman45', 'teamIDretro']
df = df.drop(columns, axis=1)
print(df.head())
print(df.shape)

print("Dataset: Success")
# Create Plot
sns.pairplot(df, kind="reg", diag_kind="hist", hue="teamID", palette="Set2")
plt.show()

print("Successful Plot")

plt.savefig('images/batting_correlation_plot_2015-2020.png')

print("Plot Saved Successful")

print("File Complete")




# DataSet
df = pd.read_csv("Lahman_Pitching_Combined.csv")

df =  df[df['yearID']>2014]
df =  df[df['IPouts']>120]
columns = ['playerID', 'G_c', 'G_1B', 'G_2B', 'G_3B', 'G_SS', 'G_LF', 'G_CF', 'G_RF', 'G_OF', 'G_DH', 'G_PH', 'G_pr', 'stint', 'birthCity', 'deathYear', 'deathMonth', 'deathDay', 'deathCountry', 'deathState', 'deathCity', 'nameFirst', 'nameLast', 'nameGiven', 'debut', 'finalGame', 'retroID', 'bbrefID', 'name', 'park', 'BPF', 'PPF', 'teamIDBR', 'teamIDlahman45', 'teamIDretro']
df = df.drop(columns, axis=1)
print(df.head())
print(df.shape)

print("Dataset: Success")
# Create Plot
sns.pairplot(df, kind="reg", diag_kind="hist", hue="teamID", palette="Set2")
plt.show()

print("Successful Plot")

plt.savefig('images/pitching_correlation_plot_2015-2020.png')

print("Plot Saved Successful")

print("File Complete")