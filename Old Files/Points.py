# Projected Rankings System

# last Update : 10.6.19


import pandas as pd
import numpy as np


currentYear = 2019 - 1

#################################################

#### Create Batting and Pitching Point totals ###

#################################################

# Creates files for batting and pitching point totals


# Procrastination Points

# ESPN Settings



def pointAmountsBat():

    global R, Single, Double, Triple, HR, TB, RBI, BB, K, SB, AB, Hits, XBH, GWRBI, IBB, HBP, SAC, CS, SBN, GIDP, CYC, GSHR, BTW, BTL
    global FC, PO, AST, OFAST, BatE, DPT

    ## Batting Scoring
    R = 1 # Runs Scored
    Single = 0 # Singles
    Double = 0 # Doubles
    Triple = 0 # Triples
    HR = 2 # Home Runs
    TB = 1 # Total Bases
    RBI = 1 # Runs Batted In
    BB = 1 # Walks
    K = -1 # Strikeouts
    SB = 1 # Stolen Bases
    AB = 0 # At Bats
    Hits = 0 # Hits
    XBH = 0 # Extra Base Hits
    GWRBI = 0 # Game Winning RBI
    IBB = 1 # Intentional Walks
    HBP = 0 # Hit by Pitch
    SAC = 0 # Sacrifices
    CS = -1 # Caught Stealing
    SBN = 0 # Net Stolen Bases
    GIDP = 0 # Ground into Double Plays
    CYC = 20 # Hitting for the Cycle
    GSHR = 4 # Grand Slam Home Runs
    BTW = 0 # Batter Team Win
    BTL = 0 # Batter Team Loss

    ## Fielding
    FC = 0 # Fielding Chances
    PO = 0 # Put Outs
    AST = 0 # Assists
    OFAST = 0 # Outfield Assists
    BatE = -1 # Errors
    DPT = 0 # Double Plays Turned

    return R, Single, Double, Triple, HR, TB, RBI, BB, K, SB, AB, Hits, XBH, GWRBI, IBB, HBP, SAC, CS, SBN, GIDP, CYC, GSHR, BTW, BTL
    return FC, PO, AST, OFAST, BatE, DPT


def pointAmountsPit():

    global IP, ER, K, SO, W, L, SV, BS, G, GS, H, RA, HR, BB, HB, WP, B, PKO, QS, CG, NH, PG, BF, PC, SOP, HD, PTW, PTL, SVHD

    ### Pitching
    IP = 3 # Innings Pitched # INNINGS PITCHED / OUTS RECORDED
    # Although Innings Pitched are typically displayed throughout the game, pitchers will accrue points for each out they record. The point value entered here applies to outs recorded. For example, if you choose a value of 2 points, a pitcher that pitches 1 inning will earn 6 points (2 points * 3 outs).
    ER = -2 # Earned Runs
    K = 1 # Strikeouts
    SO = 5 # Shutouts
    W = 5 # Wins
    L = -5 # Losses
    SV = 5 # Saves
    BS = -5 # Blown Saves
    G = 0 # Appearances
    GS = 0 # Games Started
    H = -1 # Hits Allowed
    RA = 0 # Runs Allowed
    HR = 0 # Home Runs Allowed
    BB = -1 # Walks Issued
    HB = -1 # Hit Batsmen
    WP = -1 # Wild Pitches
    B = -1 # Balks
    PKO = 2 # Pick Offs
    QS = 5 # Quality Starts
    CG = 10 # Complete Games
    NH = 15 # No Hitters
    PG = 20 # Perfect Games
    BF = 0 # Batters Faced
    PC = 0 # Pitch Count
    SOP = 0 # Save Opportunities
    HD = 0 # Holds
    PTW = 0 # Pitcher Team Win
    PTL = 0 # Pitcher Team Loss
    SVHD = 0 # Saves Plus Holds

    return IP, ER, K, SO, W, L, SV, BS, G, GS, H, RA, HR, BB, HB, WP, B, PKO, QS, CG, NH, PG, BF, PC, SOP, HD, PTW, PTL, SVHD










