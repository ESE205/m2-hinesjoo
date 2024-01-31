import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
IterCount = input("How many times would you like the LED to Blink?")
if IterCount == "":
    IterCount = 5;
IterCount = int(IterCount)
pin3 = 3
pin5 = 5
GPIO.setup(pin3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin5, GPIO.IN)
switchState= GPIO.input(pin5)
while switchState == False:
    switchState = GPIO.input(pin5)
while IterCount > 0:
    IterCount -= 1
    GPIO.output(pin3, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin3, GPIO.LOW)
    sleep(1)
GPIO.cleanup()
