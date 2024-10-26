###################################################################################
#
# Librerías
#
###################################################################################
import dash
from dash import dcc, html, Input, Output, callback
from utils import *

dash.register_page(
    __name__,
    path='/criticalPoint',
    name='criticalPoint'
)

###################################################################################
#
# Layout HTML
#
###################################################################################

layout = html.Div(className='Pages', children=[
    html.Div(className='div_parametros', children=[
        html.H2('PARAMETERS', style={'text-align': 'center'}),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Diferencial X'),
                dcc.Input(type='text', id='dx', value='x*(5-y)')  
            ], style={'padding': '10px'}),
            
            html.Div([
                html.H3('Diferencial Y'),
                dcc.Input(type='text', id='dy', value='y*(5-x)')  
            ], style={'padding': '10px'}),
        ]),
    ]),

    html.Div(className='div_grafica', children=[
        html.H2('GRAPH OF THE FIRST ORDER ODE', style={'text-align': 'center'}),
        
        html.Div(className='grafica', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_4'))
        ])
    ])
])


###################################################################################
#
# Callback principal
#
###################################################################################

@callback(
    Output('figura_4', 'figure'),
    Input('dx', 'value'),
    Input('dy', 'value'),

)
def process_inputs(dx, dy):
    print(f"Received dx: {dx}, dy: {dy}")
    fig = points_ODE(dx, dy, -2.5, 10, 25)
    return fig