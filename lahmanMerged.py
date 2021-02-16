#Lahman Dashboard

# This dashboard is a simple Batting Statistical investigation




import pandas as pd

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.express as px #(need to pip install plotly==4.4.1)
import plotly.graph_objects as go

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
# Allows Heroku to connect to servers:
server = app.server




df = pd.read_csv("Lahman_Combined.csv")


min_year = df.yearID.min()
max_year = df.yearID.max()




#---------------------------------------------------------------
app.layout = html.Div([

    html.Div([

        dbc.Row([
            dbc.Col([

                # Page Title

                html.H3("Baseball Visualizations: Lahman Database", 
                style={'fontSize': 32, 'margin-right': '5%', 'margin-left': '5%', 'margin-top': '2%', 'margin-bottom': '0.5%'})
                
            ]),

        ]),


        dbc.Row([

            # Range Slider Row

            dbc.Col( [
                html.Div([
                    # left edge Place Holder
                ]),
                
            ]),

            dbc.Col( [
                html.Div([
                    # Select Year Ranges
                    
                    dcc.RangeSlider(
                        id='Season',
                        marks={
                            1850: {'label': '1850', 'style': {'color': '#77b0b1'}},
                            1860: {'label': '1860'},
                            1870: {'label': '1870'},
                            1880: {'label': '1880', 'style': {'color': '#f50'}},
                            1890: {'label': '1890', 'style': {'color': '#77b0b1'}},
                            1900: {'label': '1900'},
                            1910: {'label': '1910'},
                            1920: {'label': '1920', 'style': {'color': '#f50'}},
                            1930: {'label': '1930', 'style': {'color': '#77b0b1'}},
                            1940: {'label': '1940'},
                            1950: {'label': '1950'},
                            1960: {'label': '1960', 'style': {'color': '#f50'}},
                            1970: {'label': '1970', 'style': {'color': '#77b0b1'}},
                            1980: {'label': '1980'},
                            1990: {'label': '1990'},
                            2000: {'label': '2000'},
                            2010: {'label': '2010', 'style': {'color': '#f50'}},
                            2020: {'label': '2020'},
                            2030: {'label': '2030'},
                            2040: {'label': '2040', 'style': {'color': '#f50'}}
                        },
                        step=1,
                        min = min_year,
                        max = max_year,
                        value = [2018, 2020],
                        dots = True,
                        allowCross = False,
                        disabled = False,
                        pushable = 0,
                        updatemode = 'drag',
                        included = True,
                        vertical = False,
                        # verticalHeight = 900,
                        className = 'None',
                        # tooltip = {"always visible":False, "placement":'bottom'}

                    ),
                ]),
                
            ], width=11),


            dbc.Col( [
                html.Div([
                    # Right edge Place Holder
                ]),
                
            ]),
        

        ]),

        dbc.Row([
            
                dbc.Col([
                    html.H6("Select X-Axis: "),
                    # Select 'X' Axis
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_X',
                        options=[
                                {'label': column, 'value': column}
                                for column in df.columns.unique()
                                ],   
                        value='G',
                        placeholder="X-Axis",
                        multi=False,
                        clearable=False,

                    ),
                    ]),

                    html.H6("Select Y-Axis: "),

                    # Select 'Y' Axis
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_Y',
                        options=[
                                {'label': column, 'value': column}
                                for column in df.columns.unique()
                                ],   
                        value='H',
                        placeholder="Y-Axis",
                        multi=False,
                        clearable=False,


                    ),
                    ]),

                    html.H6("Select Color Grouping: "),

                    # Select Color Grouping
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_Color',
                        options=[
                                {'label': column, 'value': column}
                                for column in df.columns.unique()
                                ],        
                        value='teamID',
                        placeholder="Color Grouping",
                        multi=False,
                        clearable=False,

                    ),
                    ]),
                                        
                    html.H6("Position Eligibility: "),

                    # Select Position Eligibility
                    html.Div([
                    dcc.Input(
                        id='input_pos_appear',
                        type='number',
                        step=1,
                        min=0,
                        max=200,
                        minLength=0,
                        maxLength=3,
                        value=20,
                        debounce=False,
                        placeholder='Position Eligibility',


                    ),
                    ]),

                ], style={'margin-left': '3%'}),

                dbc.Col([
                    
                    html.H6("Select Teams:"),

                    # Select Teams
                    html.Div([ 
                    dcc.Dropdown(
                        id='Team_Checkbox',
                        multi=True,
                        value = [],
                        placeholder="Select Teams"
                        ),
                    ]),
                    

                    html.H6("Select Leagues: "),

                    # Select Leagues
                    html.Div([ 
                    dcc.Dropdown(
                        id='Lg_Checkbox',
                        multi=True,
                        value = [],
                        placeholder="Select Leagues"
                        ),
                    ]),
                

                    html.H6("Select Players: "),

                    # Select Players
                    html.Div([ 
                    dcc.Dropdown(
                        id='Player_Checkbox',
                        multi=True,
                        value = [],
                        placeholder="Select Players"
                        ),
                    ]),
                    
                    html.H6("Select Positions: "),

                    # Select Positions
                    html.Div([ 
                    dcc.Dropdown(
                        id='Positions_Checkbox',
                        multi=True,
                        options=[
                                {'label': 'Pitcher', 'value': 'G_p'},
                                {'label': 'Catcher', 'value': 'G_c'},
                                {'label': '1st Baseman', 'value': 'G_as_1B'},
                                {'label': '2nd Baseman', 'value': 'G_as_2B'},
                                {'label': '3rd Baseman', 'value': 'G_as_3B'},
                                {'label': 'ShortStop', 'value': 'G_as_SS'},
                                {'label': 'Left Fielder', 'value': 'G_as_LF'},
                                {'label': 'Center Fielder', 'value': 'G_as_CF'},
                                {'label': 'Right Fielder', 'value': 'G_as_RF'},
                                {'label': 'Outfielder', 'value': 'G_as_OF'},
                                {'label': 'Pitch Hitter', 'value': 'G_as_PH'},
                                {'label': 'Pitch Runner', 'value': 'G_as_pr'},
                                {'label': 'Designated Hitter', 'value': 'G_as_DH'}
                                ], 
                        value = [],
                        placeholder="Select Positions"
                        ),
                    ]),

                
                ], style={'margin-right': '3%'}),
                     
            
        ]),

        dbc.Row([
            # Pie Charts
            dbc.Col([

                # Pie Graphs
                html.Div([

                
                dbc.Spinner(children=[
                    dcc.Graph(id='sun-plot', figure={},style={'width': '130%', 'height': '130%'}),
                ], size="lg", color="primary", type="grow", fullscreen=False,),



                dbc.Spinner(children=[
                    dcc.Graph(id='year_histo', figure={},style={'width': '100%', 'height': '30vh'}),
                ], size="lg", color="primary", type="grow", fullscreen=False,),

                ]),
                
            ], width=3),

            # Main Scatter Plot
            dbc.Col([
                html.Div([
                # Center Large Scatter Plot - with spinner
                dbc.Spinner(children=[
                    
                    dcc.Graph(id="scatter-plot", figure={},style={'width': '100%', 'height': '60vh'})

                ], size="lg", color="primary", type="grow", fullscreen=False,),
                
                ]),
                
            ], width=6),

            # Violin Plots
            dbc.Col([
                html.Div([
                # Right Violin Plot

                dbc.Spinner(children=[
                    
                dcc.Graph(id="violin-plot", figure={},style={'width': '100%', 'height': '60vh'})

                
                ], size="lg", color="primary", type="grow", fullscreen=False,),
                
                ]),
                
            ], width=3),

        ]),

        dbc.Row([



            dbc.Col([
                # BY: Years

                dbc.Spinner(children=[

                dcc.Graph(id='Year_Pie_graph', figure={},style={'width': '100%', 'height': '100%'}),

                ], size="sm", color="primary", type="grow", fullscreen=False,),

            ], width=3),


            dbc.Col([
                # BY: League

                dbc.Spinner(children=[

                dcc.Graph(id='Lg_Pie_graph', figure={},style={'width': '100%', 'height': '100%'}),

                ], size="sm", color="primary", type="grow", fullscreen=False,),

            ], width=3),


            dbc.Col([
                # BY: Teams

                dbc.Spinner(children=[
                    
                dcc.Graph(id='Team_Pie_graph', figure={},style={'width': '100%', 'height': '100%'}),

                
                ], size="sm", color="primary", type="grow", fullscreen=False,),
            ], width=3),

            dbc.Col([
                # BY: Teams

                dbc.Spinner(children=[
                    
                dcc.Graph(id='team_histo', figure={},style={'width': '100%', 'height': '100%'}),

                
                ], size="sm", color="primary", type="grow", fullscreen=False,),
            ], width=3),

        ]),

    ]),




])

