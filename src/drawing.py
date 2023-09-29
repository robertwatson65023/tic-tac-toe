import pygame
import os

from const import *

class Drawing:
    def __init__(self) -> None:
        pass

    def draw_grid(self, screen):
        for i in range(1, NB_COLUMN):
            pygame.draw.line(screen, WHITE, (i * SCREEN_SIZE // 3, 0), (i * SCREEN_SIZE // 3, SCREEN_SIZE), 5)

        for i in range(1, NB_ROW):
            pygame.draw.line(screen, WHITE, (0, i * SCREEN_SIZE // 3), (SCREEN_SIZE, i * SCREEN_SIZE // 3), 5)

        pygame.display.update()
    
    def draw_pieces(self, screen, board):
        red_circle = pygame.transform.scale(pygame.image.load(os.path.join("src/img", "red.png")), (100, 100))
        yellow_circle = pygame.transform.scale(pygame.image.load(os.path.join("src/img", "yellow.png")), (100, 100))
