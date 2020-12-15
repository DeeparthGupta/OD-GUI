import numpy as np
from cv2 import cv2

def load_yolo():
    #Load the yolov3 weights and config file with the help of dnn module of openCV.
    
    net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layers_names = net.getLayerNames()
    output_layers = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    return net, classes, colors, output_layers

def detect_objects(img, net, outputLayers):		
    #Use blobFromImage that accepts image/frame from video or webcam stream, model and output layers as parameters.	

    blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(outputLayers)
    return blob, outputs

def get_box_dimensions(outputs, height, width):
    #The list scores is created which stores the confidence corresponding to each object. Can play around with this value.
    confidence = 0.5
    boxes = []
    confs = []
    class_ids = []
    for output in outputs:
        for detect in output:
            scores = detect[5:]
            #print(scores)
            class_id = np.argmax(scores)
            conf = scores[class_id]
            if conf > confidence:
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