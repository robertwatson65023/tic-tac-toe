import pygame
import sys
import time

from game.const import *
from game.drawing import *

class Game:
    """
    Class representing the Tic Tac Toe game.
    """

    def __init__(self) -> None:
        self.board = [[0 for j in range(NB_COLUMN_ROW)] for i in range(NB_COLUMN_ROW)]
        self.drawing = Drawing()
        self.turn = 1
        self.end = False

    def launch(self):
        """
        Launch the game and detect game events.
        """
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        screen.fill(BACKGROUND_COLOR)
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
                
                    pygame.display.update()
            
            if self.end != True:
                self.drawing.draw_grid(screen)
                self.drawing.draw_pieces(screen, self.board)
                pygame.display.update()
            
            if self.check_align() != None:
                start, end = self.check_align()

                if self.end != True:
                    self.drawing.draw_line(screen, start, end)

                self.end = True
                pygame.display.update()
                time.sleep(1)
                play_again = self.drawing.end_screen(screen)
                
                if play_again:
                    self.board = [[0 for j in range(NB_COLUMN_ROW)] for i in range(NB_COLUMN_ROW)]
                    self.end = False
                    self.launch()

    def modify_board(self, column, row, value):
        """
        Modify the game board based on the player's move.

        Args:
            column (int): The column where the player placed their piece.
            row (int): The row where the player placed their piece.
            value (int): The player's turn (1 or 2).

        This method updates the board based on the player's move and advances the turn.
        """

        if self.board[column][row] == 0:
            self.board[column][row] = value
            
            if self.turn == 1:
                self.turn = 2
            
            else:
                self.turn = 1
    
    def check_align(self):
        """
        Check for winning alignment on the game board.

        Returns:
            tuple: Start and end coordinates of the winning alignment.

        This method checks for a winning alignment (three pieces in a row, column, or diagonal)
        on the game board and returns the coordinates of the winning alignment.
        """

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
