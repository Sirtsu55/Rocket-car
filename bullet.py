import pygame
from pygame.sprite import Sprite
from stats import Stats
class Bullet(Sprite):
    def __init__(self, settings, screen, car):
        '''a bullet that is fired from the car'''
        super().__init__()
        self.screen = screen
        #make a Bullet
        self.rect = pygame.Rect(0, 0,settings.bullet_w, settings.bullet_h)
        self.rect.centerx = car.car_rect.centerx
        self.rect.top = car.car_rect.top
        #store the bullets position as a float(decimal value)
        self.y = float(self.rect.y)
        self.colour = settings.bullet_colour
        self.speed = settings.b_speed
    def update(self):
        #update the decimal point of the bullet
            self.rect.y -= self.speed
            #update the pos of the bullet
            self.recty = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
    def collision_bullet(self, drones, settings, bullets):
        stats = Stats(settings, drones, bullets)
        for drone in drones:
            if self.rect.colliderect(drone):
                settings.drone_speed += settings.speed_up
                settings.drone_s_speed += settings.speed_up
                stats.points += 10
                drones.remove(drone)
