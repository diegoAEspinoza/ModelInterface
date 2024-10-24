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
    path='/SIR',
    name='Edo-Ejemplo 3'
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
                dcc.Input(type='number', value=1500, id='initial_population', step=1, min=0)  
            ]),
            html.Div([
                html.H3('Initial Infected Population'),
                dcc.Input(type='number', value=1, id='infected_population', step=1, min=0)  
            ]),
            html.Div([
                html.H3('Initial Recovery Population'),
                dcc.Input(type='number', value=0, id='recovery_population', step=1, min=0) 
            ]),
        ]),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Transmission Rate'),
                dcc.Input(type='number', value=0.0005, id='transmission_rate', step=0.0001, min=0) 
            ]),
            html.Div([
                html.H3('Recovery Rate'),
                dcc.Input(type='number', value=0.01, id='recovery_rate', step=0.001, min=0) 
            ]),
        ]),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Time'),
                dcc.Input(type='number', value=100, id='time', step=1, min=0)  
            ]),
        ]),
    ]),

    html.Div(className='div_grafica', children=[
        html.H2('GRAPH OF THE FIRST ORDER ODE', style={'text-align': 'center'}),
        
        html.Div(className='grafica', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_3'))
        ])
    ])
])

###################################################################################
#
# Callback
#
###################################################################################

@callback(
    Output('figura_3', 'figure'),
    Input('initial_population', 'value'),
    Input('infected_population', 'value'),
    Input('recovery_population', 'value'),
    Input('transmission_rate', 'value'),
    Input('recovery_rate', 'value'),
    Input('time', 'value'),
)

def grafic_SIR_model(N, I, R, beta, gamma, t):
    S = N-I-R
    # Generar la gráfica con el modelo de Lotka-Volterra
    fig = model_SIR([S, I, R], beta, gamma, t)
    return fig
