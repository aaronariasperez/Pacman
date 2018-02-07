import sys, pygame
from pygame.locals import *
import constants as CONST
import utils as UTILS
import pacman as PAC

class Core:


    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((CONST.WIDTH, CONST.HEIGHT))
        pygame.display.set_caption("Pruebas Pygame")

        self.background_image = UTILS.load_image('images/backprueba.png')


    #*************Auxiliars*************



    #*************MAINLOOP*************
    def main_loop(self):
        pacman = PAC.Pacman()

        clock = pygame.time.Clock()
        while True:
            time = clock.tick(CONST.FPS)
            keys = pygame.key.get_pressed()

            for events in pygame.event.get():
                if events.type == QUIT:
                    sys.exit(0)

            #**UPDATES**
            pacman.update(time, keys)

            #**DRAW**
            self.screen.blit(self.background_image, (0, 0))

            pacman.draw(self.screen)
            #self.screen.blit(pacman.image, pacman.rect)
            pygame.display.flip()

        return 0
