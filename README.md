<img src="https://github.com/joelt2108/SplashGuardian/blob/562c631e5119083edd847aa0cb306bb176fc3076/3d_pieces/Pictures/robot.jpeg?raw=true" align="right" width="300" alt="header pic"/>


# SplashGuardian
Get the cats out without stopping to do what you are doing

# Table of Contents
* [What is this?](#what-is-this)
* [Requeriments](#requeriments)
* [How to use](#how-to-us)
* [Components](#components)
* [Hardware Scheme](#hardware-scheme)
* [3D Pieces](#3d-pieces)
* [Software Arquitecture and Modules](#sw-arq)
* [Splash Guardian App](#sg-app)
* [Amazing Contributions](#amazing-contributions)
* [Video](#video)
* [License](#license)
* [HW/SW Bibliography](#bibliography)
* [Authors](#authors)

# What is this?
Autonomous guard robot that walks the perimeter of the house in search of intruding cats. When it detects an unidentified cat,  proceeds to shoot water in order in order to expel him from the house.

It has two operating modes, the automatic mode, where the robot patrols on its own and will shoot if it finds an intruding cat and the manual mode, where thanks to a complementary app the owner will be notified with a photo of the detection of a cat in real time, being able to decide whether to shoot or not. This mode is very useful for homes where they have cats as pets.

# Requeriments

To run the code it's needed:

- [Python 3.10.x](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [OpenCV](https://opencv.org/)
- [Matplotlib](https://matplotlib.org/)
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
- [Multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [Pyrebase](https://pypi.org/project/Pyrebase/)

Also for the Companion App it's needed:

- [Flutter](https://flutter.dev/)
- [Cloud Firebase Storage](https://firebase.google.com/docs/storage)
- [Path Provider](https://pub.dev/packages/path_provider)

# How to use
Clone this repo
 > git clone https://github.com/joelt2108/SplashGuardian.git
- For the robot code:
- Execute python script with:
 > python3 core.py

For the Splash  Guardian App:
- Open the Android Studio and select Tools from the menu bar and click on SDK Manager. 
- In the newly open window click on the plugins and in the search bar search for Flutter and Dart and then install it.
- Now after installing Flutter and Dart we are ready to import a Flutter project.
 
 
  

# Components
- Raspberry Pi 4 B
- USB Camera
- Water Pump 12v
- x2 DC Motors
- HC-SR04
- Protoboard
- Battery 9v
- Battery 5v
- Powerbank 5v
- Bridge Motor Driver l298n
- 1K resistor
- 2,2K resistor


# Hardware Scheme
Next we can see the HW Scheme of the robot, including the components:
![HW](https://github.com/joelt2108/SplashGuardian/blob/2b500098e9b533b0f96ddb3a81903da9c16eba69/3d_pieces/Pictures/Final%20HW.jpg)


# 3D Pieces
For the correct operation of the robot, it has been necessary to generate the following 3d pieces:
### Robot chassis
![Chasis](https://github.com/joelt2108/SplashGuardian/blob/befbb2aa569ef52fd8c57cf71dd9878c6da6a263/3d_pieces/Pictures/Chasis.png)

### Top
![Top](https://github.com/joelt2108/SplashGuardian/blob/befbb2aa569ef52fd8c57cf71dd9878c6da6a263/3d_pieces/Pictures/Superior.png)

### Idler wheel
![Rueda](https://github.com/joelt2108/SplashGuardian/blob/befbb2aa569ef52fd8c57cf71dd9878c6da6a263/3d_pieces/Pictures/Rueda.png)

### Support for dc-motor(x2)
![Soporte](https://github.com/joelt2108/SplashGuardian/blob/befbb2aa569ef52fd8c57cf71dd9878c6da6a263/3d_pieces/Pictures/Soporte.png)

# Software Arquitecture and Modules
Next we can see the SW arquitecture of the robot, including the modules:
![SW](https://github.com/joelt2108/SplashGuardian/blob/bdac6626d5751c185b5a642234965b51a724660c/3d_pieces/Pictures/sw_arqt.png)

- Core: This is the central module of the robot, which is responsible for joining all the other modules

- Camera: This module will be responsible for detecting real-time images that reach the robot, using the camera.

- Detection and analysis: After obtaining the images, the robot is responsible for processing the images obtained in search of cats.

- Ultrasonic Sensor: Gets the distance detected through the ultrasonic sensor connected to the raspberry.

- Water pump: module responsible for actuating the water pump connected to the raspberry.

- Navigation: In this module the robot executes an autonomous motion algorithm while looking for cats around the robot.

- Tracking: In this module the robot analyzes the position of the animal detected in the image and calculates the necessary turn to follow the animal.

- Movement: Receive instructions to perform specific movements as appropriate. Move the robot forward, backward, left and right at different speeds.

### Flow Diagram Movement
Here we can see how the robot moves. First, after initialazing the camera, searching for a cat, the robot will start the autonomous navigation process, where the robot advance during 5 seconds or until the ultrasound sensor detects an obstacle. In that case, the robot will rotate on itself, repeating the process. If a cat is detected here, the robot will follow the cat to a specific distance and will activate the water pump.

![flux](https://github.com/joelt2108/SplashGuardian/blob/bdac6626d5751c185b5a642234965b51a724660c/3d_pieces/Pictures/flux.png)


The autonomous navigation mode is perfomed with the following 3-step algorithm:

1. Move forward for 5 seconds or until a blocking object is detected
2. Perform a 360 degree spin while analizing the images recieved
3. Choose a new direction rotate right or left based on position until it finds a clear path

For all three steps the robot is constantly analyling the captured frames for cat detection. In case it detects one, it stops its current step and switches to patrol mode.

Patrol mode starts whenever the robot detects a cat, then it moves forward in the cat's direction. In case the cat is not aligned with the robot it adjusts its rotation until it faces he cat. When the robot gets close enough to the cat it activates the water pump.

# Splash Guardian App
In addition, the robot has a complementary application for Android devices, which is responsible for sending the user a real-time photo from the robot when it detects a cat.
![Gat](https://github.com/joelt2108/SplashGuardian/blob/16fdb5fd2e6771aaf1f24b85c1d7830ed9455bd4/3d_pieces/Pictures/gat.jpg)

It also allows you to remotely control the water pump when viewing the image, perfect for users who have a cat at home and do not want to get wet. The application is developed using Flutter, a framework for the Dart programming language. Firebase is also used to store photos as a link between the Raspberry and the app, thanks to its storage service.

![AppScheme](https://github.com/joelt2108/SplashGuardian/blob/bf5d9438d964a7e96ad7833e64fd358d2a8a2a02/3d_pieces/Pictures/appscheme.png)


# Amazing Contributions
- Splash Guardian allows you to go out in the garden without having to find unwanted feline guests

- Prevents cats from entering the house.

- People who are allergic to cats will no longer have to suffer.

- You will be able to open doors and windows with peace of mind

# Video


# License
MIT

# HW/SW Bibliography
- https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
- https://core-electronics.com.au/guides/object-identify-raspberry-pi/
- https://raspberrypi.stackexchange.com/questions/22105/powering-a-3-12v-water-pump-on-raspberry-pi
- https://github.com/Arijit1080/Send-Image-from-Raspberry-Pi-to-Firebase-Storage
- https://docs.flutter.dev/cookbook/persistence/reading-writing-files
- https://github.com/thisbejim/Pyrebase
- https://of3lia.com/tinkercad-tutorial-completo/


# Authors

- Marcel Sarraseca - 1531206
- Oriol Serrat - 1423392
- Domènec Madrid - 1496304
- Joel Trujillo - 1494261


