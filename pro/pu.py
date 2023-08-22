import os
import cv2

path = "pic/"
images = []

# Collect the image file names in the folder
for i in os.listdir(path):
    name, extension = os.path.splitext(i)
    if extension == ".jpg":
        file_name = path + "/" + i
        images.append(file_name)

count = len(images)

# Read the first image to get size information
first_image = cv2.imread(images[0])
height, width, channels = first_image.shape
size = (width, height)

# Create a video writer
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Add images to the video writer
for i in range(0,count):
        #image_path = os.path.join(path, images[i])
         frame = cv2.imread(images[i])
         out.write(frame)

# Release the video writer
out.release()

# Print completion message
print("Done")
