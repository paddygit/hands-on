import numpy as np
import cv2

img = cv2.imread(
    'D:\Padmanabhan\work\hands-on\Python\OpenCV\Lesson001\opencv-logo.png')
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
try:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.imwrite("output.jpg", img)
except:
    print("Image path not found.")
