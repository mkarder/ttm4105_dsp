# DSP assignment draft
## Overview
1. Shift keying - Encode data to a carrier 
    - ASK
    - FSK
    - PSK   
2. IQ plots
3. QAM: combining ASK and PSK
4. Adding noise to the picture
5. Accounting for noise - channel coding
    - CRC
    - FEC
    - RS-codes
6. End-to-end example
    - Modulation
    - Demoudlation 

Consider adding:
- Decibels (DB) 
- Signal budget 
- Multipath fading, OFDM
- Time synchronization 

## 0 Sending bits in electrical currents
- Representing 1 or 0 through e.g., voltage
Showcase how we can represent information through an electric current

## 1 Shift keying
- A sequence of bits we want to send, e.g. [1,0,1,1,1,0,0,0,1,1,0]
- How can we create a nice task for them to encode this to a carrier?
    - What can we change about a wave to make it represent a 1 or 0?

Showcase how we can use the same concept to modulate a carrier to hold information.
Might have to introduce the concept sampling at a point.

### 1a ASK
- Use amplitude as reference
- Consider adding several levels of amplitude to showcase that we can represent more than one bit of information.
    - Concept of a symbol
    - Consider showcasing how adding more levels of measurement adds need for more exact measurements.

### 1b FSK
- Same concept as ASK, but now for frequency

### 1c PSK
- Same concept as ASK, but now for phase

## 2 IQ sampling & plotting

### 2a IQ sampling
- Concept of representing a wave as an an I and Q part
- Not too theoretical, but enough to give them a simple understanding before delving into IQ-plotting

### 2b IQ plotting
- Showcase how we an represent a signal based on a varying number of symbols
- BPSK QPSK and 8-PSK

## 3 QAM
- Make them modulate information through a combination of phase and amplitude

## 4 Noise
- Showcase how noise will affect our plots
- Example using QPSK and QAM
    - Se how the plots differ based on level of noise

## 5 Channel coding
- Showcase how we can use channel coding to account for errors due to noise
- Mainly focus on FEC?
- Takeaway from this should be how the complexity of the modulation is affected by level of noise
    - Should understand that increased noise results in increased need of channel coding
    - At a certain point we would like to revert to a lower complexity modulation scheme

##  6 End-to-end 
- Putting it all together
- Have a practical example where we:  
    1. Encode a audio file to bits (sampling)
    2. Create a signal by modulating the bits to a carrier
    3. Send the results over a (possible noisy) channel
    4. Receive the signal
    5. Demodulate the signal and translate it into a audio file
- Might have to translate or provide a way to convert a audio file to .iq file
- Consider having them compare the use of of different schemes and how they can reduce the amount of information sent but also how they compare in terms of robustness (i.e., ability to handle noise)

### 6a Modulation
- Build a modulation scheme, providing own parameters such as sampling frequency, carrier frequency, modulation complexity (number of symbols) etc.

### 6b Demodulation
- Build a demodulation scheme, reversing the modulation steps in order to reconstruct the original information (audio file)
