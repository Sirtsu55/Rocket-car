import pygame
import functions as f
from settings import Settings
from car import Car
from line import Line
from pygame.sprite import Group
from stats import Stats
from car2 import Car2
from button import Button
from points import PointButton
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
    play_button = Button(d_settings, screen, 'start')
    pygame.init()
    points = PointButton(d_settings, screen, d_settings.points)
    #making a Car
    pygame.display.set_caption('Rocket Car')
    while True:
        f.check_events(d_settings, screen, car,car2, bullets, stats, play_button)
        if not stats.active:
            pygame.mouse.set_visible(True)
            d_settings = Settings()
            screen = pygame.display.set_mode((d_settings.screen_w, d_settings.screen_h))
            screen.fill(d_settings.bg_colour)
            car = Car(d_settings, screen)
            car2 = Car2(d_settings, screen)
            line = Line(screen)
            bullets = Group()
            drones = []
            stats = Stats(d_settings, drones, bullets)
            play_button = Button(d_settings, screen, 'start')
            f.screen_update(d_settings, screen, car, car2,  line, bullets, drones, stats, play_button, points)
        if stats.active:
            f.make_drones(d_settings, drones, screen)
            if stats.two_player:
                f.collision(bullets, drones, d_settings, car2)
            if len(drones) < 1:
                f.create_drone(d_settings, screen, drones)

            f.collision(bullets, drones, d_settings, car)
            car.update()
            car2.update()
            bullets.update()
            stats.reset()
            # delete the old bullets
            f.fire_bullets(d_settings, screen,car, bullets)
            f.screen_update(d_settings, screen, car, car2,  line, bullets, drones, stats, play_button, points)
run_game()
