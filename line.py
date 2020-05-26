import pygame

class Line():
    def __init__(self, screen):
        '''a class for line'''
        self.screen = screen

        self.image = pygame.image.load('C:\pyhton\img\line.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centery = self.screen_rect.centery + 100
        self.rect.right = self.screen_rect.right
    def draw_line(self):
        self.screen.blit(self.image, self.rect.center)
