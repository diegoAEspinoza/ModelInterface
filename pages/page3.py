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
        ]),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Time'),
                dcc.Input(type='number', value=100, id='time', step=1, min=0)  
            ]),
        ]),

        html.Div(className='div_flex', children=[
            html.Div([
                dcc.Checklist(
                    options=[{'label': 'Change Time (t_change)', 'value': 't_change'}],
                    value=[],  # No checkboxes selected by default
                    id='change_time_checkbox'
                ),
                html.Div([
                dcc.Input(type='number', value=20, id='change_time', step=1, min=0, disabled=True)  
                ])
            ]),

            html.Div([
                dcc.Checklist(
                    options=[{'label': 'New Transmission Rate', 'value': 'new_beta'}],
                    value=[],  # No checkboxes selected by default
                    id='new_transmission_checkbox'
                ),
                dcc.Input(type='number', value=0.0003, id='new_transmission_rate', step=0.0001, min=0, disabled=True)  
            ]),
            html.Div([
                dcc.Checklist(
                    options=[{'label': 'New Recovery Rate', 'value': 'new_gamma'}],
                    value=[],  # No checkboxes selected by default
                    id='new_recovery_checkbox', 
                ),
                dcc.Input(type='number', value=0.0001, id='new_recovery_rate', step=0.001, min=0, disabled=True)  
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
# Callback para habilitar/deshabilitar los inputs
#
###################################################################################

@callback(
    Output('change_time', 'disabled'),
    Output('new_transmission_rate', 'disabled'),
    Output('new_recovery_rate', 'disabled'),
    Input('change_time_checkbox', 'value'),
    Input('new_transmission_checkbox', 'value'),
    Input('new_recovery_checkbox', 'value'),
)
def toggle_inputs(change_time_enabled, new_beta_enabled, new_gamma_enabled):
    # Habilitar o deshabilitar los inputs basados en los checkboxes
    change_time_disabled = 'change_time' not in change_time_enabled
    new_beta_disabled = 'new_beta' not in new_beta_enabled
    new_gamma_disabled = 'new_gamma' not in new_gamma_enabled

    return change_time_disabled, new_beta_disabled, new_gamma_disabled

###################################################################################
#
# Callback principal
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
    Input('change_time', 'value'),
    Input('new_transmission_rate', 'value'),
    Input('new_recovery_rate', 'value'),
)
def grafic_SIR_model(N, I, R, beta, gamma, t, change_time, new_beta, new_gamma):
    S = N - I - R
    
    print("Hola")
    print(change_time)
    print(new_beta)
    print(new_gamma)

    # Set defaults if None
    if change_time is None or change_time == '':
        change_time = t  # or a sensible default like 100
    if new_beta is None or new_beta == '':
        new_beta = beta  # Default to original beta
    if new_gamma is None or new_gamma == '':
        new_gamma = gamma  # Default to original gamma
    
    print("Adios")
    print(change_time)
    print(new_beta)
    print(new_gamma)

    # Generate the graph with the SIR model
    fig = model_SIR([S, I, R], beta, gamma, t, change_time, new_beta, new_gamma)
    return fig
