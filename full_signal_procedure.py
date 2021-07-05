from general_math import *
from file_rw import *
import os
import heartpy as hp
import pandas as pd
from plot import *
from biosppy.signals.tools import filter_signal
import heartpy as hp
from scipy import signal

MEASUREMENTS_PATH = './contactless_signals'



def full_contact_signal_procedure(filename, sr=300):
	sig1, sig2 = read_file(filename)
	# sig1 = contact_signal_procedure(sig1, sr)
	# sig2 = contact_signal_procedure(sig2, sr)

	amp = 2 * np.sqrt(2)
	sig1 = butter_bandpass_filter(sig1, 0.75, 2.5, sr, 3)
	x = butter_bandpass_filter(sig2, 0.75, 2.5, sr, 3)
	print(x)

	with open('./eleman.txt', 'w') as f:
		for i in range(len(x)):
			row = str(x[i]) + ',' + '\t'
			f.write(row)


	f, t, Zxx = signal.stft(x, sr, nperseg=1000)
	plt.pcolormesh(t, f*60, np.abs(Zxx), vmin=0, vmax=amp, shading='gouraud')
	plt.title('STFT Magnitude')
	plt.ylabel('Frequency [Hz]')
	plt.xlabel('Time [sec]')
	plt.show()

	# PTT = get_phase_shift(sig1, sig2, sr)
	# PTT2 = lag_finder(sig1, sig2, sr)
	# plt.title(label = 'contact signal')
	# # plt.plot([i for i in range(len(sig1))], inverse_signal(sig1), color='green')
	# plt.plot([i for i in range(len(sig2))], inverse_signal(norm_signal(sig2)), color='red')
	# plt.show()
	# bpm1 = get_bpm(sig1, sr)
	# bpm2 = get_bpm(sig2, sr)
	# wd, m = hp.process(sig1, sample_rate = 300.0)
	# ibi = m['ibi']
	# print('bpm from first channel: ', bpm1)
	# print('bpm from second channel: ', bpm2)
	# print('ibi: ', ibi)
	return #bpm2, PTT2, ibi

def full_contactless_signal_procedure(filename, sr=60):
	sig1, sig2, full_sig = read_file_noncontact(filename, 0, 1)
	plt.xlabel('Отсчеты')
	plt.ylabel('Амплитуда')	
	plt.plot([i for i in range(len(sig1))], inverse_signal(norm_signal(sig1)), color='green')
	plt.show()	
	plt.xlabel('Отсчеты')
	plt.ylabel('Амплитуда')	
	plt.plot([i for i in range(len(sig1))], inverse_signal(norm_signal(sig2)), color='red')
	plt.show()	
	plt.xlabel('Отсчеты')
	plt.ylabel('Амплитуда')	
	plt.plot([i for i in range(len(sig1))], inverse_signal(norm_signal(full_sig)), color='blue')
	plt.show()	
	sig1 = contact_signal_procedure(sig1, sr)
	sig2 = contact_signal_procedure(sig2, sr)
	full_sig = contact_signal_procedure(full_sig, sr)
	full_sig = butter_bandpass_filter(full_sig, 0.75, 2.5, sr, 4)
	sig1 = butter_bandpass_filter(sig1, 0.75, 2.5, sr, 4)
	sig2 = butter_bandpass_filter(sig2, 0.75, 2.5, sr, 4)

	print(full_sig)


	bpms = []
	r = []
	g = []
	b = []
	with open('./Video.txt', 'r') as f:
		for row in f:
			row_splt = row.split(',')
			r.append(float(row_splt[1]))
			g.append(float(row_splt[2]))
			b.append(float(row_splt[3]))
	filtered_g = butter_bandpass_filter(g, 0.75, 2.5, 30, 5)
	plt.plot([i for i in range(len(filtered_g))], filtered_g, color='blue')
	plt.show()	
	for i in range(len(filtered_g) - 299):
		bpms.append(get_bpm(filtered_g[i:i+300], 30))
	plt.plot([i for i in range(len(bpms))], bpms)
	plt.show()	


	# PTT = get_phase_shift(sig1, sig2, sr)
	# PTT2 = lag_finder(sig1, sig2, sr)
	# plt.xlabel('Отсчеты')
	# plt.ylabel('Амплитуда')	
	# plt.plot([i for i in range(len(sig1))], inverse_signal(norm_signal(sig1)), color='green')
	# plt.show()	
	# plt.xlabel('Отсчеты')
	# plt.ylabel('Амплитуда')	
	# plt.plot([i for i in range(len(sig1))], inverse_signal(norm_signal(sig2)), color='red')
	# plt.show()
	# plt.xlabel('Отсчеты')
	# plt.ylabel('Амплитуда')	
	# plt.plot([i for i in range(len(sig1))], inverse_signal(norm_signal(sig1)), color='green')
	# plt.plot([i for i in range(len(sig1))], inverse_signal(norm_signal(sig2)), color='red')
	# plt.show()

	# bpm1 = get_bpm(sig1, sr)
	# bpm2 = get_bpm(sig2, sr)
	# bpm = get_bpm(full_sig, sr)
	# wd, m = hp.process(full_sig, sample_rate = sr)
	# ibi = m['ibi']
	# print('bpm from center roi: ', bpm)
	# print('bpm from first channel: ', bpm1)
	# print('bpm from second channel: ', bpm2)
	# print('ibi: ', ibi)
	# if bpm < bpm2:
	# 	bpm = bpm2
	return bpm, PTT2, ibi


def compare_signals_bpm(filename_contact, filename_noncontact, sr1=100, sr2=120):

	sig1, sig2 = read_file(filename_contact)
	vpg1, vpg2, vpg_center = read_file_noncontact(filename_noncontact, 0, 1)
	sig1, sig2 = filter_signals(sig1, sig2, 0.75, 2.5, sr1)
	vpg1, vpg2 = filter_signals(vpg1, vpg2, 0.75, 2.5, sr2)
	vpg_center = butter_bandpass_filter(vpg_center, 0.75, 2.5, sr2, order=5)

	bpm_cont = get_bpm(sig2, sr1)
	bpm_vpg = get_bpm(vpg_center,sr2)

	PTT_cont = lag_finder(sig1, sig2, sr1)
	PTT_vpg = lag_finder(vpg1, vpg2, sr2)

	measures = {'contact': [bpm_cont], 'noncontact': [bpm_vpg], 'PTT contact': [PTT_cont], 'PTT_vpg': [PTT_vpg]}
	df = pd.DataFrame(measures)
	print(df)
	return





# compare_signals_bpm('./contact_signals/Temirlan_120_c_3.txt', './contactless_signals/Temirlan_sm120_3_rPPG.txt')
# for file in os.listdir(MEASUREMENTS_PATH):
# 	if file[-1] == 't':
# 		print(file)
# 		full_contactless_signal_procedure(MEASUREMENTS_PATH + '/' + file)
# 		print()

full_contactless_signal_procedure('./contactless_signals/IMG_6298_rPPG.txt')


# full_contact_signal_procedure('./contact_signals/rtr.txt')

# bpm_cont = []
# bpm_vpg = []

# PTT_cont = []
# PTT_vpg = []

# IBI_cont = []
# IBI_vpg = []

# for file in os.listdir('./contact_signals'):
# 	for file_contactless in os.listdir('./contactless_signals'):
# 		if file[-5] == file_contactless[-10] and file[:3] == file_contactless[:3]:
# 			bpm_cont, bpm_vpg, PTT_cont, PTT_vpg, IBI_cont, IBI_vpg = compare_signals_bpm(file, file_contactless)





	




