import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go

def changing_sir_model(time_span, initial_conditions, params, new_params, t_change):
    """
    Args:
        time_span: Tuple (t0, tf) representing the start and end times.
        initial_conditions: List [S0, I0, R0] representing initial populations.
        params: Dictionary {'beta': beta, 'gamma': gamma} for the initial parameters.
        new_params: Dictionary {'beta': new_beta, 'gamma': new_gamma} for the parameters after t_change.
        t_change: Time at which the parameters change.
    Returns:
        A plotly Figure object representing the SIR model graph.
    """

    def sir_deriv(y, t, beta, gamma, t_change_, new_beta, new_gamma):
        S, I, R = y
        if t >= t_change_:
            beta = new_beta
            gamma = new_gamma
        dSdt = -beta * S * I
        dIdt = beta * S * I - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    # Solve ODE
    t = np.linspace(time_span[0], time_span[1],
                    int((time_span[1] - time_span[0]) * 10))
    args = (params['beta'],
            params['gamma'],
            t_change,
            new_params['beta'],
            new_params['gamma'])
    sol = odeint(sir_deriv, initial_conditions, t, args=args)
    S, I, R = sol[:, 0], sol[:, 1], sol[:, 2]

    # Create the plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=S, mode='lines', name='Suceptible'))
    fig.add_trace(go.Scatter(x=t, y=I, mode='lines', name='Infectado'))
    fig.add_trace(go.Scatter(x=t, y=R, mode='lines', name='Recuperado'))
    
    fig.add_shape(
        go.layout.Shape(
            type="line",
            x0=t_change,
            y0=0,
            x1=t_change,
            y1=max(max(S), max(I), max(R)),  # Line extends to the maximum y-value
            line=dict(color="grey", width=2, dash="dash"),
        )
    )

    fig.update_layout(
        title={
            'text': 'Modelo SIR cambiante',
        },
        xaxis_title='Tiempo',
        yaxis_title='Población',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    return fig

