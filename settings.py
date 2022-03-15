class Setting:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        self.screen_width=1300
        self.screen_height=700
        self.bg_color = (230,230,230)

        # ship settings
        
        self.ships_limit = 3

        # bullet settings

        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        

        # Alien settings
        
        self.fleet_drop_speed = 10
        

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullets_allowed = 4
        self.alien_speed_factor = 1

        # fleet_direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)



