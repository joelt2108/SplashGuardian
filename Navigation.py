# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:04:08 2022

@author: Oriol
"""
from math import *
import numpy as np
import Distance as sn
import Movement as mov
import Detector as det
import random
import time 
import cv2
from matplotlib import pyplot as plt
from multiprocessing import Process, Pipe

cornerPairList = []

stopDistance = 0.2
radarThreshold = 200
matrixSize = radarThreshold*2 # each cell represents a centimetre in range of ultrasound with a radius of 200cm 
collisionMatrix = np.zeros([matrixSize,matrixSize,3])
collisionMatrix[:,:,0] = np.ones([matrixSize,matrixSize])*255
collisionMatrix[:,:,1] = np.ones([matrixSize,matrixSize])*255
collisionMatrix[:,:,2] = np.ones([matrixSize,matrixSize])*255
scanTime = 1.5 # 2 sec to make a 360 deg spin
angularVelocity = radians(360)/scanTime # 0.7853981633974483
dist_array = []

def getHarrisCorners(img):
    # Load the image and convert to grayscale
    img2 = cv2.imread('test3.png')
    cv2.imshow("output", img.astype(np.uint8))
    print(img.astype(np.uint8))
    print(img.shape)
    gray = cv2.cvtColor(img.astype(np.uint8),cv2.COLOR_BGR2GRAY)
    
    # find Harris corners as we did in the previous blog
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,5,0.08)
    dst = cv2.dilate(dst,None)
    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
    dst = np.uint8(dst)
    
    # Pixel Accuracy
    # find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

    # define the criteria to stop. We stop it after a specified number of iterations
    # or a certain accuracy is achieved, whichever occurs first.
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)

    # Refine the corners using cv2.cornerSubPix()
    corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

    # To display, first convert the centroids and corners to integer
    centroids = np.int0(centroids)
    corners = np.int0(corners)

    # then i have used red color to mark Harris Corners
    # and green color to mark refined corners
    img[centroids[:,1], centroids[:,0]]=[0,0,255] # red
    img[corners[:,1], corners[:,0]] = [0,255,0] # green
    
    # show the image
    cv2.imwrite('subpixel.png', img)
    cv2.imshow('Image with corners', img) 
      
    cv2.waitKey(30000);
    cv2.destroyAllWindows();
    cv2.waitKey(1)
        
    return img

def getCoordinates(img, lowerBorder):
    # Get X and Y coordinates of all red pixels
    colour = [0,0,255]
    Y, X = np.where(np.all(img==colour,axis=2))
    print(X,Y)
    
    # Mesh coordinates list in tuple list (x, y)
    cornerPairList = list(zip(X,Y))
    
    # Check for corners in the image's border (which are not detected by harris function)
    if lowerBorder:
        borderY = int((matrixSize/2) - 1)
    else:
        borderY = 0
       
    colour = [0,0,0]
    X = np.where(np.all(img[-1, :]==colour, axis=1) )
    Y = np.array([borderY])
    borderCoord = list(zip(X[0],Y))
    cornerPairList = cornerPairList + borderCoord
    
    print(cornerPairList)
    
    return cornerPairList

# Performs a spin of 360 degrees while generating a 2d matrix map of the space
# detected around the robot. Returns a list of the obstacle's corners coordinates
# represented in the 2d matrix 
def scan(childProcess):

    global radarThreshold, collisionMatrix
    
    mov.turnRight(25)
    startTime = time.time()
    turnTime = scanTime
    
    print("Scanning for " + str(turnTime)  + " seconds")
    
    while True:
        
        #img_detection = childProcess.recv()
        #if len(img_detection[1]) != 0:
        #    print("Animal detected. Switching robot mode at" + str(elapsedTime)  + " seconds")
        #    return [], True
        
        # Send ultrasounic signal and get collision distance
        distance = sn.calc_VJ_dist()
        
        # Update time values
        currentTime = time.time()
        elapsedTime = currentTime - startTime
    
        # Get the current robot angle
        spinAngle =  degrees(angularVelocity * elapsedTime)
        auxAngle = 180 - 90 - spinAngle
        
        #("Elapsed time: " + str(elapsedTime)  + " seconds")
        #print("Robot angle: " + str(spinAngle)  + " degrees")
        
        # Store collision data in the matrix
        if distance <= radarThreshold:
            x = int( distance * sin(spinAngle) / sin(90))
            y = int( distance * sin(auxAngle) / sin(90))
            
            collisionMatrix[y][x] = [0,0,0]
    
        if elapsedTime > turnTime:
            print("Scan finished in " + str(elapsedTime)  + " seconds")
            break
        
    mov.stop() # The robot should be in starting position
    print("\n", collisionMatrix)
           
    #Once the collision scan has been completed, use harris detector to find corners in the matrix
    img_detection[0] = getHarrisCorners(collisionMatrix)
    
    
    # Split matrix into 4 submatrix
    print(img_detection[0].shape)
    upper_half = np.hsplit(np.vsplit(img_detection[0], 2)[0], 2)
    lower_half = np.hsplit(np.vsplit(img_detection[0], 2)[1], 2)
    
    upperLeft = upper_half[0]
    upperRight = upper_half[1]
    lowerLeft = lower_half[0]
    lowerRight = lower_half[1]
     
    
    # upperLeft: order the coordinates from min Y to max Y
    upperLeftCorners = getCoordinates(upperLeft, True)
    upperLeftCorners.sort(key=lambda tup: tup[1]) #ascending order by default

    #get first intersection point (first_coordinate_in_list.x, img_detection[0].size/2 - 1) -> append front list
    leftIntersection = (upperLeftCorners[0][0], int((matrixSize/2) - 1))
    upperLeftCorners.insert(leftIntersection)

    print("Upper Left Corners: ", upperLeftCorners)

    #upperRight order the coordinates from max Y to min Y
    upperRightCorners = getCoordinates(upperRight, True)
    upperRightCorners.sort(key=lambda tup: tup[1], reverse=True)

    #get second intersection point (last_coordinate_in_list.x, img_detection[0].size/2 - 1) -> append back list
    rightIntersection = (upperRightCorners[-1][0], int((matrixSize/2) - 1))

    print("Upper Right Corners:", upperRightCorners)
    
    #lowerLeft order the coordinates from max Y to min Y
    lowerLeftCorners = getCoordinates(lowerLeft, True)
    lowerLeftCorners.sort(key=lambda tup: tup[1], reverse=True)
    print("Upper Left Corners:", upperLeftCorners)
    
    #lowerRight order the coordinates from min Y to max Y
    lowerRightCorners = getCoordinates(lowerRight, True)
    lowerRightCorners.sort(key=lambda tup: tup[1])
    print("Upper Right Corners:", upperRightCorners)
    
    cornerPairList = upperLeft + upperRight + lowerLeft + lowerRight
    
    # Make tuples with adjacent corners which are not connected
    # printing original list
    print("The original corner list : " + str(cornerPairList))
      
    # consecutive element pairing 
    cornerPairList = list(zip(cornerPairList, cornerPairList[1:])) 
    print("Paired list : " + str(cornerPairList))

    #cornerPairList = []
    return cornerPairList, False
    
def normal_scan():
    global dist_array
    
    mov.turnRight(35)
    startTime = time.time()
    turnTime = scanTime
    
    print("Scanning for " + str(turnTime)  + " seconds")
    
    while True:
        
        #img_detection = childProcess.recv()
        #if len(img_detection[1]) != 0:
        #    print("Animal detected. Switching robot mode at" + str(elapsedTime)  + " seconds")
        #    return [], True
        
        # Send ultrasounic signal and get collision distance
        distance = sn.calc_VJ_dist()
        dist_array.append(distance)
        # Update time values
        currentTime = time.time()
        elapsedTime = currentTime - startTime
    
        if elapsedTime > turnTime:
            print("Scan finished in " + str(elapsedTime)  + " seconds")
            break
    print(dist_array)
    mov.stop() # The robot should be in starting position
    
def condition(element):
    return element[0] < int(matrixSize/2), element[1]
    
# Checks the distance between each pair of separate corners and the angle 
# between the robot forward direction and the coordinates of the center between
# each pair of corners. Returns the angle related to the corners with most 
# distance between. 
def chooseDirection(cornerPairList):
    
    global radarThreshold
    
    distanceList = []
    angleList = []
    
    for pair in cornerPairList:
        
        # Get distance between the pair of corners 
        distanceList.append(dist(pair[0], pair[1]))  
        
        # Get the central point between the corners
        centrePoint = midpoint(pair[0], pair[1])
        
        # Get angle between robot forward direction and the center point between the pair
        height = radarThreshold - centrePoint[1]
        base = radarThreshold - centrePoint[0]
        angle = atan(base/height)
        angleList.append(angle)
    
    if len(distanceList) == 0:
        return 180
    
    #Return angle of the pair with most distance 
    index = distanceList.index(max(distanceList)) 
    return degrees(angleList[index])

# Returns the middle point between two coordinates
def midpoint(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

def patrol(childProcess):
    
    while True:
        print("Trying detection first loop")
        img_detection = childProcess.recv()
        print("Detected: ", img_detection[1])
        if len(img_detection[1]) != 0:
            print("Animal detected! Switching robot mode at" + str(elapsedTime)  + " seconds")
            mov.stop()
            return 1
        print("Nothing detected")
            
        ### FORWARD MOVEMENT ###
        mov.goStraight()
        startTime = time.time()
        print("StartTime: ", startTime)
        forwardTime = 5
        print("Moving forward for " + str(forwardTime)  + " seconds")
        
        while True:
            print("Trying detection second loop")
            img_detection = childProcess.recv()
            print("Detected: ", img_detection[1])
            if len(img_detection[1]) != 0:
                print("Animal detected! Switching robot mode at" + str(elapsedTime)  + " seconds")
                mov.stop()
                return 1
                
            currentTime = time.time()
            print("CurrentTime: ", currentTime)
            elapsedTime = currentTime - startTime
            distance = sn.calc_VJ_dist()
            print("Elapsed Time: ", elapsedTime)

            if distance <= stopDistance:
                print("\nBlocking object detected at distance: ", distance)
                break
        
            if elapsedTime > forwardTime:
                print("Finished movement in " + str(elapsedTime)  + " seconds")
                break 
        mov.stop()
        mov.goBack()
        time.sleep(0.2)
        mov.stop()
                
        ### SCANNING ###
        #cornerPairList, animalDetected = normal_scan()
        mov.turnRight(70)
        startTime = time.time()
        turnTime = scanTime

        print("Scanning for " + str(turnTime) + " seconds")
        while True:
            print("Trying detection third loop")
            img_detection = childProcess.recv()
            print("Detected: ", img_detection[1])
            if len(img_detection[1]) != 0:
                print("Animal detected! Switching robot mode at" + str(elapsedTime)  + " seconds")
                return 1
            
            # Update time values
            currentTime = time.time()
            elapsedTime = currentTime - startTime

            if elapsedTime > turnTime:
                print("Scan finished in " + str(elapsedTime) + " seconds")
                break;
        
        mov.stop()
        time.sleep(1)

        # Check distance in front of the robot
        distance = sn.calc_VJ_dist()
        if distance > stopDistance:
            print("We can go on!")
            continue

        #angleDegrees = chooseDirection(cornerPairList)

        #angleDegrees = random.randrange(-90, 90, 1) #TODO: remove this line
        #angleDegrees = radians(angleDegrees)
        #turnTime = abs(angleDegrees)/angularVelocity
        
        ### TURN TO NEW DIRECTION ###
        startTime = time.time()
        random.seed(int(time.time()))
        direction = random.randrange(1, 2, 1)
        print("Direction: ",direction)
        if direction == 1:
            mov.turnRight(70)
            print("Turning right")
        else:
            mov.turnLeft(70)
            print("Turning left")
        
        array_dist = []
        for t in range(0,20):
            print("Trying detection fourth loop")
            img_detection = childProcess.recv()
            print("Detected: ", img_detection[1])
            if len(img_detection[1]) != 0:
                print("Animal detected! Switching robot mode at" + str(elapsedTime)  + " seconds")
                mov.stop()
                return 1
            distance = sn.calc_VJ_dist()
            array_dist.append(distance)
            if t > 7:
                if distance > max(array_dist):
                    print("S'ha trobat un valor major")
                    mov.stop()
                    if(direction == 1):
                        mov.turnLeft(70)
                        time.sleep(0.1)
                    else:
                        mov.turnRight(70)
                        time.sleep(0.1)
                    break
        mov.stop()
        time.sleep(1)

    return 0

    
        
        
    
    
    
    
    
    
    