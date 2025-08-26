import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray

flower_original = imread('flower.jpeg')
flower_gray = rgb2gray(flower_original)

# Create a 1x2 subplot grid
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot the original image in the first subplot
axs[0].imshow(flower_original)
axs[0].set_title('Original Image')
axs[0].axis('off')

# Plot the grayscale image in the second subplot
axs[1].imshow(flower_gray, cmap='gray')
axs[1].set_title('Grayscale')
axs[1].axis('off')

plt.tight_layout()

# Show the plot
plt.show()
