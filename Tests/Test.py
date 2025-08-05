import PotatoEngine as pe
print(pe.__version__)

GAME = pe.Window("Game")


class Player(pe.Sprite):
    def __init__(self, windowInstance, imagePath, pos, size):
        super().__init__(windowInstance, imagePath, pos, size)

    def update(self):
        if pe.key_press("left"):
            self.x -= 1

        elif pe.key_press("right"):
            self.x += 1

        elif pe.key_press("up"):
            self.y -= 1

        elif pe.key_press("down"):
            self.y += 1


class Main:
    def __init__(self):
        self.elf = Player(GAME, './Tests/Elf.png', (0, 0), (32, 32))
        self.test = pe.Button(GAME, "Test Button", (GAME.size[0]//2, GAME.size[1]//2), (100, 50))

        self.text = pe.Text(GAME, "Words", (0, 0, 100, 50), 'Comic Sans MS', 32, (255, 0, 0))

        self.execute()

    def render(self):
        # self.elf.render()self.game.screen.blit(self.text, self.textRect)
        self.text.render()
        self.elf.render()
        self.test.render()
        pass

    def update(self):
        self.elf.update()
        self.test.update()

        if self.test.collidepoint(pe.mouse_pos()) and pe.mouse_click("left"):
            print("Start!")

    def execute(self):
        GAME.execute(self.update, self.render)


if __name__ == '__main__':
    Main()
