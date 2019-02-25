from redisConnection import RedisTools
import time
import random
import json
from time import sleep
from Message import Message
#Global Var for cool code ;)
GPS =   "GPS"
ACC =   "ACC"
PULS    =   "PULS"
EMERG   =   "Emerg"
r = RedisTools()
start = int(time.time() )
for i in range (5000):
    #sleep(random.uniform(0,1.5))
    #Recived Message ? 
    #handle message (Commander only at Py)
    #else:collected data from sensor
    m = Message(1)
    m.withEmarg(False)
    r.pipeLpush(EMERG,m.get_data())
    print m.get_message()

    for j in range (2):
        if  j   ==  0:
            m = Message(1)
            #build Message
            m.withGps(random.randint(100,200),random.randint(50,100))
            #insert to pipe the GPS dta
            r.pipeLpush(GPS,m.get_data())
            print m.get_message()
        if  j   ==  1:
            m = Message(1)
            m.withPuls(random.randint(80,100))
            r.pipeLpush(PULS,m.get_data())
            print m.get_message()
        if  j   ==  2:
            m = Message(1)
            m.withAcc(random.randint(100,200),random.randint(100,200),random.randint(100,200))
            r.pipeLpush(ACC,m.get_data())
            print m.get_message()
    r.pipeExecute()
    #RFBREIGE BROADCAST
    if (r.llen(GPS)>1000):
        print "Empty GPS"
        r.emptyGPS()
    if (r.llen(ACC)>1000):
        print "Empty ACC"
        r.emptyACC()
    if (r.llen(PULS)>1000):
        print "Empty PULS"
        r.emptyPuls()
for i in range (r.llen(GPS)):
    print   r.lpop(GPS)

for i in range (r.llen(PULS)):
    print   r.lpop(PULS)

for i in range (r.llen(ACC)):
    print   r.lpop(ACC)

End = int(time.time() )

print 'program start at  ',start ,'and finish at end ',End,' and it take ',End-start,'sec'
