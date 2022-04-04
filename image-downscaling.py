#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 06:19:37 2022

@author: hamzakhalid
"""

import cv2
import numpy as np

def getImageArray(image):
    # Converting image to numpy array
    image_array = np.asarray(image)
    return image_array

def downscaleImage(image):
    # Validating image size
    if(image.shape[0]<=4 or image.shape[1]<=4):
        print("Image too small for downscaling!")
        return None
    
    # Downscaling by taking every 4th pixel in both directions
    # Numpy handles all the edge cases under the hood
    try:
        downscaled_img = image[::4,::4]
        return downscaled_img
    except IndexError:
        print("The image should be two dimensional.")
        return None
        
def printResolution(image):
    if image is not None:    
        print("Resolution: ", image.shape)
    else:
        print("Can not print resolution of invalid image array!")

# Driver
file_path  = "/Users/hamzakhalid/Desktop/junebrain/simple-image-downscaling/"
file_name = "uneven.jpg"
image_path = file_path + file_name
# Reading an image in grayscale
gray_scaled_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

image_array = getImageArray(gray_scaled_img)
printResolution(image_array)

downscaled_img_1 = downscaleImage(image_array)
printResolution(downscaled_img_1)

# Let's downscale one more time
downscaled_img_2 = downscaleImage(downscaled_img_1)
printResolution(downscaled_img_2)

# Let's try an invalid case
downscaled_img_3 = downscaleImage(np.array([[1,2,4], [3,4,5]]))
printResolution(downscaled_img_3)

downscaleImage(np.array([]))
