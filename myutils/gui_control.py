import pyautogui as pag
import mss
import cv2
import numpy as np


rasp_icon_pos = { 'left': 6, 'top' : 1029, 'width' : 50, 'height' : 50 }
browser_icon_pos = { 'left': 68, 'top' : 1029, 'width' : 50, 'height' : 50 }

with mss.mss() as sc:
    rasp_img = np.array(sc.grab(rasp_icon_pos))[:,:,:3]
    browser_img = np.array(sc.grab(browser_icon_pos))[:,:,:3]

cv2.imshow('rasp', rasp_img)
cv2.imshow('browser', browser_img)
cv2.waitKey(0)

'''
while True:
    x, y = pag.position()
    position_str = 'X = ' + str(x) + ' Y = ' + str(y)
    print(position_str)
'''