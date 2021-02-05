
# File uses the pybaseball python package to pull the lahman database


from pybaseball.lahman import *
#download_lahman() #download the entire lahman database to your current working directory


print("Successful Download")

import pandas as pd

def lahman_Combine():



    print("Lahman Batting")

    lahman_batting = pd.read_csv('baseballdatabank-master/core/Batting.csv')
    print(lahman_batting.shape)
    print(lahman_batting.head())


    print("Lahman Pitching")

    lahman_pitching = pd.read_csv('baseballdatabank-master/core/Pitching.csv')
    print(lahman_pitching.shape)
    print(lahman_pitching.head())

    lahman_batting = lahman_batting.add_suffix('_bat')
    lahman_pitching = lahman_pitching.add_suffix('_pit')

    print(lahman_batting.head())
    print(lahman_pitching.head())

    Full_Lahman = pd.merge(lahman_batting, lahman_pitching, left_on=['playerID_bat', 'yearID_bat', 'teamID_bat'], right_on=['playerID_pit', 'yearID_pit', 'teamID_pit'], how='outer')
    print(Full_Lahman.shape)
    print(Full_Lahman.head())

    # Full_Lahman.to_csv('Lahman_Combined.csv')


    print("Lahman Appearances")

    lahman_appearances = pd.read_csv('baseballdatabank-master/core/Appearances.csv')
    print(lahman_appearances.shape)
    print(lahman_appearances.head())

    lahman_appearances = lahman_appearances.add_suffix('_appear')

    print(lahman_appearances.head())
    print(lahman_appearances.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_appearances, left_on=['playerID_bat', 'yearID_bat', 'teamID_bat'], right_on=['playerID_appear', 'yearID_appear', 'teamID_appear'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())

    # Full_Lahman.to_csv('Lahman_Combined.csv')


    print("Lahman People")

    lahman_people = pd.read_csv('baseballdatabank-master/core/People.csv')
    print(lahman_people.shape)
    print(lahman_people.head())

    lahman_people = lahman_people.add_suffix('_people')

    print(lahman_people.head())
    print(lahman_people.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_people, left_on=['playerID_bat'], right_on=['playerID_people'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())

    print("Lahman Salaries")

    lahman_salaries = pd.read_csv('baseballdatabank-master/core/Salaries.csv')
    print(lahman_salaries.shape)
    print(lahman_salaries.head())

    lahman_salaries = lahman_salaries.add_suffix('_salaries')

    print(lahman_salaries.head())
    print(lahman_salaries.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_salaries, left_on=['playerID_bat', 'yearID_bat'], right_on=['playerID_salaries', 'yearID_salaries'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())
    """
    print("Lahman College")

    lahman_college = pd.read_csv('baseballdatabank-master/core/CollegePlaying.csv')
    print(lahman_college.shape)
    print(lahman_college.head())

    lahman_college = lahman_college.add_suffix('_college')

    print(lahman_college.head())
    print(lahman_college.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_college, left_on=['playerID_bat'], right_on=['playerID_college'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())
    """
    """
    print("Lahman Player Awards")

    lahman_award_players = pd.read_csv('baseballdatabank-master/core/AwardsPlayers.csv')
    print(lahman_award_players.shape)
    print(lahman_award_players.head())

    lahman_award_players = lahman_award_players.add_suffix('_award_players')

    print(lahman_award_players.head())
    print(lahman_award_players.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_award_players, left_on=['playerID_bat', 'yearID_bat'], right_on=['playerID_award_players', 'yearID_award_players'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())
    """
    
    print("Lahman Teams")

    lahman_teams = pd.read_csv('baseballdatabank-master/core/Teams.csv')
    print(lahman_teams.shape)
    print(lahman_teams.head())

    lahman_teams = lahman_teams.add_suffix('_teams')

    print(lahman_teams.head())
    print(lahman_teams.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_teams, left_on=['teamID_bat', 'yearID_bat'], right_on=['teamID_teams', 'yearID_teams'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())

    print("Lahman Team Franchise")

    lahman_franchises = pd.read_csv('baseballdatabank-master/core/TeamsFranchises.csv')
    print(lahman_franchises.shape)
    print(lahman_franchises.head())

    lahman_franchises = lahman_franchises.add_suffix('_franchises')

    print(lahman_franchises.head())
    print(lahman_franchises.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_franchises, left_on=['franchID_teams'], right_on=['franchID_franchises'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())



    print("Lahman Parks")

    lahman_parks = pd.read_csv('baseballdatabank-master/core/Parks.csv')
    print(lahman_parks.shape)
    print(lahman_parks.head())

    lahman_parks = lahman_parks.add_suffix('_parks')

    print(lahman_parks.head())
    print(lahman_parks.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_parks, left_on=['park_teams'], right_on=['park.name_parks'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())


    print("Lahman Home Games")

    lahman_homeGames = pd.read_csv('baseballdatabank-master/core/HomeGames.csv')
    print(lahman_homeGames.shape)
    print(lahman_homeGames.head())

    lahman_homeGames = lahman_homeGames.add_suffix('_homeGames')

    print(lahman_homeGames.head())
    print(lahman_homeGames.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_homeGames, left_on=['park.key_parks', 'yearID_bat'], right_on=['park.key_homeGames', 'year.key_homeGames'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())

    """
    print("Lahman Managers")

    lahman_managers = pd.read_csv('baseballdatabank-master/core/Managers.csv')
    print(lahman_managers.shape)
    print(lahman_managers.head())

    lahman_managers = lahman_managers.add_suffix('_managers')

    print(lahman_managers.head())
    print(lahman_managers.head())


    Full_Lahman = pd.merge(Full_Lahman, lahman_managers, left_on=['teamID_bat', 'yearID_bat'], right_on=['teamID_managers', 'yearID_managers'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())
    """
    """
    print("Lahman Fielding")


    lahman_fielding = pd.read_csv('baseballdatabank-master/core/Fielding.csv')
    print(lahman_fielding.shape)
    print(lahman_fielding.head())
    lahman_fielding = lahman_fielding.add_suffix('_field')

    print(lahman_fielding.head())
    print(lahman_fielding.head())

    Full_Lahman = pd.merge(Full_Lahman, lahman_fielding,  left_on=['playerID_bat', 'yearID_bat', 'teamID_bat'], right_on=['playerID_field', 'yearID_field', 'teamID_field'], how='left')
    Full_Lahman = Full_Lahman.drop_duplicates()
    print(Full_Lahman.shape)
    print(Full_Lahman.head())

    # Full_Lahman.to_csv('Lahman_Combined.csv')

    """
    Full_Lahman.to_csv('Lahman_Combined.csv')





lahman_Combine()