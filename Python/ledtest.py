import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
try:
	p = GPIO.PWM(27, 100)
	p.start(50)
	while True:
		pass
	#while 1==1:
	#	GPIO.output(27, True)
	#	#time.sleep(0.0001)
	#	GPIO.output(27, False)
	#	#time.sleep(0.0001)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
