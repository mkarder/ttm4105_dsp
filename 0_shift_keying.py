"""
Input: consider put a task:
 analog signal
 sampling
 quantization (?)
 Translate a sound to voltages

 Frequency of (audio) sampling: Nyquist sampling
 - Supply a FFT-functionality to  
 - Think of a 
"""

import numpy as np
import matplotlib.pyplot as plt

bits = [0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1]
sampling_freq = 0.1

# Calculate time values based on the sampling frequency
time_values = np.arange(0, len(bits) * sampling_freq, sampling_freq)

# Create voltage values based on the bit values
voltage_values = [1 if bit == 0 else 2 for bit in bits]

# Plot the voltage graph
plt.step(time_values, voltage_values, where='post', color='b', linewidth=2)

# Annotate the bit values on top of the graph
for i, bit in enumerate(bits):
    plt.text(time_values[i] + sampling_freq/4, voltage_values[i] + 0.1, str(bit), color='r')

plt.xlabel('Time (seconds)')
plt.ylabel('Voltage')
plt.title('Voltage Graph for Bits')
plt.ylim(0, 3)  # Set y-axis limits
plt.grid(True)
plt.show()

