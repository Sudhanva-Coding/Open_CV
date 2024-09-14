
## 1. Read and display an image

# import cv2

# # imread is used to read an image by passing the path of image as input
# img = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Lesson1/download.jpeg", cv2.IMREAD_COLOR)

# # There are 3 parameters to read an image - 
# #cv2.IMREAD_COLOR (1) => Specify to load the image in color
# #cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
# #cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

# # imshow is used to show the loaded image in a new window with a title
# cv2.imshow("DSLR Image", img)

# # To hold the window until the user presses a key on keyboard
# cv2.waitKey(0)

# # delete / close the image window after the key pressed
# cv2.destroyAllWindows()

## 2. Grayscale an image

#import cv2
#img = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Lesson1/download.jpeg", 0)

#cv2.imshow("image in grayscale", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

## 3. save an image after making some changes
#import cv2

#import os

# Changing the path to saved images
#saved_directory = "c:/Users/Sudhanva Akshay/OpenCV/Lesson1/temp"

#img = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Lesson1/download.jpeg", 0)
#cv2.imshow("image in black and white", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#os.chdir(saved_directory)
#cv2.imwrite("newimage.jpeg", img)
#print("Succesfully saved")


## Homework : Take any of the available image and split it in three color formats, Red , Green and Blue

import cv2
img = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Lesson1/download.jpeg",  )

#cv2.imshow("image in grayscale", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

B, G, R = cv2.split(img)

cv2.imshow("Original ", img)
cv2.waitKey(0)
cv2.imshow("Blue saturation image", B)
cv2.waitKey(0)
cv2.imshow("Red saturation image", R)
cv2.waitKey(0)
cv2.imshow("Green saturation image", G)
cv2.waitkey(0)
cv2.destroyAllWindows()