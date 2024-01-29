import cv2
import numpy as np

photo = np.zeros((700, 700, 3), dtype = 'uint8')
# photo[10:250, 149:151] = 105,200,119 /// регулировать выс, шир

# cv2.rectangle(photo, (50,50), (400,400), (105,200,119), thickness = cv2.FILLED) // квадрат
# cv2.line(photo, (0,photo.shape[0]//2), (100, photo.shape[0]//2),(105,200,119), thickness=2) // линия
# cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 50, (105,200,119), thickness=cv2.FILLED)

cv2.putText(photo, "itProger", (100,150),cv2.FONT_HERSHEY_TRIPLEX, 1, (105,200,119), thickness=1)

cv2.imshow('Res', photo)
cv2.waitKey(3000)