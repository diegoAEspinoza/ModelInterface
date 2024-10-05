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
    path='/',
    name='Edo-1'
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
                html.H3('Initial Population'),
                dcc.Input(type='number', value=10, id='pob_ini')
            ]),
        ]),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Initial Time'),
                dcc.Input(type='number', value=0, id='time_ini')
            ]),
            html.Div([
                html.H3('Final Time'),
                dcc.Input(type='number', value=60, id='time_fin')
            ]),
        ]),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Growth Rate'),
                dcc.Input(max=5, type='number', value=0.15, id='r'),
            ]),
            html.Div([
                html.H3('Carrying Capacity'),
                dcc.Input(type='number', value=150, id='K'),
            ]),
        ]),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Vector Field'),
                dcc.Input(type='number', value=15, id='mallado'),
            ]),
            html.Div([
                html.H3('Vector Size'),
                dcc.Input(type='number', value=1, id='size_vec')
            ]),
        ]),

        html.Div(className='div_button', children=[
            html.Div([
                html.Button('Vector Field', id='toggle-button', n_clicks=0, className='toggle-button')
            ]),
        ]),

    ]),

    html.Div(className='div_grafica', children=[
        html.H2('GRAPH OF THE FIRST ORDER ODE', style={'text-align': 'center'}),
        
        html.Div(className='grafica', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_1'))
        ])
    ])
])

###################################################################################
#
# Callback
#
###################################################################################

@callback(
    Output('figura_1', 'figure'),
    Input('pob_ini', 'value'),
    Input('time_ini', 'value'),
    Input('time_fin', 'value'),
    Input('r', 'value'),
    Input('K', 'value'),
    Input('mallado', 'value'),
    Input('size_vec', 'value'),
    Input('toggle-button', 'n_clicks')  # Input for the button
)

def grafica_edo1(P0, t_i, t_f, r, k, mallado, size_vec, n_clicks):
    # Determine whether to show the vector field based on button clicks
    show_vector_field = (n_clicks % 2 == 1)  # Odd clicks mean show the field

    fig = ecuacion_logistica(k, P0, r, t_i, t_f, mallado, size_vec, show_vector_field)
    return fig
