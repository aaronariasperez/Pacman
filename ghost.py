import pygame
from pygame.locals import *
import constants as CONST
import utils as UTILS

class Ghost(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = UTILS.load_image("images/ghostprueba.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = CONST.WIDTH / 2
        self.rect.centery = CONST.HEIGHT / 2
        self.speed = 0.5

    def update(self, time, keys):
        if self.rect.right <= CONST.WIDTH:
            if keys[K_d]:
                self.rect.centerx += self.speed*time
        if self.rect.left >= 0:
            if keys[K_a]:
                self.rect.centerx -= self.speed*time
        if self.rect.top >= 0:
            if keys[K_w]:
                self.rect.centery -= self.speed*time
        if self.rect.bottom <= CONST.HEIGHT:
            if keys[K_s]:
                self.rect.centery += self.speed*time