#---------------------------------------------------------------

# Update dropdown Team selection list based on years selected

@app.callback(
    Output("Team_Checkbox", "options"),
    [Input(component_id='Season',component_property='value')],
    [State("Team_Checkbox", "options")])

def dropdown_team_options(Season, options):

    dff = df

    # print(Season[0])
    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.yearID >= Smin) & (dff.yearID <= Smax)]

    teamList = dff.teamID.unique()
    # print(teamList)

    options = options=[
                    {'label': i, 'value': i}
                    for i in teamList]
    # print(options)
    return options

# Update dropdown Team selection list based on years selected

@app.callback(
    Output("Lg_Checkbox", "options"),
    [Input(component_id='Season',component_property='value')],
    [State("Lg_Checkbox", "options")])

def dropdown_lg_options(Season, options):

    dff = df

    # print(Season[0])
    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.yearID >= Smin) & (dff.yearID <= Smax)]

    lgList = dff.lgID.unique()

    options = options=[
                    {'label': i, 'value': i}
                    for i in lgList]
    # print(options)
    return options


@app.callback(
    Output("Player_Checkbox", "options"),
    [Input(component_id='Season',component_property='value'),
    Input(component_id='Lg_Checkbox',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value'),
    Input(component_id='input_pos_appear',component_property='value'),
    Input(component_id='Positions_Checkbox',component_property='value')],
    [State("Player_Checkbox", "options")])

def dropdown_player_options(Season, Lg_Checkbox, Team_Checkbox, input_pos_appear, Positions_Checkbox, options):

    dff = df

    # print(Season[0])
    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.yearID >= Smin) & (dff.yearID <= Smax)]

    if Team_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.teamID.apply(lambda x: any(item for item in Team_Checkbox if item in x))]


    if Lg_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.lgID.apply(lambda x: any(item for item in Lg_Checkbox if item in x))]

    # Player Positions
    if Positions_Checkbox == []:
        dff = dff
    else:
        PositionList = pd.DataFrame() # Clear List

        for i in Positions_Checkbox:
            print(Positions_Checkbox)
            print(i)
            print(input_pos_appear)
            PositionTemp = dff[ dff[i] >= input_pos_appear ]
            print(PositionTemp.head())
            print(PositionList.head())
            PositionList = PositionList.append(PositionTemp, ignore_index=True)
            print(PositionList.head())

        dff = PositionList



    playerList = dff.playerID.unique()
    # print(teamList)

    options = options=[
                    {'label': i, 'value': i}
                    for i in playerList]
    # print(options)
    return options



