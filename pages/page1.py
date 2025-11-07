import dash
from dash import dcc, html, Input, Output, callback
from utils import ecuacion_logistica

dash.register_page(
    __name__,
    path='/',
    name='Edo1'
)

# Layout HTML

layout = html.Div(className='flex flex-col gap-6 lg:flex-row', children=[
    html.Div(className='space-y-3 lg:max-w-60', children=[
        html.H2(className='text-2xl font-bold text-center', children='Parámetros'),
        html.Div(children=[
            html.Div([
                html.H3(className='text-xl font-semibold text-blue-800', children='Población inicial'),
                dcc.Input(type='number', value=10, id='pob_ini', className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
            ]),
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tiempo inicial'),
            dcc.Input(type='number', value=0, id='time_ini', className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tiempo final'),
            dcc.Input(type='number', value=60, id='time_fin', className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tasa de crecimiento'),
            dcc.Input(max=5, type='number', value=0.15, id='r', className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl'),
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Capacidad de carga'),
            dcc.Input(type='number', value=150, id='K', className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl'),
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Número de puntos'),
            dcc.Input(type='number', value=25, id='mallado', className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl'),
        ]),
        html.Div([
            html.H3(className='text-xl font-semibold text-blue-800', children='Tamaño de vector'),
            dcc.Input(type='number', value=1, id='size_vec', className='w-full mt-1 px-4 py-2 border-2 border-blue-600 rounded-xl')
        ]),
        html.Div(className='!mt-5', children=[
            html.Button(className='px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700', children='Campo vectorial', id='toggle-button', n_clicks=0)
        ]),
    ]),
    html.Div(className='flex-1', children=[
        html.H2(className='text-2xl font-bold text-center', children='Gráfica de la EDO de 1er Orden'),
        html.Div(className='lg:flex lg:h-full lg:justify-center lg:items-center', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_1'))
        ])
    ])
])

# Callback

@callback(
    Output('figura_1', 'figure'),
    Input('pob_ini', 'value'),
    Input('time_ini', 'value'),
    Input('time_fin', 'value'),
    Input('r', 'value'),
    Input('K', 'value'),
    Input('mallado', 'value'),
    Input('size_vec', 'value'),
    Input('toggle-button', 'n_clicks')
)
def graph(P0, t_i, t_f, r, k, mallado, size_vec, n_clicks):
    show_vector_field = (n_clicks % 2 == 1)
    fig = ecuacion_logistica(k, P0, r, t_i, t_f, mallado, size_vec, show_vector_field)
    return fig
