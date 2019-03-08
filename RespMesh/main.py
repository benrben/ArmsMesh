from rfbridge import RFBridge 
import threading
import time
from sensor import GPS,ACC,PULSE,EMARG
from Message import Message
from redisConnection import RedisTools

nodeid = 80
redisTool = RedisTools()
bridge = RFBridge(nodeid,redisTool)

sensors = []
sensors.append(GPS())
sensors.append(ACC())
sensors.append(PULSE())
sensors.append(EMARG())

def run():
        timer = int(round(time.time() * 1000))
        while(1):
                delta = int(round(time.time() * 1000))-timer
                if delta > 3000:
                        timer = int(round(time.time() * 1000))
                        for sense in sensors:
                                message = Message()
                                message.set_data(sense.collect())
                                message.set_dest(83)
                                msg = message.get_message()
                                bridge.write(msg)
                                #Here push msg to redis
                                time.sleep(1)

def main():
        print "Running..."
        t = threading.Thread(name = 'rfbridge',target=bridge.begin)
        t.start()
        time.sleep(2)
        bridge.set_nodeid(12)
        run()

if __name__ == "__main__":
        main()


