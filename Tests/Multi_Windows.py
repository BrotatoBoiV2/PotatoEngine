import PotatoEngine as pe

GAME = pe.Game("Game")
MENU = pe.Game("Menu", 400, 300)


class Main:
    def __init__(self):
        GAME.isRunning = False

        self.play = pe.Button(MENU, 'Play', (MENU.size[0]//2, MENU.size[1]//2), (150, 50))
        self.back = pe.Button(GAME, 'Back', (50, 50), (50, 50))

        self.player = pe.Sprite(GAME, './Elf.png', (GAME.size[0]//2, GAME.size[1]//2), (32, 32))

        self.execute()

    def menu_update(self):
        self.play.update()

        if self.play.is_clicked():
            MENU.isRunning = False
            GAME.isRunning = True

    def menu_render(self):
        self.play.render()

    def update(self):
        self.back.update()

        if self.back.is_clicked():
            GAME.isRunning = False
            MENU.isRunning = True

    def render(self):
        self.player.render()
        self.back.render()

    def execute(self):
        while MENU.isRunning or GAME.isRunning:
            if MENU.isRunning:
                print("Menu Render")
                MENU.execute(self.menu_update, self.menu_render)
            if GAME.isRunning:
                print("Game PLaying")
                GAME.execute(self.update, self.render)


if __name__ == '__main__':
    Main()

