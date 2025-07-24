import PotatoEngine as pe
print(pe.__version__)

GAME = pe.Game("Game")


class Player(pe.Sprite):
    def __init__(self, gameInstance, imagePath, pos, size):
        self.sprite = pe.Sprite(gameInstance, imagePath, pos[0], pos[1], size[0], size[1])
        #self.rect = self.sprite.get_rect()

        super().__init__(gameInstance, imagePath, pos[0], pos[1], size[0], size[1])

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
        self.test = pe.Button(GAME, "Test Button", (GAME.width//2, GAME.height//2), (100, 50))

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
