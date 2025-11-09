import dash
from dash import dcc, html, Input, Output, callback
from utils import *

dash.register_page(
    __name__,
    path='/',
    name='Proyecto Modelos'
)

layout = html.Div(className="space-y-9", children=[
    html.Div(className="flex flex-col gap-9 items-center", children=[
        html.Div(className="font-semibold text-2xl", children="Modelo virus informático"),
        html.Div(
            className='flex gap-6', children=[
                # Imagen 1
                html.Img(
                    className="w-[25rem]",
                    src='/assets/model.png', 
                    alt='Imagen de modelo', 
                ),
                # Imagen 2
                html.Img(
                    className="w-[25rem]",
                    src='/assets/model1.png', 
                    alt='Imagen de modelo', 
                )
            ]
        ),
    ]),
])
