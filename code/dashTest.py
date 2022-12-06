import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('First application', style={'textAlign': 'center', 'color': 'mediumturquoise'}),
    html.Div(
        html.P("First Sentence",style={'textAlign': 'center'}),
        style = {'display': 'inline-block','width': '50%'}
    ),
    html.Table([
        html.Thead(
        html.Tr([
            html.Th('header_1'),
            html.Th('header_2')
        ], style={'color': "darkOrange"})
        ),
        html.Tbody(
        html.Tr([
            html.Td('my_column_1'),
            html.Td('my_column_2')
        ])
        )
    ], style = {'display': 'inline-block','width': '50%'})
], style = {'backgroundColor': 'beige'})

app.layout = dcc.Dropdown(
    id = 'dropdown',
    options=[
    {'label':'life expendancy', 'value': 'lifeExp'},
    {'label':'population', 'value': 'pop'}
    ],
    value = 'pop', # Default value displayed in the menus.
    multi = False # Specify whether it is a multiple choice dropdown menu or not.
)
app.layout = dcc.Slider(
  id = 'Slider_1',
  min = 0,
  max = 10,
  marks = {i: str(i) for i in range(10)},
  value = 5
)




app.layout = html.Div([
    dcc.Input(id='input', value='input', type='text'),
    html.Div(id='output')
])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    return input_data

if __name__ == '__main__':
    app.run_server(debug = True, host = '0.0.0.0', port = 5000)