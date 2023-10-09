import sys
import pygame

from game.const import *

class Drawing:
    """
    Class that groups the methods that allow to draw something (lines, text...) on the screen.
    """

    def draw_grid(self, screen):
        """
        Draw the game grid on the screen.

        Args:
            screen: The Pygame screen surface.

        This method draws the grid lines on the screen to represent the Tic Tac Toe board.
        """
             
        for i in range(1, NB_COLUMN_ROW):
            pygame.draw.line(screen, GRID_COLOR, (i * SCREEN_SIZE // 3, 0), (i * SCREEN_SIZE // 3, SCREEN_SIZE), 5)

        for i in range(1, NB_COLUMN_ROW):
            pygame.draw.line(screen, GRID_COLOR, (0, i * SCREEN_SIZE // 3), (SCREEN_SIZE, i * SCREEN_SIZE // 3), 5)
    
    def draw_pieces(self, screen, board):
        """
        Draw the game pieces on the screen.

        Args:
            screen: The Pygame screen surface.
            board: The game board representing the positions of the pieces.

        This method draws the game pieces (blue and yellow circles) on the screen based on the
        board configuration.
        """
        
        size = SCREEN_SIZE / NB_COLUMN_ROW

        blue_circle = pygame.transform.scale(pygame.image.load("img/blue.png"), (70, 70))
        yellow_circle = pygame.transform.scale(pygame.image.load("img/yellow.png"), (70, 70))

        for i in range(NB_COLUMN_ROW):
            for j in range(NB_COLUMN_ROW):
                x = int(i * size)
                y = int(j * size)

                if board[i][j] == 1:
                    screen.blit(blue_circle, (x + size // 2 - 35, y + size // 2 - 35))
                
                if board[i][j] == 2:
                    screen.blit(yellow_circle, (x + size // 2 - 35, y + size // 2 - 35))
    
    def draw_line(self, screen, start, end):
        """
        Draw a winning line on the screen.

        Args:
            screen: The Pygame screen surface.
            start: The starting coordinates of the line.
            end: The ending coordinates of the line.

        This method draws a line connecting the winning pieces.
        """
        
        x_start = SCREEN_SIZE // NB_COLUMN_ROW * (start[0] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2
        y_start = SCREEN_SIZE // NB_COLUMN_ROW * (start[1] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2

        x_end = SCREEN_SIZE // NB_COLUMN_ROW * (end[0] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2
        y_end = SCREEN_SIZE // NB_COLUMN_ROW * (end[1] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2

        pygame.draw.line(screen, DARK_BLUE, (x_start, y_start), (x_end, y_end), 5)
    
    def end_screen(self, screen):
        """
        Display the end screen.

        Args:
            screen: The Pygame screen surface.

        This method displays an end screen prompting to play again and waits for the player's input.
        """

        screen.fill(BACKGROUND_COLOR)

        font = pygame.font.Font("font/Roboto-Regular.ttf", 25)
        text = font.render("Press space key to play again!", True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_SIZE // 2, SCREEN_SIZE // 2)
        
        screen.blit(text, text_rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return True
                    