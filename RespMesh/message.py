import time
class Message:
    dest = 0
    time = time.time()
    data = ''

    def puls(self,val):
        self.time = time.time()
        self.data = 'p:' + str(val)

    def emarg(self):
        self.time = time.time()
        self.data = 'e:1'
    
    def acc(self,x,y,z):
        self.time = time.time()
        self.data = 'a:x:'+str(x)+'y:'+str(y)+'z:'+str(z)

    def gps(self,x,y):
        self.time = time.time()
        self.data = 'g:'+'x:'+str(x)+'y:'+str(y)

    def get_message(self):
        msg = 'd:' + str(self.dest) + '\n'
        msg += 't:' + str(self.time) + '\n'
        msg += 'm:' + self.data + '\n'
        return msg
    
    def get_time(self):
        return self.time

    def get_dest(self):
        return self.dest
    
    def set_dest(self,nodeid):
        self.dest = nodeid