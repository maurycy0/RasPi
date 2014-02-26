import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
def swiec():
	GPIO.output(17, True)
	GPIO.output(27, True)
a=0.3
brk=False
def odej():
	global a
	while a>=0:
		a=a-0.001
		if(a>0):
			print(round(a, 3))
		if(brk == True):
			break
		if(a>0.05):
			time.sleep(0.1)
		elif(0.5>a>0.1):
			time.sleep(0.5)
		elif(a<0.1):
			time.sleep(1)
try:
	threading.Thread(target=odej).start()
	while 1==1:
		GPIO.output(17, True)
		GPIO.output(27, True)
		if(a>0):
			time.sleep(a) #Czas aktywności
		GPIO.output(17, False)
		GPIO.output(27, False)
		if(a>0):
			time.sleep(a) #Czas spoczynku
		if(abs(round(a, 3))==0):
			swiec()
			print("FULL POWAH!")
			time.sleep(2)
			GPIO.cleanup()
			break
except KeyboardInterrupt: #Na wypadek CTRL+C
	GPIO.cleanup()
	brk=True
	exit()
