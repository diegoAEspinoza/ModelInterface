# Librerias
import numpy as np 
import plotly.graph_objects as go # Grafica
import plotly.figure_factory as ff # mallado de vectores
from scipy.integrate import odeint


# Funciones

# Función Logistica Profesor
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
    - show_vector_field: Booleano para mostrar el campo de vectores.
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

    if show_vector_field:  # Conditionally show the vector field
        U = np.ones_like(T)  # Componente en t (horizontal)
        V = dP_dt           # Componente en P (vertical)

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
        showgrid=False
    )
    fig.update_yaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )

    return fig


# Funcion Logistica Alumnos
# 1. Averguar aguna Ecuacion de algun modelo y desarrollarlo con Sympy.
# 3. Agregar un botón en la cual me permita activar y desactivar el campo de vectores (RETO)

def lotka_volterra_model(X0, Y0, alpha, beta, delta, gamma, t, show_vector_field=True):
    """
    Returns a plot of the Lotka-Volterra predator-prey model with its vector field.

    Parameters:
    -------
    - alpha: Growth rate of prey.
    - beta: Rate of predation.
    - delta: Rate at which predators increase by consuming prey.
    - gamma: Natural death rate of predators.
    - X0: Initial population of prey.
    - Y0: Initial population of predators.
    - t: Time points for which the solution is computed.
    - show_vector_field: Boolean to show the vector field.

    Returns:
    -------
    - fig: A Plotly figure containing the population trajectories and vector field.
    """

    # Lotka-Volterra equations
    def model(populations, t, alpha, beta, delta, gamma):
        X, Y = populations
        dXdt = alpha * X - beta * X * Y
        dYdt = delta * X * Y - gamma * Y
        return [dXdt, dYdt]

    # Solve the differential equations
    initial_conditions = [X0, Y0]
    time_points = np.linspace(0, t, 100)  # Generate 100 time points
    solution = odeint(model, initial_conditions, time_points, args=(alpha, beta, delta, gamma))
    X, Y = solution.T

    # Create the Plotly figure
    fig = go.Figure()

    # Add the prey population trace
    fig.add_trace(go.Scatter(x=time_points, y=X, mode='lines', name='Prey (X)', line=dict(color='blue')))

    # Add the predator population trace
    fig.add_trace(go.Scatter(x=time_points, y=Y, mode='lines', name='Predator (Y)', line=dict(color='red')))

    if show_vector_field:
        # Create a grid for vector field
        X_range = np.linspace(0, t, 20)
        Y_range = np.linspace(0, max([X0,Y0]), 20)
        X_mesh, Y_mesh = np.meshgrid(X_range, Y_range)

        # Calculate the derivatives for the vector field
        dXdt_mesh = alpha * X_mesh - beta * X_mesh * Y_mesh
        dYdt_mesh = delta * X_mesh * Y_mesh - gamma * Y_mesh

        # Create the vector field with Plotly
        fig.add_trace(go.Scatter(
            x=X_mesh.flatten(),
            y=Y_mesh.flatten(),
            mode='lines',
            line=dict(color='red', dash='dash'),  # No markers shown
            name='Vector Field'
        ))

        # Add arrows for the vector field
        fig.add_traces(ff.create_quiver(
            X_mesh, Y_mesh, dXdt_mesh, dYdt_mesh,
            scale=0.1,
            line=dict(color='gray', width=1),
            showlegend=False
        ).data)

    # Update layout
    fig.update_layout(
        title={
            'text': 'Lotka-Volterra Model with Vector Field',
            'x': 0.5,
            'y': 0.92,
            'xanchor': 'center'
        },
        xaxis_title='Time (t)',
        yaxis_title='Population (P)',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    return fig