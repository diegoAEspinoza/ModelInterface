import dash
from dash import dcc, html, Input, Output, callback
from utils import *

dash.register_page(
    __name__,
    path='/simulacion',
    name='Proyecto Modelos'
)

layout = html.Div(className="space-y-9", children=[
    
    html.Div(className="flex flex-col gap-6", children=[
        html.Div(className="space-y-3", children=[
            html.H2(className="font-semibold text-blue-500 text-center text-3xl", children='Parámetros'),
            html.Div(className="flex gap-10", children=[
                # Parámetros generales
                html.Div(className='flex-1 space-y-1', children=[
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Población inicial'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=998, id='pob_ini', debounce=True, step=1)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Expuestos'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0, id='pob_exp', debounce=True, step=1)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Infectados'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=1, id='pob_inf', debounce=True, step=1)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Asintomáticos'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=1, id='pob_asin', debounce=True, step=1)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Recuperados'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0, id='pob_rec', debounce=True, step=1)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tiempo'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=10, id='tiempo', debounce=True, step=1)
                    ]),
                ]),
                # Parámetros adicionales
                html.Div(className="flex-1", children=[
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de nacimientos'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.0613, id='Lambda', debounce=True, step=0.0001)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de muerte natural'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.0688, id='mu', debounce=True, step=0.0001)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de infección del Asintomático'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.35, id='lambda1', debounce=True, step=0.01)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de daño Asintomático'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.08, id='xi1', debounce=True, step=0.01)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de daño Infectado'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.07, id='xi2', debounce=True, step=0.01)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de contacto'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.01, id='beta', debounce=True, step=0.01)
                    ]),
                ]),
                html.Div(className="flex-1", children=[
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Proporción a Infectado'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.7, id='rho1', debounce=True, step=0.1)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Proporción a Recuperado'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.05, id='rho2', debounce=True, step=0.01)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de egreso del Expuesto'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.75, id='alpha', debounce=True, step=0.15)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de recuperación del Asintomático'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.04, id='delta', debounce=True, step=0.01)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de recuperación del Infectado'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.1, id='psi', debounce=True, step=0.1)
                    ]),
                    html.Div([
                        html.H3(className="text-xl font-semibold text-blue-800", children='Tasa de pérdida de inmunidad'),
                        dcc.Input(className="w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl", type='number', value=0.001, id='eta', debounce=True, step=0.001)
                    ]),
                ]),
            ]),
        ]),
        html.Div(className="", children=[
            html.Span(className="text-2xl font-semibold text-blue-800", children="Tasa de reproducción básica: "),
            html.Span(id="basic"),
        ]),
        # Sección de gráfica
        html.Div(className="flex-1", children=[
            html.H2(className="font-semibold text-blue-500  text-center text-3xl", children='Resultados'),
            html.Div(className='grid grid-cols-3 gap-6', children=[
                html.Div(className="col-span-3", children=dcc.Loading(type='default', children=dcc.Graph(id='COMPLETO'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='suceptibles'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='expuesto'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='infectado'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='asintomatico'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='recuperado'))),
            ])
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
    Output('basic', 'children'),
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
    fig, R_0 = SIARS(populations, t, Lambda, mu, lambda1, xi, beta, p, alpha, delta, psi, eta)
    
    # Unpack the figures
    fig_t = fig[0]  # Combined figure
    individual_figs = fig[1]  # List of individual compartment figures

    # Return the combined figure for the 'COMPLETO' graph, and the individual graphs for the others
    return fig_t, individual_figs[0], individual_figs[1], individual_figs[2], individual_figs[3], individual_figs[4], R_0
