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
        html.Div(className="font-semibold text-2xl", children=""),
        html.Div(
            className='flex flex-wrap justify-center gap-6', 
            children=[
                
                html.Div(className="flex flex-col items-center gap-3", children=[
                    html.H3(className="font-semibold text-blue-800 text-3xl", children="Diagrama del Modelo"), 
                    
                    html.Img(
                        className="w-full shadow-lg rounded-md",
                        src='/assets/diagram.png', 
                        alt='Diagrama del modelo SEIARS', 
                    ),
                ]),
            ]
        ),

        html.Div(
            className='flex flex-wrap justify-center gap-6', 
            children=[
                
                html.Div(className="flex flex-col items-center gap-3", children=[
                    html.H3(className="font-semibold text-blue-800 text-3xl", children="Modelo Matemático"), 
                    
                    html.Img(
                        className="w-full shadow-lg rounded-md",
                        src='/assets/model.png', 
                        alt='Diagrama del modelo SEIARS', 
                    ),
                ]),
            ]
        ),
        html.Div(
            className='flex flex-wrap justify-center gap-6', 
            children=[
                html.Div(className="flex flex-col items-center gap-3", children=[
                    html.H3(className="font-semibold text-blue-800 text-3xl", children="Notación del modelo SEIARS"), 
                    
                    html.Img(
                        className="w-full shadow-lg rounded-md",
                        src='/assets/model1.png', 
                        alt='Notación del modelo SEIARS', 
                    )
                ])
            ]
        ),
    ]),
])