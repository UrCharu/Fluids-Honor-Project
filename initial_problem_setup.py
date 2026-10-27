import numpy as np
import matplotlib.pyplot as plt

"""
This is an initial file with thoughts about the functions we will be using. None of this is 
permanent.

Add as you please, just add comments for clarity. 
"""

# universal constants
P_atm = 101.3 #kPa
g = 9.81 #m/s^2
pi = np.pi


# Bernoulli calculator for pressure at desired point:
def bernoulli(rho ,P1, V1, z1, V2, z2):
    """
    Inputs: density of fluid, initial pressure, initial velocity, initial height, final velocity, final height
    Output: final pressure
    """

    P2 = P1 + .5*rho*( V1**2 - V2**2) + rho*g*(z1 - z2)
    return P2

# Flow Continuity
def flow_continuity():
    pass

# Differential equation for pressure as a function of time. 
def differential_flow_eq(t_max, dt, rho, C, Q_in, Q_out, Q_leek, D_in, D_out, D_leek, A):

    """
    Inputs: Dimensions of setup, density of fluid, maximum time for running simulation, pressure coefficient, timestep duration
    Output: The pressure derivative as a function of time at all time points within the maximum time required. 
    """

    nt = np.floor(t_max/dt) # I'll put a better way to get the number of timesteps later
    P_prime = np.zeros(nt)
    const = (pi/ (4*A*rho*C))*(Q_in*D_in**2 - Q_out*D_out**2 - Q_leek*D_leek**2)

    for n in range(nt-1):
        P_prime[n] = const * (n * dt) # n*dt is the time
    return P_prime
