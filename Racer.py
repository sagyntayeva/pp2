# импорт библиотек
import pygame, sys
from pygame.locals import *
import random, time
import os

# Инициализация 
pygame.init()

# Настройка FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Цвета
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Параметры экрана и игры
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Шрифты
font = pygame.font.SysFont("Times New Roman", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Game Over", True, BLACK)

# Базовый путь к  пикчам
BASE_PATH = r"C:\Users\ranid\OneDrive\Desktop\pp2"

# Загрузка фона
background = pygame.image.load(os.path.join(BASE_PATH, "AnimatedStreet.png"))

# Создание экрана
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Гонщик")

# Основные функции в классе

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(os.path.join(BASE_PATH, "Enemy.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  
 
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(os.path.join(BASE_PATH, "Player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(BASE_PATH, "Coin.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

# Обьекты-спрайты
P1 = Player()
E1 = Enemy()
C1 = Coin()

coins = pygame.sprite.Group()
coins.add(C1)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Изменение скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игра
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.25     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10)) # отоброжает скор

    counter = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(counter, (370, 10))

    # Отрисовывает движение
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # Набор поинтов
    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collided_coins:
        COINS += 1
        pygame.mixer.Sound(os.path.join(BASE_PATH, "catch.mp3")).play()
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Удар с машиной
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(os.path.join(BASE_PATH, "crash.wav")).play()
        time.sleep(0.5) #пауза для игры чтобы звук игрался
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() #все спрайты и сохранение удаляются
        time.sleep(2)
        pygame.quit()
        sys.exit()          

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
