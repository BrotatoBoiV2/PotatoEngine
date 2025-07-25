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

        self.width = width
        self.height = height

        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()

        self.isRunning = True

    def execute(self, update, render, fps=60):
        while self.isRunning:
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.isRunning = False
                if event.type == pg.KEYDOWN:
                    Input._update()

           
            Input._update()

            if update:
                update()

            self.screen.fill((0, 0, 0))

            if render:
                render()

            pg.display.update()

            self.clock.tick(fps)

        pg.quit()


### ~~~ Sprite Class. ~~~ ###
class Sprite(pg.Rect):
    def __init__(self, game, imagePath, x, y, width, height):
        image = pg.image.load(imagePath).convert_alpha()

        self.image = pg.transform.scale(image, (width, height))
        self.game = game

        super().__init__(x, y, width, height)

        self.center = (x, y)

    def render(self):
        self.game.screen.blit(self.image, self)
        # pg.draw.rect(self.game.screen, (255, 0, 0), self)


class Text:
    def __init__(self, gameInstance, text, rect, font, size, color=(0, 0, 0)):
        text = str(text)

        self.game = gameInstance
        self.font = pg.font.SysFont(font, size)
        self.text = self.font.render(text.encode(), True, color)
        self.rect = rect
        self.color = color

    def render(self):
        self.game.screen.blit(self.text, self.rect)


class Button(pg.Rect):
    def __init__(self, game, text, pos, size):
        self.game = game
        
        super().__init__(pos[0], pos[1], size[0], size[1])

        self.center = pos
        self.text = Text(game, text, self, 'Comic Sans MS', 32)

    def render(self):
        pg.draw.rect(self.game.screen, self.color, self)
        self.text.render()

    def update(self):
        mousePos = pg.mouse.get_pos()

        if self.collidepoint(mousePos):
            self.color = (125, 0, 0)
        else:
            self.color = (255, 0, 0)


### ~~~ Handle the Inputs. ~~~ ###
class Input:
    keys = {}
    mouseButtons = {}

    @staticmethod
    def _update():
        Input.keys = pg.key.get_pressed()
        Input.mouseButtons = pg.mouse.get_pressed()
        
### ~~ Check if a key was pressed. ~~ ###
def key_press(key):
    keys = {
        "left": pg.K_LEFT,
        "right": pg.K_RIGHT,
        "up": pg.K_UP,
        "down": pg.K_DOWN,
        "w": pg.K_w,
        "s": pg.K_s,
        "i": pg.K_i,
        "k": pg.K_k,
    }

    return Input.keys[keys[key]]

def mouse_click(button):
    buttons = {
        "left": 0,
        "middle": 1,
        "right": 2
    }

    return Input.mouseButtons[buttons[button]]
    
def mouse_pos():
    return pg.mouse.get_pos()