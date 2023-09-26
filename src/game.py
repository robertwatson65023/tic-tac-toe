import pygame
import sys

class Game:
    def __init__(self) -> None:
        pass

    def launch(self):
        pygame.init()

        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Tic Tac Toe")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
