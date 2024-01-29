import cv2
import numpy as np

img = cv2.imread('images/color.jpeg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

img = cv2.merge([r,g,b])

cv2.imshow('Res',img)
cv2.waitKey(3000)