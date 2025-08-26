import cv2
import numpy as np

# read import images 
img = cv2.imread('E:\student_corner\DIP\practical\images.jpeg', 0)

# show original images
cv2.imshow('Original', img)
cv2.waitKey(0)

# define the kernel
kernel = np.ones((3, 3), np.uint8)

# compute the morphological gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# display the gradient image
cv2.imshow("morphological gradient kernel = 3X3", gradient)

if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows()
