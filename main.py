import pygame
from src.keyboard_listener import KeyboardListener
from src.mouse_tracker import MouseTracker


#TODO Mouse tracking position convertion


pygame.init()


KListener = KeyboardListener()
#MTracker = MouseTracker()
clock = pygame.time.Clock()


icon = pygame.image.load( 'test/icon.png' )
pygame.display.set_icon( icon )
window = pygame.display.set_mode( ( 400, 400 ) )
pygame.display.set_caption( "SMASH the keyboard dog!" )


idle_img = pygame.image.load( 'test/dog_idle.png' )
hit_img = pygame.image.load( 'test/dog_hit.png' )
current_img = idle_img


state = True
KListener.start()
#MTracker.start()
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

    if KListener.pressed_key:
        current_img = hit_img
        
    else:
        current_img = idle_img

    window.fill( ( 54, 159, 50 ) )
    window.blit( current_img, ( 0, 0 ) )
    pygame.display.flip()
    clock.tick( 60 )

KListener.stop()
#MTracker.stop()
pygame.quit()