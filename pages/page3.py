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
                html.H3('Initial Transmission Rate'),
                dcc.Input(type='number', value=0.0005, id='transmission_rate', step=0.0001, min=0) 
            ]),
            html.Div([
                html.H3('Initial Recovery Rate'),
                dcc.Input(type='number', value=0.01, id='recovery_rate', step=0.001, min=0) 
            ]),
            html.Div([
                html.H3('Time'),
                dcc.Input(type='number', value=100, id='time', step=1, min=0)  
            ]),
        ]),

        html.Div(className='div_flex', children=[
           dcc.Checklist(
                options=[{'label': 'Enable inputs', 'value': 'enable', 'className': 'checklist-label'}],
                value=[],  # No checkboxes selected by default
                id='checkbox'
            ),
            html.Div(className='div_flex', children=[
                html.Div([
                    html.H3('Change Time'),
                   dcc.Input(type='number', value=20, id='change_time', step=1, min=0, disabled=True),
                ]),
                html.Div([
                    html.H3('New Recovery Rate'),
                    dcc.Input(type='number', value=0.0001, id='new_recovery_rate', step=0.0021, min=0, disabled=True),
                ]),
                html.Div([
                    html.H3('New Transmission Rate'),
                    dcc.Input(type='number', value=0.0003, id='new_transmission_rate', step=0.0001, min=0, disabled=True)
                ]),
            ]),
        ]),
    ]),

    html.Div(className='div_grafica', children=[
        html.H2('SIR Model with Parameter Change', style={'text-align': 'center'}),
        
        html.Div(className='grafica', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_3'))
        ])
    ])
])


###################################################################################
#
# Callback principal
#
###################################################################################

@callback(
    Output('change_time', 'disabled'),
    Output('new_recovery_rate', 'disabled'),
    Output('new_transmission_rate', 'disabled'),
    Output('figura_3', 'figure'),
    Input('checkbox', 'value'),
    Input('initial_population', 'value'),
    Input('infected_population', 'value'),
    Input('recovery_population', 'value'),
    Input('transmission_rate', 'value'),
    Input('recovery_rate', 'value'),
    Input('time', 'value'),
    Input('change_time', 'value'),
    Input('new_recovery_rate', 'value'),
    Input('new_transmission_rate', 'value'),
)

def grafic_SIR_model(checkbox_value, N, I, R, beta, gamma, t, change_time, new_gamma, new_beta):
    
    # Activar/desactivar según si el checkbox está marcado
    enabled = 'enable' in checkbox_value

    if not enabled:
       change_time = t
       new_beta = beta
       new_gamma = gamma

    # Ensure initial conditions
    S = N - I - R
    
    # Generate the SIR model graph
    fig = model_SIR([S, I, R], beta, gamma, t, change_time, new_beta, new_gamma)
    return not enabled, not enabled, not enabled, fig

