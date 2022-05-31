# SplashGuardian


# Table of Contents
* [What is this?](#what-is-this)
* [Requeriments](#requeriments)
* [How to use](#how-to-us)
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
-[Flutter](https://flutter.dev/)
-[Cloud Firebase Storage](https://firebase.google.com/docs/storage)
-[Path Provider](https://pub.dev/packages/path_provider)


