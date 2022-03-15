import pygame
from game_stats import GameStats
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button
from instructions import Instructions
from scoreboard import ScoreBoard


def run_game():
    "Initialize game and creating a screen"
    pygame.init()

    # settings
    ai_settings = Setting()
    from alien import Alien
    
    screen=pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # Make a ship, a group of bullets, and a group of alien
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    ## Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")
    info = Instructions(ai_settings, screen)
    
    # Create the fleet of the alien
    gf.create_fleet(ai_settings, screen, ship, aliens)
    "Game main loop"
    while True:
        gf.check_events(ai_settings, screen,
             stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullet(ai_settings, 
                screen, stats, sb, ship, aliens, bullets)        
            gf.update_aliens(ai_settings, stats, 
            screen, sb, ship, aliens, bullets) 

        gf.update_screen (ai_settings, screen, 
            stats, sb, ship, aliens, bullets, play_button, info)



        

run_game()

