import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
#
#capturing frames from a camera
cap = cv2.VideoCapture(0)

# looping in order to initialize capturing
while 1:
    ret, img = cap.read()
    # converting to grayscale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y+h, x: x+w]
        roi_color = img [y:y+h, x: x+w] 
# Detects eyes of different sizes in the input image
        eyes = eye_cascade.detectMultiScale(roi_gray) 
  
        #To draw a rectangle in eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

    # displaying the image in window
    cv2.imshow("img", img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# close the window
cap.release()

cv2.destroyAllWindows()