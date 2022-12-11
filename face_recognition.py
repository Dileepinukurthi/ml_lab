import cv2 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Will be provided make sure the xml file is in same directory
img =  cv2.imread('ironman.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
x , y , w , h = faces[0]
cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
cv2.imshow('img',img)
cv2.waitKey(0)
