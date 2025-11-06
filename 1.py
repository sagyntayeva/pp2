import pygame
from datetime import datetime
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickey Clock")


leftarm = pygame.image.load('C:\\Users\\ranid\\OneDrive\\Desktop\\pp2\\second.png').convert_alpha()
rightarm = pygame.image.load('C:\\Users\\ranid\\OneDrive\\Desktop\\pp2\\minute.png').convert_alpha()
mainclock = pygame.transform.scale(pygame.image.load('C:\\Users\\ranid\\OneDrive\\Desktop\\pp2\\base_micky.jpg').convert_alpha(),(800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.now()
    minute = current_time.minute
    second = current_time.second + current_time.microsecond / 1000000

   
    minute_angle = minute * 6+45
    second_angle = second * 6  

  
    screen.blit(mainclock, (0, 0))

    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2))
    screen.blit(rotated_rightarm, rightarmrect)

    
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40, 600)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2))
    screen.blit(rotated_leftarm, leftarmrect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
