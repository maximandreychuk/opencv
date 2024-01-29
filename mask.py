import cv2
import numpy

photo = cv2.imread('images/color.jpeg')
img=numpy.zeros(photo.shape[:2],dtype='uint8')

circle = cv2.circle(img.copy(),(200,200), 100, 255, cv2.FILLED)
square = cv2.rectangle(img.copy(), (25,25), (250,350), 255, cv2.FILLED)

img = cv2.bitwise_and(photo,photo, mask=circle)
# img = cv2.bitwise_or(circle,square)
# img = cv2.bitwise_xor(circle,square)
# img = cv2.bitwise_not(circle,square)




cv2.imshow('Res',img)
cv2.waitKey(3000)