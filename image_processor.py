import cv2
import numpy as np


def full_frame_procedure(frame, N):

	one_frame_values = []

	skin = detect_skin(frame)
	
	segmented_parts = frame_2_part_segmentor(skin, N)

	for segment in segmented_parts:
		val = get_1vpg_val(segment)
		one_frame_values.append(val)

	center_roi = get_center_roi(skin)
	center_roi_val = get_1vpg_val(center_roi)

	return one_frame_values, skin, center_roi_val, segmented_parts, center_roi


def detect_skin(frame):
	lower = np.array([0, 48, 80], dtype = "uint8")
	upper = np.array([20, 255, 255], dtype = "uint8")
	converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	skinMask = cv2.inRange(converted, lower, upper)
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
	skinMask = cv2.erode(skinMask, kernel, iterations = 2)
	skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
	skin = cv2.bitwise_and(frame, frame, mask = skinMask)
	# cv2.imshow('converted', converted)
	# cv2.imshow('skinMask', skinMask)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	return skin

def frame_segmentor(frame, N):
	'''roi = image[startY:endY, startX:endX]'''
	height = frame.shape[0]
	width = frame.shape[1]

	startY = 0
	endY = height
	startX = [i * (width/N) for i in range(N)]
	endX = [i * (width/N) for i in range(1, N+1)]

	segmented_parts = []
	for i in range(N):
		segmented_parts.append(frame[startY:endY, int(startX[i]):int(endX[i])])

	return segmented_parts

def frame_2_part_segmentor(frame, N):
	'''returns only first and last parts'''
	height = frame.shape[0]
	width = frame.shape[1]

	startY = 0
	endY = height
	endX_1 = width/N
	startX_2 = width - (width/N)

	segmented_parts = []

	# first_part = frame[startY:endY, 0:int(endX_1)]
	# second_part = frame[startY:endY,  int(startX_2):width]
	first_part = frame[startY:endY, 100:int(endX_1)+100]
	second_part = frame[startY:endY,  int(startX_2):width]
	# first_part = frame[int(height/2  - (0.05*height)):int(height/2 + (0.05*height)), 0:int(0.1*width)]
	# second_part = frame[int(height/2  - (0.05*height)):int(height/2 + (0.05*height)),  int(width - 0.1*width):int(width)]

	segmented_parts.append(first_part)
	segmented_parts.append(second_part)

	return(segmented_parts)

def get_1vpg_val(skin):
	green_channel = skin[:, :, 1]
	blue_channel = skin[:, :, 0]
	red_channel = skin[:, :, 2]

	NonZero_G = green_channel[np.nonzero(green_channel)]
	NonZero_B = blue_channel[np.nonzero(blue_channel)]
	NonZero_R = red_channel[np.nonzero(red_channel)]


	one_vpg_val = NonZero_G.mean() / (NonZero_B.mean() + NonZero_R.mean())

	return one_vpg_val

def get_center_roi(skin):
	# height = skin.shape[0]
	# width = skin.shape[1]
	# startY = 0
	# endY = height
	# center_roi = skin[startY:endY, int(0.4*width):int(0.6*width)]


	height = skin.shape[0]
	width = skin.shape[1]
	startY = int(height/2  - (0.05*height))
	endY = int(height/2 + (0.05*height))
	center_roi = skin[startY:endY, int(0.45*width):int(0.55*width)]
	return center_roi


def get_1vpg_gray(skin):

    gray = cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)
    roi = gray
    ## end Roi

    # Find intensity (average or median or sum?)
    rowSum = np.sum(roi, axis=0)
    colSum = np.sum(rowSum, axis=0)
    allSum = rowSum + colSum

    intensity = np.median(np.median(allSum))

    # intensity = np.mean(roi)
    
    return intensity





