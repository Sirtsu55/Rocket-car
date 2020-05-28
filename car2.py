import pygame
import time


from stats import Stats
class Car2():
    def __init__(self, settings, screen):
        '''Car class and its start'''
        self.screen = screen
        self.settings = settings
        #load the car file
        self.image = pygame.image.load('C:\pyhton\img\car.png')
        self.car_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start a car at the bottom of the screen
        self.car_rect.centerx = self.screen_rect.centerx - 20
        self.car_rect.centery = self.screen_rect.bottom
        self.car_rect.bottom = self.screen_rect.bottom
        #convert the centerx to a float to get accurate measurements
        self.centerx = float(self.car_rect.centerx)
        self.centery = float(self.car_rect.centery)
        #movement flags
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False


    def update(self):

        if self.moving_right and self.car_rect.right < self.screen_rect.right:
            self.centerx += self.settings.speed
        if self.moving_left and self.car_rect.left > 0:
            self.centerx -= self.settings.speed
        if self.moving_up and self.car_rect.top > 400:
            self.centery -= self.settings.speed
        if self.moving_down and self.car_rect.bottom < 600:
            self.centery += self.settings.speed

        self.car_rect.centerx = self.centerx
        self.car_rect.centery = self.centery



    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.car_rect)


    def collision_car(self, drones, bullets):
        stats = Stats(self.settings, drones, bullets)
        for drone in drones:
            if self.car_rect.colliderect(drone):
                stats.settings.lives -= 1
                time.sleep(self.settings.sleep_time)
                drones.remove(drone)
