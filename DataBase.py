import pyrebase
import os
import cv2
import Detector as det
import time
import water_pump as wp
firebaseConfig = {
    'apiKey': "AIzaSyAy6IRiXUNwzdTh4sp4VWpTbnvZemncNvM",
    'authDomain': "imagerpi-bef13.firebaseapp.com",
    'projectId': "imagerpi-bef13",
    'storageBucket': "imagerpi-bef13.appspot.com",
    'messagingSenderId': "553544890209",
    'appId': "1:553544890209:web:987ae70e9f2a18f07af720",
    'databaseURL': "gs://imagerpi-bef13.appspot.com"

}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

wp.setup()

while True:
    # Leemos input de la camara
    success, img = cap.read() 
    
    img, objectsInfo = det.getObjects(img, 0.45, 0.2, objects=['cat'])
    cv2.imshow('webCam', img)
    cv2.waitKey(500);
    
    if objectsInfo != []:
        cv2.imwrite("output.jpg",img)
        storage.child("output.jpg").put("output.jpg")
        print("Se ha enviado la imagen")
        time.sleep(5)
        print("Se ha recibido")
        storage.child("read.txt").download("read.txt")
        datos = open("read.txt", "r")
        valores = []
        for linea in datos:
            if linea == "false":
                wp.pulse()
            
capture.release()
cv2.destroyAllWindows()
        
        
    
