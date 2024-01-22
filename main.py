import random

import pygame
import itertools


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sp = [2, 4]
        count = 0
        self.board = [[0] * width for _ in range(height)]
        for y in range(height):
            for x in range(width):
                if count < 2 and random.randint(0, 1) == 0:
                    self.board[y][x] = self.sp[random.randint(0, 1)]
                    count += 1
        # значения по умолчанию
        self.left = 10
        self.top = 20
        self.cell_size = 50
        self.count = 0
        with open('best_score.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        self.best_score = int(text)
        self.flag_score = False
        if self.best_score == 0:
            self.flag_score = True
        self.score = 0

    def render(self, screen):
        colors = [pygame.Color("black"), pygame.Color("red"), pygame.Color("blue")]
        for x, y in itertools.product(range(self.width), range(self.height)):
            pygame.draw.rect(screen, pygame.Color("white"), (
                x * self.cell_size + 5, y * self.cell_size + 5, self.cell_size,
                self.cell_size), 1)
            font = pygame.font.Font(None, 30)
            if self.board[y][x] != 0:
                text = font.render(f"{self.board[y][x]}", True, (255, 255, 255))
                screen.blit(text, (x * self.cell_size + 20, y * self.cell_size + 13, self.cell_size,
                                   self.cell_size))
            text = font.render(f"Счёт: {self.score}", False, (255, 255, 255))
            screen.blit(text, (50 * self.width + 10, 5, 10,
                               10))
            text = font.render(f"Лучший счёт: {self.best_score}", False, (255, 255, 255))
            screen.blit(text, (50 * self.width + 10, 30, 10,
                               10))

    # cell - кортеж (x, y)
    def on_click(self, cell):
        x = cell[1]
        y = cell[0]
        if self.board[cell[1]][cell[0]] == 1 and self.count % 2 == 0:
            self.board[x] = [1] * self.width
            for i in range(self.height):
                self.board[i][y] = 1
            self.count += 1

        if self.board[cell[1]][cell[0]] == 2 and self.count % 2 != 0:
            self.board[x] = [2] * self.width
            for i in range(self.height):
                self.board[i][y] = 2
            self.count += 1

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def wichside(self, flag):
        board = 0
        flag1 = True
        board = self.board
        if flag == 0:
            for y in range(self.height):
                for x in range(self.width):
                    if self.board[y][x] == 0:
                        pass
                    else:
                        for x1 in range(self.width - 1, 0, -1):
                            if self.board[y][x1 - 1] == 0:
                                self.board[y][x1 - 1] = self.board[y][x1]
                                self.board[y][x1] = 0
                            if self.board[y][x1] == self.board[y][x1 - 1]:
                                self.board[y][x1 - 1] = 2 * self.board[y][x1]
                                self.board[y][x1] = 0
                                if self.flag_score:
                                    self.score += self.board[y][x1 - 1]
                                    self.best_score += self.board[y][x1 - 1]
                                else:
                                    self.score += self.board[y][x1 - 1]
        if flag == 1:
            for y in range(self.height):
                for x in range(self.width):
                    if self.board[y][x] == 0:
                        pass
                    else:
                        for x1 in range(0, self.width - 1):
                            if self.board[y][x1 + 1] == 0:
                                self.board[y][x1 + 1] = self.board[y][x1]
                                self.board[y][x1] = 0
                            if self.board[y][x1] == self.board[y][x1 + 1]:
                                self.board[y][x1 + 1] = 2 * self.board[y][x1]
                                self.board[y][x1] = 0
                                if self.flag_score:
                                    self.score += self.board[y][x1 + 1]
                                    self.best_score += self.board[y][x1 + 1]
                                else:
                                    self.score += self.board[y][x1 + 1]
        if flag == 2:
            for y in range(self.height):
                for x in range(self.width):
                    if self.board[y][x] == 0:
                        pass
                    else:
                        for y1 in range(self.width - 1, 0, -1):
                            if self.board[y1 - 1][x] == 0:
                                self.board[y1 - 1][x] = self.board[y1][x]
                                self.board[y1][x] = 0
                            if self.board[y1][x] == self.board[y1 - 1][x]:
                                self.board[y1 - 1][x] = 2 * self.board[y1][x]
                                self.board[y1][x] = 0
                                if self.flag_score:
                                    self.score += self.board[y - 1][x]
                                    self.best_score += self.board[y - 1][x]
                                else:
                                    self.score += self.board[y - 1][x]
        if flag == 3:
            for y in range(self.height):
                for x in range(self.width):
                    if self.board[y][x] == 0:
                        pass
                    else:
                        for y1 in range(0, self.width - 1):
                            if self.board[y1 + 1][x] == 0:
                                self.board[y1 + 1][x] = self.board[y1][x]
                                self.board[y1][x] = 0
                            if self.board[y1][x] == self.board[y1 + 1][x]:
                                self.board[y1 + 1][x] = 2 * self.board[y1][x]
                                self.board[y1][x] = 0
                                if self.flag_score:
                                    self.score += self.board[y1 + 1][x]
                                    self.best_score += self.board[y1 + 1][x]
                                else:
                                    self.score += self.board[y1 + 1][x]
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0 and random.randint(0, 1) == 1:
                    self.board[y][x] = self.sp[random.randint(0, 1)]
                    break
            else:
                continue
            break
        if board == self.board:
            print('Конец')
        self.end(1)

    def end(self, flag):
        count_flag = 0
        count_end = 0
        if flag == 0:
            with open('best_score.txt', 'w', encoding='utf-8') as file:
                print(self.best_score, self.score)
                if self.best_score == 0:
                    text = file.write(f'{int(self.score)}')
                else:
                    if self.best_score < self.score:
                        text = file.write(f'{int(self.score)}')
                    if self.best_score == self.score:
                        text = file.write(f'{int(self.score)}')
                    if self.best_score > self.score:
                        text = file.write(f'{int(self.best_score)}')
        if flag == 1:
            for y in range(self.height):
                for x in range(self.width):
                    for x1 in range(self.width - 1, 0, -1):
                        if self.board[y][x1 - 1] == 0 or self.board[y][x1] == self.board[y][x1 - 1]:
                            pass
                        else:
                            count_end += 1
            if count_end == 48:
                count_flag += 1
        print(count_end)


def main():
    pygame.init()
    w = int(input())
    h = int(input())

    # поле 5 на 7
    board = Board(w, h)
    size = 50 * w + 250, 50 * h + 40
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Реакция на события от мыши')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                board.end(0)
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.wichside(0)
                    board.render(screen)
                if event.key == pygame.K_RIGHT:
                    board.wichside(1)
                if event.key == pygame.K_UP:
                    board.wichside(2)
                if event.key == pygame.K_DOWN:
                    board.wichside(3)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
