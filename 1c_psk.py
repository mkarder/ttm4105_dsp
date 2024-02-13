# Stole from https://www.rfwireless-world.com/source-code/Python/PSK-modulation-python-code.html

import matplotlib.pyplot as plt
import numpy as np
from binarygen import binary
from math import pi
plt.close('all')

# Carrier wave and binary signal configuration parameters
Fs = 1000 # Samples per second
fc = 50 # Carrier frequency 50 Hz, 50 cycles/sec
T = 1 # Total simulation time in seconds
t = np.arange(0, T, 1/Fs)
Td = 0.1 # Bit duration
Nsamples = int(Td*Fs) # Samples in one bit duration
Nsym = int(np.floor(np.size(t)/Nsamples))

# Binary waveform generation
sig = binary(Nsym,Nsamples)

# PSK waveform generation
phase= pi + pi*sig/2
Xpsk = np.sin(2*pi*fc*t + phase)

# Binary waveform and PSK modulation waveform Plots
figure, axis = plt.subplots(2)
axis[0].plot(t, sig)
axis[0].set_title("Binary digital data")
axis[1].plot(t, Xpsk, 'r')
axis[1].set_title("PSK modulated signal")
plt.tight_layout()
plt.show()