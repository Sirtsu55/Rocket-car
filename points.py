import pygame
import pygame.font

class PointButton():
    pygame.init()
    '''points counter'''
    def __init__(self, settings, screen, points):
        self.screen = screen
        self.settings = settings

        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 20
        self.b_colour = self.settings.bg_colour
        self.txt_colour = (0,0,0)
        self.font = pygame.font.SysFont(None, 30)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left
        self.show_points(points, self.settings)

    def show_points(self, points, settings):
        point_num = "{:,}".format(int(settings.points))
        points = 'points: '+str(point_num) + str(points)
        self.points_img = self.font.render(str(points), True,self.txt_colour, self.b_colour)
        self.points_rect = self.points_img.get_rect()
        self.points_rect.center = self.rect.center

    def draw_points(self):
        self.screen.fill(self.b_colour, self.rect)
        self.screen.blit(self.points_img, self.points_rect)
