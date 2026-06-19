import pygame

# 初始化飞船并设置初始位置
class Ship:
    def __init__(self,game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.location_x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.location_x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.location_x -= self.settings.ship_speed

        self.rect.x = self.location_x