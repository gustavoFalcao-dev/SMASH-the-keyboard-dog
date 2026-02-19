from pynput import mouse


class MouseTracker:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.listener = mouse.Listener(on_move=self.on_move)
    
    def on_move(self,_x,_y):
        self.posx = _x
        self.posy = _y

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

    def getx(self):
        return self.posx
    
    def gety(self):
        return self.posy