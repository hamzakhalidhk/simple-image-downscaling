#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 06:19:37 2022

@author: hamzakhalid
"""

import cv2
import numpy as np

file_path  = "/Users/hamzakhalid/Desktop/junebrain/simple-image-downscaling/"
file_name = "uneven.jpg"
image_path = file_path + file_name

# Reading an image in grayscale
gray_scaled_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Converting image to numpy array
downscaled_img = np.asarray(gray_scaled_img)
print("Resolution before downscaling: ", downscaled_img.shape)

# Downscaling by taking every 4th pixel in both directions
# Numpy handles all the edge cases under the hood
downscaled_img = downscaled_img[::4,::4]
print("Resolution after downscaling: ", downscaled_img.shape)
