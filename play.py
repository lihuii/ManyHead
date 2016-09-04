import random
import os
from sys import exit

import pygame
from pygame.locals import * 


def game(fullscreen=True):
    os.chdir(os.getcwd())

    background_image_filename = 'bg.jpg'
    mouse_image_filename = 'head2.png'

    pygame.mixer.init(frequency=22050,size=-16,channels=4)
    sound1 = pygame.mixer.Sound('start.wav')
    chan1 = pygame.mixer.find_channel()
    chan1.queue(sound1)
    if fullscreen == True:
        screen = pygame.display.set_mode((1600, 900),pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((1600, 900))
        
    pygame.display.set_caption("Hello, Head!")

    background = pygame.image.load(background_image_filename).convert()
    mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()


    while True:

        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
        screen.blit(background,(0,0))
        
        x,y = pygame.mouse.get_pos()
        
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2
        
        screen.blit(mouse_cursor,(x,y))
        
        pygame.display.flip()
        