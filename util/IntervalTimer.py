import threading

class IntervalTimer():
    '''Class that utilies the threading.Timer to create a timer that fires continously in a given interal until cancled.'''
    def __init__(self, interval, callback, *args, **kwargs):
        self.interval = interval
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        
        self.timer = threading.Timer(interval, self.on_timer)
        self.timer.start()
        
    def on_timer(self):
        print('On timer')
        self.callback(*self.args, **self.kwargs)
        self.timer.run()
        
    def start_timer(self):
        self.timer.start()
        
    def cancel(self):
        self.timer.cancel()