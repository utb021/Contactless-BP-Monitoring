import matplotlib.pyplot as plt
import numpy as np
from general_math import *

def plot_signal(signal, sr):
	time = np.arange(0, len(signal)/sr, 1/sr)
	plt.plot(time, signal, color = "green")	
	plt.show()
	return


def plot_2_signals(sig1, sig2, sr):
	time = np.linspace(0, len(sig1)/sr, len(sig1))
	plt.plot(time, sig1, color = "green")	
	plt.plot(time, sig2, color = "red")
	plt.show()
	return

def plot_vpg_peaks(signal, peaks_max_ind, peaks_max):
	time = np.arange(0, len(signal)/59.96, 1/59.96)
	plt.plot([i for i in range(len(signal))], signal, color = "green")	
	plt.plot(peaks_max_ind, peaks_max, 'o')
	plt.show()
	return

def plot_spectrum(signal):
	fourier_transform = np.fft.rfft(signal)
	abs_fourier_transform = np.abs(fourier_transform)
	power_spectrum = np.square(abs_fourier_transform)
	frequency = np.linspace(0, 59.96/2, len(power_spectrum))
	ind_of_max_arg = np.argmax(power_spectrum)
	hr = frequency[ind_of_max_arg]
	print('heart rate is equal ', hr*60, ' bpm')
	plt.plot(frequency, power_spectrum)
	plt.show()
	return




