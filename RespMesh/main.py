from rfbridge import RFBridge 
import threading
import time

bridge = RFBridge()

def testFunction():
        timer = int(round(time.time() * 1000))
        while(1):
                delta = int(round(time.time() * 1000))-timer
                if delta > 3000:
                        timer = int(round(time.time() * 1000))
                        bridge.write('0 <GPS 42.12 12.32>')
                        time.sleep(1)



def main():
        print "Running..."
	
        t = threading.Thread(name = 'rfbridge',target=bridge.begin)
        t.start()
        testFunction()
	

if __name__ == "__main__":
        main()


