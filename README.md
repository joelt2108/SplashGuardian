# SplashGuardian


# Table of Contents
* [What is this?](#what-is-this)
* [Requeriments](#requeriments)
* [How to use](#how-to-us)
* [Components](#components)
* [Hardware Scheme](#hardware-scheme)
* [3D Pieces](#3d-pieces)
* [Software Modules](#software-modules)
* [Amazing Contributions](#amazing-contributions)
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


# Authors

- Marcel Sarraseca - 1531206
- Oriol Serrat - 1423392
- Domènec Madrid - 1496304
- Joel Trujillo - 1494261


