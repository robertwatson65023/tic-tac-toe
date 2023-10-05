import pygame
import os

from game.const import *

class Drawing:
    def __init__(self) -> None:
        pass

    def draw_grid(self, screen):
        for i in range(1, NB_COLUMN_ROW):
            pygame.draw.line(screen, LINES_COLOR, (i * SCREEN_SIZE // 3, 0), (i * SCREEN_SIZE // 3, SCREEN_SIZE), 5)

        for i in range(1, NB_COLUMN_ROW):
            pygame.draw.line(screen, LINES_COLOR, (0, i * SCREEN_SIZE // 3), (SCREEN_SIZE, i * SCREEN_SIZE // 3), 5)
    
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
    
    def draw_line(self, screen, start, end):
        x_start = SCREEN_SIZE // NB_COLUMN_ROW * (start[0] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2
        y_start = SCREEN_SIZE // NB_COLUMN_ROW * (start[1] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2

        x_end = SCREEN_SIZE // NB_COLUMN_ROW * (end[0] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2
        y_end = SCREEN_SIZE // NB_COLUMN_ROW * (end[1] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2

        pygame.draw.line(screen, BLUE, (x_start, y_start), (x_end, y_end), 5)
