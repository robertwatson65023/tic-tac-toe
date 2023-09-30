import pygame
import os

from game.const import *

class Drawing:
    def __init__(self) -> None:
        pass

    def draw_grid(self, screen):
        for i in range(NB_COLUMN_ROW):
            pygame.draw.line(screen, WHITE, (i * SCREEN_SIZE // 3, 0), (i * SCREEN_SIZE // 3, SCREEN_SIZE), 5)

        for i in range(NB_COLUMN_ROW):
            pygame.draw.line(screen, WHITE, (0, i * SCREEN_SIZE // 3), (SCREEN_SIZE, i * SCREEN_SIZE // 3), 5)

        pygame.display.update()
    
    def draw_pieces(self, screen, board):
        size = SCREEN_SIZE / NB_COLUMN_ROW

        for i in range(NB_COLUMN_ROW):
            for j in range(NB_COLUMN_ROW):
                x = int(i * size)
                y = int(j * size)

                if board[i][j] == 1:
                    pygame.draw.circle(screen, RED, (x + size // 2, y + size // 2), size // 2 - 25)
                
                if board[i][j] == 2:
                    pygame.draw.circle(screen, YELLOW, (x + size // 2, y + size // 2), size // 2 - 25)
                