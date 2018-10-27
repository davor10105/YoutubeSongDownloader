from PIL import Image
import pytesseract
import argparse
import cv2
import os
import numpy as np

'''
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	cv2.imwrite("slika.png",gray)
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
        break
'''

image=cv2.imread("slika.png")

gray=cv2.threshold(image,150,255,cv2.THRESH_TRUNC & cv2.THRESH_BINARY)[1]
#gray=cv2.medianBlur(gray,3)

cv2.imwrite("gray.png",gray)

print("ugasena kamera")
text=pytesseract.image_to_string(Image.open("gray.png"))

#os.remove("slika.png")

print(text)


