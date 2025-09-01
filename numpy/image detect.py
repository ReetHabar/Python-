import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load an image (convert to grayscale for simplicity)
image_path = '"C:\Users\HP\Downloads\WhatsApp Image 2024-12-19 at 21.35.38_5189c586.jpg"'  # Replace with your image file
image = Image.open(image_path).convert('L')  # Convert to grayscale
image_array = np.array(image)

# Display the original image
plt.imshow(image_array, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.show()

# Basic image properties
print("Image Shape:", image_array.shape)
print("Min pixel value:", np.min(image_array))
print("Max pixel value:", np.max(image_array))

# Normalize the image (scale pixel values between 0 and 1)
normalized_image = image_array / 255.0

# Apply basic transformations
flipped_image = np.flipud(image_array)  # Flip vertically
rotated_image = np.rot90(image_array)   # Rotate 90 degrees counterclockwise

# Display transformations
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(flipped_image, cmap='gray')
plt.title('Flipped Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(rotated_image, cmap='gray')
plt.title('Rotated Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(normalized_image, cmap='gray')
plt.title('Normalized Image')
plt.axis('off')

plt.show()

# Edge detection using a simple filter (Sobel-like)
sobel_filter = np.array([[-1, 0, 1], 
                        [-2, 0, 2], 
                        [-1, 0, 1]])

# Apply filter using convolution
from scipy.signal import convolve2d
edge_detected_image = convolve2d(image_array, sobel_filter, mode='same')

# Display the edge-detected image
plt.imshow(edge_detected_image, cmap='gray')
plt.title('Edge Detected Image')
plt.axis('off')
plt.show()