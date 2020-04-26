from video_processor import *
from image_processor import *
from general_math import*
import matplotlib.pyplot as plt

PATH = '/home/temirlan/Документы/IMG_0672.MOV'




signal = full_video_file_procedure(PATH)


part_1 = signal[0]
part_2 = signal[1]
part_3 = signal[2]
part_4 = signal[3]
part_5 = signal[4]

part_1_f = butter_bandpass_filter(part_1, 0.8, 4, 30)
part_2_f = butter_bandpass_filter(part_2, 0.8, 4, 30)
part_3_f = butter_bandpass_filter(part_3, 0.8, 4, 30)
part_4_f = butter_bandpass_filter(part_4, 0.8, 4, 30)
part_5_f = butter_bandpass_filter(part_5, 0.8, 4, 30)

cross_corr4 = find_phase_shift(part_1_f, part_2_f, part_3_f, part_4_f, part_5_f)


# spectra, freqs = get_fourier_result(filtered_signal, 1/30)
time = np.arange(0, len(part_1_f)/30, 1/30)
plt.plot([i for i in range(len(cross_corr4))], cross_corr4)
# plt.plot(time, part_1_f)
# plt.plot(time, part_5_f)
plt.show()
