import math
import numpy as np
import matplotlib.pyplot as plt

Vol_tot = (math.pi*D_in**2/4) * L_in + (math.pi*D_out**2.4) * L_out
Vol_path = (math.pi*D_icp**2/4) * L_icp

t_fill = Vol_tot / Q_out
tau = Vol_path / Q_out

def C_out_eqn(t):
    conditions = [t <= t_fill, t > t_fill]
    functions = [0, C_out]
    return np.piecewise(t, conditions, functions)

def C_icp_eqn(t):
  conditions = [t <= t_fill + tau, t > t_fill + tau]
  functions = [0, C_out]
  return np.piecewise(t, conditions, functions)


t_max = 1.5 * (t_fill + tau) # max time for graphing, 150% of time required for concentration to reach icp inlet

t = np.linspace(0, t_max, 1000) # timestep, seconds
y1 = C_in * np.ones(1000)
y2 = C_out_eqn(t)
y3 = C_icp_eqn(t)

plt.plot(t, y1, label="C_in")
plt.plot(t, y2, label="C_out")
plt.plot(t, y3, label="C_icp")
plt.text(t_fill, 0, "t_fill")
plt.text(t_fill + tau, 0, "t_fill + tau")
plt.title("concentration at specificed points (inlet, outlet, icp inlet)")
plt.legend()
