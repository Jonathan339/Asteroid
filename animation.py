import constants


class Animation:

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.vx = 10
        self.vy = 10
        self.key = []

    def update(self):
        pygame.display.update()

    def move(self):
        pass

    def key_handle(self)-> None:
        """
        Captura los eventos del teclado.
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            pos = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONDOWN:
                self.clicks.append(pos)
                print(pos)

    def draw(self):
        surface.blit(self.image, self.rect)
