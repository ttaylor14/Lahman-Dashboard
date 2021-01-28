#Lahman Dashboard

# This dashboard is a simple Batting Statistical investigation




import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px #(need to pip install plotly==4.4.1)

df = pd.read_csv("baseballdatabank-master\core\Batting.csv")

min_year = df.yearID.min()
max_year = df.yearID.max()

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__)

#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Label(['Baseball Visualization']),



        dcc.RangeSlider(
            id='Season',
            marks={
                2000: {'label': '2000', 'style': {'color': '#77b0b1'}},
                2010: {'label': '2010'},
                2015: {'label': '2015'},
                2020: {'label': '2020', 'style': {'color': '#f50'}}
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
            verticalHeight = 900,
            className = 'None',
            # tooltip = {"always visible":False, "placement":'bottom'}

        ),  

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
                    {'label': 'GIDP', 'value': 'GIDP'}
            ],
            value='G',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
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
                    {'label': 'GIDP', 'value': 'GIDP'}
            ],
            value='H',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),

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
                    {'label': 'GIDP', 'value': 'GIDP'}
            ],
            value='teamID',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),

        dcc.Checklist(
            id='Team_Checkbox',
            options=[
                {'label': 'ARI', 'value': 'ARI'},
                {'label': 'ATL', 'value': 'ATL'},
                {'label': 'BAL', 'value': 'BAL'},
                {'label': 'BOS', 'value': 'BOS'},
                {'label': 'CHC', 'value': 'CHN'},
                {'label': 'CWS', 'value': 'CHA'},
                {'label': 'CIN', 'value': 'CIN'},
                {'label': 'CLE', 'value': 'CLE'},
                {'label': 'COL', 'value': 'COL'},
                {'label': 'DET', 'value': 'DET'},
                {'label': 'HOU', 'value': 'HOU'},
                {'label': 'KC', 'value': 'KCA'},
                {'label': 'LAA', 'value': 'LAA'},
                {'label': 'LAD', 'value': 'LAN'},
                {'label': 'MIA', 'value': 'MIA'},
                {'label': 'MIL', 'value': 'MIL'},
                {'label': 'MIN', 'value': 'MIN'},
                {'label': 'NYM', 'value': 'NYN'},
                {'label': 'NYY', 'value': 'NYA'},
                {'label': 'OAK', 'value': 'OAK'},
                {'label': 'PHI', 'value': 'PHI'},
                {'label': 'PIT', 'value': 'PIT'},
                {'label': 'SD', 'value': 'SDN'},
                {'label': 'SEA', 'value': 'SEA'},
                {'label': 'SF', 'value': 'SFN'},
                {'label': 'STL', 'value': 'SLN'},
                {'label': 'TB', 'value': 'TBA'},
                {'label': 'TEX', 'value': 'TEX'},
                {'label': 'TOR', 'value': 'TOR'},
                {'label': 'WSH', 'value': 'WAS'}
            ],

            value=['SLN', 'PIT', 'CHN', 'MIL', 'CIN']


        ) 


        ]),

    html.Div([
        dcc.Graph(id='Team_Pie_graph'),
        dcc.Graph(id="scatter-plot")
    ]),


])

#---------------------------------------------------------------


# PieGraph
@app.callback(
    Output(component_id='Team_Pie_graph', component_property='figure'),
    [Input(component_id='dropdown_X', component_property='value'),
    Input(component_id='Season',component_property='value'),
    Input(component_id='Team_Checkbox',component_property='value')]
)

def update_graph(my_dropdown,Season,Team_Checkbox):

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






if __name__ == '__main__':
    app.run_server(debug=True)

#  Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

