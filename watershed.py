import cv2 as cv
#import numpy as np
from IPython.display import Image, display
#from matplotlib import pyplot as plt

import numpy as np 
from skimage import io, color, filters, morphology, segmentation
from scipy import ndimage as ndi

# load image 
img = io.imread('E:\student_corner\DIP\practical\coin.png')

# convert to grayscale
gray_image = color.rgb2gray(img)

# compute the gradient
gradient = filters.sobel(gray_image)

# Create markers for the watershed algorithm
markers = np.zeros_like(gray_image)
markers[gray_image < 0.2] = 1 # background markers
markers[gray_image < 0.8] = 2 # foreground markers

# Apply the watershed algorithm
labels = segmentation.watershed(gradient, markers)

# Save or diplay the result
io.imsave('segmented_images.png', labels.astype(np.uint8) * 255) #save the result



#plot the image
def imshow(img, ax=None) :
    if ax is None:
        ret, encoded = cv.imencode("E:\student_corner\DIP\practical\.jpg", img)
        display(Image(encoded))
    else:
        ax.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)) 
        ax.axis('off')

#image loading
img = cv.imread("E:\student_corner\DIP\practical\coin.png")  
# show image
imshow(img)
