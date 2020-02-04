#--- external modules ---#
import sys #system module
from time import sleep # time module with the function of sleep, sleep pauses the python program from executing
import RPi.GPIO as GPIO # imports the GPIO library to 

GPIO.setmode(GPIO.BOARD)     # set up BAOARD GPIO numbering
#--- Set up input pin, for sensor ---#
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#--- Set up LED output ---#
GPIO.setup(20, GPIO.OUT)

#--- Callback function to run when motion detected ---#
def motionSensor(channel):
   GPIO.output(20, GPIO.LOW)
   if GPIO.input(21):     # True = Rising
       global counter
       counter += 1
       GPIO.output(20, GPIO.HIGH)

#--- add event listener on pin 21 for motion sensor ---#
GPIO.add_event_detect(21, GPIO.BOTH, callback=motionSensor, bouncetime=300) 

counter = 0
try:
   while True:
       sleep(1)         # wait 1 second
finally:                   # run on exit
   GPIO.cleanup()         # clean up
   print("All cleaned up")
