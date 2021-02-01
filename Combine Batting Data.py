
import pandas as pd



def drop_y(df):
    # list comprehension of the cols that end with '_y'
    to_drop = [x for x in df if x.endswith('_y')]
    df.drop(to_drop, axis=1, inplace=True)

print('Add Batting')
df = pd.read_csv("baseballdatabank-master/core/Batting.csv")

print(df.shape)
print(df.head())

print('Add Apperances')
# Add Poisition Appearances
appearances = pd.read_csv('baseballdatabank-master/core/Appearances.csv')
df = pd.merge(df, appearances, left_on=['playerID', 'yearID', 'teamID'], right_on=['playerID', 'yearID', 'teamID'], how='left', suffixes=('', '_y'))
 
print(df.shape)
print(df.head())

drop_y(df)


print(df.shape)
print(df.head())

print('Add Player Info')
# Add Player Information
people = pd.read_csv('baseballdatabank-master/core/People.csv')
df = pd.merge(df, people, left_on=['playerID'], right_on=['playerID'], how='left', suffixes=('', '_y'))
 
print(df.shape)
print(df.head())

drop_y(df)

print(df.shape)
print(df.head())

print('Add Team Info')
# Add Team Information
team = pd.read_csv('baseballdatabank-master/core/Teams.csv')
df = pd.merge(df, team, left_on=['teamID', 'yearID', 'lgID'], right_on=['teamID', 'yearID', 'lgID'], how='left', suffixes=('', '_y'))
 
print(df.shape)
print(df.head())

drop_y(df)

print(df.shape)
print(df.head())


# Relabel Columns
df.rename(columns = {'G_P':'G_as_P',
                        'G_C':'G_as_C',
                        'G_1b':'G_as_1B',
                        'G_2b':'G_as_2B',
                        'G_3b':'G_as_3B',
                        'G_ss':'G_as_SS',
                        'G_lf':'G_as_LF',
                        'G_cf':'G_as_CF',
                        'G_rf':'G_as_RF',
                        'G_of':'G_as_OF',
                        'G_dh':'G_as_DH',
                        'G_ph':'G_as_PH',
                        'G_Pr':'G_as_PR',
                        'W':'Team_W',
                        'L':'Team_L',
                        'RA':'Team_RA',
                        'ER':'Team_ER',
                        'ERA':'Team_ERA',
                        'CG':'Team_CG',
                        'SHO':'Team_SHO',
                        'SV':'Team_SV',
                        'IPOUTS':'Team_IPOUTS',
                        'HA':'Team_HA',
                        'HRA':'Team_HRA',
                        'BBA':'Team_BBA',
                        'SOA':'Team_SOA',
                        'E':'Team_E',
                        'DP':'Team_DP',
                        'FP':'Team_FP'}, inplace = True) 

print(df.shape)
print(df.head())


df.to_csv('Lahman_Batting_Combined.csv')


print(df.shape)
print(df.head())




