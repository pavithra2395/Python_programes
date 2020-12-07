"""
 * Python script to demonstrate simple thresholding.
 *
 * usage: python Threshold.py <filename> <sigma> <threshold>
"""
import sys
import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import skimage.viewer

# get filename, sigma, and threshold value from command line
filename = sys.argv[1]
sigma = float(sys.argv[2])
t = float(sys.argv[3])

# read and display the original image
image = skimage.io.imread('D:\\puppies\\misalignment\\MR192.jpg')
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# blur and grayscale before thresholding
blur = skimage.color.rgb2gray(image)
blur = skimage.filters.gaussian(blur, sigma=k)

# perform inverse binary thresholding
mask = blur < t_rescaled

# use the mask to select the "interesting" part of the image
sel = np.zeros_like(image)
sel[mask] = image[mask]

# display the result
viewer = skimage.viewer.ImageViewer(sel)
viewer.view()