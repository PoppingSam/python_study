import sys
import pygame
from python_grammer.new_study.char import Char

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = (134, 155, 169)
        self.char = Char(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_RIGHT:
                        self.char.move_right = True
                    elif event.key ==pygame.K_LEFT:
                        self.char.move_left = True
                    elif event.key ==pygame.K_UP:
                        self.char.move_up = True
                    elif event.key ==pygame.K_DOWN:
                        self.char.move_down = True
                elif event.type == pygame.KEYUP:
                    if event.key ==pygame.K_RIGHT:
                        self.char.move_right = False
                    elif event.key ==pygame.K_LEFT:
                        self.char.move_left = False
                    elif event.key ==pygame.K_UP:
                        self.char.move_up = False
                    elif event.key ==pygame.K_DOWN:
                        self.char.move_down = False

            self.screen.fill(self.bg_color)
            self.char.blitme()
            self.char.update()
            pygame.display.flip()

if __name__ == "__main__":
    ai = Game()
    ai.run_game()