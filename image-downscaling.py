#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 06:19:37 2022

@author: hamzakhalid
"""

import cv2

file_path  = "/Users/hamzakhalid/Desktop/junebrain/simple-image-downscaling/"
file_name = "uneven.jpg"
image_path = file_path + file_name

# Reading an image in grayscale
gray_scaled_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)