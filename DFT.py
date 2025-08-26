import numpy as np
import matplotlib.pyplot as plt

# Generate sample signal
def generate_signal(frequencies, sample_rate, duration):
    t = np.arange(0, duration, 1/sample_rate)  # Time vector
    signal = sum(np.sin(2 * np.pi * f * t) for f in frequencies)  # Sum of sinusoids
    return t, signal

# Compute the DFT Using FFT
def compute_dft(signal):
    return np.fft.fft(signal)  # Compute the FFT of the signal


def compute_idft(dft_signal):
    return np.fft.ifft(dft_signal)  # Compute the inverse FFT to get the time-domain signal back

# Parameters
sample_rate = 1000  # Sampling frequency in Hz
duration = 1.0      # Duration in seconds
frequencies = [50, 150]  # Frequencies of the signal components in Hz

# Generate the signal
t, signal = generate_signal(frequencies, sample_rate, duration)

# Compute DFT
dft_signal = compute_dft(signal)
frequencies_dft = np.fft.fftfreq(len(dft_signal), 1/sample_rate)

# Compute IDFT to verify
idft_signal = compute_idft(dft_signal)

# Plotting
plt.figure(figsize=(14, 6))

# Original Signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# DFT Magnitude Spectrum
plt.subplot(2, 1, 2)
plt.stem(frequencies_dft[:len(frequencies_dft)//2], np.abs(dft_signal[:len(dft_signal)//2]),)
plt.title('DFT Magnitude Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
