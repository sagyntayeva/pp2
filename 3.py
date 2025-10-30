import pygame
pygame.init()

width, height = 800, 600
radius = 25
speed = 7
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")
x, y = width // 2, height // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and x - radius - speed >= 0:
            x -= speed
        elif event.key == pygame.K_RIGHT and x + radius + speed <= width:
            x += speed
        elif event.key == pygame.K_UP and y - radius - speed >= 0:
            y -= speed
        elif event.key == pygame.K_DOWN and y + radius + speed <= height:
            y += speed


    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, (255, 255, 0), (x, y), radius)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
