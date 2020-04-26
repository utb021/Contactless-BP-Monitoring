from scipy.signal import butter, lfilter, lfilter_zi
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import correlate

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    zi = lfilter_zi(b, a)
    y, z = lfilter(b, a, data, zi=zi*data[0])
    return y

def butter_bandpass(lowcut, highcut, fs, order=3):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def get_fourier_result (signal, period):
    complex_four = np.fft.fft(signal)
    spectra = np.absolute(complex_four)
    freqs = []
    for i in range(len(signal)):
        freqs.append(1/(period*len(signal))*i)
    return spectra, freqs

# def plot_spectrum(signal):
# 	time_old = np.arange(0, len(signal)/30, 1/30)
# 	C = abs(np.fft.fft(signal))
# 	freq = np.fft.fftfreq(len(time_old), d=1/30)
# 	plt.plot(freq, C)
# 	plt.show()
# 	return None

def plot_signal(signal):
	time = np.arange(0, len(signal)/30, 1/30)
	plt.plot(time, signal)
	plt.show()
	return None

def find_phase_shift(sig1, sig2, sig3, sig4, sig5):
	cross_corr1 = correlate(sig1, sig2, 'full', 'direct')
	cross_corr2 = correlate(sig2, sig3, 'full', 'direct')
	cross_corr3 = correlate(sig3, sig4, 'full', 'direct')
	cross_corr4 = correlate(sig4, sig5, 'full', 'direct')
	print(len(cross_corr1)/2 - np.argmax(cross_corr1), ' ',len(cross_corr2)/2 -  np.argmax(cross_corr2), ' ' ,len(cross_corr3)/2 -  np.argmax(cross_corr3), ' ',len(cross_corr4)/2 -  np.argmax(cross_corr4))
	return cross_corr4
