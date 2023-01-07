import pygame

class snake():

    def __init__(self) -> None:
        self.snakelength = 2
        self.snakehead = (425, 235)
        self.snaketail = (420, 225)

    def check_location():
        pass

    def update():
        pass

    def relocate_apple():
        pass

    def render(self):
        pygame.init()

        horizontal = 850
        vertical = 470
        screen = pygame.display.set_mode((horizontal, vertical))

        pygame.display.set_caption("SnakeGame")

        clock = pygame.time.Clock()

        backGround = pygame.image.load('Images/background.jpg')
        backGroundRec = backGround.get_rect(center = (horizontal/2, vertical/2))

        screen.blit(backGround, backGroundRec)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)