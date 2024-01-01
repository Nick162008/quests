import pygame
import itertools


class Cub:
    # создание поля
    def __init__(self, width, height):
        self.x = 0
        self.y = 0

    def render(self, screen):
        if self.x == 0 and self.y == 0:
            pygame.draw.rect(screen, pygame.Color("grey"), (250, 250, 50, 10), 0)
            pass
        else:
            pygame.draw.rect(screen, pygame.Color("blue"), (self.x, self.y, 20, 20), 0)
            pygame.draw.rect(screen, pygame.Color("grey"), (250, 250, 50, 10), 0)
            self.y += 1

    def get_click(self, pos):
        self.x = pos[0]
        self.y = pos[1]



def main():
    pygame.init()
    w, h = 500, 500
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Платформы')
    clock = pygame.time.Clock()
    # поле 5 на 7
    board = Cub(w, h)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        clock.tick(50)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
