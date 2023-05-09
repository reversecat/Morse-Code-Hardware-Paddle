import time

MIN_SEC = 60

class MorseTimer:
    def __init__(self, wpm):
        self.last_time = time.time()
        self.update_wpm(wpm)
        self.active = False
        self.str_buffer = ""
    
    def update_wpm(self, wpm):
        self.wpm = wpm
        self.break_time = MIN_SEC / wpm
        self.dot_threshold = self.break_time / 2
    
    def getTimeDiff(self):
        return time.time() - self.last_time
    
    def signal(self):
        time_passed = getTimeDiff()
        self.last_time = time.time()
        self.active = True
        if time_passed < self.dot_threshold:
            self.str_buffer += "."
            return
        elif time_passed < self.break_time:
            self.str_buffer += "-"
            return
        self.active = False
        self.str_buffer + "/"
    
    def tick(self):
        if getTimeDiff(self) > self.break_time:
            signal(self)
            ret_val = self.str_buffer
            self.str_buffer = ""
            return ret_val
        return ""
            
    def is_active(self):
        return self.active