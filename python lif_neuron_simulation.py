import numpy as np
import matplotlib.pyplot as plt
# Time parameters
dt = 1e-3          # Time step = 1 ms
T = 0.2            # Total simulation time = 200 ms
time = np.arange(0, T, dt)

# LIF neuron parameters
V_rest = 0.0       # Resting potential
V_reset = 0.0      # Reset potential
V_th = 1.0         # Threshold potential
tau = 20e-3        # Membrane time constant (20 ms)
R = 1.0            # Membrane resistance
I = np.ones(len(time)) * 1.2   # Constant current
V = np.zeros(len(time))        # Membrane potential
spike = np.zeros(len(time))    # Spike outputc
V[0] = V_rest                  # Initial voltage
for t in range(1, len(time)):
    # Update membrane potential
    V[t] = V[t-1] + (dt / tau) * (-(V[t-1] - V_rest) + R * I[t])

    # Spike generation
    if V[t] >= V_th:
        spike[t] = 1
        V[t] = V_reset


#LIF Neuron Membrane Potential
plt.figure(figsize=(10,4))
plt.plot(time*1000, V, label="Membrane Potential")
plt.axhline(V_th, color='r', linestyle='--', label="Threshold")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage")
plt.title("LIF Neuron Membrane Potential")
plt.legend()
plt.grid()
plt.show()




#Spike Train Output
plt.figure(figsize=(10,3))
plt.stem(time*1000, spike)
plt.xlabel("Time (ms)")
plt.ylabel("Spike")
plt.title("Spike Train Output")
plt.grid()
plt.show()
firing_rate = np.sum(spike) / T
print("Firing Rate:", firing_rate, "Hz")



#Simulate and Calculate Firing Rates
I_values = [0.6, 1.0, 1.4]
rates = []

for I_const in I_values:
    I = np.ones(len(time)) * I_const

    V = np.zeros(len(time))        # Membrane potential
    spike = np.zeros(len(time))    # Spike output
    V[0] = V_rest                  # Initial voltage

    for t in range(1, len(time)):
        # Update membrane potential
        V[t] = V[t-1] + (dt / tau) * (-(V[t-1] - V_rest) + R * I[t])

        # Spike generation
        if V[t] >= V_th:
            spike[t] = 1
            V[t] = V_reset

    firing_rate = np.sum(spike) / T
    rates.append(firing_rate)

print("Firing rates for different input currents:", rates)



#Plot Firing Rate vs. Input Current
plt.figure(figsize=(8, 5))
plt.plot(I_values, rates, 'o-')
plt.title('Firing Rate vs. Input Current')
plt.xlabel('Input Current (I)')
plt.ylabel('Firing Rate (Hz)')
plt.grid(True)
plt.show()
