import pygame
from pygame import *

game_flag = True


def main(game_flag):  # основной метод игры
    init()
    display.set_mode((600, 400))

    while game_flag:  # основной цикл игры
        # pass
        # events содержит список событий
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                game_flag = False


if __name__ == '__main__':
    main(game_flag)
