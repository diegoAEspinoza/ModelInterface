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
    html.Div(className='content', children=[
        
        html.Div(className='div_parametros', children=[
            html.H2('PARAMETERS', style={'text-align': 'center'}),
            html.Div(className='div_flex', children=[
                html.Div([
                    html.H3('Diferencial X'),
                    dcc.Input(type='text', id='dx', value='x*(5-y)')  
                ]),

                html.Div([
                    html.H3('Diferencial Y'),
                    dcc.Input(type='text', id='dy', value='y*(5-x)'), 
                ]),
            ]),
        
            html.Div(className='div_flex', children=[
                html.Div([
                    html.H3('Lower Limit'),
                    dcc.Input(type='number', value=-2, id='lower_limit', step=1)  
                ]),

                html.Div([
                    html.H3('Upper Limit'),
                    dcc.Input(type='number', value=10, id='upper_limit', step=1)  
                ]),
            ]),

            html.Div(className='div_flex', children=[
                html.Div([
                    html.H3('Number of points'),
                    dcc.Input(type='number', value=25, id='point_number', step=1, min=0)  
                ]),

                html.Div([
                    html.H3('Vector Size'),
                    dcc.Input(type='number', value=0.2, id='scale_factor', step=0.1, min=0)  
                ]),
            ]),
        ]),

        html.Div(className='div_resultados', children=[
            html.H2('RESULTS', style={'text-align': 'center'}),
            html.Div(id='text', children=[])
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
    Output('text', 'children'),
    Input('dx', 'value'),
    Input('dy', 'value'),
    Input('lower_limit', 'value'),
    Input('upper_limit', 'value'),
    Input('point_number', 'value'),
    Input('scale_factor', 'value'),
)
def process_inputs(dx, dy,a, b, n, scale_factor):
    fig, text = points_ODE(dx, dy, a, b, n, scale_factor)
    formatted_text = "       ".join(text)

    return fig, formatted_text