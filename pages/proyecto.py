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
    path='/proyect',
    name='proyect'
)

###################################################################################
#
# Layout HTML
#
###################################################################################
layout = html.Div(className='', children=[

    # Sección de imágenes
    html.Div(
        className='div_imagen', 
        style={
            'display': 'flex',  # Usar Flexbox para centrar
            'justify-content': 'center',  # Centrar horizontalmente
            'align-items': 'center',  # Centrar verticalmente
            'gap': '20px'  # Espacio entre las imágenes
        },
        children=[
            # Imagen 1
            html.Img(
                src='/assets/model.png', 
                alt='Imagen de modelo', 
                style={'width': '45%', 'height': 'auto'}  # Ajustar tamaño
            ),
            # Imagen 2
            html.Img(
                src='/assets/model1.png', 
                alt='Imagen de modelo', 
                style={'width': '45%', 'height': 'auto'}  # Ajustar tamaño
            )
        ]
    ),

    # Sección de parámetros
    html.Div(className='div_parametros', children=[

        html.H2('PARAMETERS', style={'text-align': 'center'}),

        # Parámetros generales
        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Población inicial'),
                dcc.Input(type='number', value=1000, id='pob_ini')
            ]),
            html.Div([
                html.H3('Expuestos'),
                dcc.Input(type='number', value=0, id='pob_exp')
            ]),
            html.Div([
                html.H3('Infectados'),
                dcc.Input(type='number', value=1, id='pob_inf')
            ]),
            html.Div([
                html.H3('Asintomáticos'),
                dcc.Input(type='number', value=1, id='pob_asin')
            ]),
            html.Div([
                html.H3('Recuperados'),
                dcc.Input(type='number', value=0, id='pob_rec')
            ]),
            html.Div([
                html.H3('Tiempo'),
                dcc.Input(type='number', value=10, id='tiempo')
            ]),
        ]),

        # Parámetros adicionales
        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Lambda'),
                dcc.Input(type='number', value=0.0613, id='Lambda')
            ]),
            html.Div([
                html.H3('mu'),
                dcc.Input(type='number', value=0.0688, id='mu')
            ]),
            html.Div([
                html.H3('lambda'),
                dcc.Input(type='number', value=0.35, id='lambda1')
            ]),
            html.Div([
                html.H3('xi1'),
                dcc.Input(type='number', value=0.08, id='xi1')
            ]),
            html.Div([
                html.H3('xi2'),
                dcc.Input(type='number', value=0.07, id='xi2')
            ]),
            html.Div([
                html.H3('beta'),
                dcc.Input(type='number', value=0.01, id='beta')
            ]),
        ]),
        html.Div(className='div_flex', children=[
             html.Div([
                html.H3('rho1'),
                dcc.Input(type='number', value=0.7, id='rho1')
            ]),
            html.Div([
                html.H3('rho2'),
                dcc.Input(type='number', value=0.05, id='rho2')
            ]),
            html.Div([
                html.H3('alpha'),
                dcc.Input(type='number', value=0.75, id='alpha')
            ]),
            html.Div([
                html.H3('delta'),
                dcc.Input(type='number', value=0.04, id='delta')
            ]),
            html.Div([
                html.H3('psi'),
                dcc.Input(type='number', value=0.1, id='psi')
            ]),
            html.Div([
                html.H3('eta'),
                dcc.Input(type='number', value=0.001, id='eta')
            ]),
        ])
    ]),

    # Sección de gráfica
   html.Div(className='div_grafica', children=[
    html.H2('GRAPH OF THE FIRST ORDER ODE', style={'text-align': 'center'}),
    
    html.Div(className='grafica', children=[
        # El gráfico 'COMPLETO' estará solo en su propia fila
        html.Div([
            dcc.Loading(type='default', children=dcc.Graph(id='COMPLETO')),
        ], className='grafica_completo'),
        
        # Los siguientes gráficos compartirán fila de 2 en 2
        html.Div([
            dcc.Loading(type='default', children=dcc.Graph(id='suceptibles')),
            dcc.Loading(type='default', children=dcc.Graph(id='expuesto')),
        ], className='grafica_par'),
        
        html.Div([
            dcc.Loading(type='default', children=dcc.Graph(id='infectado')),
            dcc.Loading(type='default', children=dcc.Graph(id='asintomatico')),
        ], className='grafica_par'),
        
        # El gráfico 'recuperado' estará solo en su propia fila
        html.Div([
            dcc.Loading(type='default', children=dcc.Graph(id='recuperado')),
        ], className='grafica_recuperado'),
    ])
])
])


###################################################################################
#
# Callback principal
#
###################################################################################
@callback(
    Output('COMPLETO', 'figure'),
    Output('suceptibles', 'figure'),
    Output('expuesto', 'figure'),
    Output('infectado', 'figure'),
    Output('asintomatico', 'figure'),
    Output('recuperado', 'figure'),
    Input('pob_ini', 'value'),
    Input('pob_exp', 'value'),
    Input('pob_inf', 'value'),
    Input('pob_asin', 'value'),
    Input('pob_rec', 'value'),
    Input('tiempo', 'value'),
    Input('Lambda', 'value'),
    Input('mu', 'value'),
    Input('lambda1', 'value'),
    Input('xi1', 'value'),
    Input('xi2', 'value'),
    Input('beta', 'value'),
    Input('rho1', 'value'),
    Input('rho2', 'value'),
    Input('alpha', 'value'),
    Input('delta', 'value'),
    Input('psi', 'value'),
    Input('eta', 'value'),
)
def grafic_SIR_model(N, E, I, A, R, t, Lambda, mu, lambda1, xi1, xi2, beta, p1, p2, alpha, delta, psi, eta):
    # Initial populations and parameters
    S = N - E - I - A - R
    populations = [S, E, I, A, R]
    xi = [xi1, xi2]
    p = [p1, p2]

    # Generate the graphs
    fig = SIARS(populations, t, Lambda, mu, lambda1, xi, beta, p, alpha, delta, psi, eta)
    
    # Unpack the figures
    fig_t = fig[0]  # Combined figure
    individual_figs = fig[1]  # List of individual compartment figures

    # Return the combined figure for the 'COMPLETO' graph, and the individual graphs for the others
    return fig_t, individual_figs[0], individual_figs[1], individual_figs[2], individual_figs[3], individual_figs[4]


###################################################################################
#
# Pruebas
#
###################################################################################
