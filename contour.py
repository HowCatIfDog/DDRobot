import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread('/home/seth/Robotics/DDRobot/sidewalk.jpg',cv2.IMREAD_GRAYSCALE)

image = cv2.GaussianBlur(image,(5,5),0)

plt.subplot(211),plt.imshow(image,cmap = 'gray')

n = 140

th, im_th = cv2.threshold(image, n, 255, cv2.THRESH_BINARY);

plt.subplot(212),plt.imshow(im_th,cmap = 'gray')

"""

#im_th_inv = cv2.bitwise_not(im_th)
im_floodfill = im_th.copy()
im_floodfill1 = im_th.copy()

h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);

# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)

im_out = im_th | im_floodfill_inv

im_out = cv2.bitwise_not(im_out)

plt.subplot(223),plt.imshow(im_out,cmap = 'gray')

"""
im_out = cv2.bitwise_not(im_th)

contours, hierarchy = cv2.findContours(im_out,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
	cnt = contours[i]

	area = cv2.contourArea(cnt)
	print(area)

plt.tight_layout()
plt.show()

