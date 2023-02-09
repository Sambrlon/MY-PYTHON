import pygame
import sys
import random

# Инициализация pygame
pygame.init()

# Установка размеров окна
win_width = 720
win_height = 720

# Инициализация окна
win = pygame.display.set_mode((win_width, win_height))

# Настройка частоты обновления экрана
clock = pygame.time.Clock()

# Установка цвета змейки и яблока
snake_color = (255, 0, 0)
apple_color = (0, 255, 0)

# Установка ширины и высоты квадрата змейки
block_size = 20

# Установка шрифта для отображения счета
font = pygame.font.Font(None, 25)


class Snake:
    def __init__(self):
        self.x = [290, 290, 290, 290, 290]
        self.y = [290, 270, 250, 230, 210]
        self.direction = 0
        self.length = 5

    # Обновление координат змейки
    def update(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # Определение направления движения змейки
        if self.direction == 0:
            self.x[0] = self.x[0] + block_size
        if self.direction == 1:
            self.x[0] = self.x[0] - block_size
        if self.direction == 2:
            self.y[0] = self.y[0] - block_size
        if self.direction == 3:
            self.y[0] = self.y[0] + block_size

    # Отрисовка змейки

    def draw(self, win):
        for i in range(self.length):
            pygame.draw.rect(
                win, snake_color, (self.x[i], self.y[i], block_size, block_size))


class Apple:
    def __init__(self):
        self.x = 0
        self.y = 0

    # Обновление координат яблока
    def update(self, snake):
        self.x = round(random.randrange(
            0, win_width - block_size) / 20.0) * 20.0
        self.y = round(random.randrange(
            0, win_height - block_size) / 20.0) * 20.0

        for i in range(snake.length):
            if self.x == snake.x[i] and self.y == snake.y[i]:
                self.update(snake)

    # Отрисовка яблока
    def draw(self, win):
        pygame.draw.rect(win, apple_color,
                         (self.x, self.y, block_size, block_size))


def game_over(win, score):
    font = pygame.font.Font(None, 30)
    game_over_text = font.render(
        "Игра окончена. Ваш счет: " + str(score), True, (255, 255, 255))
    win.blit(game_over_text, [win_width / 6, win_height / 3])
    pygame.display.update()
    pygame.time.wait(3000)
    sys.exit()


def display_score(win, score):
    score_text = font.render("Счет: " + str(score), True, (255, 255, 255))
    win.blit(score_text, [10, 10])


def main():
    # Инициализация змейки и яблока
    snake = Snake()
    apple = Apple()

    # Инициализация счета
    score = 0

    # Инициализация главного цикла
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != 3:
                    snake.direction = 2
                if event.key == pygame.K_DOWN and snake.direction != 2:
                    snake.direction = 3
                if event.key == pygame.K_LEFT and snake.direction != 0:
                    snake.direction = 1
                if event.key == pygame.K_RIGHT and snake.direction != 1:
                    snake.direction = 0

    # Очистка экрана
    win.fill((0, 0, 0))

    # Обновление змейки
    snake.move()

    # Обработка столкновения с яблоком
    if snake.x[0] == apple.x and snake.y[0] == apple.y:
        apple.update(snake)
        snake.eat()
        score += 1

    # Обработка столкновения со стеной
    if snake.x[0] < 0 or snake.x[0] >= win_width or snake.y[0] < 0 or snake.y[0] >= win_height:
        game_over(win, score)

    # Обработка столкновения самой с собой
    for i in range(1, snake.length):
        if snake.x[0] == snake.x[i] and snake.y[0] == snake.y[i]:
            game_over(win, score)

    # Отрисовка змейки и яблока
    snake.draw(win)
    apple.draw(win)

    # Отображение счета
    display_score(win, score)

    # Обновление экрана
    pygame.display.update()

    # Установка частоты кадров
    clock.tick(snake_speed)


if name == 'main':
    main()
