import cv2

def loading_displaying_saving():
    img = cv2.cv2.imread('girl.jpeg', cv2.IMREAD_GRAYSCALE)
    cv2.cv2.imshow('girl', img)
    cv2.cv2.waitKey(0)
    cv2.cv2.imwrite('graygirl.jpeg', img)