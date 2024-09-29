from dash import Dash, html, dcc
import dash


app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True
)


app.layout = html.Div(children=[

    html.Div(className='header', children=[
        html.Img(className='sm_logo', src='assets/imgs/UNMSM.png'),
        html.H1('INTERFAZ GRÁFICA', className='main_title')
    ]),

    html.Div(className='contenedor_navegacion', children=[
        dcc.Link(html.Button('Edo 1er Orden', className='boton edo_1'), href='/'),
        dcc.Link(html.Button('Edo 2do Orden', className='boton edo_2'), href='/Edo2doOrden')
    ]),

    dash.page_container

])


if __name__ == '__main__':
    app.run(debug=True, port='1254')
