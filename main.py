import pygame
from pynput import keyboard


pygame.init()
TestWindow = pygame.display.set_mode( ( 400, 400 ) )
pygame.display.set_caption( "Hello world" )

idle_img = pygame.image.load( 'test/test_dog.png' )
hit_img = pygame.image.load( 'test/hit.png' )

current_img = idle_img
pressed_key = set()

def on_press( key ):
    pressed_key.add( key )

def on_release( key):
    pressed_key.discard( key )


listener = keyboard.Listener( on_press=on_press, on_release=on_release )
listener.start()

clock = pygame.time.Clock()

state = True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

    if pressed_key:
        current_img = hit_img
        
    else:
        current_img = idle_img

    TestWindow.fill( ( 255, 255, 255 ) )
    TestWindow.blit( current_img, ( 0, 0 ) )
    pygame.display.flip()
    clock.tick( 60 )

listener.stop()
pygame.quit()