import pygame
import sys

from game.const import *
from game.drawing import *

class Game:
    def __init__(self) -> None:
        self.board = tableau = [[0 for j in range(NB_COLUMN_ROW)] for i in range(NB_COLUMN_ROW)]
        self.drawing = Drawing()

    def launch(self):
        pygame.init()

        screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Tic Tac Toe")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.drawing.draw_grid(screen)
            self.drawing.draw_pieces(screen, self.board)
