import cv2
import numpy as np
# img1 = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Basic_Utility_Functions/sample_image_1.jpg", cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# gray_blurred = cv2.blur(gray, (3, 3))

# detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)

# if detected_circles is not None:
#     detected_circles = np.uint16(np.around(detected_circles))
#     for pt in detected_circles[0, :] :
#         a, b, r = pt[0], pt[1], pt[2]
#         cv2.circle(img1, (a,b), r, (0, 255, 0), 2)
#         cv2.circle(img1, (a, b), 1, (0, 0, 255), 3)
#         cv2.imshow("Detected Circles", img1)
#         cv2.waitKey(0)

# cv2.destroyAllWindows()

# Count number of circles in an image
img1 = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Lesson_2_and_3_Basic_Utility_Functions/Test_Image_2.jpg", 0)

params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
params.filterByArea = True
params.minArea = 100
# Set Circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.9
# Set Convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.2
# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01
# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
	
# Detect blobs
keypoints = detector.detect(img1)

# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(img1, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)