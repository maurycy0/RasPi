import RPi.GPIO as GPIO
def andi(ch):
	'''MAX 1248 Analog-Digital coverter library for Python 3. Library uses standard ports marked as SPI to comunicate with MAX. To use it, you need
	to have installed RPi.GPIO lib. Usage: 'ADClib.andi(chnl)' where chnl is channel that you want to recive data from. (If other than 1-4 given, 
	the default is 1). Data is represented as voltage rounded to four decimal places. To get rid of 'channel already in use' warnings, add at the end
	of your	program that line: 'ADClib.GPIO.cleanup()' Root is needed to use GPIO.
	(C) 2014 Maurycy Piecha AKA C4N4D4. If you have any questions write me an e-mail at maurycy.piecha@yahoo.com'''
	dout = [0,0,0,0,0,0,0,0,0,0,0,0]
	din = [0,1,1,1,1,0,0,1] #Default ch1	
	if ch==1:
		din = [0,1,1,1,1,0,0,1] #ch1
	if ch==2:
		din = [0,1,1,1,1,0,1,1] #ch2
	if ch==3:
		din = [0,1,1,1,0,1,0,1] #ch3
	if ch==4:
		din = [0,1,1,1,0,1,1,1] #ch4		
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(22, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(19, GPIO.OUT)
	GPIO.setup(21, GPIO.IN)
	GPIO.output(22, 1)
	GPIO.output(22, 0)
	GPIO.setup(22, GPIO.IN)
	GPIO.output(24, 0)
	count = 7
	while count>=0: #Settings write loop
		GPIO.output(19, din[count])
		GPIO.output(23, 1)
		GPIO.output(19, 0)
		GPIO.output(23, 0)
		count=count-1
	GPIO.output(24, 1)
	while GPIO.input(22)==False: #Wait for SSTRB
		pass
	GPIO.output(24, 0)
	GPIO.output(23, 1)
	GPIO.output(19, 0)
	GPIO.output(23, 0)	
	count = 11
	while count>=0: #Data read loop
		dout[count]=str(GPIO.input(21)) 
		GPIO.output(23, 1)	
		GPIO.output(23, 0)
		GPIO.output(19, 0)	
		count=count-1
	GPIO.output(24, 1)
	dout.reverse() #Little endian to big endian
	rever = ''.join(dout) #Array to int
	rever = int(rever, 2) #Convert from binary
	return round(rever*0.00061, 4) #Converting to volts and rounding to 4 decimal places, then returning
	GPIO.cleanup() #Cleanup
