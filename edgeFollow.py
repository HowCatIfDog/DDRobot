from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
import cv2
from matplotlib import pyplot as plt
import numpy as np

#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT =   8	# ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 20	# IN1 - Forward Drive
REVERSE_LEFT_PIN = 21	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT =   9  # ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 5	# IN1 - Forward Drive
REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive

STANDBY_PIN =       27  # High enables moving

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)
standby = PWMOutputDevice(STANDBY_PIN)

def allStop():
	forwardLeft.value = False
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = False
	driveLeft.value = 0
	driveRight.value = 0

def forwardDrive():
	print("going forward")
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.7
	driveRight.value = 0.7

def reverseDrive():
	print("going backwards")
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0

def spinLeft():
	print("spin left")
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1.0
	driveRight.value = 1.0

def SpinRight():
	print("spin right")
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0

def forwardTurnLeft():
	print("forward turn left")
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.2
	driveRight.value = 0.8

def forwardTurnRight():
	print("forward turn right")
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.8
	driveRight.value = 0.2

def reverseTurnLeft():
	print("reverse turn left")
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.2
	driveRight.value = 0.8

def reverseTurnRight():
	print("reverse turn right")
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.8
	driveRight.value = 0.2

def updatePWM(right, left):
	driveLeft.value = left;
	driveRight.value = right;

# set the maximum value that you can threshhold (255 white)
alpha_slider_max = 255

# name of the window being outputed
title_window = 'Contour Tresh'

# initalize the array that will store the 2 pixel values needed
# for comparison
areaArray = [0,0]

cap = cv2.VideoCapture(0)

# the function called for utilizing the trackbar (implementaion below)
def passfunc(val):
	pass

# set the trackbar name
trackbar_name = "Threshold"

# name the window what the title name is above
cv2.namedWindow(title_window, cv2.WINDOW_NORMAL)

cv2.createTrackbar(trackbar_name, title_window , 0, 	alpha_slider_max, passfunc)

left = 0.5
right =0.5
forwardDrive()
Kp = 1.0

while(True):
	# read the image in (note) needs to be swapped over to video but
	# is fine rn for testing on a static image
	ret, image = cap.read()

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# blur the image to get some of the garbage out
	gray = cv2.GaussianBlur(gray,(5,5),0)

	# create the trackbar that updates everytime you move it to a new
	# position and calls the on_trackbar function
	N = cv2.getTrackbarPos(trackbar_name, title_window)

	# threshold the given image at the value from the trackbar
	th, im_th = cv2.threshold(gray, N, 255, cv2.THRESH_BINARY);

	# copy the original imae into the floodfill images used to fill
   # holes in the image
	im_floodfill = im_th.copy()
	im_floodfill1 = im_th.copy()

	# get the height and width of the image
	h, w = im_th.shape[:2]

	# make the mask needed for the floodfill operation. Needs to
	# be 2 more than the height and width for the floodfill func
	mask = np.zeros((h+2, w+2), np.uint8)

	# Floodfill from point (0, 0)
	cv2.floodFill(im_floodfill, mask, (0,0), 255);

	# Floodfill from point (w - 2,0) idk why it is minus 2 but it
	# yelled at me until I did minus 2
	cv2.floodFill(im_floodfill1, mask, (w - 2,0), 255);

	# bitwise or the first floodfill and & the next.
	# (note) might want o check if it is doing the correct thing
	im_out = im_th | im_floodfill

	im_out = im_th & im_floodfill1

	# inverse the image so that the area outside the path is white

	# show the image in the window with the trackbar
	cv2.imshow(title_window, im_out)

	total = im_out.size
	whitePixels = cv2.countNonZero(im_out)
	ratio = whitePixels/total
	left += ratio*Kp
	right += -ratio*kp
	updatePWM(right, left)
	print(ratio)
	#return ratio
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break



cap.release()
cv2.destroyAllWindows()
