import sys, pygame
from pygame.locals import *
import constants as CONST
import utils as UTILS
import pacman as PAC

class Core:


    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((CONST.WIDTH, CONST.HEIGHT))
        pygame.display.set_caption("Pacman Remake by AaronArias")

        #self.background_image = UTILS.load_image('images/backprueba.png')
        self.wall_image = UTILS.load_image('images/wall.png')
        self.floor_image = UTILS.load_image('images/floor.png')

    #*************Auxiliars*************
    def drawMap(self):
        self.screen.fill((0,0,0))

        for i in range(CONST.ROWS):
            for j in range(CONST.COLS):
                if CONST.gameMap[j,i]==1:
                    self.screen.blit(self.wall_image, (i*CONST.CELL_TAM, j*CONST.CELL_TAM))
                elif CONST.gameMap[j,i]==0:
                    self.screen.blit(self.floor_image, (i*CONST.CELL_TAM, j*CONST.CELL_TAM))


    #*************MAINLOOP*************
    def main_loop(self):
        pacman = PAC.Pacman()

        clock = pygame.time.Clock()
        while True:
            print(CONST.gameMap)

            time = clock.tick(CONST.FPS)
            keys = pygame.key.get_pressed()

            for events in pygame.event.get():
                if events.type == QUIT:
                    sys.exit(0)

            #**UPDATES**
            pacman.update(time, keys)

            #**DRAW**
            #self.screen.blit(self.background_image, (0, 0))
            self.drawMap()

            pacman.draw(self.screen)
            #self.screen.blit(pacman.image, pacman.rect)
            pygame.display.flip()

        return 0
