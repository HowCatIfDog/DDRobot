<<<<<<< HEAD
def Ratio():
	import cv2
	from matplotlib import pyplot as plt
	import numpy as np

	# set the maximum value that you can threshhold (255 white)
	alpha_slider_max = 255

	# name of the window being outputed
	title_window = 'Contour Tresh'

	# initalize the array that will store the 2 pixel values needed
	# for comparison
	areaArray = [0,0]



	# read the image in (note) needs to be swapped over to video but
	# is fine rn for testing on a static image
	image = cv2.imread('/home/pi/Documents/DDRobot/sidewalk.jpg',cv2.IMREAD_GRAYSCALE)
	#image = cv2.imread('/home/sriddick/Documents/Final_Project/DDRobot/refpic2.jpg',cv2.IMREAD_GRAYSCALE)

	# blur the image to get some of the garbage out
	image = cv2.GaussianBlur(image,(5,5),0)

	# name the window what the title name is above
	cv2.namedWindow(title_window)

	# set the trackbar name
	trackbar_name = "Threshold"

	# create the trackbar that updates everytime you move it to a new
	# position and calls the on_trackbar function
	cv2.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)

	# Show the starting image
	on_trackbar(0)

	# Wait until user press some key to quit
	cv2.waitKey()


	# the function called for utilizing the trackbar (implementaion below)
	def on_trackbar(N):

		# threshold the given image at the value from the trackbar
		th, im_th = cv2.threshold(image, N, 255, cv2.THRESH_BINARY);

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
		im_out = cv2.bitwise_not(im_out)

		total = im_out.total()
		whitePixels = countNonZero(im_out)
		ratio = whitePixels/total
		return ratio

		# # show the image in the window with the trackbar
		# cv2.imshow(title_window, im_out)
		#
		# # find the contours of the image
		# contours, hierarchy = cv2.findContours(im_out,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		# j = 0
		# # find the areas of the contours
		# for i in range(len(contours)):
		# 	cnt = contours[i]
		# 	area = cv2.contourArea(cnt)
		#
		# 	# check to see if the contours are greater than 1000
		# 	# in order to get rid of the contours not needed
		# 	# (note) no error checking rn so until it gets to the point
		# 	# where there is realitevly 2 distinct contours it throws
		# 	# some wack shit
		# 	if(area > 1000):
		# 		areaArray[j] = area
		# 		j = j+1
		#
		# # output the areas to the screen
		# for k in range(len(areaArray)):
		# 	print(areaArray[k])
=======
import cv2
from matplotlib import pyplot as plt
import numpy as np

# set the maximum value that you can threshhold (255 white)
alpha_slider_max = 255

# name of the window being outputed
title_window = 'Contour Tresh'

# initalize the array that will store the 2 pixel values needed
# for comparison
areaArray = [0,0]

# the function called for utilizing the trackbar (implementaion below)
def on_trackbar(N):
	
	# threshold the given image at the value from the trackbar
	th, im_th = cv2.threshold(image, N, 255, cv2.THRESH_BINARY);

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
	
	# show the image in the window with the trackbar
	cv2.imshow(title_window, im_out)

	# find the contours of the image
	contours, hierarchy = cv2.findContours(im_out,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	j = 0
	# find the areas of the contours
	for i in range(len(contours)):
		cnt = contours[i]
		area = cv2.contourArea(cnt)
		
		# check to see if the contours are greater than 1000
		# in order to get rid of the contours not needed
		# (note) no error checking rn so until it gets to the point
		# where there is realitevly 2 distinct contours it throws 
		# some wack shit
		if(area > 1000):
			areaArray[j] = area
			j = j+1

	# output the areas to the screen
	for k in range(len(areaArray)):
		print(areaArray[k])

# read the image in (note) needs to be swapped over to video but
# is fine rn for testing on a static image
image = cv2.imread('/home/pi/Documents/DDRobot/darkTest8.jpg',cv2.IMREAD_GRAYSCALE)
#image = cv2.imread('/home/sriddick/Documents/Final_Project/DDRobot/refpic2.jpg',cv2.IMREAD_GRAYSCALE)

# blur the image to get some of the garbage out
image = cv2.GaussianBlur(image,(5,5),0)

# name the window what the title name is above
cv2.namedWindow(title_window, cv2.WINDOW_NORMAL)

# set the trackbar name
trackbar_name = "Threshold"

# create the trackbar that updates everytime you move it to a new
# position and calls the on_trackbar function
cv2.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)

# Show the starting image
on_trackbar(0)

# Wait until user press some key to quit
cv2.waitKey()
>>>>>>> cdfea7ef8a32bdb38dfc3131bc6aaf7953375e1e
