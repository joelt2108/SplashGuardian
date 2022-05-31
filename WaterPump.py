import RPi.GPIO as GPIO
import time
# Pins
waterbomb = 18

def setup():
    GPIO.setmode(GPIO.BCM)  # GPIO numbering
    GPIO.setup(waterbomb,GPIO.OUT)

def pulse():
    GPIO.output(waterbomb,GPIO.HIGH)
    print("Echando agua durante 0.2 segundos...")
    time.sleep(0.2)
    GPIO.output(waterbomb, GPIO.LOW)

setup()
pulse()