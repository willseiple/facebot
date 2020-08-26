from cv2 import VideoCapture, namedWindow, destroyAllWindows, imshow, waitKey, resize, cvtColor, COLOR_BGR2GRAY
# from cv2 import *
# from threading import Thread
# import sys
# import numpy as np
# import time
# from imutils.video import FPS
# import imutils

# # import Queue from Python 3
# if sys.version_info >= (3,0):
#     from queue import Queue
# else:
# # import Queue for Python 2.7
#     from Queue import Queue

# class FileVideoStream:
#     def __init__(self, path, queue_size=512):
#         # init file video stream along with boolean
#         # used to indicate if thread should be stopped
#         self.stream = VideoCapture(path)
#         self.stopped = False
#         # init queue used to store frames read from video file
#         self.Q = Queue(maxsize=queue_size)

#     def start(self):
#         # start a thread to read frames from the file video stream
#         t = Thread(target=self.update, args=())
#         t.daemon = True
#         t.start()
#         return self

#     def update(self):
#         # loop infinitely
#         while True:
#             # if thread indicator varibale is set, stop thread
#             if self.stopped:
#                 return
#             # otherwise ensure queue has room
#             if not self.Q.full():
#                 # read next frame
#                 grabbed, frame = self.stream.read()
#                 # if grabbed False, end of video
#                 if not grabbed:
#                     self.stop()
#                     return
#                 self.Q.put(frame)

#     def read(self):
#         # return next frame in queue
#         return self.Q.get()

#     def more(self):
#         # return True if still frames in queue
#         return self.Q.qsize() > 0

#     def stop(self):
#         # indicate the thread should be stopped
#         self.stopped = True

# set binds and frame locations
blink = (55, 20)
smile = (140, 110)
right = (300, 240)
left =  (600, 240)
idle =  (900, 600)

binds = {'b' : blink,
         's' : smile,
         'r' : right,
         'l' : left,
         'i' : idle,}


def play(start, duration, video, win_size, win_name, speed=1):
    '''
    play video for duration starting at frame, record next action
    '''
    # record = keyboard.start_recording()
    start /= 2
    duration /= 2
    key = None
    cur = start
    # set current frame
    video.set(1, start)
    # iterate over all frames
    while cur < start + duration:

        # frame = video.read()
        # frame = resize(frame, win_size)
        # frame = cvtColor(frame, COLOR_BGR2GRAY)
        # frame = np.dstack([frame, frame, frame])

        # putText(frame, "Queue Size: {}".format(fvs.Q.qsize()), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # imshow(win_name, frame)
        # waitKey(1)

        grabbed, frame = video.read()
        # for _ in range(speed-1):
        #     video.read()
        if not grabbed:
            break
            # take user input
        new = chr(waitKey(1) & 0xFF)
        if ord(new) != 255:
            if new == 'q' or new == 'c':
                return new
            key = new
        sized = resize(frame, win_size)
        imshow(win_name, frame)
        cur += speed

    return key

def wait(video, win_size, win_name):
    '''
    waits for input after displaying home frame
    '''
    video.set(1, 1)
    ret, frame = video.read()

    frame = resize(frame, win_size)
    # frame = cvtColor(frame, COLOR_BGR2GRAY)
    # frame = np.dstack([frame, frame, frame])

    # putText(frame, "Queue Size: {}".format(fvs.Q.qsize()), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # imshow(win_name, frame)
    # waitKey(1)

    imshow(win_name, frame)
    # listen for keypress forever
    follow = chr(waitKey() & 0xFF)
    return follow

def main(filename, win_size, win_name, speed=1):
    '''
    opens window and responds to user input
    closes when user presses "q"
    '''
    cap = VideoCapture(filename)
    namedWindow(win_name, 1)

    follow = None

    while cap.isOpened():
        if follow == 'q':
            break
        if follow in binds:
            follow = play(binds[follow][0], binds[follow][1], cap, win_size=win_size, win_name=win_name, speed=speed)
        else:
            follow = wait(cap, win_size=win_size, win_name=win_name)

    cap.release()
    destroyAllWindows()

# def slow_go():
#     stream = cv2.VideoCapture('data/willbot.mp4')
#     fps = FPS().start()

#     while True:
#     # grab the frame from the threaded video file stream
#         (grabbed, frame) = stream.read()
#         # if the frame was not grabbed, then we have reached the end
#         # of the stream
#         if not grabbed:
#             break
#         # resize the frame and convert it to grayscale (while still
#         # retaining 3 channels)
#         # frame = resize(frame, width=450)
#         # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # frame = np.dstack([frame, frame, frame])
#         # display a piece of text to the frame (so we can benchmark
#         # fairly against the fast method)
#         # frame = imutils.resize(frame, width = 3840)
#         cv2.putText(frame, "Slow Method", (10, 30),
#             cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  
#         # show the frame and update the FPS counter
#         cv2.imshow("Frame", frame)
#         cv2.waitKey(1)
#         fps.update()

#     fps.stop()
#     print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
#     print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
#     # do a bit of cleanup
#     stream.release()
#     cv2.destroyAllWindows()

# def go():

#     fvs = FileVideoStream('data/willbot.mp4').start()
#     time.sleep(2)
#     fps = FPS().start()

#     while fvs.more():
#     # grab the frame from the threaded video file stream, resize
#     # it, and convert it to grayscale (while still retaining 3
#     # channels)
#         frame = fvs.read()
#         # frame = imutils.resize(frame, width = 500)
#         # display the size of the queue on the frame
#         cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),
#             (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)    
#         # show the frame and update the FPS counter
#         cv2.imshow("Frame", frame)
#         cv2.waitKey(1)
#         fps.update()
#     # do a bit of cleanup
#     fps.stop()
#     print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
#     print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
#     cv2.destroyAllWindows()
#     fvs.stop()


if __name__ == '__main__':
    main('data/willbot.mp4', (3840, 2460), 'window')
    # main('data/willbot.mp4', (3840,2160), 'bot')
    # go()
