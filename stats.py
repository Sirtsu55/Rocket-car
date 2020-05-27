class Stats():
    """a class whre all the game stats will be"""
    def __init__(self, settings, drones, bullets):
        self.settings = settings
        self.points = 0
        self.lives = 1
        self.bullets = bullets
        self.drones = drones
    def reset(self):
        self.points = 0
        self.lives = 5
        self.bullets.empty()
        for i in self.drones:
            self.drones.remove(i)
        print('yee')
