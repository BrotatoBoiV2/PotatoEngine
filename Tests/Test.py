import PotatoEngine as pe
print(pe.__version__)

GAME = pe.Game("Game")


class Player(pe.Sprite):
    def __init__(self, gameInstance, imagePath, pos, size):
        #self.sprite = Sprite(gameInstance, imagePath, pos[0], pos[1], size[0], size[1])
        #self.rect = self.sprite.get_rect()

        super().__init__(gameInstance, imagePath, pos[0], pos[1], size[0], size[1])

    def update(self):
        if pe.key_pressed("left"):
            self.x -= 1

        elif pe.key_pressed("right"):
            self.x += 1

        elif pe.key_pressed("up"):
            self.y -= 1

        elif pe.key_pressed("down"):
            self.y += 1


class Main:
    def __init__(self):
        # self.elf = Player(GAME, './Elf.png', (0, 0), (32, 32))

        self.execute()

    def render(self):
        # self.elf.render()
        pass

    def update(self):
        # self.elf.update()
        pass

    def execute(self):
        GAME.execute(self.update, self.render)


if __name__ == '__main__':
    Main()
