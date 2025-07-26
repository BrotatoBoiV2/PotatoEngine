# Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
# Program Name: Game Engine.
# Description: This is a library to make game writing a bit easier.
# Date: July/08/2025
# Version: 0.1.2-2025.07.26


import pygame as pg


### ~~~ Main Game Class. ~~~ ###
class Game:
    def __init__(self, title="Game", width=800, height=600):
        self.title = title
        self.size = (width, height)

        pg.init()

        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()

        self.isRunning = True

    def execute(self, update, render, fps=60):
        pg.display.set_caption(self.title)
        pg.display.set_mode(self.size)
        
        while self.isRunning:
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.isRunning = False
                # if event.type in [pg.KEYDOWN, pg.KEYUP, pg.MOUSEBUTTONUP, pg.MOUSEBUTTONDOWN]:
                #     Input._update()

           
                Input.update()

            if update:
                update()

            self.screen.fill((0, 0, 0))

            if render:
                render()

            pg.display.update()

            self.clock.tick(fps)

        #pg.quit()


### ~~~ Sprite Class. ~~~ ###
class Sprite(pg.Rect):
    def __init__(self, game, imagePath, pos, size):
        image = pg.image.load(imagePath).convert_alpha()

        self.image = pg.transform.scale(image, (size[0], size[1]))
        self.game = game

        super().__init__(pos[0], pos[1], size[0], size[1])

        self.center = (pos[0], pos[1])

    def render(self):
        self.game.screen.blit(self.image, self)
        # pg.draw.rect(self.game.screen, (255, 0, 0), self)


### ~~ Text Class. ~~~ ###
class Text:
    def __init__(self, gameInstance, text, rect, font, size, color=(0, 0, 0)):
        text = str(text)

        self.game = gameInstance
        self.font = pg.font.SysFont(font, size)
        self.text = self.font.render(text.encode(), True, color)
        if type(rect) == pg.Rect:
            self.rect = rect
        else:
            self.rect = pg.Rect(rect[0], rect[1], rect[2], rect[3])
        self.color = color

    def render(self):
        self.game.screen.blit(self.text, self.rect)


### ~~~ Button Class. ~~~ ###
class Button(pg.Rect):
    def __init__(self, game, text, pos, size, color=(255, 0, 0)):
        self.game = game
        self.color = color

        super().__init__(pos[0], pos[1], size[0], size[1])

        self.center = pos
        self.text = Text(game, text, self, 'Comic Sans MS', 32)

    def render(self):
        pg.draw.rect(self.game.screen, self.color, self)
        self.text.render()

    def is_clicked(self):
        if self.collidepoint(mouse_pos()):
            if mouse_click("left"):
                print("CLcickef")
                return True
            else:
                return False

    def update(self):
        if self.collidepoint(mouse_pos()):
            self.color = (125, 0, 0)
        else:
            self.color = (255, 0, 0)


### ~~~ Handle the Inputs. ~~~ ###
class Input:
    keys = {}
    mouseButtons = {}

    # @staticmethod
    def update():
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

### ~~~ Check if a mouse button has been clicked. ~~~ ###
def mouse_click(button):
    buttons = {
        "left": 0,
        "middle": 1,
        "right": 2
    }

    return Input.mouseButtons[buttons[button]]
    
### ~~~ Return the position of the mouse. ~~~ ###
def mouse_pos():
    return pg.mouse.get_pos()