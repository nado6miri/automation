#-*- coding:utf-8 -*-

import time
import sys
import cv2
from matplotlib import pyplot as plt
import numpy as np
import cv2
import numpy as np 
img1 = cv2.imread('images/flower1.jpg')
img2 = cv2.imread('images/flower2.jpg')

img3 = cv2.add(img1, img2)
cv2.imshow('add', img3)


def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('W', 'image', 0, 100, nothing)

while True:
    w = cv2.getTrackbarPos('W','image')
    dst = cv2.addWeighted(img1,float(100-w) * 0.01, img2,float(w) * 0.01,0)
    cv2.imshow('dst', dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break;

cv2.destroyAllWindows()