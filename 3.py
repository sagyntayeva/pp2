import pygame

pygame.init()


width, height = 800, 600
radius = 25
speed = 30
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")
x, y = width // 2, height // 2

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                x -= speed
            elif event.key == pygame.K_RIGHT and x + radius + speed <= width:
                x += speed
            elif event.key == pygame.K_UP and y - radius - speed >= 0:
                y -= speed
            elif event.key == pygame.K_DOWN and y + radius + speed <= height:
                y += speed
            if x<0:
                x=800
            if x>800:
                x=0
        


    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, (255,0 , 0), (x, y), radius)  
    pygame.display.flip()

    pygame.time.delay(60)

pygame.quit()
