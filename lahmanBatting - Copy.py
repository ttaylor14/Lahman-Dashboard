#Lahman Dashboard

# This dashboard is a simple Batting Statistical investigation




import pandas as pd

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px #(need to pip install plotly==4.4.1)


# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# Allows Heroku to connect to servers:
server = app.server




df = pd.read_csv("baseballdatabank-master/core/Batting.csv")


min_year = df.yearID.min()
max_year = df.yearID.max()



#---------------------------------------------------------------
app.layout = html.Div([

    html.Div([

        dbc.Row([
            dbc.Col([

                # Page Title

                html.H3("Baseball Visualizations: Batting")
                
            ]),

        ]),


        dbc.Row([

            dbc.Col( [

                # Select Year Ranges
                html.Div([
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
                ],
                style={"height": "50%", "width": "80%"}),
                
            ]),
        
        # width={'size': 2, "offset": 1, 'order': 0}
        ]),

        dbc.Row([
            
                dbc.Col([

                    # Select 'X' Axis
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_X',
                        
                        options=[
                                {'label': 'Season', 'value': 'yearID'},
                                {'label': 'Team', 'value': 'teamID'},
                                {'label': 'League', 'value': 'lgID'},                
                                {'label': 'G', 'value': 'G'},
                                {'label': 'AB', 'value': 'AB'},
                                {'label': 'R', 'value': 'R'},
                                {'label': 'H', 'value': 'H'},
                                {'label': '2B', 'value': '2B'},
                                {'label': '3B', 'value': '3B'},
                                {'label': 'HR', 'value': 'HR'},
                                {'label': 'RBI', 'value': 'RBI'},
                                {'label': 'SB', 'value': 'SB'},
                                {'label': 'CS', 'value': 'CS'},
                                {'label': 'BB', 'value': 'BB'},
                                {'label': 'SO', 'value': 'SO'},
                                {'label': 'IBB', 'value': 'IBB'},
                                {'label': 'HBP', 'value': 'HBP'},
                                {'label': 'SH', 'value': 'SH'},
                                {'label': 'SF', 'value': 'SF'},
                                {'label': 'GIDP', 'value': 'GIDP'}],
                        
                        value='G',
                        multi=False,
                        clearable=False,
                        #style={"width": "50%"}

                    ),
                    ]),

                    # Select 'Y' Axis
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_Y',
                        
                        options=[
                                {'label': 'Season', 'value': 'yearID'},
                                {'label': 'Team', 'value': 'teamID'},
                                {'label': 'League', 'value': 'lgID'},                
                                {'label': 'G', 'value': 'G'},
                                {'label': 'AB', 'value': 'AB'},
                                {'label': 'R', 'value': 'R'},
                                {'label': 'H', 'value': 'H'},
                                {'label': '2B', 'value': '2B'},
                                {'label': '3B', 'value': '3B'},
                                {'label': 'HR', 'value': 'HR'},
                                {'label': 'RBI', 'value': 'RBI'},
                                {'label': 'SB', 'value': 'SB'},
                                {'label': 'CS', 'value': 'CS'},
                                {'label': 'BB', 'value': 'BB'},
                                {'label': 'SO', 'value': 'SO'},
                                {'label': 'IBB', 'value': 'IBB'},
                                {'label': 'HBP', 'value': 'HBP'},
                                {'label': 'SH', 'value': 'SH'},
                                {'label': 'SF', 'value': 'SF'},
                                {'label': 'GIDP', 'value': 'GIDP'}],
                        
                        value='H',
                        multi=False,
                        clearable=False,
                        #style={"width": "50%"}


                    ),
                    ]),

                    # Select Color Grouping
                    html.Div([
                    dcc.Dropdown(
                        id='dropdown_Color',
                        
                        options=[
                                {'label': 'Season', 'value': 'yearID'},
                                {'label': 'Team', 'value': 'teamID'},
                                {'label': 'League', 'value': 'lgID'},                
                                {'label': 'G', 'value': 'G'},
                                {'label': 'AB', 'value': 'AB'},
                                {'label': 'R', 'value': 'R'},
                                {'label': 'H', 'value': 'H'},
                                {'label': '2B', 'value': '2B'},
                                {'label': '3B', 'value': '3B'},
                                {'label': 'HR', 'value': 'HR'},
                                {'label': 'RBI', 'value': 'RBI'},
                                {'label': 'SB', 'value': 'SB'},
                                {'label': 'CS', 'value': 'CS'},
                                {'label': 'BB', 'value': 'BB'},
                                {'label': 'SO', 'value': 'SO'},
                                {'label': 'IBB', 'value': 'IBB'},
                                {'label': 'HBP', 'value': 'HBP'},
                                {'label': 'SH', 'value': 'SH'},
                                {'label': 'SF', 'value': 'SF'},
                                {'label': 'GIDP', 'value': 'GIDP'}],
                                
                        value='teamID',
                        multi=False,
                        clearable=False,
                        #style={"width": "50%"}

                    ),
                    ]),

                # width = {'size': 1, "offset": 1, 'order': 1}
                ]),

                dbc.Col([

                    # Select Teams
                    html.Div([ 
                    dcc.Dropdown(
                        id='Team_Checkbox',
                        options=[
                            {'label': i, 'value': i}
                            for i in df['teamID'].unique()
                            ],
                        multi=True,
                        value=['SLN', 'PIT', 'CHN', 'MIL', 'CIN']


                        ),
                    ]),
                    
                
                    # width = {'size': 2, "offset": 1, 'order': 2}
                ]),
                     
            
        ]),


        dbc.Row([
            dbc.Col([

                # Pie Graphs
                html.Div([
                # BY: Years
                dcc.Graph(id='Year_Pie_graph', figure={}),
                ]),
                
                html.Div([
                # BY: League
                dcc.Graph(id='Lg_Pie_graph', figure={}),
                ]),
                
                html.Div([
                # BY: Teams
                dcc.Graph(id='Team_Pie_graph', figure={}),
                ]),
                
            ]),

            dbc.Col([
                html.Div([
                # Center Large Scatter Plot
                dcc.Graph(id="scatter-plot", figure={})
                ]),
                
            ]),

            dbc.Col([
                html.Div([
                # Right Violin Plot
                dcc.Graph(id="violin-plot", figure={})
                ]),
                
            ]),

        ]),



    ]),




])

