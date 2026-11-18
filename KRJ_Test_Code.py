#imports
import numpy as np
import matplotlib as plt
pi = np.pi
g = 9.81 #m/s^2
P_atm = 1 #Pa = N/m^2

#Inlet information
print("UPSTREAM INFO")
print()
print("Please select your upstream setup from the following:")
print("If you type A : An atmospheric fee resorvoir with a liquid supply pump")
print("If you type B : A gas-pressurized feed resorvoir")
Upstream_choice = input("Input Upstream Selection here: ")

P_atm_upstream = 0
def Upstream_setup(upstream_choice): #function to select upstream setup and get values
    if upstream_choice == 'A': #Upstream A
        P_atm_upstream = float(input("What is the atmospheric pressure? "))
        Pump_info = input("Pump info?? ") #what information do we need on the pump?
        return [P_atm_upstream, Pump_info]
    
    if upstream_choice == 'B': #Upstream B
        P_gas_initial = float(input("What is the initial gage pressure of the tank? "))
        Pump_info = input("Pump info??? ") # same question abt what pump info would be?
        return
    
    else:
        Upstream_choice = input("Your selection was not recognized, please input an upstream option: ")

Upstream_setup(Upstream_choice)

print()
#Outlet information
print("DOWNSTREAM INFO")
print()
print("Please select your downstream setup from the following:")
print("If you type A : An atmospheric collection resovoir")
print("If you type B : A withdrawal pump that sends effluent toward the ICP-MS")
Downstream_choice = input("Input Downstream Selection here: ")

def Downstream_setup(downstream_choice):
    if downstream_choice == 'A':
        P_atm_downstream = float(input("What is the atmospheric pressure? "))
        #how big are the tanks?????
        return
    
    if downstream_choice == 'B':
        Pump_data = input("What is pump? ")
        return
    
    else:
        Downstream_choice = input("Your selection was not recognized, please input a downstream option: ")

Downstream_setup(Downstream_choice)

print()
#given for main setup
print("DATA INPUTS")
print()

rho_in = float(input("Input density of fluid: "))

Q_in = float(input("Input Qin(t): ")) #m^3/s
P_in = float(input("Input Pin(t): ")) #Pa = N/m^s
C_in = float(input("Input Cin(t): "))
D_in = float(input("Input tube diameter in: ")) #meters
Theta_in = float(input("Input inlet tube angle: ")) #degrees
L_in = float(input("Input tube length in: ")) #meters
print()
Q_out = float(input("Input Qout(t): ")) #m^3/s
P_out = float(input("Input Pout(t): ")) #Pa = N/m^s
C_out = float(input("Input Cout(t): "))
D_out = float(input("Input tube diameter out: ")) #meters
Theta_out = float(input("Input outlet tube angle: ")) #degrees
L_out = float(input("Input tube length out: ")) #meters
print()
frict_coeff = float(input("Input coefficient of friction: "))
surface_tension = float(input("Input surface tension of fluid: "))
conc_in = float(input("Input initial ion concentration: "))

#starting equations
def Q_leak(Q_supply, Q_withdrawal): #continuity
  Leak = Q_supply - Q_withdrawal
  return Leak

def Pressure_bernoulli(P1, rho1, V1, z1): #bernoulli for one side
  Bernoulli = P1 + (1/2 * rho1 * V1 * V1) + (rho1 * g * z1)
  return Bernoulli

def Tube_Loss(u, l, d):
    P_loss_per_length = (128 * u * l)/(pi * (d**4))
    return P_loss_per_length #Pa/m

def PV_nRT(p, v, n, r, t): #gas equation for upstream A

#over the 5 points
A_tube1 = (pi/4) * (D_in * D_in)
A_in = (pi/4) *(D_in * D_in)
V_in = Q_in / A_in
z_in = (L_in) * (np.sin(Theta_in))
#find pressure at point 1
v1 = Q_in / A_tube1
z_1 = (1/2) * (np.sin(Theta_in))
tube_loss_1 = Tube_Loss(frict_coeff, L_in, D_in)
length_1 = L_in/2
bernoulli_1 = Pressure_bernoulli(P_in, rho_in, V_in, z_in)
Pressure_1 = bernoulli_1 - ((1/2) * rho_in * v1 * v1) - (rho_in * g * z_1) - (tube_loss_1 * length_1)

# Give answers
print()
print("Answers")
print()

print("Area of tube in:", A_in)
print("Area of tube 1:", A_tube1)
print("Height of z1:", z_1)
print("Bernoulli of point 1:", bernoulli_1)
print("Pressure at point 1:", Pressure_1)
