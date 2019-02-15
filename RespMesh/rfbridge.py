import serial
import sys

ser = serial.Serial('COM4',115200,timeout=0)
# ser= serial.Serial('/dev/ttyUSB0',115200)                

class RFBridge:
        def __init__(self,nodeid):
                self.nodeid = nodeid

	def begin(self):
                while 1:                                
                        if(ser.in_waiting > 0):
                                line = self.read()
                                print line
                                if line == '<START>':
                                        self.set_nodeid(self.nodeid)  

	def read(self):
                return ser.readline()

	def write(self,message):
                ser.writelines('<SEND>'+'\n'+str(message))

        def set_nodeid(self,nodeid):
                ser.writelines('<SET_NODE_ID>'+'\n'+str(nodeid))