import cv2
from image_processor import *

def full_video_file_procedure(file_name):
	cap = cv2.VideoCapture(file_name)

	if cap.isOpened() == False:
		print('Porlems with file')
		return None

	signal = {0:[], 1:[], 2:[], 3:[], 4:[]}

	while cap.isOpened():
		ret, frame = cap.read()
		if ret == False:
			print('THE END')
			break
		# cv2.imshow('frame',frame)
		# if cv2.waitKey(1) & 0xFF == ord('q'):
		# 	break
		values = one_frame_procedure(frame)
		for i in range(5):
			signal[i].append(values[i])
	return signal

