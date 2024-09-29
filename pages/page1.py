###################################################################################
#
# Librerías
#
###################################################################################
import dash
from dash import dcc, html, Input, Output, callback
from utils import ecuacion_logistica

dash.register_page(
    __name__,
    path='/',
    name='Edo-1'
)

###################################################################################
#
# Layout HTML
#
###################################################################################

layout = html.Div(className='Pages', children=[

    html.Div(className='div_parametros', children=[

        html.H2('PARÁMETROS'),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Población Inicial'),
                dcc.Input(type='number', value=10, id='pob_ini')
            ]),
            html.Div([
                html.H3('Tiempo Inicial'),
                dcc.Input(type='number', value=0, id='time_ini')
            ]),
            html.Div([
                html.H3('Tiempo Final'),
                dcc.Input(type='number', value=60, id='time_fin')
            ]),
        ]),

        html.H3('Tasa de Crecimiento'),
        dcc.Input(max=5, type='number', value=0.15, id='r'),

        html.H3('Capacidad de Carga'),
        dcc.Input(type='number', value=150, id='K'),

        html.H3('Malla para el Campo de Vectores'),
        dcc.Slider(min=1, max=40, step=1, value=15, marks=None, tooltip={'placement':'bottom', 'always_visible':True}, id='mallado'),

        html.H3('Tamaño del Vector'),
        dcc.Slider(min=0.1, max=2, step=0.1, value=1, id='size_vec')
    ]),

    html.Div(className='div_grafica', children=[
        html.H2('GRÁFICA DE LA EDO DE 1ER ORDEN'),
        dcc.Loading(
            type='default',
            children=dcc.Graph(id='figura_1')
        )
    ])

])


###################################################################################
#
# Callback
#
###################################################################################

@callback(
    Output('figura_1', 'figure'),
    Input('pob_ini', 'value'),
    Input('time_ini', 'value'),
    Input('time_fin', 'value'),
    Input('r', 'value'),
    Input('K', 'value'),
    Input('mallado', 'value'),
    Input('size_vec', 'value'),
)

def grafica_edo1(P0, t_i, t_f, r, k, mallado, size_vec):
    fig = ecuacion_logistica(k, P0, r, t_i, t_f, mallado, size_vec)
    return fig