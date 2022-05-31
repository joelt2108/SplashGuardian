import RPi.GPIO as GPIO
import time

# Pins from Raspberry Pi 4B

# Left wheel
motor1e2 = 24
motor1m2 = 23

# Right wheel
motor2e1 = 27
motor2m1 = 22
pwm = None
pwm2 = None

def setup():
    global pwm
    global pwm2
    GPIO.setmode(GPIO.BCM)  # GPIO numbering
    
    GPIO.setup(motor1e2,GPIO.OUT)
    GPIO.setup(motor1m2,GPIO.OUT)
    GPIO.setup(motor2e1,GPIO.OUT)
    GPIO.setup(motor2m1,GPIO.OUT)
    pwm = GPIO.PWM(motor1e2, 1000)
    pwm2 = GPIO.PWM(motor2e1, 1000)
    
def turnLeft(dc):
    GPIO.output(motor2e1,GPIO.HIGH)
    GPIO.output(motor2m1,GPIO.HIGH)
    pwm2.start(dc)
    
def turnRight(dc):
    GPIO.output(motor1e2,GPIO.HIGH)
    GPIO.output(motor1m2,GPIO.LOW)
    pwm.start(dc)
    

def goStraight():
    GPIO.output(motor2e1,GPIO.HIGH)
    GPIO.output(motor2m1,GPIO.HIGH)
    GPIO.output(motor1e2,GPIO.HIGH)
    GPIO.output(motor1m2,GPIO.LOW)

def goBack():
    GPIO.output(motor2e1,GPIO.HIGH)
    GPIO.output(motor2m1,GPIO.LOW)
    GPIO.output(motor1e2,GPIO.HIGH)
    GPIO.output(motor1m2,GPIO.HIGH)
    
def stop():
    pwm.stop()
    pwm2.stop()
    GPIO.output(motor2e1,GPIO.LOW)
    GPIO.output(motor2m1,GPIO.LOW)
    GPIO.output(motor1e2,GPIO.LOW)
    GPIO.output(motor1m2,GPIO.LOW)
    time.sleep(1)

def clean():
    GPIO.cleanup()
    
def visionMovement(d):
    if d <= -220 and d > -240:
        print("Going right")
        turnLeft(20)
        time.sleep(0.05)
        stop()
    elif d >= 220 and d < 240:
        print("Going Left")
        turnRight(20)
        time.sleep(0.05)
        stop()
    elif d > -220 and d < 220:
        print("Going Straight")
        goStraight()
    else:
        print("Stopped")
        stop()
    
setup()
goStraight()
time.sleep(0.5)
stop()
    