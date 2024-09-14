import cv2
import os
from PIL import Image

# Change the directory as per own folder path where the images are located
os.chdir("C:/Users/Sudhanva Akshay/OpenCV/Photos")
path = "C:/Users/Sudhanva Akshay/OpenCV/Photos"

mean_height = 0
mean_width = 0

num_off_images = len(os.listdir(".")) ## This gives us count of images. Here in this case it is 13
#num_off_images = os.listdir(".") ## This prints all the items in this directory/folder
#print("Count of images : ", num_off_images)

for file in os.listdir("."):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height

mean_width = mean_width // num_off_images
mean_height = mean_height // num_off_images

print(mean_width)
print(mean_height)

for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        img = Image.open(os.path.join(path, file))
        width, height = img.size
        print(width, height)

        imgresized = img.resize((mean_width, mean_height), Image.LANCZOS)
        imgresized.save(file, "png", quality = 95)
        print(img.filename.split('\\')[-1], " is resized")

def video_generator():
    video_name = "MY_COLLAGE_VIDEO.avi" 
    os.chdir("C:/Users/Sudhanva Akshay/OpenCV/Photos")
    images = []
    for img in os.listdir("."):
        if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png"):
            images.append(img)

    # array images should only consider the image files and ignore others
    print(images)

    frame = cv2.imread(os.path.join(".", images[0]))
    # setting the sizes
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    # appending images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))
    
    cv2.destroyAllWindows()
    video.release()
    
video_generator()