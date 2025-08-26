import cv2
import numpy as np

from matplotlib import pyplot as plt


color_image = cv2.imread('E:\student_corner\DIP\practical\lena noicy.jpeg')
gray_img = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
sliding_window_size_x = 5
sliding_window_size_y = 5

mean_filter_kernel = np.ones((sliding_window_size_x,sliding_window_size_y),np.float32)/(sliding_window_size_x*sliding_window_size_y)
filtered_image = cv2.filter2D(gray_img,-1,mean_filter_kernel)

plt.subplot(121),plt.imshow(gray_img),plt.title('Original Noisy Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(filtered_image),plt.title('Filtered Image')
plt.xticks([]), plt.yticks([])
plt.show()
