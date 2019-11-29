#! bin/python
import pygame as pg

pg.init()
size = width, height = 288, 512
pg.display.set_caption('Flappybird')
screen = pg.display.set_mode(size)
CLOCK = pg.time.Clock()
running = True
fps = 30
speed = 2
BIRD = [pg.image.load('FlapPyBird-master/assets/sprites/bluebird-midflap.png').convert_alpha(),
        pg.image.load('FlapPyBird-master/assets/sprites/bluebird-upflap.png').convert_alpha(),
        pg.image.load('FlapPyBird-master/assets/sprites/bluebird-downflap.png').convert_alpha()]

class moveimage:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pg.image.load(image).convert_alpha()

    def movescenario(self, x, y=0):
        self.x = x
        self.y = y
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x + width, self.y))

    def get_x_image(self):
        return self.image.get_rect()[2]

    def get_y_image(self):
        return self.image.get_rect()[3]

    def invert_y_image_and_move(self, x, y=0):
        self.x = x
        self.y = y
        inverteimage = pg.transform.flip(self.image, False, True)
        screen.blit(inverteimage, (self.x, self.y))
        screen.blit(inverteimage, (self.x + width, self.y))

class bird:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.images = image

    def render(self, image):
        self.image =  image
        screen.blit(self.images[self.image], (self.x, self.y))

    def get_x_image(self):
        return self.images[0].get_rect()[2]

    def get_y_image(self):
        return self.images[0].get_rect()[3]


posx_background = 0
posx_floor = 0
posx_pipe = width * 2
BACKGROUND = moveimage(posx_background, 0, 'FlapPyBird-master/assets/sprites/background-day.png')
FLOOR = moveimage(posx_background, 0, 'FlapPyBird-master/assets/sprites/base.png')
PIPE = moveimage(posx_background, 0, 'FlapPyBird-master/assets/sprites/pipe-green.png')
BIRD1 = bird(width / 2 - BIRD[0].get_rect()[2] / 2, height / 2 - BIRD[0].get_rect()[3] / 2, BIRD)
while running:
    for image in [0, 1, 2]:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
        BACKGROUND.movescenario(posx_background)
        FLOOR.movescenario(posx_floor, height - FLOOR.get_y_image() )
        PIPE.movescenario(posx_pipe, BACKGROUND.get_y_image() * (2/3))
        PIPE.invert_y_image_and_move(posx_pipe, BACKGROUND.get_y_image() * -(1/3))
        BIRD1.render(image)
        posx_background -= speed
        posx_floor -= speed * 2
        posx_pipe -= speed * 2
        if posx_background < -width:
            posx_background = 0
        if posx_floor < -width:
            posx_floor = 0
        if posx_pipe < -width:
            posx_pipe = 0
        CLOCK.tick(30)
        pg.display.flip()
pg.quit()
