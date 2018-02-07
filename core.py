import sys, pygame
from pygame.locals import *
import constants as CONST
import utils as UTILS

class Core:


    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((CONST.WIDTH, CONST.HEIGHT))
        pygame.display.set_caption("Pruebas Pygame")

        self.background_image = UTILS.load_image('images/background.jpg')


    #*************Auxiliars*************



    #*************MAINLOOP*************
    def main_loop(self):
        while True:
            for events in pygame.event.get():
                if events.type == QUIT:
                    sys.exit(0)

            self.screen.blit(self.background_image, (0, 0))
            pygame.display.flip()

        return 0
