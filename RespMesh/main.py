from rfbridge import RFBridge 
import threading
import time
from message import Message

bridge = RFBridge()

def testFunction():
        timer = int(round(time.time() * 1000))
        message = Message()
        while(1):
                delta = int(round(time.time() * 1000))-timer
                if delta > 3000:
                        timer = int(round(time.time() * 1000))
                        message.gps(23.12,23.12)
                        message.set_dest(0)
                        bridge.write(message.get_message())
                        time.sleep(1)
                        message.acc(23.12,23.12,15.23)
                        message.set_dest(0)
                        bridge.write(message.get_message())
                        time.sleep(1)
                        message.puls(144)
                        message.set_dest(0)
                        bridge.write(message.get_message())
                        time.sleep(1)



def main():
        print "Running..."  
        t = threading.Thread(name = 'rfbridge',target=bridge.begin)
        t.start()
        testFunction()

if __name__ == "__main__":
        main()


