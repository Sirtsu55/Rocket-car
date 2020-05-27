class Settings():
    def __init__(self):
        '''settings for the game'''
        # screen settings
        self.screen_w = 1000  #screen width
        self.screen_h = 600   #screen height
        self.bg_colour = (60,60,60)
        self.speed = 2
        self.b_speed = 10
        self.bullet_w = 40
        self.bullet_h = 10
        self.bullet_colour = 255, 0, 0
        self.max_bullets = 2
        self.drone_speed = 0.3
        self.drone_s_speed = 0.1
        self.speed_up = 0.01
