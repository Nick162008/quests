import pygame
import itertools


class vent:
    # создание поля
    def __init__(self, width, height):
        self.x = width // 2
        self.y = height // 2
        self.x11 = self.x - 15
        self.y11 = self.x - 65
        self.x12 = self.x + 15
        self.y12 = self.x - 65
        self.v = 0

    def render(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), (self.x, self.y), 10)
        if 20 <= self.x11 <= self.x and 20 <= self.y11 <= self.y:
            self.x11 += 1
            self.y11 -= 1
        if self.x <= self.x11 <= 181 and 20 <= self.y11 <= self.y:
            self.x11 -= 1
            self.y11 -= 1
        if self.x <= self.x11 <= 181 and self.y <= self.y11 <= 181:
            self.x11 += 1
            self.y11 -= 1
        if 20 <= self.x11 <= self.x and self.y <= self.y11 <= 181:
            self.x11 += 1
            self.y11 += 1

        if 20 <= self.x12 <= self.x and 20 <= self.y12 <= self.y:
            self.x12 -= 1
            self.y12 += 1
        if self.x <= self.x12 <= 181 and 20 <= self.y12 <= self.y:
            self.x12 += 1
            self.y12 += 1
        if self.x <= self.x12 <= 181 and self.y <= self.y12 <= 181:
            self.x12 -= 1
            self.y12 += 1
        if 20 <= self.x12 <= self.x and self.y <= self.y12 <= 181:
            self.x12 -= 1
            self.y12 -= 1
        pygame.draw.polygon(screen, pygame.Color("white"),
                            [[self.x, self.y], [self.x11, self.y11], [self.x12, self.y12]])


def main():
    pygame.init()
    w, h = 201, 201
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Реакция на события от мыши')
    clock = pygame.time.Clock()
    # поле 5 на 7
    board = vent(w, h)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        clock.tick(70)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
