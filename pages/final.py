import dash
from dash import dcc, html, Input, Output, callback
from utils import *

dash.register_page(
    __name__,
    path='/final',
    name='Proyecto Final Modelos'
)

layout = html.Div(className="space-y-9", children=[
    html.Div(className="flex flex-col gap-6", children=[
        html.Div(className="space-y-3", children=[
            html.H2(className="font-semibold text-center text-2xl", children='Parámetros'),
            html.Div(className="flex gap-10", children=[
                # Parámetros generales
                html.Div(className='flex-1 space-y-1', children=[
                    html.Div([
                        html.H3(className="font-semibold", children='S0 (Susceptibles iniciales):'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=100, id='S0', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='I0 (Infectados iniciales):'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=1, id='I0', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='R0 (Recuperados iniciales):'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=0, id='R0', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Tiempo máximo de simulación:'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=5, id='t_max', debounce=True)
                    ]),
                ]),
                # Parámetros adicionales
                html.Div(className="flex-1", children=[
                    html.Div([
                        html.H3(className="font-semibold", children='Beta (Tasa de infección):'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=0.1, step=0.01, id='beta', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Psi (Tasa de recuperación):'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=0.05, step=0.01, id='psi', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Alpha (Tasa de pérdida de inmunidad):'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=0.3, step=0.01, id='alpha', debounce=True)
                    ]),
                ]),
            ]),
        ]),
        # Sección de gráfica
        html.Div(className="flex-1", children=[
            html.H2(className="font-semibold text-center text-2xl", children='Resultados'),
            html.Div(className='grid grid-cols-3 gap-6', children=[
                html.Div(className="col-span-3", children=dcc.Loading(type='default', children=dcc.Graph(id='graph-combined'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='graph-S'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='graph-I'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='graph-R'))),
            ])
        ])
    ])
])

@callback(
    Output('graph-combined', 'figure'),
    Output('graph-S', 'figure'),
    Output('graph-I', 'figure'),
    Output('graph-R', 'figure'),
    Input('S0', 'value'),
    Input('I0', 'value'),
    Input('R0', 'value'),
    Input('beta', 'value'),
    Input('psi', 'value'),
    Input('alpha', 'value'),
    Input('t_max', 'value')
)
def update_SIRS_graphs(S0, I0, R0, beta, psi, alpha, t_max):
    fig_combined, fig_S, fig_I, fig_R = solve_and_plot_sir(S0, I0, R0, beta, psi, alpha, t_max=t_max)
    return fig_combined, fig_S, fig_I, fig_R

