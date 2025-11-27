import pygame
import random
from connect import connect

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


def get_username():
    font = pygame.font.Font(None, 40)
    input_text = ""
    active = True

    while active:
        screen.fill(BLACK)

        title = font.render("Enter your username:", True, WHITE)
        screen.blit(title, (150, 120))

        pygame.draw.rect(screen, WHITE, (150, 180, 300, 40), 2)

        text_surface = font.render(input_text, True, WHITE)
        screen.blit(text_surface, (160, 185))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.strip() != "":
                        return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < 15:
                        input_text += event.unicode

        pygame.display.flip()

username = get_username()
print(f"User: {username}")

def user(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user_data = cur.fetchone()

    if user_data is None:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, 0, 1))
        conn.commit()
    else:
        user_id = user_data[0]

    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
    score_data = cur.fetchone()

    cur.close()
    conn.close()
    
    return user_id, score_data[0], score_data[1]

user_id, score, level = user(username)
speed = 5 + (level - 1) * 2


class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or 
            new_head in self.body):
            return False
        
        self.body.insert(0, new_head)
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
        self.weight = random.choice([1, 2, 3])
        self.timer = random.randint(50, 75)

    def generate_food_pos(self, snake_body):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def update_timer(self):
        self.timer -= 1
        return self.timer > 0

snake = Snake()
food = Food(snake.body)
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
            elif event.key == pygame.K_p:
                # Пауза и сохранение прогресса
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
                            paused = False

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
        food = Food(snake.body)
    
    snake.draw()
    food.draw()
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
