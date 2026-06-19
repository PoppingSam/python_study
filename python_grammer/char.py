import pygame

class Char:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("D:/VscodeProject/PythonNotebook/" \
        "alien_invasion/images/char.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.location_x = int(self.rect.x)
        self.location_y = int(self.rect.y)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.location_x += 2
        if self.move_left and self.rect.left > 0:
            self.location_x -= 2
        if self.move_up and self.rect.top > 0:
            self.location_y -= 2
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.location_y += 2
        
        self.rect.x = self.location_x
        self.rect.y = self.location_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
