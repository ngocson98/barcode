# Importing library
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Make one method to decode the barcode
def BarcodeReader(image):
    # read the image in numpy array using cv2
    img = cv2.imread(image)

    # Decode the barcode image
    detectedBarcodes = decode(img)

    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:

        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:

            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            myData = barcode.data.decode('utf-8')
            myType = barcode.type

            cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)
            cv2.putText(img, myType + ": " + myData, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 150), 2)
            if barcode.data != "":
                # Print the barcode data
                print(barcode.data)
                print(barcode.type)

    # Display the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Take the image from user
    image = "images/barcodes.png"
    BarcodeReader(image)
