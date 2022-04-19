##
# importing the module
import cv2
import numpy as np
import pytesseract
# function to display the coordinates of
# of the points clicked on the image
cropping=[]
def click_event(event, x, y, flags, params):
	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)
		cropping.append([(x,y)])

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('image', img)

	# checking for right mouse clicks
	if event==cv2.EVENT_RBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)
		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('image', img)

##
vidcap = cv2.VideoCapture('Video.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.png" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  count += 1
##
for i in range(0,count):
  if i==0:
    img = cv2.imread("frame0.png", 1)
    img = cv2.resize(img, (1920, 1080))
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  img = cv2.imread("frame%d.png" % i,1)
  img = cv2.resize(img, (1920, 1080))
  cropped_image = img[cropping[0][0][1]:cropping[1][0][1], cropping[0][0][0]:cropping[1][0][0]]
  cv2.imwrite("cropped%d.png" % i, cropped_image)
cropping=[]
##

import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\milaghas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
image = cv2.imread("cropped1.png")
median = cv2.medianBlur(image,5)
gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
# thresh = cv2.adaptiveThreshold(median, 100, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 2)
# cv2.imshow("gray", gray);
# cv2.imshow("thresh", thresh);
cv2.imshow("image", image);
cv2.waitKey(0);
# convolved_rgb_sharpen = cv2.convolver_rgb(image, sharpen, 1)

text = pytesseract.image_to_string(image,config="--psm 6")
# text = pytesseract.image_to_string(gray,config="--psm 6")
print(text)
##
boxes = pytesseract.image_to_boxes(image)
cv2.imshow('Detected text', img)
cv2.waitKey(0)
### Apply identity kernel

kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

kernel2 = np.ones((5, 5), np.float32) / 25

kernel3 = np.array([[0, -1,  0],
                   [-1,  6, -1],
                    [0, -1,  0]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)

cv2.imshow('Original', image)
cv2.imshow('Identity', identity)

cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(identity,nice=10,config="--psm 6")
print(text)
