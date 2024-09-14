import cv2
import numpy as np
img1 = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Basic_Utility_Functions/image_4.jpg")
# cv2.imshow("Original image", img1)
# cv2.waitKey(0)

#gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grayscaled image", gray_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# grayscaling an image using average of pixels method
#gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#(row, col) = img1.shape[0:2]

#for i in range(row):
	#for j in range(col):
		# Find the average of the BGR pixel values
		#img1[i, j] = sum(img1[i, j]) * 0.33

# cv2.imshow("Grayscaled image", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# rotating an image
# (rows, cols) = img1.shape[:2]

# # getRotationMatrix2D creats=es a matrix which is needed for transformation
# M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
# res = cv2.warpAffine(img1, M, (cols, rows))
# cv2.imwrite("result.jpg", res)

# Edge detection in an image
img2 = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Basic_Utility_Functions/sample_image_1.jpg")
# using canny edge detection algorithm we are going to identify the edges 
# edges = cv2.Canny(img2, 100, 200)
# cv2.imwrite("result1.jpg", edges)

# convert image from one color scheme to another

# conversion of image to be done from rgb to hsv
hsvimage = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
cv2.imshow("window_name", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()




