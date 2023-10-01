import pygame
import sys

from game.const import *
from game.drawing import *

class Game:
    def __init__(self) -> None:
        self.board = tableau = [[0 for j in range(NB_COLUMN_ROW)] for i in range(NB_COLUMN_ROW)]
        self.drawing = Drawing()
        self.turn = 1

    def launch(self):
        pygame.init()

        screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Tic Tac Toe")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()

                        # column

                        if pos[0] <= SCREEN_SIZE / 3:
                            column = 0

                        elif pos[0] <= SCREEN_SIZE / 3 * 2:
                            column = 1

                        elif pos [0] <= SCREEN_SIZE:
                            column = 2
                        
                        # row

                        if pos[1] <= SCREEN_SIZE / 3:
                            row = 0

                        elif pos[1] <= SCREEN_SIZE / 3 * 2:
                            row = 1

                        elif pos [1] <= SCREEN_SIZE:
                            row = 2

                        # modify board

                        if self.turn == 1:
                            self.modify_board(column, row, self.turn)
                        
                        if self.turn == 2:
                            self.modify_board(column, row, self.turn)

            self.drawing.draw_grid(screen)
            self.drawing.draw_pieces(screen, self.board)
    
    def modify_board(self, column, row, value):
        if self.board[column][row] == 0:
            self.board[column][row] = value
            
            if self.turn == 1:
                self.turn = 2
            
            else:
                self.turn = 1
