import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def solve_and_plot_sir(S0, I0, R0, beta, psi, alpha, t_max=100, num_points=1000):
    """
    Resuelve el modelo SIR y genera gráficos de la solución.

    Args:
        S0: Número inicial de dispositivos susceptibles.
        I0: Número inicial de dispositivos infectados.
        R0: Número inicial de dispositivos recuperados.
        beta: Tasa de infección.
        psi: Tasa de recuperación.
        alpha: Tasa de pérdida de inmunidad.
        t_max: Tiempo máximo de simulación.
        num_points: Número de puntos de tiempo para la simulación.

    Returns:
        Una tupla de 4 figuras de plotly:
        - Una figura con las gráficas de S(t), I(t) y R(t) juntas.
        - Una figura con la gráfica de S(t).
        - Una figura con la gráfica de I(t).
        - Una figura con la gráfica de R(t).
    """

    # Definir el sistema de ecuaciones diferenciales
    def sir_model(y, t, beta, psi, alpha):
        S, I, R = y
        dSdt = alpha * R - beta * S * I
        dIdt = beta * S * I - psi * I
        dRdt = psi * I - alpha * R
        return [dSdt, dIdt, dRdt]

    # Condiciones iniciales
    y0 = [S0, I0, R0]

    # Vector de tiempo
    t = np.linspace(0, t_max, num_points)

    # Resolver el sistema de ecuaciones diferenciales
    sol = odeint(sir_model, y0, t, args=(beta, psi, alpha))
    S, I, R = sol.T

    # Crear la figura con las 3 gráficas juntas
    fig_combined = make_subplots(rows=1, cols=1)

    fig_combined.add_trace(go.Scatter(x=t, y=S, mode='lines', name='Susceptibles (S)', line=dict(color='blue')))
    fig_combined.add_trace(go.Scatter(x=t, y=I, mode='lines', name='Infectados (I)', line=dict(color='orange')))
    fig_combined.add_trace(go.Scatter(x=t, y=R, mode='lines', name='Recuperados (R)', line=dict(color='green')))

    fig_combined.update_layout(title='Modelo SIR',
                                xaxis_title='Tiempo (años)',
                                yaxis_title='Número de dispositivos',
                                template='plotly_white',
                                legend=dict(x=0.7, y=0.95))

    # Crear las figuras individuales
    fig_S = go.Figure(data=[go.Scatter(x=t, y=S, mode='lines', name='Susceptibles (S)', line=dict(color='blue'))])
    fig_S.update_layout(title='Susceptibles (S)', xaxis_title='Tiempo (años)', yaxis_title='Número de dispositivos', template='plotly_white')

    fig_I = go.Figure(data=[go.Scatter(x=t, y=I, mode='lines', name='Infectados (I)', line=dict(color='orange'))])
    fig_I.update_layout(title='Infectados (I)', xaxis_title='Tiempo (años)', yaxis_title='Número de dispositivos', template='plotly_white')

    fig_R = go.Figure(data=[go.Scatter(x=t, y=R, mode='lines', name='Recuperados (R)', line=dict(color='green'))])
    fig_R.update_layout(title='Recuperados (R)', xaxis_title='Tiempo (años)', yaxis_title='Número de dispositivos', template='plotly_white')

    return fig_combined, fig_S, fig_I, fig_R

