import cv2
import numpy as np


img = cv2.imread('images/color.jpeg')
# img = cv2.flip(img,1) отзеркаливание

def rotate(img_param, angle):
    height, widht = img_param.shape[:2]
    point = (widht//2, height//2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (widht, height))

def transform(img_param, x, y):
    mat = np.float32([[1,0,x], [0,1,y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1],img_param.shape[0]))

# img = rotate(img,90)
img = transform(img, 30, 200)

cv2.imshow('Res', img)
cv2.waitKey(3000)
# while True:
#     success, img = cap.read()
#     img = cv2.Canny(img,200, 200)
#     kernel = np.ones((5,5), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations = 1)
#     cv2.imshow('Res', img)
    
#     if cv2.waitKey(8000):
#         break
# cap = cv2.VideoCapture(0) /// доступ к камере
# cap.set(3,500)
# cap.set(4,300) /// размеры изображения окна


# img = cv2.imread('images/color.jpeg')
# img = cv2.GaussianBlur(img,(9,9), 0) /// размытие
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) /// к серому
# img = cv2.Canny(img,200, 200)
# kernel = np.ones((5,5), np.uint8)
# img = cv2.dilate(img, kernel, iterations=1)
# img = cv2.erode(img, kernel, iterations = 1)


