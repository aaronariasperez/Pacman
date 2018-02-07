import pygame
from pygame.locals import *
import constants as CONST

class Ghost(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/ghost.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = CONST.WIDTH / 2
        self.rect.centery = CONST.HEIGHT / 2
        self.speed = 1
