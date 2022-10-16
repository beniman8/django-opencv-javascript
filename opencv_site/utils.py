# Utils is where your costumade code go in order for django to use it
import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
    ('NO_FILTER','no filter'),
    ('COLORIZED','colorized'),
    ('GRAYSCALE','grayscale'),
    ('BLURRED','blurred'),
    ('BINARY','binary'),
    ('INVERT','invert'),


    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
get_image(hsv)


#Grayscale
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
get_image(gray,cmap='gray')


# Blurred
width,height = normal.shape[:2]
print(width,height)

if width > 500:
    k=(50,50)
elif width > 200 and width <= 500:
    k=(25,25)
    
else:
    k=(10,10)
    
blur = cv2.blur(normal,k)
get_image(blur)


#Binary

v, binary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
get_image(binary,cmap='gray')


#Invert

invert = cv2.bitwise_not(binary)
get_image(invert,cmap='gray')
"""


def get_filtered_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if action == "NO_FILTER":
        filtered = image
    elif action == "COLORIZED":
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif action == "GRAYSCALE":
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif action == "BLURRED":
        width, height = img.shape[:2]
        if width > 500:
            k = (50, 50)
        elif width > 200 and width <= 500:
            k = (25, 25)
        else:
            k = (10, 10)
        blur = cv2.blur(img, k)
        filtered = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

    elif action == "BINARY":

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, filtered = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    elif action == 'INVERT':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, imag = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        filtered = cv2.bitwise_not(imag)
    return filtered
