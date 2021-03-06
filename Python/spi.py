import RPi.GPIO as GPIO
import os
import time
file = open("kaszwyn.txt", "w")
file.write("")
file.close()
file = open("kaszwyn.txt", "a")
din = [0,1,1,1,1,0,0,1] #ch1
#din = [0,1,1,1,1,0,1,1] #ch2
#din = [0,1,1,1,0,1,0,1] #ch3
#din = [0,1,1,1,0,1,1,1] #ch4
dout = [0,0,0,0,0,0,0,0,0,0,0,0]
kaszref = 5000
kaszlicz = kaszref
kaszdan = []
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.IN)
GPIO.output(22, 1)
GPIO.output(22, 0)
GPIO.setup(22, GPIO.IN)
start = time.clock()
while kaszlicz>=0:
#while True:	
	GPIO.output(24, 0)
	licznik = 7
	while licznik>=0:
		GPIO.output(19, din[licznik])
		GPIO.output(23, 1)
		GPIO.output(19, 0)
		GPIO.output(23, 0)
		licznik=licznik-1
	GPIO.output(24, 1)
	while GPIO.input(22)==False:
		pass
	GPIO.output(24, 0)
	GPIO.output(23, 1)
	GPIO.output(19, 0)
	GPIO.output(23, 0)	
	licznik = 11
	while licznik>=0:
		dout[licznik]=str(GPIO.input(21))
		GPIO.output(23, 1)	
		GPIO.output(23, 0)
		GPIO.output(19, 0)	
		licznik=licznik-1
	GPIO.output(24, 1)
	dout.reverse()
	tset = ''.join(dout)
	tset = int(tset, 2)
	kaszdan.append(round(tset*0.00061, 3))
	#print(str(round(tset*0.00061, 3))+"\r", end="")
	#try:
	#	time.sleep(0.1)
	#except KeyboardInterrupt:
	#	GPIO.cleanup()
	#	exit()
	#kaszlicz=kaszlicz-1
#print(kaszdan)
end = time.clock()
print("Odczyt danych trwał "+str(round(end-start, 3))+"s")
kaszlicz = kaszref
start = time.clock()
while kaszlicz>=0:
	file.write(str(kaszdan[kaszlicz])+"\n")
	kaszlicz=kaszlicz-1
end = time.clock()
print("Zapis do pliku trwał "+str(round(end-start, 5))+"s")
file.close()
GPIO.cleanup()
