import sys
class Stats():
    """a class whre all the game stats will be"""
    def __init__(self, settings, drones, bullets):
        self.settings = settings
        self.bullets = bullets
        self.drones = drones
        self.settings = settings
        self.active = True
        self.two_player = False
    def reset(self):
        if self.settings.lives == 0:
            sys.exit()
