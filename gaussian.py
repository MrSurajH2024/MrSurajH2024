import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def create_gaussian_kernel(size, sigma):
    """Create a Gaussian kernel."""
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-0.5 * (xx**2 + yy**2) / sigma**2)
    kernel /= np.sum(kernel)  # Normalize the kernel
    return kernel

def apply_gaussian_filter(image, sigma):
    """Apply Gaussian filter to an image."""
    return gaussian_filter(image, sigma=sigma)

# Load a sample image (you can replace this with your own image)
from skimage import data, color
image = color.rgb2gray(data.astronaut())

# Define Gaussian filter parameters
sigma = 2.0  # Standard deviation of the Gaussian kernel

# Apply Gaussian filter
filtered_image = apply_gaussian_filter(image, sigma)

# Plot the original and filtered images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image with Gaussian Filter')
plt.axis('off')

plt.tight_layout()
plt.show()
