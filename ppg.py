import numpy as np
import cv2
import matplotlib.pyplot as plt

PATH = './IMG_0672.MOV'

def full_video_file_procedure(file_name):

	cap = cv2.VideoCapture(file_name)

	if cap.isOpened() == False:
		print('Porlems with file')
		return None

	signal = []
	while cap.isOpened():
		ret, frame = cap.read()
		if ret == Flase:
			print('THE END')
			break
		value = one_frame_procedure(frame)
		signal.append(value)
	return signal

def one_frame_procedure(frame):
	skin = detect_skin(frame)
	value = calculate_average_green(skin)
	return value

def detect_skin(frame):
	min_YCrCb = np.array([0,133,77],np.uint8)
	max_YCrCb = np.array([255,173,127],np.uint8)
	imageYCrCb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)
	skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)
	contours, hierarchy = cv2.findContours(skinRegion.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for i, c in enumerate(contours):
		area = cv2.contourArea(c)
		if area > 400000:
			masked_img = frame.copy()
			cv2.fillPoly(frame, contours, [0, 0, 0])
			skin = masked_img - frame #skin and black background
	return skin

def calculate_average_green(skin):
	

