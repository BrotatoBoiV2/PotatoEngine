# Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
# Program Name: Game Engine.
# Description: This is a library to make game writing a bit easier.
# Date: July/08/2025
# Version: 0.3-2025.07.11


import pygame as pg


### ~~~ Main Game Class. ~~~ ###
class Game:
    def __init__(self, title="Game", width=800, height=600):
        pg.init()

        pg.display.set_caption(title)

        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()

        self.isRunning = True

    def execute(self, update, render, fps=60):
        while self.isRunning:
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.isRunning = False

            keys = pg.key.get_pressed()
            Input._update(keys)

            if update:
                update()

            self.screen.fill((0, 0, 0))

            if render:
                render()

            pg.display.update()

            self.clock.tick(fps)

        pg.quit()


### ~~~ Sprite Class. ~~~ ###
class Sprite:
    def __init__(self, game, imagePath, x=0, y=0, width=32, height=32):
        image = pg.image.load(imagePath).convert_alpha()

        self.image = self.image = pg.transform.scale(image, (width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.game = game

    def get_rect(self):
        return (self.x, self.y, self.width, self.height)

    def render(self):
        self.game.screen.blit(self.image, (self.x, self.y))


### ~~~ Handle the Inputs. ~~~ ###
class Input:
    key = None

    @staticmethod
    def _update(keyStates):
        Input.keys = keyStates


### ~~ Check if a key was pressed. ~~ ###
def key_pressed(key):
    keys = {
        "left": pg.K_LEFT,
        "right": pg.K_RIGHT,
        "up": pg.K_UP,
        "down": pg.K_DOWN,
    }

    return Input.keys[keys[key]]

