from video_processor import *
from image_processor import *
from general_math import*
import matplotlib.pyplot as plt
import numpy as np

PATH = 'IMG_0672.MOV'




signal = full_video_file_procedure(PATH)


part_1 = signal[0]
part_2 = signal[1]
part_3 = signal[2]
part_4 = signal[3]
part_5 = signal[4]




time = np.arange(0, len(part_1)/30, 1/30)

p1, p2, sh = full_signals_procedure(part_5, part_1)

print(np.corrcoef(p1, p2))

print(sh)
plt.plot(time, p1)
plt.plot(time, p2)
plt.show()


