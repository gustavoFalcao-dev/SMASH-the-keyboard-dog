from pynput import mouse


class MouseTracker:
    def __init__( self ):
        self.mpos = [ 0, 0 ]
        self.listener = mouse.Listener( on_move=self.on_move)

    def on_move( self, x, y ):
        self.mpos[ 0 ] = x
        self.mpos[ 1 ] = y

    def start( self ):
        self.listener.start()

    def stop( self ):
        self.listener.stop()
        