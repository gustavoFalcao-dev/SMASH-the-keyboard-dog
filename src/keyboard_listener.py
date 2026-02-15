from pynput import keyboard


class KeyboardListener:
    def __init__( self ):
        self.pressed_key = set()
        self.listener = keyboard.Listener( on_press=self.on_press, on_release=self.on_release )

    def on_press( self, key ):
        self.pressed_key.add( key )

    def on_release( self, key ):
        self.pressed_key.discard( key )

    def start( self ):
        self.listener.start()

    def stop( self ):
        self.listener.stop()