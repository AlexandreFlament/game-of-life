import pygame
from pygame.locals import *
from gameoflife import GameOfLife

pygame.init()

class Display():

    def __init__(self, size, screensize = (pygame.display.Info().current_w, pygame.display.Info().current_h), initialboard = None):

        self.x_screen_size = screensize[0]
        self.y_screen_size = screensize[1]

        self.screen = pygame.display.set_mode((self.x_screen_size, self.y_screen_size))
        pygame.display.set_caption('GOL')

        self.clock = pygame.time.Clock()
        self.speed = 1

        self.size = size
        self.display = pygame.Surface((size*10, size*10))

        self.gol = GameOfLife(size)

        self.whitesquare = pygame.image.load("cell.png")

        self.running = True


    def randstart(self):

        self.gol.randboard()

        self.display.fill((0,0,0))

        for y in range(self.size):
            for x in range(self.size):
                if self.gol.board[x][y] == 1:
                    self.display.blit(self.whitesquare, (x*10,y*10))


    def updateboard(self):
        self.gol.update_board()

        for y in range(self.size):
            for x in range(self.size):
                if self.gol.board[x][y] == 1:
                    self.display.blit(self.whitesquare, (x*10,y*10))
    

    def liferunner(self):
        while self.running:
            self.display.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    pass
                if event.type == KEYUP:
                    pass
                if event.type == MOUSEWHEEL:
                    if event.y < 0 and -event.y > self.speed-1:
                        self.speed = 1
                    else:
                        self.speed += event.y
            
            self.updateboard()
            
            self.screen.blit(pygame.transform.scale(self.display, (self.x_screen_size, self.y_screen_size)), (0,0))
            pygame.display.update()
            self.clock.tick(self.speed)


d = Display(200, (1300,1300))
d.randstart()
d.liferunner()