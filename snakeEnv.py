import pygame

class snake():

    def __init__(self) -> None:
        self.snake = 2

    def render(self):
        pygame.init()

        screen = pygame.display.set_mode((800, 400))

        pygame.display.set_caption("SnakeGame")

        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)