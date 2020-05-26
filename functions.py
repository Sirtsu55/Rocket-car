import sys
import pygame
import random

from bullet import Bullet
from drone import Drone

def speed_up(settings, drones, screen):
    if len(drones) == 0:
        create_fleet(settings, screen, drones)
        settings.drone_speed += settings.speed_up
        settings.drone_s_speed += settings.speed_up

def remove_drone(settings, screen, drones):
    for drone in drones:
        if drone.y >= settings.screen_h:
            drones.remove(drone)
def get_number_drones(settings, drone_width):
    '''how many drones fit on the screen'''
    available_space_x = settings.screen_w
    number_drones_x = int(available_space_x / (2 * drone_width))
    number_drones_x = random.randint(4, number_drones_x)
    return number_drones_x

def create_drone(settings, screen, drones, drone_num):
    drone = Drone(settings, screen)
    drone_width = drone.rect.width
    drone.x = drone_width + 2 * drone_width * drone_num
    drone.rect.x = drone.x
    drones.add(drone)

def create_fleet(settings, screen, drones):
    drone = Drone(settings, screen)
    number_drones_x = get_number_drones(settings, drone.rect.width)
    for drone_num in range(number_drones_x):
        create_drone(settings, screen, drones, drone_num)

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

def screen_update(d_settings, screen, car, line, bullets, drones):
    screen.fill(d_settings.bg_colour)
    car.draw()
    line.draw_line()
    #draw all the bullets on the screen
    draw_bullets(bullets)
    drones.draw(screen)
    pygame.display.flip()
