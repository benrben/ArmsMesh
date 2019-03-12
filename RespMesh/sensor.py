import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library    
import threading


class GPS:
    def __init__(self):
        self.longitude = 12.12
        self.latitude = 34.12

    def collect(self):
        value = 'G:'
        value += str(self.latitude)
        value += ','
        value += str(self.longitude)
        return value

class ACC:
    def __init__(self):
        self.x = 1.12
        self.y = 3.12
        self.z = 5.00

    def collect(self):
        value = 'A:'
        value += str(self.x)
        value += ','
        value += str(self.y)
        value += ','
        value += str(self.z)
        return value


class PULSE:
    def __init__(self):
        self.value=120

    def collect(self):
        value = 'P:'
        value += str(self.value)
        return value


class EMARG:
    def __init__(self):
        self.value = False
        self.setup()
        # t = threading.Thread(name = 'emarglisten',target=self.listen)
        # t.start()


    def setup(self):
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(10,GPIO.RISING,callback=self.listen) # Setup event on pin 10 rising edge
    
    def collect(self):
        result = 'E:'
        result += str(self.value)
        self.value = False
        return result

    def listen(self):
        while True: # Run forever
            if GPIO.input(10) == GPIO.HIGH:
                self.value = True