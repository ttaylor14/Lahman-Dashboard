import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('Lahman_Database/core/Batting.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['yearID'].min(),
        max=df['yearID'].max(),
        value=df['yearID'].min(),
        marks={str(year): str(year) for year in df['yearID'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.yearID == selected_year]
    traces = []
    for i in filtered_df.teamID.unique():
        df_by_teamID = filtered_df[filtered_df['teamID'] == i]
        traces.append(go.Scatter(
            x=df_by_teamID['AB'],
            y=df_by_teamID['HR'],
            text=df_by_teamID['teamID'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Home Runs', 'range': [0, 100]},
            margin={'l': 0, 'b': 0, 't': 1, 'r': 1},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
