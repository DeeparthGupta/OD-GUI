from threading import Thread
from cv2 import cv2
from collections import deque

class InputStream:
# Creates a new thread to retrieve frames using multithreading.
    def __init__(self,src = 0, memory = None):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        # self.memory = deque(maxlen=memory) if memory else None

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
                
                """ if self.memory is not None:
                    try:
                        self.memory.appendleft(self.frame) # Push to memory queue
                    except Exception as e:
                        print(e) """
                            
    """ def get_frame(self): 
    # Return the frame
        if self.memory is not None:
            try:
                return self.memory.pop()
            except Exception as e:
                print(e)

        else: return self.frame   """    

    def start(self):
    # Starts the threaded capture
        Thread(target=self.get, args=()).start()
        print('Capture started')
        return self

    def stop(self): 
    # Stop the threaded capture    
        self.stopped = True
        print('Video capture stopped')