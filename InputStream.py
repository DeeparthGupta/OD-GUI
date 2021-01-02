from threading import Thread
from cv2 import cv2
from queue import Queue, Empty, Full

class InputStream:
# Creates a new thread to retrieve frames using multithreading.
    def __init__(self,src = 0, memory = None):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.memory = Queue(memory) if memory else None

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
                
                if self.memory is not None:
                    try:
                        self.memory.put(self.frame, block=True,timeout=2.0) # Push to memory queue
                    except Full:
                        print('ERROR: Memory full timeout.') 
                        self.stop()    
                               
    
    def get_frame(self): 
    # Return the frame
        if self.memory:
            try:
                return self.memory.get(block=True, timeout=2.0)
            except Empty:
                print('ERROR: Memory empty timeout.')
                self.stop()
        else: return self.frame      

    def start(self):
    # Starts the threaded capture
        Thread(target=self.get, args=()).start()
        print('Capture started')
        return self

    def stop(self): 
    # Stop the threaded capture    
        self.stopped = True
        print('Video capture stopped')