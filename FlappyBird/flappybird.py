#!bin/python
import pygame as pg
from random import randint

RESOLUTION = WIDTH, HEIGHT = 288, 512
SCREEN = pg.display.set_mode(RESOLUTION)
pg.display.set_caption('FlappyBird')
CLOCK = pg.time.Clock()
FPS = 30
RUNNING = True
SPEED = 2
HEIGHT_GEP_PIPE = 6
SIZE_GEP_PIPE = 3

class Scenario:
    def __init__(self, image, posx=0, posy=0 , inverted=False):
        if inverted:
            self.image = pg.transform.flip(image, False, True)
        else:
            self.image = image
        self.posx = posx
        self.posy = posy


    def render(self):
        SCREEN.blit(self.image, (self.posx, self.posy))

    def render_and_move(self, posx, posy=0):
        self.posx -= posx
        self.posy = posy
        SCREEN.blit(self.image, (self.posx, self.posy))
        SCREEN.blit(self.image, (self.posx + WIDTH, self.posy))
        if self.posx < -WIDTH:
            self.posx = 0

class Scenario_pipe:
    def __init__(self, image, posx=0, posy=0 , inverted=False):
        if inverted:
            self.image = pg.transform.flip(image, False, True)
        else:
            self.image = image
        self.posx = posx
        self.posy = posy

    def render(self):
        SCREEN.blit(self.image, (self.posx, self.posy))

    def render_and_move(self, posx, posy=0):
        self.posx -= posx
        self.posy = posy
        SCREEN.blit(self.image, (self.posx + WIDTH, self.posy))
        SCREEN.blit(self.image, (self.posx + WIDTH*2, self.posy))
        if self.posx + WIDTH < -WIDTH:
            self.posx = -WIDTH

BACKGROUND = pg.image.load('FlapPyBird-master/assets/sprites/background-day.png').convert_alpha()
FLOOR = pg.image.load('FlapPyBird-master/assets/sprites/base.png').convert_alpha()
PIPE = pg.image.load('FlapPyBird-master/assets/sprites/pipe-green.png').convert_alpha()
background = Scenario(BACKGROUND)
floor = Scenario(FLOOR)
pipe_down = Scenario_pipe(PIPE)
pipe_up = Scenario_pipe(PIPE, 0, 0, True)

while RUNNING:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUNNING = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                RUNNING = False
    background.render_and_move(SPEED)
    pipe_down.render_and_move(SPEED, HEIGHT - BACKGROUND.get_rect()[3] * (HEIGHT_GEP_PIPE/12))
    pipe_up.render_and_move(SPEED, BACKGROUND.get_rect()[3] * -((HEIGHT_GEP_PIPE-SIZE_GEP_PIPE)/12))
    floor.render_and_move(SPEED, HEIGHT - FLOOR.get_rect()[3])
    pg.display.flip()
    CLOCK.tick(FPS)
