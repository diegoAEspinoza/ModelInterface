import numpy as np 
import plotly.graph_objects as go
import plotly.figure_factory as ff
from scipy.integrate import odeint


def SIARS (populations, t, Lambda, mu, lambda1, xi, beta, p, alpha, delta, psi, eta):
    def model(populations, t, Lambda, mu, lambda1, xi, beta, p, alpha, delta, psi, eta):
        S, E, I, A, R = populations
        xi1, xi2 = xi
        p1, p2 = p

        dSdt = Lambda - beta*S*(I+lambda1*A) - mu*S + eta*R
        dEdt = beta*S*(I + lambda1*A) - (alpha + mu)*E
        dIdt = p1*alpha*E - (psi + mu + xi2)*I
        dAdt = (1-p1 - p2)*alpha*E -(delta + mu + xi1)*A
        dRdt = psi*I + delta*A + p2*alpha*E - (eta+mu)*R
        return dSdt, dEdt, dIdt,dAdt,dRdt
    
    
    t = np.linspace(0,t,100*t)
    solution = odeint(model, populations, t, args=(Lambda, mu, lambda1, xi, beta, p, alpha, delta, psi, eta))

    S, E, I, A, R = solution.T


     # Create Plotly figure
    fig_t = go.Figure()

    fig_t.add_trace(go.Scatter(x=t, y=S, mode='lines', name='Susceptibles', line=dict(color='blue')))
    fig_t.add_trace(go.Scatter(x=t, y=E, mode='lines', name='Expuestos', line=dict(color='orange')))
    fig_t.add_trace(go.Scatter(x=t, y=I, mode='lines', name='Infectados', line=dict(color='red')))
    fig_t.add_trace(go.Scatter(x=t, y=A, mode='lines', name='Asintomáticos', line=dict(color='green')))
    fig_t.add_trace(go.Scatter(x=t, y=R, mode='lines', name='Recuperados', line=dict(color='purple')))

    fig_t.update_layout(
        title='Evolución de la Población en el Modelo SIARS',
        xaxis_title='Tiempo (años)',
        yaxis_title='Número de individuos',
        template='plotly_white'
    )

    fig = [go.Figure(),go.Figure(),go.Figure(),go.Figure(),go.Figure()]
    fig[0].add_trace(go.Scatter(x=t, y=S, mode='lines', name='Susceptibles', line=dict(color='blue')))
    fig[1].add_trace(go.Scatter(x=t, y=E, mode='lines', name='Expuestos', line=dict(color='orange')))
    fig[2].add_trace(go.Scatter(x=t, y=I, mode='lines', name='Infectados', line=dict(color='red')))
    fig[3].add_trace(go.Scatter(x=t, y=A, mode='lines', name='Asintomáticos', line=dict(color='green')))
    fig[4].add_trace(go.Scatter(x=t, y=R, mode='lines', name='Recuperados', line=dict(color='purple')))

    fig[0].update_layout(
        title='Evolución de la Población en el Modelo SIARS',
        xaxis_title='Tiempo (años)',
        yaxis_title='Número de Suceptibles',
        template='plotly_white'
    )
    fig[1].update_layout(
        title='Evolución de la Población en el Modelo SIARS',
        xaxis_title='Tiempo (años)',
        yaxis_title='Número de Expuesto',
        template='plotly_white'
    )
    fig[2].update_layout(
        title='Evolución de la Población en el Modelo SIARS',
        xaxis_title='Tiempo (años)',
        yaxis_title='Número de Infectados',
        template='plotly_white'
    )
    fig[3].update_layout(
        title='Evolución de la Población en el Modelo SIARS',
        xaxis_title='Tiempo (años)',
        yaxis_title='Número de Asistomaticos',
        template='plotly_white'
    )
    fig[4].update_layout(
        title='Evolución de la Población en el Modelo SIARS',
        xaxis_title='Tiempo (años)',
        yaxis_title='Número de Recuperados',
        template='plotly_white'
    )

    # Calcular R_0

    xi1, xi2 = xi
    p1, p2 = p

    R_0 = np.sqrt((alpha*beta*Lambda/(mu*(alpha + mu)))*((p1/(psi + mu + xi2))+ (lambda1*(1 - p1 - p2)/(delta + mu + xi1))))

    return [fig_t,fig], R_0
