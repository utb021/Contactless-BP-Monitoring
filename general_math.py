from scipy.signal import butter, lfilter, lfilter_zi, filtfilt
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from peakdetect import peakdetect
from scipy.interpolate import interp1d


def contact_signal_procedure(ch1, sr):
    ch2 = interpolate(ch1, 1)
    ch3 = butter_bandpass_filter(ch1, 0.75, 2.5 , sr, 3)
    ch4 = normalize(ch3)
    return ch4

def interpolate(signal,factor):
    x = np.arange(0,len(signal))
    INT = interp1d(x,signal)
    x = np.arange(0,len(signal)-1,1/factor)
    signal = INT(x)
    return np.asarray(signal)

def butter_bandpass(lowcut, highcut, fs, order=3):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    zi = lfilter_zi(b, a)
    y, z = lfilter(b, a, data, zi=zi*data[0])
    return y


def normalize(signal):
    signal = signal - np.mean(signal)
    s = signal / np.max(np.abs(signal))
    return s

def inverse_signal(signal): # type  of ppg is np.array
	signal = np.array(signal)
	new_vpg = []
	moda = sum(signal)/len(signal)
	for i in -signal:
		new_vpg.append(i + 2*moda)
	return new_vpg

def norm_signal(sp):
    max = np.max(sp)
    norm = []
    for i in range(len(sp)):
        norm.append(sp[i] / max)
    return norm


def get_phase_shift(sig1, sig2, sr):
    cross_corr = signal.correlate(sig2, sig1, 'full', 'direct')
    shift = np.argmax(cross_corr) - len(sig1)
    plt.plot([i for i in range(len(cross_corr))], cross_corr)
    plt.show()
    print('Time delay is ', shift/sr)
    return shift/sr


def get_bpm(signal, sr):
    signal = np.array(signal)
    fourier_transform = np.fft.rfft(signal)
    abs_fourier_transform = np.abs(fourier_transform)
    power_spectrum = np.square(abs_fourier_transform)
    frequency = np.linspace(0, sr/2, len(power_spectrum))
    ind_of_max_arg = np.argmax(power_spectrum)
    hr = frequency[ind_of_max_arg]
    bpm = hr*60
    # plt.xlabel("Частота, Гц")
    # plt.ylabel("Амплитуда")
    # plt.plot(frequency, power_spectrum)
    # plt.show()
    return bpm

def lag_finder(y1, y2, sr):
    n = len(y1)

    corr = signal.correlate(y2, y1, mode='same') / np.sqrt(signal.correlate(y1, y1, mode='same')[int(n/2)] * signal.correlate(y2, y2, mode='same')[int(n/2)])

    delay_arr = np.linspace(-0.5*n/sr, 0.5*n/sr, n)
    delay = delay_arr[np.argmax(corr)]
    print('y2 is ' + str(delay) + ' behind y1')

    # plt.figure()
    # plt.plot(delay_arr, corr)
    # plt.title('Lag: ' + str(np.round(delay, 3)) + ' s')
    # plt.xlabel('Lag')
    # plt.ylabel('Correlation coeff')
    # plt.show()
    return delay



