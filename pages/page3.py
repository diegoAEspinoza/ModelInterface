import dash
from dash import dcc, html, Input, Output, callback
from utils import changing_sir_model

dash.register_page(
    __name__,
    path='/Edo3',
    name='Edo3'
)

# Layout HTML

layout = html.Div(className='flex flex-col gap-6 lg:flex-row', children=[
    html.Div(className='space-y-3 lg:max-w-60', children=[
        html.H2(className='text-2xl font-bold text-center', children='Parámetros'),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tiempo'),
            dcc.Input(type='number', value=15, id='time', step=1, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Susceptibles'),
            dcc.Input(type='number', value=100, id='s0', step=1, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Infectados'),
            dcc.Input(type='number', value=6, id='i0', step=1, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Recuperados'),
            dcc.Input(type='number', value=0, id='r0', step=1, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tasa de contagio'),
            dcc.Input(type='number', value=0.01, id='beta', step=0.01, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tasa de recuperación'),
            dcc.Input(type='number', value=0.1, id='gamma', step=0.01, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tiempo de cambio'),
            dcc.Input(type='number', value=3, id='t_change', step=1, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Nueva tasa de contagio'),
            dcc.Input(type='number', value=0.02, id='new_beta', step=0.01, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Nueva tasa de recuperación'),
            dcc.Input(type='number', value=0.1, id='new_gamma', step=0.01, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
    ]),
    html.Div(className='flex-1', children=[
        html.H2(className='text-2xl font-bold text-center', children='Modelo SIR cambiante'),
        html.Div(className='lg:flex lg:h-full lg:justify-center lg:items-center', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_3'))
        ])
    ])
])

# Callback

@callback(
    Output('figura_3', 'figure'),
    Input('time', 'value'),
    Input('s0', 'value'),
    Input('i0', 'value'),
    Input('r0', 'value'),
    Input('beta', 'value'),
    Input('gamma', 'value'),
    Input('new_beta', 'value'),
    Input('new_gamma', 'value'),
    Input('t_change', 'value')
)
def graph(t, S0, I0, R0, beta, gamma, new_beta, new_gamma, t_change):
    fig = changing_sir_model((0,t),
                             [S0, I0, R0],
                             {'beta': beta, 'gamma': gamma},
                             {'beta': new_beta, 'gamma': new_gamma},
                             t_change)
    return fig

