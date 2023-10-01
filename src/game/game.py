import pygame
import sys

from game.const import *
from game.drawing import *

class Game:
    def __init__(self) -> None:
        self.board = tableau = [[0 for j in range(NB_COLUMN_ROW)] for i in range(NB_COLUMN_ROW)]
        self.drawing = Drawing()
        self.turn = 1
        self.end = False

    def launch(self):
        pygame.init()

        screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Tic Tac Toe")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN and self.end != True:
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
            
            if self.check_align() != None:
                self.end = True

                start, end = self.check_align()
                self.drawing.draw_line(screen, start, end)
            
            pygame.display.update()
    
    def modify_board(self, column, row, value):
        if self.board[column][row] == 0:
            self.board[column][row] = value
            
            if self.turn == 1:
                self.turn = 2
            
            else:
                self.turn = 1
    
    def check_align(self):
        for i in range(NB_COLUMN_ROW):
            if self.board[i][0] != 0:
                to_check = self.board[i][0]

                if self.board[i][1] == to_check and self.board[i][2] == to_check:
                    s, e = [i, 0], [i, 2]
                    return s, e
                
                if i == 0:
                    if self.board[1][1] == to_check and self.board[2][2] == to_check:
                        s, e = [0, 0], [2, 2]
                        return s, e
                
                if i == 2:
                    if self.board[1][1] == to_check and self.board[0][2] == to_check:
                        s, e = [2, 0], [0, 2]
                        return s, e
                            
            if self.board[0][i] != 0:
                to_check = self.board[0][i]

                if self.board[1][i] == to_check and self.board[2][i] == to_check:
                    s, e = [0, i], [2, i]
                    return s, e

