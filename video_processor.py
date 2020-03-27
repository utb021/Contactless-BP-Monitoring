import cv2
from image_processor import *

def full_video_file_procedure(file_name):

	cap = cv2.VideoCapture(file_name)

	if cap.isOpened() == False:
		print('Porlems with file')
		return None

	signal = []
	while cap.isOpened():
		ret, frame = cap.read()

		if ret == False:
			print('THE END')
			break
		cv2.imshow("disp", frame)
		values = one_frame_procedure(frame)
		signal.append(values)
	return signal[:5]
