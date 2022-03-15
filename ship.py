import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship

        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start ship at bottom center
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        # decimal value of the center of the ship
        self.center = float(self.rect.centerx)

        #Moving flag
        self.moving_right = False
        self.moving_left = False
    def center_ship(self):
        """Center ship on the screen"""
        self.center =self.screen_rect.centerx

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor

        # Update rect object frm self.center
        self.rect.centerx=self.center


    def blitme(self):
        """Draw the ship at current position"""

        self.screen.blit(self.image, self.rect)
