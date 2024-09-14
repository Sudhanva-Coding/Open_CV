#Example for resizing an image 
import cv2
import numpy as np
# img1 = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Basic_Utility_Functions/sample_image_1.jpg", 1)
# cv2.imshow("Original image", img1)

# # the order of dimension is (width, height)
# resized = cv2.resize(img1, (500, 250))
# cv2.imshow("Resized image", resized)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#blurring of an image
#blurring are of three types Gaussian blur, median blur, bilateral blur.

img1 = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Basic_Utility_Functions/Test_image_2.jpg", 1)
cv2.imshow("Original image", img1)

# cv2.waitKey(0)
# # Gaussian blur - used mostly in machine learning pre processing steps
# gaussian = cv2.GaussianBlur(img1, (7, 7), 0)
# cv2.imshow("Gaussian blurring", gaussian)
# cv2.waitKey(0)

# # median blurring - used in digital processing it preserves edges but removes noise
# median = cv2.medianBlur(img1, 5)
# cv2.imshow("Median blurring", median)
# cv2.waitKey(0)

# #Bilateral blur - only sharp edges are preserved here
# Bilateral = cv2.bilateralFilter(img1, 9, 75, 75)
# cv2.imshow(" Bilateral blurring", Bilateral)
# cv2.waitKey(0)
# #cv2.destroyAllWindows()

# Bordering an image
#cv2.BorderTypes
#cv2.BORDER_CONSTANT
#Bordered_image = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1)
#cv2.imshow("Bordered image", Bordered_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows

# reflective border around an image
Bordered_image = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT, value = 1)
cv2.imshow("Bordered image", Bordered_image)
cv2.waitKey(0)
cv2.destroyAllWindows



