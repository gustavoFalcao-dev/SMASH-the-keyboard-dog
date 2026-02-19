import pygame
import os
from src.keyboard_listener import KeyboardListener
from src.mouse_tracker import MouseTracker


#TODO Mouse tracking global position convertion to relative
#TODO Use the position convertion to lock the mouse in a box
#TODO OOP the shit out of all of that
#FIXME Lag bug as u try to move the window

posx = 100
posy = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{posx}, {posy}"

pygame.init()


KListener = KeyboardListener()
MTracker = MouseTracker()
clock = pygame.time.Clock()


icon = pygame.image.load( 'test/icon.png' )
pygame.display.set_icon( icon )
window = pygame.display.set_mode( ( 400, 400 ) )
pygame.display.set_caption( "SMASH the keyboard dog!" )


idle_img = pygame.image.load( 'test/dog_idle.png' )
hit_img = pygame.image.load( 'test/dog_hit.png' )
current_img = idle_img
mouse_img = pygame.image.load( 'test/mousemenor.png' ).convert_alpha()
mposx = 0
mposy = 0


state = True
KListener.start()
MTracker.start()
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

    if KListener.pressed_key:
        current_img = hit_img
        
    else:
        current_img = idle_img

    window.fill( ( 54, 159, 50 ) )
    window.blits( blit_sequence=( ( current_img, ( 0, 0 ) ), ( mouse_img, ( mposx, mposy ) ) ) )
    pygame.display.flip()
    clock.tick( 60 )
    mposx = MTracker.getx()
    mposy = MTracker.gety()
  

KListener.stop()
MTracker.stop()
pygame.quit()