@app.callback(
    Output(component_id='Year_Pie_graph', component_property='figure'),
    Output(component_id='Lg_Pie_graph', component_property='figure'),
    Output(component_id='Team_Pie_graph', component_property='figure'),
    Output("scatter-plot", "figure"), 
    Output("violin-plot", "figure"), 
    Output("sun-plot", "figure"),
    Output("team_histo", "figure"), 
    Output("year_histo", "figure"), 
    [Input(component_id='dropdown_X', component_property='value'),
    Input(component_id='dropdown_Y',component_property='value'),
    Input(component_id='dropdown_Color',component_property='value'),
    Input(component_id='Season',component_property='value'),
    Input(component_id='Player_Checkbox',component_property='value'),
    Input(component_id='Lg_Checkbox',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value'),
    Input(component_id='input_pos_appear',component_property='value'),
    Input(component_id='Positions_Checkbox',component_property='value'),]
)


def update_scatter_plot(dropdown_X,dropdown_Y,dropdown_Color,Season,Player_Checkbox,Lg_Checkbox, Team_Checkbox,input_pos_appear,Positions_Checkbox):

    dff = df


    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.yearID >= Smin) & (dff.yearID <= Smax)]

    if Team_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.teamID.apply(lambda x: any(item for item in Team_Checkbox if item in x))]



    if Player_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.playerID.apply(lambda x: any(item for item in Player_Checkbox if item in x))]



    if Lg_Checkbox == []:
        dff = dff
    else:
        dff = dff[dff.lgID.apply(lambda x: any(item for item in Lg_Checkbox if item in x))]

    
    # Player Positions
    if Positions_Checkbox == []:
        dff = dff
    else:
        PositionList = pd.DataFrame() # Clear List

        for i in Positions_Checkbox:
            print(Positions_Checkbox)
            print(i)
            print(input_pos_appear)
            PositionTemp = dff[ dff[i] >= input_pos_appear ]
            print(PositionTemp.head())
            print(PositionList.head())
            PositionList = PositionList.append(PositionTemp, ignore_index=True)
            print(PositionList.head())

        dff = PositionList

    #Pie Graphs


    pieyear=px.pie(
            data_frame=dff,
            names=dff.yearID,
            hole=.3,
            )



    pielg=px.pie(
            data_frame=dff,
            names=dff.lgID,
            hole=.3,
            )



    pieteam=px.pie(
            data_frame=dff,
            names=dff.teamID,
            hole=.3,
            )



    scatter = px.scatter(
        dff, x=dropdown_X, y=dropdown_Y, 
        color=dropdown_Color, size=dropdown_Y, 
        hover_data=[dff.nameGiven, dff.playerID, dff.yearID, dff.name])




    violin = px.violin(
        dff, x=dropdown_Y, 
        color=dropdown_Color, orientation='h',
        hover_data=[dff.nameGiven, dff.playerID])


    sunteam=px.sunburst(dff,
            path=['lgID', 'teamID'],
            color='lgID'
            )

# 'G_p','G_c','G_as_1B','G_as_2B','G_as_3B','G_as_SS','G_as_LF','G_as_CF','G_as_RF','G_as_OF','G_as_PH','G_as_pr','G_as_DH'
    teamHisto=px.histogram(dff,
            x=dff.teamID
            )

    yearHisto=px.histogram(dff,
            x=dff.yearID,
            color=dff.yearID
            )


    return pieyear, pielg, pieteam, scatter, violin, sunteam, teamHisto, yearHisto





if __name__ == '__main__':
    app.run_server(debug=True)

#  Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

