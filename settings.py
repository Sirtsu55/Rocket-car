class Settings():
    def __init__(self):
        '''settings for the game'''
        # screen settings
        self.screen_w = 1000  #screen width
        self.screen_h = 600   #screen height
        self.bg_colour = (60,60,60)
        self.speed = 1
        self.b_speed = 10
        self.bullet_w = 40
        self.bullet_h = 10
        self.bullet_colour = 255, 0, 0
        self.max_bullets = 2
        self.drone_speed = 0.05
        self.drone_s_speed = 1
        self.speed_up = 0.05
        self.lives = 5
        self.points = 0
        self.sleep_time = 0.3
        self.points_earn = 1000
        self.level_up_scale = 1.5
        self.level_up = [i * (self.points_earn * 10 * self.level_up_scale) for i in range(1,11)]
