###################################################################################
#
# Librerías
#
###################################################################################
import dash
from dash import dcc, html, Input, Output, callback
from utils import *

dash.register_page(
    __name__,
    path='/proyect',
    name='proyect'
)

###################################################################################
#
# Layout HTML
#
###################################################################################

layout = html.Div(className='Pages', children=[
    html.H2('EN PROCESO... PERO CON SUERTE SE TERMINA', style={'text-align': 'center'}),
])


###################################################################################
#
# Callback principal
#
###################################################################################


###################################################################################
#
# Pruebas
#
###################################################################################
"""
Gamma= 3
mu = 2
gamma =4
xi = [5, 5]
beta = 10
p = [2.2 , 06.6]
alpha = 2.2
delta = 7.96
psi = 0.1
eta = 7

S, E, I, A, R = 10000, 1, 1, 1, 0
populations = [S, E, I, A, R]

t = np.linspace(0,100,100)

solution= odeint(model, populations, t, args=(Gamma, mu, gamma, xi, beta, p, alpha, delta, psi, eta))

#plt.plot(t, solution[:,0], label="Suseptibles")
#plt.plot(t, solution[:,1], label="Expuesto")
plt.plot(t, solution[:,2], label="Infectados")
plt.plot(t, solution[:,3], label="Asintomaticos")
plt.plot(t, solution[:,4], label="Recuperados")
plt.legend()
plt.show()

"""