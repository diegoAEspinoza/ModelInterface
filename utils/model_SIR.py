import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go  # Graph

def model_SIR(initial_conditions, beta, gamma, t, t_change, new_beta=None, new_gamma=None):
    """
    Simulates the SIR (Susceptible-Infected-Recovered) model to predict the 
    spread of an infectious disease in a population, allowing changes to 
    beta or gamma at a specified time.

    Parameters:
    - initial_conditions (list): List of three elements representing the initial 
      conditions for susceptible (S), infected (I), and recovered (R) populations.
    - beta (float): Initial transmission rate of the disease (probability of infection).
    - gamma (float): Initial recovery rate (proportion of infected that recover per time unit).
    - t (int): Maximum simulation time.
    - t_change (int): Time when parameter changes will occur.
    - new_beta (float, optional): New beta value after t_change.
    - new_gamma (float, optional): New gamma value after t_change.

    Returns:
    - fig (plotly.graph_objects.Figure): Graph of the susceptible, infected, 
      and recovered populations over time.
    """

    # Define the differential equations for the SIR model
    def SIR_odeint(y, t, beta, gamma, change_time, new_beta, new_gamma):
        S, I, R = y
        
        # Apply condition for changing beta and gamma
        if t > change_time:
            beta = new_beta  # Change to new beta
            gamma = new_gamma  # Change to new gamma

        dSdt = -beta * S * I
        dIdt = beta * S * I - gamma * I
        dRdt = gamma * I
        
        return dSdt, dIdt, dRdt

    # Define the time points over which to solve the ODE
    time_points = np.linspace(0, t, 100)
    
    # Solve the system of differential equations
    solution = odeint(SIR_odeint, initial_conditions, time_points, 
                      args=(beta, gamma, t_change, new_beta, new_gamma))

    # Separate the solutions for S, I, and R
    S, I, R = solution.T  

    # Create the Plotly figure
    fig = go.Figure()

    # Add traces for each population to the figure
    fig.add_trace(go.Scatter(x=time_points, y=S, mode='lines', name='Susceptible', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=time_points, y=I, mode='lines', name='Infected', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=time_points, y=R, mode='lines', name='Recovered', line=dict(color='green')))

    # Update the layout of the graph
    fig.update_layout(
        title={
            'text': 'SIR Model with Parameter Change',
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

    # Add contours to the axes
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
