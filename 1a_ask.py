# Source: https://www.rfwireless-world.com/source-code/Python/ASK-modulation-python-code.html

import matplotlib.pyplot as plt
import numpy as np
from binarygen import binary
from math import pi
plt.close('all')

# Carrier wave and binary waveform configuration parameters
Fs = 1000 # Samples per second
fc = 25 # Carrier frequency 100 Hz, 100 cycles/sec
T = 1 # Total simulation time in seconds
t = np.arange(0, T, 1/Fs)
x =np.sin(2*pi*fc*t)
Td = 0.1 # Bit duration
Nsamples = int(Td*Fs) # Samples in one bit duration = 100
Nsym = int(np.floor(np.size(t)/Nsamples)) # = 10

# Python code to generate binary stream of data
sig = binary(Nsym, Nsamples)

# ASK waveform generation
Xask = x * sig

# Binary waveform and ASK waveform Plots
figure, axis = plt.subplots(2)
axis[0].plot(t,sig)
axis[0].set_title("Binary digital data")
axis[1].plot(t, Xask)
axis[1].set_title("ASK modulated signal")
plt.tight_layout()
plt.show()