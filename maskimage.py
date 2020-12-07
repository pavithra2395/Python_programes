"""
 * Python program to apply a mask to an image.
 *
"""
import numpy as np
import skimage
from skimage.viewer import ImageViewer

# Load the original image
image = skimage.io.imread("D:\\puppies\\misalignment\\MR192.jpg")

# Create the basic mask
mask = np.ones(shape=image.shape[0:2], dtype="bool")

# Draw a filled rectangle on the mask image
rr, cc = skimage.draw.rectangle(start=(600, 300), end=(800, 600))
mask[rr, cc] = False

# Apply the mask and display the result
image[mask] = 100

viewer = ImageViewer(image)
viewer.show()