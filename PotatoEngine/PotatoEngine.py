# Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
# Program Name: Game Engine.
# Description: This is a library to make game writing a bit easier.
# Date: July/08/2025
# Version: 0.1.2-2025.08.05


import pygame as pg


### ~~~ Main Game Class. ~~~ ###
class Window:
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
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.isRunning = False
           
                Input.update(event)

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
    def __init__(self, window, imagePath, pos, size):
        image = pg.image.load(imagePath).convert_alpha()

        self.image = pg.transform.scale(image, (size[0], size[1]))
        self.window = window

        super().__init__(pos[0], pos[1], size[0], size[1])

        self.center = (pos[0], pos[1])

    def render(self):
        self.window.screen.blit(self.image, self)
        # pg.draw.rect(self.game.screen, (255, 0, 0), self)


### ~~ Text Class. ~~~ ###
class Text:
    def __init__(self, window, text, rect, font, fontSize, color=(0, 0, 0)):
        text = str(text)

        self.window = window
        self.font = pg.font.SysFont(font, size)
        self.text = self.font.render(text.encode(), True, color)
        if type(rect) == pg.Rect:
            self.rect = rect
        else:
            self.rect = pg.Rect(rect[0], rect[1], rect[2], rect[3])
        self.color = color

    def render(self):
        self.window.screen.blit(self.text, self.rect)


### ~~~ Button Class. ~~~ ###
class Button(pg.Rect):
    def __init__(self, window, text, pos, size, color=(255, 0, 0)):
        self.window = window
        self.color = color

        super().__init__(pos[0], pos[1], size[0], size[1])

        self.center = pos
        self.text = Text(window, text, self, 'Comic Sans MS', 32)

    def render(self):
        pg.draw.rect(self.window.screen, self.color, self)
        self.text.render()

    def is_clicked(self):   return self.collidepoint(mouse_pos()) and mouse_click("left")

    def update(self):
        if self.collidepoint(mouse_pos()):
            self.color = (125, 0, 0)
        else:
            self.color = (255, 0, 0)


### ~~~ Handle the Inputs. ~~~ ###
class Input:
    keys = {}
    mouseButtons = (False, False, False)
    mousePressed = {0:False, 1:False, 2:False}
    mouseReleased = {0:False, 1:False, 2:False}
    mouseClicked = {0:False, 1:False, 2:False}

    @staticmethod
    def update(event):
        Input.keys = pg.key.get_pressed()
        Input.mouseButtons = pg.mouse.get_pressed()
        
        Input.mousePressed = {0:False, 1:False, 2:False}
        Input.mouseReleased = {0:False, 1:False, 2:False}
        Input.mouseClicked = {0:False, 1:False, 2:False}

        if event.type == pg.MOUSEBUTTONDOWN:
            Input.mousePressed[event.button-1] = True
        if event.type == pg.MOUSEBUTTONUP:
            Input.mouseReleased[event.button-1] = True
            Input.mouseClicked[event.button-1] = True

### ~~ Check if a key was pressed. ~~ ###
def key_press(key):
    keys = { "left": pg.K_LEFT, "right": pg.K_RIGHT, "up": pg.K_UP,
            "down": pg.K_DOWN, "a": pg.K_a, "b": pg.K_b, "c": pg.K_c,
            "d": pg.K_d, "e": pg.K_e, "f": pg.K_f, "g": pg.K_g, 
            "h": pg.K_h, "i": pg.K_i, "j": pg.K_j, "k": pg.K_k, 
            "l": pg.K_l, "m": pg.K_m, "n": pg.K_n, "o": pg.K_o, 
            "p": pg.K_p, "q": pg.K_q, "r": pg.K_r, "s": pg.K_s,
            "t": pg.K_t, "u": pg.K_u, "v": pg.K_v, "w": pg.K_w, 
            "x": pg.K_x, "y": pg.K_y, "z": pg.K_z }

    return Input.keys[keys[key]]

### ~~~ Check if a mouse button has been clicked. ~~~ ###
def mouse_click(button):
    buttons = {
        "left": 0,
        "middle": 1,
        "right": 2
    }

    return Input.mouseClicked[buttons[button]]
    
### ~~~ Return the position of the mouse. ~~~ ###
def mouse_pos():
    return pg.mouse.get_pos()