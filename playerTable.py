import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('Lahman_Database/core/Batting.csv')

#df = df[df['yearID'] == 2018]

# Clean Years
df = df[df['yearID'] >= 2000]

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

        dcc.Dropdown(
            id='XAxis',
            options=[{'label': i, 'value': i} for i in df.columns.values],
            value='HR'
        ),

        dcc.Dropdown(
            id='YAxis',
            options=[{'label': i, 'value': i} for i in df.columns.values],
            value='AB'
        ),

        dcc.RangeSlider(
            id='year_slider',
            min=2000,
            max=2018,
            marks={
                2000: {'label': '2000', 'style': {'color': '#f50'}},
                2005: {'label': '2005'},
                2010: {'label': '2010'},
                2015: {'label': '2015'},
                2018: {'label': '2018', 'style': {'color': '#f50'}}
            },
            value=[2017, 2018]
        ),

        dcc.Graph(id='Center_Graph'),


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
        ),

    html.Div(id='output-container-range-slider')
])

# Callback Function
@app.callback(
    Output('Center_Graph', 'figure'),
    [Input('XAxis', 'value'),
     Input('YAxis', 'value'),
     Input('year_slider', 'value')])


def update_graph(XAxis, YAxis, year_value):
    dff = df[df['yearID'] == year_value]




    return {
        'data': [go.Scatter(
            x=dff[dff['Indicator Name'] == XAxis]['Value'],
            y=dff[dff['Indicator Name'] == YAxis]['Value'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': XAxis
            },
            yaxis={
                'title': YAxis
            },
            hovermode='closest'
        )
    }



if __name__ == '__main__':
    app.run_server(debug=True)

