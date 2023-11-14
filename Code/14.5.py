import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load audio file
y, sr = librosa.load('ITDS\Week8\\1.mp3')

# Perform FFT
fft_result = np.fft.fft(y)

# Calculate frequency values corresponding to the FFT components
freq = np.fft.fftfreq(len(y), 1/sr)

# Plot the log-amplitude spectrum
plt.plot(freq, 20 * np.log10(np.abs(fft_result)))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Log-Amplitude Spectrum (dB)')
plt.title('Spectrum of the Audio Signal')
plt.show()
