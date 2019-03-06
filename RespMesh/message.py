import time
class Message:
    dest = 0
    time = time.time()
    data = ''

    def set_data(self,data):
        self.data = data

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