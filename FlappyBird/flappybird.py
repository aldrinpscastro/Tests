#!bin/python
import pygame as pg

resolution = width, height = 288, 512
screen = pg.display.set_mode(resolution)
pg.display.set_caption('FlappyBird')
clock = pg.time.Clock()
fps = 30
gravity = 3
speed = 2
weight = 1
running = True
angle = 0

class Scenario:
    def __init__(self, image, x=0, y=0, invert=False):
        self.x = x
        self.y = y
        if not invert:
            self.image = pg.image.load(image).convert_alpha()
        else:
            self.image = pg.transform.flip(pg.image.load(image).convert_alpha(), False, True)

    def show_on_screen(self):
        screen.blit(self.image, (self.x, self.y))

    def move_on_screen(self, x, y=0):
        self.x -= x
        self.y = y
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x + width, self.y))
        if self.x < -width:
            self.x = 0

    def get_rect(self):
        return (pg.Rect((self.x, self.y, self.image.get_rect()[2], self.image.get_rect()[3])),
                pg.Rect((self.x + width, self.y, self.image.get_rect()[2], self.image.get_rect()[3])))

class Bird:
    def __init__(self, sprite, x=0, y=0):
        self.x = x
        self.y = y
        self.sprite = pg.image.load(sprite).convert_alpha()

    def show_on_screen(self):
        screen.blit(self.sprite, (self.x, self.y))

    def move_on_screen(self, sprite, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle
        if self.angle != 0:
            self.sprite = pg.transform.rotate(pg.image.load(sprite).convert_alpha(), self.angle)
        else:
            self.sprite = pg.image.load(sprite).convert_alpha()
        screen.blit(self.sprite, (self.x, self.y))

    def set_rect(self):
        return pg.Rect((self.x, self.y, self.sprite.get_rect()[2], self.sprite.get_rect()[3]))

background = Scenario('FlapPyBird-master/assets/sprites/background-day.png')
floor = Scenario('FlapPyBird-master/assets/sprites/base.png')
pipes_down = Scenario('FlapPyBird-master/assets/sprites/pipe-green.png')
pipes_up = Scenario('FlapPyBird-master/assets/sprites/pipe-green.png', 0, 0, True)
BIRD = ['FlapPyBird-master/assets/sprites/bluebird-midflap.png',
        'FlapPyBird-master/assets/sprites/bluebird-upflap.png',
        'FlapPyBird-master/assets/sprites/bluebird-downflap.png']
bird = Bird(BIRD[0])
posX_bird = (width - pg.image.load(BIRD[0]).get_rect()[2]) / 2
posY_bird = (height - pg.image.load(BIRD[0]).get_rect()[3]) / 2
while running:
    #Detecting key down.
    for sprite in BIRD:
        for event in pg.event.get():

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    #jumping
                    markY = posY_bird - 60
                    angle = 22.5
                    while posY_bird >= markY:
                        background.move_on_screen(speed)
                        floor.move_on_screen(speed * 2, height - 112)
                        pipes_down.move_on_screen(speed * 2, height - height * (1/3))
                        pipes_up.move_on_screen(speed * 2, height * -(1/3))
                        bird.move_on_screen(BIRD[2], posX_bird, posY_bird, angle)
                        posY_bird -= pg.image.load(sprite).get_rect()[3] / 2
                        gravity = 3
                        pg.display.flip()
                        clock.tick(fps)
                    angle = 0
                if event.key == pg.K_ESCAPE:
                    running = False

        #Showing images
        background.move_on_screen(speed)
        floor.move_on_screen(speed * 2, height - 112)
        pipes_down.move_on_screen(speed * 2, height - height * (1/3))
        pipes_up.move_on_screen(speed * 2, height * -(1/3))
        bird.move_on_screen(sprite, posX_bird, posY_bird, angle)
        if angle == 0:
            angle = -22.5
            if angle == -22.5:
                angle = -45
                if angle == -45:
                    angle = -67.5
                    if angle == -67.5:
                        angle = -90
        posY_bird += gravity
        gravity += weight

        #Detecting collisions.
        if (bird.set_rect().colliderect(pipes_down.get_rect()[1]) == 1 or
            bird.set_rect().colliderect(pipes_down.get_rect()[0]) == 1 or
            bird.set_rect().colliderect(pipes_up.get_rect()[1]) == 1 or
            bird.set_rect().colliderect(pipes_up.get_rect()[0]) == 1 or
            bird.set_rect().colliderect(floor.get_rect()[1]) == 1 or
            bird.set_rect().colliderect(floor.get_rect()[0]) == 1):
            running = False
        pg.display.flip()
        clock.tick(fps)