#---------------------------------------------------------------


# PieGraph
@app.callback(
    Output(component_id='Year_Pie_graph', component_property='figure'),
    [Input(component_id='dropdown_X', component_property='value'),
    Input(component_id='Season',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value')]
)

def update_Year_Pie(my_dropdown,Season,Team_Checkbox):

    dff = df

    print(Season[0])
    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.yearID >= Smin) & (dff.yearID <= Smax)]

    dff = dff[dff.teamID.apply(lambda x: any(item for item in Team_Checkbox if item in x))]

    piechart=px.pie(
            data_frame=dff,
            names=dff.yearID,
            hole=.3,
            )

    return (piechart)

@app.callback(
    Output(component_id='Lg_Pie_graph', component_property='figure'),
    [Input(component_id='dropdown_X', component_property='value'),
    Input(component_id='Season',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value')]
)

def update_Lg_Pie(my_dropdown,Season,Team_Checkbox):

    dff = df

    print(Season[0])
    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.yearID >= Smin) & (dff.yearID <= Smax)]

    dff = dff[dff.teamID.apply(lambda x: any(item for item in Team_Checkbox if item in x))]

    piechart=px.pie(
            data_frame=dff,
            names=dff.lgID,
            hole=.3,
            )

    return (piechart)

@app.callback(
    Output(component_id='Team_Pie_graph', component_property='figure'),
    [Input(component_id='dropdown_X', component_property='value'),
    Input(component_id='Season',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value')]
)

def update_Team_Pie(my_dropdown,Season,Team_Checkbox):

    dff = df

    print(Season[0])
    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.yearID >= Smin) & (dff.yearID <= Smax)]

    dff = dff[dff.teamID.apply(lambda x: any(item for item in Team_Checkbox if item in x))]

    piechart=px.pie(
            data_frame=dff,
            names=dff.teamID,
            hole=.3,
            )

    return (piechart)




@app.callback(
    Output("scatter-plot", "figure"), 
    [Input(component_id='dropdown_X', component_property='value'),
    Input(component_id='dropdown_Y',component_property='value'),
    Input(component_id='dropdown_Color',component_property='value'),
    Input(component_id='Season',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value')]
)


def update_scatter_plot(dropdown_X,dropdown_Y,dropdown_Color,Season,Team_Checkbox):

    dff = df


    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.yearID >= Smin) & (dff.yearID <= Smax)]

    dff = dff[dff.teamID.apply(lambda x: any(item for item in Team_Checkbox if item in x))]

    fig = px.scatter(
        dff, x=dropdown_X, y=dropdown_Y, 
        color=dropdown_Color, size=dropdown_Y, 
        hover_data=[dff.playerID])
    return fig

@app.callback(
    Output("violin-plot", "figure"), 
    [Input(component_id='dropdown_X', component_property='value'),
    Input(component_id='dropdown_Y',component_property='value'),
    Input(component_id='dropdown_Color',component_property='value'),
    Input(component_id='Season',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value')]
)

def update_violin_plot(dropdown_X,dropdown_Y,dropdown_Color,Season,Team_Checkbox):

    dff = df


    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.yearID >= Smin) & (dff.yearID <= Smax)]

    dff = dff[dff.teamID.apply(lambda x: any(item for item in Team_Checkbox if item in x))]

    fig = px.violin(
        dff, x=dropdown_Y, 
        color=dropdown_Color, orientation='h',
        hover_data=[dff.playerID])
    return fig





if __name__ == '__main__':
    app.run_server(debug=True)

#  Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

