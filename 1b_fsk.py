# Source: https://www.rfwireless-world.com/source-code/Python/FSK-modulation-python-code.html

import matplotlib.pyplot as plt
import numpy as np
from binarygen import binary
from math import pi
plt.close('all')

# Carrier wave and binary signal configuration parameters
Fs = 1000 # Samples per second
fc = 30 # Carrier frequency 30 Hz, 30 cycles/sec
T = 1 # Total simulation time in seconds, 1sec
t = np.arange(0, T, 1/Fs)
Td = 0.1 # Bit duration
Nsamples = int(Td*Fs) # Samples in one bit duration
Nsym = int(np.floor(np.size(t)/Nsamples))
# Binary waveform generation
sig = binary(Nsym,Nsamples)
# FSK waveform generation
f = fc + fc*sig/2
Xfsk = np.sin(2*pi*f*t)
# Binary waveform and FSK modulation waveform Plots
figure, axis = plt.subplots(2)
axis[0].plot(t, sig)
axis[0].set_title("Binary digital data")
axis[1].plot(t, Xfsk, 'r')
axis[1].set_title("FSK modulated signal")
plt.tight_layout()
plt.show()
