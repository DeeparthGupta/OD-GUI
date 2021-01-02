import numpy as np
from cv2 import cv2


class Detector:
# Class that runs object detection on an input frame.
    def __init__(self, support_dir, size=(320,320)):
        self.yolo_dir = support_dir
        self.size = size
        self.model, self.classes, self.output_layers = self.load_yolo()        
    
    def load_yolo(self):
    # Load the yolov3 weights and config file with the help of dnn module of openCV.
        weights = self.yolo_dir + 'yolov3.weights'
        config = self.yolo_dir + 'yolov3.cfg'
        names = self.yolo_dir + 'coco.names'
        
        # Configure the neural net.
        net = cv2.dnn.readNet(weights,config)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        
        classes = []
        with open(names, "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layers_names = net.getLayerNames()
        output_layers = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
        return net, classes, output_layers

    def detect_objects(self,img, net, outputLayers):		
    # Use blobFromImage that accepts image/frame from video or webcam stream, model and output layers as parameters.          
        blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=self.size, mean=(0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)
        outputs = net.forward(outputLayers)
        return outputs

    def get_box_dimensions(outputs, height, width, threshold):
    # The list scores is created which stores the confidence corresponding to each object.     
        boxes = []
        confs = []
        class_ids = []
        for output in outputs:
            for detect in output:
                scores = detect[5:]
                #print(scores)
                class_id = np.argmax(scores)
                conf = scores[class_id]
                if conf > threshold:
                    center_x = int(detect[0] * width)
                    center_y = int(detect[1] * height)
                    w = int(detect[2] * width)
                    h = int(detect[3] * height)
                    x = int(center_x - w/2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confs.append(float(conf))
                    class_ids.append(class_id)

        return boxes, confs, class_ids

    def draw_labels(boxes, confs, class_ids, classes, img): 
    # Draw bounding box and add object labels to it.
        indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                cv2.rectangle(img, (x,y), (x+w, y+h), thickness=2)
                cv2.putText(img, label, (x, y - 5), font, 1,thickness=1)
        
        return img

    def run_detection(self, frame, threshold = 0.5):    
    # Accept a frame, run detection on it and draw a box around the detection.
        height, width = frame.shape[:1]
        outputs = self.detect_objects(frame, self.model, self.output_layers)
        boxes, confidence, class_ids = self.get_box_dimensions(outputs,height,width,threshold)
            
        return self.draw_labels(boxes,confidence,class_ids,self.classes,frame)