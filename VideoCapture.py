from threading import Thread
from cv2 import cv2

class VideoCapture:

    def __init__(self,src = 0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def start(self):
        Thread(target=self.get, args=()).start()
        print('Capture started')
        return self

    def stop(self):
        self.stopped = True
        print('Video capture stopped')