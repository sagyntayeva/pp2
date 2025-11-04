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
BLUE = (0, 0, 255)
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
        
        # Проверка столкновения со стенами
        if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
            return False
        
        # Проверка столкновения с самой собой
        if new_head in self.body:
            return False
        
        self.body.insert(0, new_head)
        return True

    def grow(self):
        pass 

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
        self.position = self.generate_food_position(snake_body)

    def generate_food_position(self, snake_body):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_body:  # Еда не должна быть на змеее
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


snake = Snake()
food = Food(snake.body)
score = 0
level = 1
speed = 5  
clock = pygame.time.Clock()
running = True

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
    
  
    if not snake.move():
        running = False  # Если столкнулась со стеной 
    
    # Проверка поедания еды
    if snake.body[0] == food.position:
        score += 1
        snake.grow()
        food = Food(snake.body)
        
        # Повышение уровня каждые 3 очка
        if score % 3 == 0:
            level += 1
            speed += 2 
    else:
        snake.shrink()  

    
    snake.draw()
    food.draw()
    
    # Отображение счета и уровня
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
