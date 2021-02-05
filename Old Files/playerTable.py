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

        params = ['Weight', 'Torque', 'Width', 'Height', 'Efficiency', 'Power', 'Displacement']

        # Data Table
        dash_table.DataTable(
            id='table-editing-simple',
            columns=(
                [{'id': 'Model', 'name': 'Model'}] +
                [{'id': p, 'name': p} for p in params]
            ),
            data=[
                dict(Model=i, **{param: 0 for param in params})
                for i in range(1, 5)
            ],
            editable=True
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



@app.callback(
    Output('table-editing-simple-output', 'figure'),
    Input('table-editing-simple', 'data'),
    Input('table-editing-simple', 'columns'))
def display_output(rows, columns):
    dff=df
    dff = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    return {
        'data': [{
            'type': 'parcoords',
            'dimensions': [{
                'label': col['name'],
                'values': dff[col['id']]
            } for col in columns]
        }]
    }


if __name__ == '__main__':
    app.run_server(debug=True)

