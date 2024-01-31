import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pin11 = 11
pin5 = 5
GPIO.setup(pin11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin5, GPIO.IN)

switchState = GPIO.input(pin5)
while switchState == False:
    switchState = GPIO.input(pin5)
    sleep(.5)

GPIO.output(pin11, GPIO.HIGH)
sleep(.5)
GPIO.cleanup()
