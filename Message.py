import json
import time
#Global Var for cool code ;)
GPS     =   "GPS"   
ACC     =   "ACC"  
PULS    =   "PULS" 
Time    =   "Time"   
FLAG    =   "FLAG" 
EMERG   =   "Emerg"
witeSpace   =   " "
nothing =   ""
OR  =   "|"
P   =   "P"    
A   =   "A" 
Y   =   "y" 
X   =   "x" 
G   =   "G"
Z   =   "z"    
E   =   "E" 
D   =   "D" 
M   =   "M" 
T   =   "T"
HB  =   "HB"
F   =   "F"

class Message():
    def __init__(self, nodeId):#Init with nodeID#
        self.src = nodeId
        self.dataToRedis = {}
        self.dest = 0 
    
    def withPuls(self,val):#SettingPulse#
        self.set_time(time.time())
        self.setDataToPrint(P,str(val))
        self.setDataToRedis(PULS,{HB:str(val),Time:self.get_time()})
        return self

    def withEmarg(self,val):#SettingEmerg
        self.set_time(time.time())
        self.setDataToPrint(E,str(val))
        self.setDataToRedis(EMERG,{FLAG:str(val),Time:self.get_time()})
        return self

    def withAcc(self,x,y,z):
        self.set_time(time.time())
        self.setDataToPrint(A,{X:str(x),Y:str(y),Z:str(z)})
        self.setDataToRedis(ACC, {'X' : x , 'Y' : y , 'Z' : z,Time:self.get_time()})
        return self
    
    def withGps(self,x,y):
        self.set_time(time.time())
        self.setDataToPrint(G,{X:str(x),Y:str(y)})
        self.setDataToRedis(GPS,{'X':x ,'Y':y,Time:self.get_time()})
        return self

    def set_time(self,time):
        self.time =  int(time)

    def get_time(self):
        return self.time

    def get_dest(self):
        return self.dest
    
    def set_dest(self,nodeid):
        self.dest = nodeid
    
    def get_data(self):
        return json.dumps(self.dataToRedis)

    def get_message(self):
        try:
            self.msg.clear()
        except :
            self.msg = {}
        self.msg={D:str(self.dest),T:str(self.time),M:self.dataToPrint,F:self.src}
        return json.dumps(self.msg).replace(witeSpace, nothing).replace('{',nothing).replace('}',nothing).replace('"',nothing).replace("M:",OR).replace("'",nothing)

    def setDataToPrint(self,prifix,value):
        try:
            self.dataToPrint.clear()
        except :
            self.dataToPrint = {}
        temp = str(value) + OR
        self.dataToPrint = {prifix:temp}
        self.set_time(int(time.time()))

    def setDataToRedis(self,key,data):
        try:
            self.dataToRedis.clear()
        except :
            self.dataToPrint = {}
        self.dataToRedis[key] = data 
