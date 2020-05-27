import pygame
from pygame.sprite import Sprite
import random
class Drone(Sprite):
    def __init__(self, settings, screen):
        '''make a drone and then spawn it at the top'''
        super().__init__()
        self.screen =  screen
        self.settings = settings
        #load the drone
        self.image = pygame.image.load('C:\pyhton\img\drone.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.screen_rect.top
        self.rect.centerx = random.randint(0, self.settings.screen_w)

        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)
    def bounce_and_down(self,settings):
        if self.y <= settings.screen_h:
                self.y += +settings.drone_speed
        #MAKE THE DRONE BOUNCE AND GO SIDEWAYS
        if self.x <= settings.screen_w :
            self.x += settings.drone_s_speed
        if self.x >=settings.screen_w:
            settings.drone_s_speed = -settings.drone_s_speed
            self.x += settings.drone_s_speed
        if self.x <= 0:
            settings.drone_s_speed = -settings.drone_s_speed
            self.x += settings.drone_s_speed

    def update(self, settings):
            # MAKE THE DRONE GO DOWN
            Drone.bounce_and_down(self, settings)
            self.rect.centery = int(self.y)
            self.rect.centerx = int(self.x)
    def blitme(self):
        '''draw the drone'''
        self.screen.blit(self.image, self.rect)
