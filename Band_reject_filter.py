import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

def band_reject_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='bandstop')
    y = lfilter(b, a, data)
    return y

def generate_sample_signal(fs, T, f0, f1):
    t = np.arange(0, T, 1/fs)
    signal = 0.5 * np.sin(2 * np.pi * f0 * t) + 0.5 * np.sin(2 * np.pi * f1 * t)
    return t, signal

# Define parameters
fs = 1000.0       # Sampling frequency in Hz
T = 1.0           # Duration in seconds
f0 = 50.0         # Frequency of first sine wave in Hz
f1 = 200.0        # Frequency of second sine wave in Hz
lowcut = 45.0     # Lower cutoff frequency in Hz
highcut = 55.0    # Upper cutoff frequency in Hz

# Generate sample signal
t, signal = generate_sample_signal(fs, T, f0, f1)

# Apply band reject filter
filtered_signal = band_reject_filter(signal, lowcut, highcut, fs)

# Plot results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal)
plt.title('Filtered Signal (Band Reject)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
