import pygame
import random

pygame.init()

# Окно и сетка
W = 600
H = 400
CELL = 20
COLS = W // CELL
ROWS = H // CELL

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Zmeika")

class Snake:
    
    def __init__(self):
        # начальная длина змейки
        self.body = [(6, 8), (5, 8), (4, 8)]
        # направление: (1,0) вправо, (-1,0) влево, (0,1) вниз, (0,-1) вверх
        self.dir = (1, 0)

    def move(self):
        # сдвигаем голову на одну клетку
        hx, hy = self.body[0]
        nx = hx + self.dir[0]
        ny = hy + self.dir[1]
        new = (nx, ny)

        # проверка выхода за границы
        if nx < 0 or nx >= COLS or ny < 0 or ny >= ROWS:
            return False

        # проверка, не врезалась ли в себя
        if new in self.body:
            return False

        # вставляем новую голову
        self.body.insert(0, new)
        return True

    def change_dir(self, d):
        # нельзя сразу развернуться на 180 градусов
        if (d[0], d[1]) != (-self.dir[0], -self.dir[1]):
            self.dir = d

    def draw(self):
        # рисуем каждую клетку тела змейки
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x * CELL, y * CELL, CELL, CELL))

class Food:
    def __init__(self, snake_body):
        # создаём еду в случайном месте, где нет змейки
        self.pos = self.new_pos(snake_body)

    def new_pos(self, snake_body):
        # случайная клетка, где нет змеи
        while True:
            x = random.randint(0, COLS - 1)
            y = random.randint(0, ROWS - 1)
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        # рисуем еду
        x, y = self.pos
        pygame.draw.rect(screen, RED, (x * CELL, y * CELL, CELL, CELL))

def main():
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = 1
    clock = pygame.time.Clock()
    speed = 6  # начальная скорость
    running = True

    while running:
        screen.fill(BLACK)

        # обработка событий клавиатуры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_dir((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_dir((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_dir((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_dir((1, 0))

        # двигаем змейку, если False — игра окончена
        if not snake.move():
            break

        # если съели еду — увеличиваем счёт и создаём новую еду
        if snake.body[0] == food.pos:
            score += 1
            food = Food(snake.body)
        else:
            # иначе просто удаляем хвост 
            snake.body.pop()

        # увеличение уровня каждые 5 очков
        new_level = score // 5 + 1
        if new_level > level:
            level = new_level
            speed += 1  # увеличиваем скорость игры

        # рисуем змейку и еду
        snake.draw()
        food.draw()

        # выводим счёт и уровень на экран
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}   Level: {level}", True, WHITE)
        screen.blit(text, (10, 10))

        # обновляем экран
        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()

if __name__ == '__main__':
    main()
