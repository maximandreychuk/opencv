import cv2
import numpy

img = cv2.imread('images/color.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

for (x,y,w,h) in results:
    cv2.rectangle(img,(x,y), (x+w, y+h),(0), thickness=3)




cv2.imshow('Res',img)
cv2.waitKey(3000)