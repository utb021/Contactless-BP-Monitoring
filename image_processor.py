import numpy as np
import cv2


def one_frame_procedure(frame):
	skin = detect_skin(frame)
	values = []
	
	for part in divide_into_5_parts(skin):
		value = calculate_average_green(part)
		values.append(value)

	return values

def detect_skin(frame):
	min_YCrCb = np.array([0,133,77],np.uint8)
	max_YCrCb = np.array([255,173,127],np.uint8)
	imageYCrCb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)
	skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)
	contours, hierarchy = cv2.findContours(skinRegion.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	for i, c in enumerate(contours):

		area = cv2.contourArea(c)
		if area > 400000:


			cv2.drawContours(frame, contours, -1, (0, 255, 0), 3) 
			cv2.imshow('Contours', frame) 
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

			masked_img = frame.copy()
			cv2.fillPoly(frame, contours, [0, 0, 0])
			skin = masked_img - frame #skin and black background



	return skin

def calculate_average_green(skin):
	green_channel = skin[:, :, 1]
	NonZero_G = green_channel[np.nonzero(green_channel)]
	average_green = NonZero_G.mean()
	return average_green

def divide_into_5_parts(frame):
	part_1 = frame[0:720, 0:256]
	part_2 = frame[0:720, 256:512]
	part_3 = frame[0:720, 512:768]
	part_4 = frame[0:720, 768:1024]
	part_5 = frame[0:720, 1024:1280]
	return part_1, part_2, part_3, part_4, part_5



