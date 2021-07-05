''' This part of code extracts frames from the video. 
Then frames are processed by 'image_processor.py'
All signals are stored in vpg_signals '''

import cv2
from image_processor import *


global N 
#N = 20 # The number of parts segmented in video file

def full_video_file_procedure(file_name):
	cap = cv2.VideoCapture(file_name)

	if cap.isOpened() == False:
		print('The file can not be opened. Check the file.')
		return None
	# Generation of dict.Key is num of part. Value is vpg from each part	
	method = '2'
	N = 20

	if method == 'N':
		vpg_signals = dict.fromkeys([i for i in range(N)])
		center_roi_vpg = []
		for i in range(N):
			vpg_signals[i] = []

	elif method == '2':
		vpg_signals = {0:[], 1:[]}
		center_roi_vpg = []

			
	while cap.isOpened():
		ret, frame = cap.read()
		if ret == False:
			print('Finish')
			break

		one_frame_values, skin, center_roi_val, segmented_parts, center_roi = full_frame_procedure(frame, N)
		center_roi_vpg.append(center_roi_val)
		
		if method == 'N':
			for i in range(N):
				vpg_signals[i].append(one_frame_values[i])
		elif method == '2':
			for i in range(2):
				vpg_signals[i].append(one_frame_values[i])


		cv2.imshow('skin', skin)
		cv2.imshow('seg1', segmented_parts[0])
		cv2.imshow('seg2', segmented_parts[1])
		cv2.imshow('center_roi', center_roi)


		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	return vpg_signals, center_roi_vpg



