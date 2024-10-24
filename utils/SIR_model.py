import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go # Grafica

def model_SIR(initial_conditions, beta, gamma, t):
    """
    Falta
    """

    # Define the SIR model
    def SIR_odeint(y, t, beta, gamma):
        S, I, R = y
        
        #aplicar condicion

        dSdt = -beta*S*I
        dIdt = beta*S*I - gamma*I
        dRdt = gamma*I
        
        return dSdt, dIdt, dRdt

    time_points = np.linspace(0, t, 100)
    solution = odeint(SIR_odeint, initial_conditions, time_points, args=(beta, gamma))

    S, I, R = solution.T  

    # Crear la figura de Plotly
    fig = go.Figure()

    # Añadir la trazas a la figura
    fig.add_trace(go.Scatter(x=time_points, y=S, mode='lines', name='Susceptible', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=time_points, y=I, mode='lines', name='Infected', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=time_points, y=R, mode='lines', name='Recovered', line=dict(color='green')))

    # Actualizar el diseño
    fig.update_layout(
        title={
            'text': 'Modelo de Lotka-Volterra',
            'x': 0.5,
            'y': 0.92,
            'xanchor': 'center'
        },
        xaxis_title='Tiempo (t)',
        yaxis_title='Población (P)',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    # Contorno a la gráfica
    fig.update_xaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=True
    )
    fig.update_yaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=True
    )

    return fig