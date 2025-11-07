import dash
from dash import dcc, html, Input, Output, callback
from utils import lotka_volterra_model

dash.register_page(
    __name__,
    path='/Edo2',
    name='Edo2'
)

# Layout HTML

layout = html.Div(className='flex flex-col gap-6 lg:flex-row', children=[
    html.Div(className='space-y-3 lg:max-w-60', children=[
        html.H2(className='text-2xl font-bold text-center', children='Parámetros'),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Población inicial (Presas)'),
            dcc.Input(type='number', value=80, id='prey_ini', step=1, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Población inicial (Depredadores)'),
            dcc.Input(type='number', value=20, id='pred_ini', step=1, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl') 
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tasa de nacimiento (Presas)'),
            dcc.Input(type='number', value=0.2, id='prey_grow', step=0.01, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl') 
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tasa de depredación'),
            dcc.Input(type='number', value=0.03, id='pred_rate', step=0.01, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl') 
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tasa de nacimiento (Depredadores)'),
            dcc.Input(type='number', value=0.01, id='pred_grow', step=0.01, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')  
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tasa de mortalidad (Depredadores)'),
            dcc.Input(type='number', value=0.1, id='pred_mort', step=0.01, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')  
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tiempo'),
            dcc.Input(type='number', value=12, id='time', step=1, min=0, className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')  
        ]),
    ]),
    html.Div(className='flex-1', children=[
        html.H2(className='text-2xl font-bold text-center', children='Gráfica de la EDO de 2 variables'),
        html.Div(className='lg:flex lg:h-full lg:justify-center lg:items-center', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_2'))
        ])
    ])
])

# Callback

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
def graph(x0=40, y0=9, alpha=0.1, beta=0.02, delta=0.01, gama=0.1, t=5):
    fig = lotka_volterra_model(x0, y0, alpha, beta, delta, gama, t)
    return fig
