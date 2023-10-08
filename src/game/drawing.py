import sys
import pygame

from game.const import *

class Drawing:
    def __init__(self) -> None:
        pass

    def draw_grid(self, screen):
        for i in range(1, NB_COLUMN_ROW):
            pygame.draw.line(screen, GRID_COLOR, (i * SCREEN_SIZE // 3, 0), (i * SCREEN_SIZE // 3, SCREEN_SIZE), 5)

        for i in range(1, NB_COLUMN_ROW):
            pygame.draw.line(screen, GRID_COLOR, (0, i * SCREEN_SIZE // 3), (SCREEN_SIZE, i * SCREEN_SIZE // 3), 5)
    
    def draw_pieces(self, screen, board):
        blue_circle = pygame.transform.scale(pygame.image.load("img/blue.png"), (70, 70))
        yellow_circle = pygame.transform.scale(pygame.image.load("img/yellow.png"), (70, 70))
        size = SCREEN_SIZE / NB_COLUMN_ROW

        for i in range(NB_COLUMN_ROW):
            for j in range(NB_COLUMN_ROW):
                x = int(i * size)
                y = int(j * size)

                if board[i][j] == 1:
                    screen.blit(blue_circle, (x + size // 2 - 35, y + size // 2 - 35))
                
                if board[i][j] == 2:
                    screen.blit(yellow_circle, (x + size // 2 - 35, y + size // 2 - 35))
    
    def draw_line(self, screen, start, end):
        x_start = SCREEN_SIZE // NB_COLUMN_ROW * (start[0] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2
        y_start = SCREEN_SIZE // NB_COLUMN_ROW * (start[1] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2

        x_end = SCREEN_SIZE // NB_COLUMN_ROW * (end[0] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2
        y_end = SCREEN_SIZE // NB_COLUMN_ROW * (end[1] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2

        pygame.draw.line(screen, DARK_BLUE, (x_start, y_start), (x_end, y_end), 5)
    
    def end_screen(self, screen):
        screen.fill(BACKGROUND_COLOR)
        font = pygame.font.Font("game/font/Roboto-Regular.ttf", 25)
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
                    