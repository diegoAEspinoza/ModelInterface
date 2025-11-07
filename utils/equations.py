import numpy as np 
import plotly.graph_objects as go
import plotly.figure_factory as ff
from scipy.integrate import odeint

# Ecuación logística del Profesor
def ecuacion_logistica(K: float, P0: float, r: float, t0: float, t: float, cant: float, scale: float, show_vector_field: bool):
    """
    Retorna una gráfica de la ecuacion logistica con su campo vectorial.

    Parámetros:
    -------
    - K: Capacidad de carga.
    - P0: Poblacion Inicial.
    - r: Tasa de crecimineto poblacional.
    - t0: Tiempo inicial.
    - t: Tiempo final.
    - cant: Las particiones para el eje temporal y espacial.
    - scale: Tamaño del vector del campo vectorial.
    - show_vector_field: Booleano para mostrar el campo vectorial.
    """

    # Rango de P y t
    P_values = np.linspace(0, K + 5, cant)
    t_values = np.linspace(0, t, cant)

    # Crear una malla de puntos (P, t)
    T, P = np.meshgrid(t_values, P_values)

    # Definir la EDO
    dP_dt = r * P * (1 - P / K)

    # Solucion exacta de la Ecuación Logística
    funcion = K * P0 * np.exp(r * t_values) / (P0 * np.exp(r * t_values) + (K - P0) * np.exp(r * t0))

    # Crear la figura
    fig = go.Figure()

    if show_vector_field:
        U = np.ones_like(T)
        V = dP_dt

        # Crear el campo de vectores con Plotly
        quiver = ff.create_quiver(
            T, P, U, V,
            scale=scale,
            line=dict(color='black', width=1),
            showlegend=False
        )
        fig.add_traces(quiver.data)

    # Crear la función logística
    fig.add_trace(
        go.Scatter(
            x=t_values,
            y=funcion,
            line=dict(color='blue'),
            name='Ecuación Logística'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[0, t],
            y=[K, K],
            mode='lines',
            line=dict(color='red', dash='dash'),
            name='Capacidad de carga'
        )
    )

    # Etiquetas para la gráfica
    fig.update_layout(
        title={
            'text': 'Campo de vectores de dP/dt = rP(1 - P/k)',
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

    # Contorno a la grafica
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

# Función logística del alumno
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
    """

    # Ecuaciones de Lotka-Volterra
    def lotka_volterra(populations, t, alpha, beta, delta, gamma):
        X, Y = populations
        dXdt = alpha * X - beta * X * Y 
        dYdt = delta * X * Y - gamma * Y
        return [dXdt, dYdt]

    # Resolver las ecuaciones diferenciales
    initial_conditions = [X0, Y0]
    time_points = np.linspace(0, t, 100)
    X, Y = odeint(lotka_volterra, initial_conditions, time_points, args=(alpha, beta, delta, gamma)).T

    # Crear la figura de Plotly
    fig = go.Figure()

    # Añadir la población de presas
    fig.add_trace(go.Scatter(x=time_points, y=X, mode='lines', name='Presas (X)', line=dict(color='blue')))

    # Añadir la población de depredadores
    fig.add_trace(go.Scatter(x=time_points, y=Y, mode='lines', name='Depredadores (Y)', line=dict(color='red')))

    # Etiquetas para la gráfica
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
