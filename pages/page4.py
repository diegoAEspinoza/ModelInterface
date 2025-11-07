import dash
from dash import dcc, html, Input, Output, callback
from utils import points_ODE

dash.register_page(
    __name__,
    path='/Edo4',
    name='Edo4'
)

layout = html.Div(className='flex flex-col gap-6 lg:flex-row', children=[
    html.Div(className='space-y-3 lg:max-w-60', children=[
        html.Div(className='div_parametros', children=[
            html.H2('Parámetros', className='text-2xl font-bold text-center'),
            html.Div(className='div_flex', children=[
                html.Div([
                    html.H3('Diferencial X'),
                    dcc.Input(type='text', id='dx', value='x*(5-y)')  
                ]),

                html.Div([
                    html.H3('Diferencial Y'),
                    dcc.Input(type='text', id='dy', value='y*(5-x)'), 
                ]),
            ]),
        
            html.Div(className='div_flex', children=[
                html.Div([
                    html.H3('Límite inferior'),
                    dcc.Input(type='number', value=-2, id='lower_limit', step=1)  
                ]),

                html.Div([
                    html.H3('Límite superior'),
                    dcc.Input(type='number', value=10, id='upper_limit', step=1)  
                ]),
            ]),

            html.Div(className='div_flex', children=[
                html.Div([
                    html.H3('Número de puntos'),
                    dcc.Input(type='number', value=25, id='point_numbe', step=1, min=0)  
                ]),

                html.Div([
                    html.H3('Tamaño del vector'),
                    dcc.Input(type='number', value=0.2, id='scale_factor', step=0.01, min=0)  
                ]),
            ]),
        ]),

        html.Div(children=[
            html.H2('Resultados', className='text-2xl font-bold text-center'),
            html.Pre(id='text', className='py-4 overflow-x-auto')
        ]),
    ]),

    html.Div(className='flex-1', children=[
        html.H2('Gráfica', className='text-2xl font-bold text-center'),
        html.Div(className='grafica', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_4'))
        ])
    ])
])

@callback(
    Output('figura_4', 'figure'),
    Output('text', 'children'),
    Input('dx', 'value'),
    Input('dy', 'value'),
    Input('lower_limit', 'value'),
    Input('upper_limit', 'value'),
    Input('point_numbe', 'value'),
    Input('scale_factor', 'value'),
)
def process_inputs(dx, dy,a, b, n, scale_factor):
    fig,text = points_ODE(dx, dy, a, b, n, scale_factor)
    return fig, text

