import Navigation as nav
import Follower as fol
import Detector as det
from multiprocessing import Process, Pipe
import cv2
import keyboard

patrol_state = 0
follower_state = 1

currentState = patrol_state

def parentData(parent):
    global currentState
    # Inicializamos lectora de video con indice 0
    cap = cv2.VideoCapture(0)
    print("[PARENT]: Start recording...")
    # Medidas de la pantalla que muestran las imagenes con la deteccion
    cap.set(3,640)
    cap.set(4,480)
   
    thickness = 2
    color = (0,0,255)
    
    while True:
        print("[PARENT]: Starting loop")
        # Leemos input de la camara
        success, img = cap.read() 
        img, objectsInfo = det.getObjects(img, 0.45, 0.2, objects=['cat'])
        img_detection = [img, objectsInfo]
        ''' This function sends the data for the parent process '''
        parent.send(img_detection)
        print("Waiting state")
        #currentState = parent.recv()
        print("State: ", currentState)
        
    parent.close()
    child.close()
    cv2.VideoCapture(0).release()

def childData(child):
    currentState = patrol_state
    while True: 
        if currentState == patrol_state:
            print("Patrol state")
            currentState = nav.patrol(child)
        elif currentState == follower_state:
            currentState = fol.run(child)

if __name__ == "__main__":
    
    parent, child = Pipe() # Create Pipe
    
    process1 = Process(target = parentData, args = (parent,)) # Create a process for handling parent data
    process2 = Process(target = childData, args = (child,)) # Create a process for handling child data
    
    process1.start() # Start the  parent process
    process2.start() # Start the child process
           
