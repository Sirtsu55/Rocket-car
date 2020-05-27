import pygame
import functions as f
from settings import Settings
from car import Car
from line import Line
from pygame.sprite import Group
from stats import Stats

def run_game():

    d_settings = Settings()
    screen = pygame.display.set_mode((d_settings.screen_w, d_settings.screen_h))
    screen.fill(d_settings.bg_colour)
    car = Car(d_settings, screen)
    line = Line(screen)
    bullets = Group()
    drones = []
    f.create_drone(d_settings, screen, drones)
    pygame.init()
    #making a Car
    pygame.display.set_caption('Rocket Car')
    while True:
        f.make_drones(d_settings, drones, screen)
        f.check_events(d_settings, screen, car, bullets)
        f.collision(bullets, drones, d_settings, car)
        car.update()
        bullets.update()
        # delete the old bullets
        f.fire_bullets(d_settings, screen,car, bullets)
        f.screen_update(d_settings, screen, car, line, bullets, drones)
run_game()
