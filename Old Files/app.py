import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



# Step 1: Launch the Application
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Step 2: Import the Data
dfPeo = pd.read_csv('Lahman_Database/core/People.csv')

dfTMFran = pd.read_csv('Lahman_Database/core/TeamsFranchises.csv')
dfCPlay = pd.read_csv('Lahman_Database/core/CollegePlaying.csv')


df = pd.read_csv('Lahman_Database/core/Batting.csv')
dfBatPost = pd.read_csv('Lahman_Database/core/BattingPost.csv')

dfPit = pd.read_csv('Lahman_Database/core/Pitching.csv')
dfPitPost = pd.read_csv('Lahman_Database/core/Pitching.csv')

dfFie = pd.read_csv('Lahman_Database/core/Fielding.csv')
dfFiePost = pd.read_csv('Lahman_Database/core/FieldingPost.csv')

dfApp = pd.read_csv('Lahman_Database/core/Appearances.csv')



available_indicators = df['teamID'].unique()
available_Col = df.columns.values



# Step 3: Create Dash Layout
app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Checklist(
                id='Check',
                options=[
                {'label': 'People', 'value': 'People'},
                {'label': 'Batting', 'value': 'Batting'},
                {'label': 'Pitching', 'value': 'Pitching'},
                {'label': 'Fielding', 'value': 'Fielding'},
                ],
                value=['Batting']
            ),

            #Team ID
            dcc.Dropdown(
                id='Team',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='RC1'
            ),

            # X Axis Stat
            dcc.Dropdown(
                id='xaxis_column_name',
                options=[{'label': i, 'value': i} for i in available_Col],
                value='AB'
            ),

            # Y Axis Stat
            dcc.Dropdown(
                id='yaxis_column_name',
                options=[{'label': i, 'value': i} for i in available_Col],
                value='HR'
            ),
        ],


        style={'width': '48%', 'display': 'inline-block'}),

    ]),



    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        id='year--slider',
        min=df['yearID'].min(),
        max=df['yearID'].max(),
        value=df['yearID'].max(),
        marks={str(year): str(year) for year in df['yearID'].unique()},
        step=None
    )
])





# Step 4: Add Callback Function
@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis_column_name', 'value'),
     Input('yaxis_column_name', 'value'),
     Input('xaxis_column_type', 'value'),
     Input('yaxis_column_type', 'value'),
     Input('year--slider', 'value')])


def update_graph(xaxis_column_name, yaxis_column_name,
                 year_value):
    dff = df[df['yearID'] == year_value]




    return {
        'data': [go.Scatter(
            x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            text=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],

    }




# Step 5: Add the Server Clause
if __name__ == '__main__':
    app.run_server(debug=True)
