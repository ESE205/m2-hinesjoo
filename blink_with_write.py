import RPi.GPIO as GPIO
from time import sleep
import argparse
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin11 = 11
pin5 = 5

GPIO.setup(pin11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin5, GPIO.IN)

parser = argparse.ArgumentParser(description=
                'Reads in Debug, Frequency, and Time Arguments')
parser.add_argument('--Time', type=int,
                    default=5, help='Total time for blinks to occur (default: 5)')
parser.add_argument('--Period', type=float,
                    default=1, help='Timer per blink (default: 1)')
parser.add_argument('--Debug', type=bool,
                    default=False, help='Will it print extra debug print statements.')
args = parser.parse_args()

Time = args.Time
Period = args.Period
Debug = args.Debug
Freq = 1/Period

IterCount = Freq * Time
IterCount = int(IterCount)
loop = 0;

switchState= GPIO.input(pin5)
while switchState == False:
    switchState = GPIO.input(pin5)

with open('data.txt', 'a') as f:
    loop = 0
    while IterCount > 0:
        loop += 1
        if Debug:
            print(f'Number of times through loop: {loop}')
        IterCount -= 1

        GPIO.output(pin11, GPIO.HIGH)
        f.write(f'{loop}\tON\n')
        sleep(1 / Freq)

        GPIO.output(pin11, GPIO.LOW)
        f.write(f'{loop}\tOFF\n')
        sleep(1 / Freq)

GPIO.cleanup()
