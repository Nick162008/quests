import pygame


def sphere(screen):
    screen.fill(pygame.Color('white'))
    y1 = n / 2
    y2 = 0
    y3 = n / 2
    y4 = n

    x1 = 0
    x2 = n / 2
    x3 = n
    x4 = n / 2
    count = width / n
    for i in range(int(count)):
        for g in range(int(count)):
            pygame.draw.polygon(screen, (pygame.Color("orange")), [[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
            x1 += n
            x2 += (n / 2) * 2
            x3 += n
            x4 += (n / 2) * 2
        y1 += (n / 2) * 2
        y2 += n
        y3 += (n / 2) * 2
        y4 += n

        x1 = 0
        x2 = n / 2
        x3 = n
        x4 = n / 2


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    size = width, height = 300, 300
    n = int(input())
    screen = pygame.display.set_mode(size)
    sphere(screen)
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
