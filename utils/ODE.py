import plotly.graph_objects as go
import plotly.figure_factory as ff # mallado de vectores
import numpy as np
from sympy import symbols, sympify, Matrix, solve, simplify

def points_ODE(dx_input, dy_input, a, b, n):
    """
    Generates a vector field plot from given first-order ordinary differential equations (ODEs).
    
    Parameters:
    - dx_input (str): Expression for the change in x (dx).
    - dy_input (str): Expression for the change in y (dy).
    - a (float): Minimum value for the x and y axes.
    - b (float): Maximum value for the x and y axes.
    - n (int): Number of points to create in each dimension for the grid.

    Returns:
    - fig (plotly.graph_objects.Figure): Plotly figure containing the vector field and critical points.
    """

    # Define symbols
    x_sym, y_sym = symbols("x y")

    # Convert input expressions to symbolic form
    dx = sympify(dx_input)
    dy = sympify(dy_input)

    # Calculate critical points
    A = np.array(solve([dx, dy], (x_sym, y_sym))).astype(float)

    # Create a mesh grid for the plot
    x_vals = np.linspace(a, b, n)
    y_vals = np.linspace(a, b, n)
    X_, Y_ = np.meshgrid(x_vals, y_vals)

    # Create empty matrices to store the vector field components
    U = np.zeros_like(X_)
    V = np.zeros_like(Y_)

    for i in range(X_.shape[0]):
        for j in range(X_.shape[1]):
            U[i, j] = dx.subs({x_sym: X_[i, j], y_sym: Y_[i, j]})
            V[i, j] = dy.subs({x_sym: X_[i, j], y_sym: Y_[i, j]})

    # Normalize the vector field
    N = np.hypot(U, V) + 1e-8  # Prevent division by zero
    U_normalized = U / N
    V_normalized = V / N

    fig = go.Figure()
    quiver = ff.create_quiver(X_, Y_, U_normalized, V_normalized)
    fig.add_traces(quiver.data)
    fig.add_traces(go.Scatter(x = A[:,0], y = A[:,1], mode='markers'))

    return fig