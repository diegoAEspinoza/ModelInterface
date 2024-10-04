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
    path='/Edo2doOrden',
    name='Edo-Ejemplo 2'
)

###################################################################################
#
# Layout HTML
#
###################################################################################

layout = html.Div('Pagina 2')