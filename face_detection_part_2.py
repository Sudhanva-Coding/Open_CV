import cv2, numpy, os, sys
size = 4
haar_file = "haarcascade_frontalface_default.xml"
datasets = "datasets"

# part 1 : creating fisher recognizer
print("recognizing faces, please be in sufficient lines")

# creating a list of images and list of corresponding names
(images, levels, names, id) = ([], [], {}, 0)

for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + "/" + filename
            label = id 
            images.append(cv2.imread(path, 0))
            levels.append(int(label))
        id += 1
(width, height) = (130, 100)

# Create a Numpy array from the two lists above
(images, labels) = [numpy.array(lis) for lis in [images, labels]]
 
# OpenCV trains a model from the images
# NOTE FOR OpenCV2: remove '.face'
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

