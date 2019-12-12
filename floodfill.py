import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import data, feature, exposure
    
img = cv2.imread('/home/seth/path.jpg',0)

im_in = cv2.GaussianBlur(img,(5,5),0)

n = 155

th, im_th = cv2.threshold(im_in, n, 255, cv2.THRESH_BINARY);

plt.subplot(221),plt.imshow(im_in,cmap = 'gray')
plt.subplot(222),plt.imshow(im_th,cmap = 'gray')
# Copy the thresholded image.
im_floodfill = im_th.copy()

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)

# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0, 0), 255);

# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Combine the two images to get the foreground.
fill_image = im_th | im_floodfill_inv

plt.subplot(223),plt.imshow(fill_image,cmap = 'gray')

plt.show()
