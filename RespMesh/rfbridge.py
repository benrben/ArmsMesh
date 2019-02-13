import serial


class RFBridge:
	ser= serial.Serial('/dev/ttyUSB0',115200)
	def begin(self):
                        while 1:                                
                                if(self.ser.in_waiting > 0):
                                        line = self.read()
                                        print line

	def read(self):
                        return self.ser.readline()

	def write(self,message):
                        self.ser.write('<SEND>')
                        self.ser.write(message)
