import pygame
import functions as f
from settings import Settings
from car import Car
from line import Line
from pygame.sprite import Group
from stats import Stats
from car2 import Car2

def run_game():

    d_settings = Settings()
    screen = pygame.display.set_mode((d_settings.screen_w, d_settings.screen_h))
    screen.fill(d_settings.bg_colour)
    car = Car(d_settings, screen)
    car2 = Car2(d_settings, screen)
    line = Line(screen)
    bullets = Group()
    drones = []
    stats = Stats(d_settings, drones, bullets)
    f.create_drone(d_settings, screen, drones)
    pygame.init()
    #making a Car
    pygame.display.set_caption('Rocket Car')
    while True:
        f.check_events(d_settings, screen, car,car2, bullets)
        if stats.active:
            f.make_drones(d_settings, drones, screen)
            f.collision(bullets, drones, d_settings, car)
            car.update()
            car2.update()
            bullets.update()
            stats.reset()
            # delete the old bullets
            f.fire_bullets(d_settings, screen,car, bullets)
            f.screen_update(d_settings, screen, car,car2,  line, bullets, drones)
            print(d_settings.points, d_settings.lives)
run_game()
