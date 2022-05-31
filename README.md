# SplashGuardian
Get the cats out without stopping to do what you are doing

# Table of Contents
* [What is this?](#what-is-this)
* [Requeriments](#requeriments)
* [How to use](#how-to-us)
* [Components](#components)
* [Hardware Scheme](#hardware-scheme)
* [3D Pieces](#3d-pieces)
* [Software Arquitecture](#sw-arq)
* [Software Modules](#software-modules)
* [Splash Guardian App](#sg-app)
* [Amazing Contributions](#amazing-contributions)
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
- Clone this repo
- > git clone https://github.com/joelt2108/SplashGuardian.git
For the robot code:
- Execute python script with:
- > python3 core.py

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

# License
MIT

# HW/SW Bibliography
- https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
- https://raspberrypi.stackexchange.com/questions/22105/powering-a-3-12v-water-pump-on-raspberry-pi
- https://github.com/Arijit1080/Send-Image-from-Raspberry-Pi-to-Firebase-Storage
- https://docs.flutter.dev/cookbook/persistence/reading-writing-files
- https://github.com/thisbejim/Pyrebase
- https://of3lia.com/tinkercad-tutorial-completo/
- 
- 

# Authors

- Marcel Sarraseca - 1531206
- Oriol Serrat - 1423392
- Domènec Madrid - 1496304
- Joel Trujillo - 1494261


