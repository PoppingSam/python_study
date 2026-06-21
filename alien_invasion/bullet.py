import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.bullet_color = game.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.bullet_location_y = float(self.rect.y)

    def update(self):
        self.bullet_location_y -= self.settings.bullet_speed
        self.rect.y = self.bullet_location_y
