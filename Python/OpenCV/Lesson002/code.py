import numpy as np
import cv2
img = cv2.imread(
    "D:\Padmanabhan\work\hands-on\Python\OpenCV\Lesson002\\test_image.png", 1)
print("print(img)")
print(img)

print("print(type(img))")
print(type(img))

print("print(len(img))")
print(len(img))

print("print(len(img[0]))")
print(len(img[0]))

print("print(len(img[0][0]))")
print(len(img[0][0]))

print("print(img.shape)")
print(img.shape)

print("print(img.dtype)")
print(img.dtype)

print("print(img[5, 10])")
print(img[5, 10])

print("print(img[5, 30])")
print(img[5, 30])

print("print(img[5, 50])")
print(img[5, 50])

print("print(img[30, 15])")
print(img[30, 15])

print("print(img[30, 45])")
print(img[30, 45])

print("print(img[:, :, 0])")
print(img[:, :, 0])

print("print(img.size)")
print(img.size)
