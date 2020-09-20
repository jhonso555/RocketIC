# import the necessary packages
import cv2
total = 0
video = cv2.VideoCapture('./src/Video_4.mp4')
total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(total)