import sys
import pygame
import random

from bullet import Bullet
from drone import Drone
from car import Car
from points import PointButton

def collision(bullets, drones, settings, car):
    for bullet in bullets:
        bullet.collision_bullet(drones, settings, bullets)

    for drone in drones:
        car.collision_car(drones, bullets)

def update_drones(drones, settings):
    for drone in drones:
        drone.update(settings)
        drone.blitme()

def make_drones(settings, drones, screen):
    for drone in drones:
        if drones[-1].rect.centery >= 200 :
            create_drone(settings, screen, drones)
def remove_and_speedup_drone(settings, screen, drones):
    for drone in drones:
        if drone.y >= settings.screen_h:
            drones.remove(drone)
            settings.drone_speed += settings.speed_up
            settings.drone_s_speed += settings.speed_up
            settings.lives -= 1


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
def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.active = True
        pygame.mouse.set_visible(False)

def keydown(event, settings, screen ,car,car2, bullets, stats): #keydown events


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


        if stats.two_player:
            if event.key == pygame.K_d:
                car2.moving_right = True

            elif event.key == pygame.K_a:
                car2.moving_left = True
            elif event.key == pygame.K_w:
                car2.moving_up = True
            elif event.key == pygame.K_s:
                car2.moving_down = True
            elif event.key == pygame.K_LALT:
                #make a new bullet and add it into the bullets Group
                make_bullets(settings, screen, car2, bullets)




def keyup(event, settings, screen, car, car2, bullets): #key up events
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            car.moving_right = False

        elif event.key == pygame.K_LEFT:
            car.moving_left = False
        elif event.key == pygame.K_UP:
            car.moving_up = False
        elif event.key == pygame.K_DOWN:
            car.moving_down = False

        if event.key == pygame.K_d:
            car2.moving_right = False

        elif event.key == pygame.K_a:
            car2.moving_left = False
        elif event.key == pygame.K_w:
            car2.moving_up = False
        elif event.key == pygame.K_s:
            car2.moving_down = False


def check_events(settings, screen ,car, car2 , bullets, stats, play_button):
    for event in pygame.event.get():
        quit(event)
        if event.type == pygame.KEYDOWN:
            keydown(event, settings, screen, car, car2, bullets, stats)
        elif event.type == pygame.KEYUP:
            keyup(event, settings, screen, car, car2, bullets)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)


def screen_update(d_settings, screen, car, car2, line, bullets, drones, stats, play_button, points):
    screen.fill(d_settings.bg_colour)
    points = PointButton(d_settings, screen, ' HP: '+str(d_settings.lives))
    points.draw_points()
    if stats.active == False:
        car.draw()
        line.draw_line()
        play_button.draw_button()
        pygame.display.flip()
    if stats.two_player:
        car2.draw()
    if stats.active:
        car.draw()
        line.draw_line()
        update_drones(drones, d_settings)
        remove_and_speedup_drone(d_settings, screen, drones)
        #draw all the bullets on the screen
        draw_bullets(bullets)
        pygame.display.flip()
