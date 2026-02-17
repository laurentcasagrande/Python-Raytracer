import cv2
import os
from natsort import natsorted  


input_folder = "Ratte" 
output_video = "Ratte/horizontal rotierende Ratte.avi"
laufzeit = 8

images = [img for img in os.listdir(input_folder) if img.lower().endswith(".png")]
images = natsorted(images)
fps = len(images) / laufzeit

first_image_path = os.path.join(input_folder, images[0])
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

for image in images:
    img_path = os.path.join(input_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)

video.release()
