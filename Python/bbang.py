import RPi.GPIO as GPIO
import time
#NIE ZAPOMNIJ 0x I ""!
#Prawidłowe użycie: htp("0x12")
def htb(heks):
	l = bin(int(heks, 16))[2:].zfill(8)
	return l
din = [1,0,0,1,1,1,1,0] #Dla channel 1 din = [0,1,1,1,1,0,0,1]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.IN)
#print(1)
#GPIO.output(19, 1)
#in = GPIO.input(21)
GPIO.output(22, 1)
GPIO.output(22, 0)
GPIO.setup(22, GPIO.IN)
GPIO.output(24, 0)
licznik = 7
#print(2)
while licznik>=0:
	GPIO.output(19, din[licznik])
	GPIO.output(23, 1)
	GPIO.output(23, 0)
	GPIO.output(19, 0)
	licznik=licznik-1
#print(3)
GPIO.output(24, 1)
while GPIO.input(22)==False:
	time.sleep(0.000001)
#print(4)
GPIO.output(24, 0)
GPIO.output(23, 1)
GPIO.output(23, 0)
GPIO.output(19, 0)
#print(5)
licznik = 11
odata=0
dout = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#print(6)
while licznik>=0: #Całe wczytywanie jest złe, jeśli nawet nie cały program :(
	dout[licznik]=GPIO.input(21) #FIXME
	odata=odata+dout[licznik]*2^(licznik-3) 
	GPIO.output(23, 1)	
	GPIO.output(23, 0)
	GPIO.output(19, 0)	
	licznik=licznik-1
#print(7)
GPIO.output(24, 1)
print(dout)
print(odata*2.5/4096)
GPIO.cleanup()
