import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)

if __name__ == "__main__":
    ai = Game()
    ai.run_game()