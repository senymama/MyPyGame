import pygame
from pygame import *

init()
display.set_mode((600, 400))

while 1:
    # pass
    # events содержит список событий
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit('hhhhhhhhh')
