from cv2 import *

cap = VideoCapture('data/willbot.mp4')
yes, frame = cap.read()
print(type(frame))
while True:
    imshow('frame', frame)