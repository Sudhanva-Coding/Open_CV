# arithmetic operation on images
import cv2
import numpy as np
img1 = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Basic_Utility_Functions/image_4.jpeg", cv2.IMREAD_COLOR)
img2 = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Basic_Utility_Functions/image_5.jpeg", cv2.IMREAD_COLOR)

weightedsum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)
cv2.imshow("Weighted image ", weightedsum)
cv2.waitKey(0)
cv2.destroyAllWindows()

#C:\Users\Sudhanva Akshay\OpenCV\Basic_Utility_Functions\sample_image_3.jpg

## Do the arithmetic operation for subtraction of images just like the above one
## Write a program to resize an image