def points(currentSeason):
    data = pd.read_csv('Lahman_Database/core/Batting.csv')
    data = data[data['yearID'] == currentSeason]

    fielding = pd.read_csv('Lahman_Database/core/Fielding.csv')
    fielding = fielding[fielding['yearID'] == currentSeason]
    fielding = fielding.rename(columns = {"SB": "SB_F", "CS": "CS_F", "G": "G_F", "GS": "GS_F"})
    fielding = fielding.groupby('playerID').agg(sum)

    data = pd.merge(data, fielding, on='playerID', how='inner')

    pointAmountsBat()
    singles = data['H'] - data['2B'] - data['3B'] - data['HR']
    data.insert(9, '1B', singles)

    points = ( ( R * data['R'] )
    + ( Single * data['1B'] )
    + ( Double * data['2B'] )
    + ( Triple * data['3B'] )
    + ( HR * data['HR'] )
    + ( TB * ( data['1B'] + (2 * data['2B']) + (3 * data['3B']) + (4 * data['HR']) ) )
    + ( RBI * data['RBI'] )
    + ( BB * data['BB'] )
    + ( K * data['SO'] )
    + ( SB * data['SB'] )
    + ( AB * data['AB'] )
    + ( Hits * data['H'])
    + ( XBH * ( data['2B'] + data['3B'] + data['HR']) )
    + ( IBB * data['IBB'] )
    + ( HBP * data['HBP'] )
    + ( CS * data['CS'] )
    # need add fielding
    - ( BatE * data['E'] )
    + ( DPT * data['DP'] )
    + ( PO * data['PO'] )
    + ( AST * data['A'] )
    )



    # missing Sac and GWRBI and everything past CS

    data.insert(0, 'Points', points)
    data['Points'] = data['Points'].round(decimals=0)
    data = data.sort_values('Points', ascending=False)
    data = data.reset_index(drop=True)

    # print(data.head())


    pdata = pd.read_csv('Lahman_Database/core/Pitching.csv')
    pdata = pdata[pdata['yearID'] == currentSeason]
    pdata = pd.merge(pdata, fielding, on='playerID', how='inner')

    pointAmountsPit()

    ppoints = ( ( IP/3 * pdata['IPouts'] )
    + ( ER * pdata['ER'] )
    + ( K * pdata['SO'] )
    + ( SO * pdata['SHO'] )
    + ( W * pdata['W'] )
    + ( L * pdata['L'] )
    + ( SV * pdata['SV'] )
    + ( G * pdata['G'] )
    + ( GS * pdata['GS'] )
    + ( H * pdata['H'] )
    + ( RA * pdata['R'] )
    + ( HR * pdata['HR'] )
    + ( BB * pdata['BB'] )
    + ( HB * pdata['HBP'] )
    + ( IBB * pdata['IBB'] )
    + ( B * pdata['BK'] )
    #+ ( PKO * pdata['PKO'] )
    + ( QS * pdata['BK'] )
    + ( CG * pdata['CG'] )
    #+ ( NH * pdata['NH'] )
    #+ ( PG * pdata['PG'] )
    #+ ( BF * pdata['BF'] )
    #+ ( SOP * pdata['SOP'] )
    #+ ( HD * pdata['HD'] )
    # need add fielding
    - ( BatE * data['E'] )
    )

    pdata.insert(0, 'Points', ppoints)
    pdata['Points'] = pdata['Points'].round(decimals=0)
    pdata = pdata.sort_values('Points', ascending=False)
    pdata = pdata.reset_index(drop=True)

    # print(pdata.head())

    rankings = pd.merge(data, pdata, how='outer')
    rankings = rankings.sort_values('Points', ascending=False)
    rankings = rankings.reset_index(drop=True)

    # print(rankings.head())

    names = pd.read_csv('Lahman_Database/core/people.csv')
    rankings = pd.merge(rankings, names, on='playerID', how='inner')

    appear = pd.read_csv('Lahman_Database/core/Appearances.csv')
    appear = appear[appear['yearID'] == currentSeason]
    rankings = pd.merge(rankings, appear, on='playerID', how='inner')

    rankings = rankings.sort_values('Points', ascending=False)
    rankings = rankings.reset_index(drop=True)
    # print(rankings.head())

    rankings.to_csv('rankings.csv')


def PointCycle():
    global currentYear

    yearRange = list(range(2000, currentYear + 1))
    # print(yearRange)
    for x in yearRange:
        # print(X)
        points(x)
        R = pd.read_csv('rankings.csv')
        filename = "YearPoints/%s.csv" % x
        R.to_csv(filename, sep=',', index=False, encoding='utf-8')
        print(str(x) + ": Successful")




PointCycle()
