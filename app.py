from dash import Dash, html, dcc
import dash


app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True
)


app.layout = html.Div(className='back',children=[
    html.Div(className='header', children=[
        html.Div(className='header-content', children=[
            html.Img(className='sm_logo', src='assets/imgs/UNMSM.png'),
            html.Div(className='text', children=[
                html.H1('INTERFAZ GRÁFICA', className='main_title'),
                html.H3('Nombre: Espinoza Huaman, Diego Alexhander'),
                html.H3('Codigo: 22140106')
            ])
        ])
    ]),
    
    html.Div(className='contenedor_navegacion', children=[
        dcc.Link(html.Button('Logistic Function', className='boton edo_1'), href='/'),
        dcc.Link(html.Button('Lotka-Volterra Model', className='boton edo_2'), href='/lotka_volterra_model'),
        dcc.Link(html.Button('SIR Model', className='boton edo_3'), href='/SIR'),
    ]),
    
    dash.page_container
])


if __name__ == '__main__':
    app.run(debug=True, port='1254')
