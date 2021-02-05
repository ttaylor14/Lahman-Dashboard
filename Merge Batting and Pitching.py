import pandas as pd



def drop_y(df):
    # list comprehension of the cols that end with '_y'
    to_drop = [x for x in df if x.endswith('_y')]
    df.drop(to_drop, axis=1, inplace=True)

print('Add Batting')
df = pd.read_csv('Lahman_Batting_Combined.csv')

print(df.shape)
print(df.head())

print('Add Apperances')
# Add Poisition Appearances
appearances = pd.read_csv('Lahman_Batting_Combined.csv')
df = pd.merge(df, appearances, left_on=['playerID', 'yearID', 'teamID'], right_on=['playerID', 'yearID', 'teamID'], how='left', suffixes=('', '_y'))
 
print(df.shape)
print(df.head())

drop_y(df)



df.to_csv('Lahman_Combined.csv')


print(df.shape)
print(df.head())


