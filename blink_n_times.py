import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
IterCount = input("How many times would you like the LED to Blink?")
if IterCount == "":
    IterCount = 5;
IterCount = int(IterCount)
pin11 = 11
pin5 = 5
GPIO.setup(pin11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin5, GPIO.IN)
switchState= GPIO.input(pin5)
while switchState == False:
    switchState = GPIO.input(pin5)
while IterCount > 0:
    IterCount -= 1
    GPIO.output(pin11, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin11, GPIO.LOW)
    sleep(1)
GPIO.cleanup()
