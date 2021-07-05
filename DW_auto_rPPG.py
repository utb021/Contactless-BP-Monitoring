import os
from video_processor import *
from image_processor import *
from file_rw import *

VIDEO_PATH = './videos'
MEASUREMENTS_PATH = './contactless_signals'

print(os.listdir(VIDEO_PATH))

for file in os.listdir(VIDEO_PATH):

	if file == '.DS_Store':
		continue

	# input('enter to continue')

	file_name = MEASUREMENTS_PATH + '/' + file[:-4] + '_rPPG' + '.txt'

	only_name = file[:-4] + '_rPPG' + '.txt'
	if only_name in os.listdir(MEASUREMENTS_PATH):
		print('{} has arlready been DONE!'.format(only_name))
		continue

	else:
		print('Processing {}'.format(file))
		signals, center_roi_vpg = full_video_file_procedure(VIDEO_PATH + '/' + file)
		write_file_noncontact(file_name, signals, center_roi_vpg)






