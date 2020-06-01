import pygame.font
import pygame

class Button():
    def __init__(self,settings, screen, msg):
        pygame.init()
        """make a button to start the game"""
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.b_colour = self.settings.bg_colour
        self.txt_colour = (0, 255,0)
        self.font = pygame.font.SysFont('calibri', 48)
        self.rect = pygame.Rect(0,0, self.width, self. height)
        self.rect.center = self.screen_rect.center
        self.show_msg(msg)

    def show_msg(self, msg):
        self.msg_img = self.font.render(msg, True,self.txt_colour, self.b_colour)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center
    def draw_button(self):
        #draw a button
        self.screen.fill(self.b_colour, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
