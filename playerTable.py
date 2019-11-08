import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('Lahman_Database/core/Batting.csv')

df = df[df['yearID'] == 2018]

app = dash.Dash(__name__)

app.layout = html.Div([

        # First Check Box Selection
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

        # Graph Box-Plot
        dcc.Graph(
            figure={
            'data': [
                go.Scatter(
                x= df['HR'],
                y= df['SO'],
                mode = 'markers'
                )]
            },
            id='box-plot-1'

        ),


        # Data Table
        dash_table.DataTable(
            id='datatable',
            columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns],
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            data=df.to_dict('records'),
            style_table={
                'maxHeight': '300px',
                'overflowY': 'scroll',
                'overflowX': 'scroll',
                'border': 'thin lightgrey solid'
            }
        )

])



if __name__ == '__main__':
    app.run_server(debug=True)

