import cv2
import numpy as np
img1 = cv2.imread("c:/Users/Sudhanva Akshay/OpenCV/Basic_Utility_Functions/sample_image_1.jpg")

# start coordinate here represents top left corner of an image and n coordinate here represents the bottom right of an image
# start_point = (0, 0)
# end_point = (250, 250)

# color = (0, 255, 0)
# thickness = 9

# # using cv2.line method we are going to draw a line on the image
# image = cv2.line(img1, start_point, end_point, color, thickness)

# draw a rectangle on the image
# start_point = (5, 5)
# end_point = (600, 600)
# color = (0, 0, 0)
# # line thickness of 2px
# thickness = -1

# image = cv2.rectangle(img1, start_point, end_point, color, thickness)
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# draw a circle on the image

# centre_coordinate = (600, 600)
# radius = 150
# color = (0, 0, 255)
# thickness = -1

# image = cv2.circle(img1, centre_coordinate, radius, color, thickness)
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# text on the image

font = cv2.FONT_HERSHEY_SIMPLEX
org = (300, 300)
font_scale = 1
color = (255, 0, 0)
thickness = 2

image = cv2.putText(img1, "Hi this is Sudhanvas image editing tutorial", org, font, font_scale, color, thickness, cv2.LINE_AA)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()




