import cv2
import keyboard
import time
import Movement as mov
from multiprocessing import Process, Pipe
import water_pump as wp

# Leemos los nombres de las clases del dataset
# COCO dataset https://cocodataset.org/
classNames = []
classFile = "coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

# Configuracion y pesos de la red neuronal entrenada con el coco datasetr
configPath = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "frozen_inference_graph.pb"

lbl = 'coco_labels.txt'

# Setup de la red neuronal
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Distance from center of frame on both sides. The object being tracked must be brought inside this zone while tracking
tolerance = 0.1
# Deviation of the center of object from center of frame
xDeviation = 0

objXCenter = 0

objYCenter = 0

trackingData=[0,0,0,0]

draw = True

# FunciÓn que procesa y analiza cada frame
def getObjects(img, threshold, nms, objects=[]):

    classIds, confs, bbox = net.detect(img, confThreshold=threshold, nmsThreshold=nms)
  
    # print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectsInfo =[]
    if len(classIds) != 0:
        
        # Por cada objeto detectado comprobamos si corresponde con uno de los objetos en nuestra lista 
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects: 
                # Guardamos la información del objeto detectado y printamos su bounding box
                objectsInfo.append([box, className])
                if (draw):
                    cv2.rectangle(img, box, color = (51,255,51), thickness=2)
                    cv2.putText(img, classNames[classId-1].upper(), (box[0]+12, box[1]+32),         
                    cv2.FONT_HERSHEY_COMPLEX, 1 ,(0,0,0), 2)
                    cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+30),         
                    cv2.FONT_HERSHEY_COMPLEX, 1 ,(119,255,0), 2)  
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200, box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (119,255,0), 2)
    
    return img, objectsInfo

# 
def trackObjects(objectsInfo):
   
    global xDeviation, yMax, objXCenter, objYCenter, tolerance, trackingData
    
    if(len(objectsInfo)==0):
        print("no objects to track")
        trackingData=[0,0,0,0]
        return
    
    # TODO: detectar el elemento mas cercano
    # Esto tal vez sería detectando el objecto más grande??
    closestObj = objectsInfo[0]
    bbox = closestObj[0] 
    xMin, yMin, xMax, yMax = list(bbox)
    
    print("/*** Medidas del objeto ***/")
    print("Xmax = ", xMax)
    print("Xmin = ", xMin)
    print("Ymax = ", yMax)
    print("yMin = ", yMin)
    xMax = xMax + xMin
    yMax = yMax+yMin
    
    xDiff = xMax - xMin
    yDiff = yMax - yMin
    print("x diff: ", round(xDiff, 5))
    print("y diff: ", round(yDiff, 5))
                
    objXCenter = xMin + (xDiff/2)
    objXCenter = round(objXCenter, 3)
    
    objYCenter = yMin + (yDiff/2)
    objYCenter = round(objYCenter, 3)
    
    print("[",objXCenter, objYCenter,"]")
        
    xDeviation = 320 - objXCenter
    yMax = round(yMax, 3)
        
    print("{", xDeviation, yMax, "}")
   
    # thread = Thread(target = move_robot)
    # thread.start()
    
    trackingData[0] = objXCenter
    trackingData[1] = objYCenter
    trackingData[2] = xDeviation
    trackingData[3] = yMax


def run(childProcess): 
    
    global xDeviation, yMax, objXCenter, objYCenter, tolerance, trackingData
   
    thickness = 2
    color = (0,0,255)
    
    timeout = 5 # 5 Seconds
    startTime = 0
    wp.setup()
    
    while True:
        
        img, objectsInfo = childProcess.recv()
        
        # Si dejamos de detectar animal, pasados 5 segundos volvemos al estado patrol
        if len(objectsInfo) == 0 and startTime == 0:
            startTime = time.time() 
        elif len(objectsInfo) == 0 and startTime != 0:
            currentTime = time.time()
            elapsedTime = currentTime - startTime
            if elapsedTime > timeout:
                mov.stop()
                return 0
            
        elif len(objectsInfo) != 0:
            startTime = 0
        
        trackObjects(objectsInfo)
        
        print("Centro de la imagen en la posición: \n x = ", objXCenter ,"; y = ", objYCenter)
        
        start_point = ( int(objXCenter) , int(objYCenter))
        end_point = (320, int(objYCenter))
        
        if (draw):
            cv2.line(img, start_point, end_point, color, thickness)
            
        mov.visionMovement(xDeviation)
        wp.pulse()
        objXCenter = 320
        xDeviation = 0
    
    return 0
   
        
        
        
        