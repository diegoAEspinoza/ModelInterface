import numpy as np 
import plotly.graph_objects as go # Grafica
import plotly.figure_factory as ff # mallado de vectores
from scipy.integrate import odeint


def SIARS (Gamma, mu, gamma, xi, beta, p, alpha, delta, psi, eta, t):
    def model(populations, t, Gamma, mu, gamma, xi, beta, p, alpha, delta, psi, eta):
        S, E, I, A, R = populations
        xi1, xi2 = xi
        p1, p2 = p

        dSdt = Gamma - beta*S*(I+gamma*A) - mu*S + eta*R
        dEdt = beta*S*(I + gamma*A) - (alpha + mu)*E
        dIdt = p1*alpha*E - (psi + mu + xi2)*I
        dAdt = (1-p1 - p2)*alpha*E -(delta + mu + xi1)*A
        dRdt = psi*I + delta*A + p2*alpha*E - (eta+mu)*R
        return [dSdt, dEdt, dIdt,dAdt,dRdt]
    
    S, E, I, A, R = 10000, 1, 1, 1, 0
    populations = [S, E, I, A, R]
    t = np.linspace(0,100,100)
    solution= odeint(model, populations, t, args=(Gamma, mu, gamma, xi, beta, p, alpha, delta, psi, eta))