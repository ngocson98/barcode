import cv2
import numpy as np
from pyzbar.pyzbar import Decoded, decode

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
while True:
    ret, img = cap.read()
    for barcode in decode(img):
        # print(barcode.data)
        myData = barcode.data.decode('utf-8')
        myType = barcode.type
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 2)
        pts2 = barcode.rect
        cv2.putText(img, myType + ": " + myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 165, 0), 2)

        #print(myType + ": " + myData)
    cv2.imshow('Read BarCode', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()