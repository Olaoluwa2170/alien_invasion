import pygame.font


class Instructions():

    def __init__(self, ai_settings, screen):
        """Initialize buttons attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the botton.
        self.width, self.height = 1200, 100
        self.button_color = (230, 230, 230)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont("Montserrat", 48)

        # Build the botton's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.screen_rect.top

        # The button message needs to nbe prepped only once
        msg = " ~~ Welcome to Alien invasion By Babalola Elisha ~~"
                
        
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, 
            self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instruction(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
