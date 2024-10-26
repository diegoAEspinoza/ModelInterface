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
    path='/lotka_volterra_model',
    name='Edo-Ejemplo 2'
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
                html.H3('Initial Prey Population'),
                dcc.Input(type='number', value=40, id='prey_ini', step=1, min=0)  
            ]),
            html.Div([
                html.H3('Initial Predation Population'),
                dcc.Input(type='number', value=9, id='pred_ini', step=1, min=0) 
            ]),
            html.Div([
                html.H3('Time'),
                dcc.Input(type='number', value=5, id='time', step=1, min=0)  
            ]),
        ]),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Prey Growth Rate'),
                dcc.Input(type='number', value=0.1, id='prey_grow', step=0.01, min=0) 
            ]),
            html.Div([
                html.H3('Predation Rate'),
                dcc.Input(type='number', value=0.02, id='pred_rate', step=0.01, min=0) 
            ]),
        ]),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Predator Growth Rate'),
                dcc.Input(type='number', value=0.01, id='pred_grow', step=0.01, min=0)  
            ]),
            html.Div([
                html.H3('Predator Mortality Rate'),
                dcc.Input(type='number', value=0.1, id='pred_mort', step=0.01, min=0)  
            ]),
        ]),
    ]),

    html.Div(className='div_grafica', children=[
        html.H2('Lotka-Volterra Model', style={'text-align': 'center'}),
        
        html.Div(className='grafica', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_2'))
        ])
    ])
   
])

###################################################################################
#
# Callback
#
###################################################################################
@callback(
    Output('figura_2', 'figure'),
    Input('prey_ini', 'value'),
    Input('pred_ini', 'value'),
    Input('prey_grow', 'value'),
    Input('pred_rate', 'value'),
    Input('pred_grow', 'value'),
    Input('pred_mort', 'value'),
    Input('time', 'value'),
)
def grafica_edo1(x0=40, y0=9, alpha=0.1, beta=0.02, delta=0.01, gama=0.1, t=5):


    # Generar la gráfica con el modelo de Lotka-Volterra
    fig = lotka_volterra_model(x0, y0, alpha, beta, delta, gama, t)
    return fig
