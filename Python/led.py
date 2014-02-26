import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
try:
	while 1==1:
		GPIO.output(17, True)
		GPIO.output(27, False)
		time.sleep(0.5) #Czas aktywności
		GPIO.output(17, False)
		GPIO.output(27, True)
		time.sleep(0.5) #Czas spoczynku
except KeyboardInterrupt: #Na wypadek CTRL+C
	GPIO.cleanup()
	exit()

