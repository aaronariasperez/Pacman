import pygame
from pygame.locals import *
import constants as CONST
import utils as UTILS
import pyganim as ANIM

#Global variables
sprite_speed = 0.2

class Pacman(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(0,0,23,25)
        self.rect.centerx = CONST.WIDTH / 2
        self.rect.centery = CONST.HEIGHT / 2
        self.posMatrix_i = 2
        self.posMatrix_j = 2
        self.speed = 0.2
        self.state = 0

        self.load_animations()


    def updateRightMovement(self):
        aux = int(((self.rect.centerx+12.5)/float(CONST.WIDTH)) * CONST.COLS)

        if CONST.gameMap[self.posMatrix_i,aux] == 0 or CONST.gameMap[self.posMatrix_i,aux] == 3:
            CONST.gameMap[self.posMatrix_i, self.posMatrix_j] = 0
            self.posMatrix_j = aux
            CONST.gameMap[self.posMatrix_i,aux] = 3
        else:
            self.rect.centerx = self.posMatrix_j * (CONST.WIDTH/CONST.COLS) + 12.5

    def updateLeftMovement(self):
        aux = int(((self.rect.centerx-12.5)/float(CONST.WIDTH)) * CONST.COLS)

        if CONST.gameMap[self.posMatrix_i,aux] == 0 or CONST.gameMap[self.posMatrix_i,aux] == 3:
            CONST.gameMap[self.posMatrix_i, self.posMatrix_j] = 0
            self.posMatrix_j = aux
            CONST.gameMap[self.posMatrix_i,aux] = 3
        else:
            self.rect.centerx = self.posMatrix_j * (CONST.WIDTH/CONST.COLS) + 12.5

    def updateUpMovement(self):
        aux = int(((self.rect.centery-12.5)/float(CONST.HEIGHT)) * CONST.ROWS)

        if CONST.gameMap[aux,self.posMatrix_j] == 0 or CONST.gameMap[aux,self.posMatrix_j] == 3:
            CONST.gameMap[self.posMatrix_i, self.posMatrix_j] = 0
            self.posMatrix_i = aux
            CONST.gameMap[aux,self.posMatrix_j] = 3
        else:
            self.rect.centery = self.posMatrix_i * (CONST.HEIGHT/CONST.ROWS) + 12.5

    def updateDownMovement(self):
        aux = int(((self.rect.centery+12.5)/float(CONST.HEIGHT)) * CONST.ROWS)

        if CONST.gameMap[aux,self.posMatrix_j] == 0 or CONST.gameMap[aux,self.posMatrix_j] == 3:
            CONST.gameMap[self.posMatrix_i, self.posMatrix_j] = 0
            self.posMatrix_i = aux
            CONST.gameMap[aux,self.posMatrix_j] = 3
        else:
            self.rect.centery = self.posMatrix_i * (CONST.HEIGHT/CONST.ROWS) + 12.5

    def load_animations(self):
        #right->0
        #left->1
        #up->2
        #down->3
        self.pacmanAnim={}
        self.pacmanAnim[0] = ANIM.PygAnimation([('images/pacman_R1.png', sprite_speed),
                                                ('images/pacman_R2.png', sprite_speed)])
        self.pacmanAnim[2] = ANIM.PygAnimation([('images/pacman_U1.png', sprite_speed),
                                                ('images/pacman_U2.png', sprite_speed)])

        self.pacmanAnim[1] = self.pacmanAnim[0].getCopy()
        self.pacmanAnim[1].flip(True, False)
        self.pacmanAnim[1].makeTransformsPermanent()

        self.pacmanAnim[3] = self.pacmanAnim[2].getCopy()
        self.pacmanAnim[3].flip(False, True)
        self.pacmanAnim[3].makeTransformsPermanent()

        #init animations
        self.moveConductor = ANIM.PygConductor(self.pacmanAnim)
        self.moveConductor.play()

    def update(self, time, keys):
        if self.rect.right <= CONST.WIDTH:
            if keys[K_d]:
                self.state=0
                self.rect.centerx += self.speed*time

                self.updateRightMovement()

        if self.rect.left >= 0:
            if keys[K_a]:
                self.state=1
                self.rect.centerx -= self.speed*time

                self.updateLeftMovement()

        if self.rect.top >= 0:
            if keys[K_w]:
                self.state=2
                self.rect.centery -= self.speed*time

                self.updateUpMovement()

        if self.rect.bottom <= CONST.HEIGHT:
            if keys[K_s]:
                self.state=3
                self.rect.centery += self.speed*time

                self.updateDownMovement()

    def draw(self,screen):
        if self.state==0:
            self.pacmanAnim[0].blit(screen, self.rect)
        if self.state==1:
            self.pacmanAnim[1].blit(screen, self.rect)
        if self.state==2:
            self.pacmanAnim[2].blit(screen, self.rect)
        if self.state==3:
            self.pacmanAnim[3].blit(screen, self.rect)
