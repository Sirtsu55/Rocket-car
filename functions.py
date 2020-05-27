import sys
import pygame
import random

from bullet import Bullet
from drone import Drone
def bullet_collision(bullets, drones, settings, points):
    for bullet in bullets:
        bullet.collision(drones, settings, points)

def update_drones(drones, settings):
    for drone in drones:
        drone.update(settings)
        drone.blitme()

def make_drones(settings, drones, screen):
    for drone in drones:
        if drones[-1].rect.centery >= 150 or len(drones) == 1:
            create_drone(settings, screen, drones)
def remove_and_speedup_drone(settings, screen, drones, lives):
    for drone in drones:
        if drone.y >= settings.screen_h:
            lives -= 1
            if lives == 0:
                sys.exit()
            drones.remove(drone)
            settings.drone_speed += settings.speed_up
            settings.drone_s_speed += settings.speed_up


def create_drone(settings, screen, drones):
    drone = Drone(settings, screen)
    drones.append(drone)

def fire_bullets(settings, screen, car, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

def make_bullets(settings, screen, car, bullets):
    if len(bullets) < settings.max_bullets:
        new_bullet = Bullet(settings, screen, car)
        bullets.add(new_bullet)
def draw_bullets(bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def quit(event):
    if event.type == pygame.QUIT:       #exit the game
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            sys.exit()

def keydown(event, settings, screen ,car, bullets): #keydown events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            car.moving_right = True
        elif event.key == pygame.K_LEFT:
            car.moving_left = True
        elif event.key == pygame.K_UP:
            car.moving_up = True
        elif event.key == pygame.K_DOWN:
            car.moving_down = True
        elif event.key == pygame.K_SPACE:
            #make a new bullet and add it into the bullets Group
            make_bullets(settings, screen, car, bullets)



def keyup(event, settings, screen, car, bullets): #key up events
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            car.moving_right = False

        elif event.key == pygame.K_LEFT:
            car.moving_left = False
        elif event.key == pygame.K_UP:
            car.moving_up = False
        elif event.key == pygame.K_DOWN:
            car.moving_down = False


def check_events(settings, screen ,car , bullets):
    for event in pygame.event.get():
        quit(event)
        if event.type == pygame.KEYDOWN:
            keydown(event, settings, screen, car, bullets)
        elif event.type == pygame.KEYUP:
            keyup(event, settings, screen, car, bullets)

def screen_update(d_settings, screen, car, line, bullets, drones, points, lives):
    screen.fill(d_settings.bg_colour)
    car.draw()
    line.draw_line()
    bullet_collision(bullets, drones, d_settings, points)
    update_drones(drones, d_settings)
    remove_and_speedup_drone(d_settings, screen, drones, lives)
    #draw all the bullets on the screen
    draw_bullets(bullets)
    pygame.display.flip()
