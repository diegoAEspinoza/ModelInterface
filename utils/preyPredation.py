import numpy as np 
import plotly.graph_objects as go # Grafica
import plotly.figure_factory as ff # mallado de vectores
from scipy.integrate import odeint


def lotka_volterra_model(X0, Y0, alpha, beta, delta, gamma, t):
    """
    Devuelve un gráfico del modelo depredador-presa de Lotka-Volterra.

    Parámetros:
    -------
    - alpha: Tasa de crecimiento de las presas.
    - beta: Tasa de depredación.
    - delta: Tasa a la que los depredadores aumentan al consumir presas.
    - gamma: Tasa natural de mortalidad de los depredadores.
    - X0: Población inicial de presas.
    - Y0: Población inicial de depredadores.
    - t: Puntos de tiempo para los cuales se computa la solución.

    Retorna:
    -------
    - fig: Una figura de Plotly que contiene las trayectorias de población.
    """

    # Ecuaciones de Lotka-Volterra
    def model(populations, t, alpha, beta, delta, gamma):
        X, Y = populations
        dXdt = alpha * X - beta * X * Y  # Cambio en la población de presas
        dYdt = delta * X * Y - gamma * Y  # Cambio en la población de depredadores
        return [dXdt, dYdt]

    # Resolver las ecuaciones diferenciales
    initial_conditions = [X0, Y0]  # Condiciones iniciales
    time_points = np.linspace(0, t, 100)  # Generar 100 puntos de tiempo
    solution = odeint(model, initial_conditions, time_points, args=(alpha, beta, delta, gamma))
    X, Y = solution.T  # Transponer la solución para obtener X y Y

    # Crear la figura de Plotly
    fig = go.Figure()

    # Añadir la traza de la población de presas
    fig.add_trace(go.Scatter(x=time_points, y=X, mode='lines', name='Presas (X)', line=dict(color='blue')))

    # Añadir la traza de la población de depredadores
    fig.add_trace(go.Scatter(x=time_points, y=Y, mode='lines', name='Depredadores (Y)', line=dict(color='red')))

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