import cv2
print(cv2.__version__)
capture = cv2.VideoCapture(0)
while True:
    ret, img = capture.read()
    cv2.imshow("From camera:", img)
    k =