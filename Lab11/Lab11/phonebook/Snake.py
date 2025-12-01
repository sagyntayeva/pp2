import pygame
import random

# Инициализация Pygame
pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20 
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Проверка столкновений
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or 
            new_head in self.body):
            return False
        
        self.body.insert(0, new_head)  # Добавляем голову
        return True  

    def shrink(self):
        self.body.pop() 

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake_body):
        self.position = self.generate_food_pos(snake_body)
        self.weight = random.choice([1, 2, 3])  # Рандомный вес еды
        self.timer = random.randint(50, 75)  # Время исчезновения еды

    def generate_food_pos(self, snake_body):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_body:  # Еда не должна быть на змейке
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def update_timer(self):
        self.timer -= 1
        return self.timer > 0

snake = Snake()
food = Food(snake.body)
score = 0
level = 1
speed = 5  
clock = pygame.time.Clock()
running = True

import psycopg2
from connect import connect

def user(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user is None:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, 0, 1))
        conn.commit()
    else:
        user_id = user[0]

    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
    score_data = cur.fetchone()

    cur.close()
    conn.close()
    
    return user_id, score_data[0], score_data[1]

username = input("Enter your username: ")
print(f"User: {username}")
user_id, score, level = user(username)
speed = 5 + (level - 1) * 2


while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))
            elif event.key == pygame.K_p:
                print("Игра на паузе. Сохраняю прогресс...")
                conn = connect()
                cur = conn.cursor()
                cur.execute("""
                    UPDATE user_score
                    SET score = %s, level = %s
                    WHERE user_id = %s
                """, (score, level, user_id))
                conn.commit()
                cur.close()
                conn.close()

                paused = True
                while paused:
                    for pause_event in pygame.event.get():
                        if pause_event.type == pygame.QUIT:
                            running = False
                            paused = False
                        elif pause_event.type == pygame.KEYDOWN and pause_event.key == pygame.K_p:
                            paused = False  # снять с паузы
    
    if not snake.move():
        running = False 
    
    if snake.body[0] == food.position:  
        score += food.weight
        food = Food(snake.body) 

        if score % 3 == 0:
            level += 1
            speed += 2  

    else:
        snake.shrink() 

    
    if not food.update_timer():
        food = Food(snake.body)  # Генерация новой еды
    
    snake.draw()
    food.draw()
    
    # Отображение счета и уровня
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
