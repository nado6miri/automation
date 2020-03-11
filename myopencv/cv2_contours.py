
import time
import sys
import cv2
from matplotlib import pyplot as plt
import numpy as np

#image = cv2.imread("./test.jpg", cv2.IMREAD_UNCHANGED)
image = cv2.imread("./test.jpg", cv2.IMREAD_COLOR)
cv2.imshow("TT", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

b, g, r = cv2.split(image)
image2 = cv2.merge([r, g, b])
plt.imshow(image2)
plt.xticks([])
plt.yticks([])
plt.show()
cv2.waitKey(0)

img_color = cv2.imread('test.png')
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
cv2.imshow("COLOR_BGR2GRAY", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    #print (cnt)
    cv2.drawContours(img_color, [cnt], 0, (0, 0, 255), 1)  # blue

cv2.imshow("result", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()


for cnt in contours:
    area = cv2.contourArea(cnt)
    #print(area)

cv2.imshow("result", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

image3 = np.zeros((512, 512, 3), np.uint8)
image3 = cv2.line(image3, (0,0), (511, 511), (0, 0, 255), 5)
image3 = cv2.rectangle(image3, (100,100), (400, 400), (255, 0, 0), 3)
#cv2.imshow('image3', image3)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# callback함수
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image3,(x,y), 100,(255,0,0),-1)
        cv2.imshow("image3", image3)


cv2.namedWindow("image3")
cv2.setMouseCallback("image3", draw_circle)
cv2.imshow("image3", image3)

while(1) :
    if(cv2.waitKey(0) & 0xFF == 27) :
        break

cv2.destroyAllWindows()
