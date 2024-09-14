import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)

# stroring single frame as background
_, background = cap.read()
time.sleep(2)
_, background = cap.read()

# define all the kernels size
open_kernel = np.ones((5, 5), np.uint8)
close_kernel = np.ones((7, 7), np.uint8)
dilation_kernel = np.ones((10, 10), np.uint8)

# function to remove noise from mask
def filter_mask(mask):
    close_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, close_kernel)
    open_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, open_kernel)
    dilation = cv2.dilate(open_mask, dilation_kernel, iterations=1)
    return dilation

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while cap.isOpened():
    ret, frame = cap.read()
    


    
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([50, 80, 50])
    upper_bound = np.array([90, 255, 255])

    mask = filter_mask(mask)
    cloak = cv2.bitwise_and(background, background, mask=mask)
    inverse_mask = cv2.bitwise_not(mask)
    current_backgrond = cv2.bitwise_and(frame, frame, mask=inverse_mask)
    combined = cv2.add(cloak, current_backgrond)
    cv2.imshow("Final output", combined)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()