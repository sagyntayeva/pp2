import pygame

pygame.init() # инициаоизация

painting = []
timer = pygame.time.Clock()
fps = 60 # фпс
activeColor = (0, 0, 0)
activeShape = 0
w = 800 # ширина экрана
h = 600 # высота экрана

screen = pygame.display.set_mode([w, h]) # выводит экран
pygame.display.set_caption("Paint") 

def drawDisplay():
    pygame.draw.rect(screen, (229,255,204), [0, 0, w, 86]) #panel 
    pygame.draw.line(screen, 'gray', [0, 85], [w, 85]) 
    rect = [pygame.draw.rect(screen, (96, 96, 96), [10, 10, 70, 70]), 0] #grey square ,save in list
    pygame.draw.rect(screen, 'white', [20, 20, 50, 50])
    circ = [pygame.draw.rect(screen, (96, 96, 96), [100, 10, 70, 70]), 1]
    pygame.draw.circle(screen, 'white', [135, 45], 30)

    #Цвета
    blue = [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25]), (0, 0, 255)]
    red = [pygame.draw.rect(screen, (255, 0, 0), [w - 35, 35, 25, 25]), (255, 0, 0)]
    green = [pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25]), (0, 255, 0)]
    yellow = [pygame.draw.rect(screen, (255, 255, 0), [w - 60, 35, 25, 25]), (255, 255, 0)]
    black = [pygame.draw.rect(screen, (0, 0, 0), [w - 85, 10, 25, 25]), (0, 0, 0)]
    purple = [pygame.draw.rect(screen, (255, 0, 255), [w - 85, 35, 25, 25]), (255, 0, 255)]

    eraser = [pygame.draw.rect(screen, (253, 166, 215), [w - 610, 20, 50, 50]), (255, 255, 255)] #Eraser

    return [blue, red, green, yellow, black, purple, eraser], [rect, circ]
def drawPaint(paints):
    for paint in paints:
        if paint[2] == 1:
            pygame.draw.circle(screen, paint[0], paint[1], 15) #draw a circle with color r=15
        elif paint[2] == 0:
            pygame.draw.rect(screen, paint[0], [paint[1][0]-15, paint[1][1]-15, 30, 30])# -15 for center of cube
def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0:
            pygame.draw.rect(screen, activeColor, [mouse[0]-15, mouse[1]-15, 30, 30])
        if activeShape == 1:
            pygame.draw.circle(screen, activeColor, mouse, 15)
run = True
while run:
    timer.tick(fps) #фпс
    screen.fill('white') # заполняет экран
    colors, shape = drawDisplay() # рисует

    mouse = pygame.mouse.get_pos() # следит за мышкой
    draw()
    click = pygame.mouse.get_pressed()[0] # нажимание клавиши чек
    if click and mouse[1] > 100:
        painting.append((activeColor, mouse, activeShape)) # добавляет где мышка
    drawPaint(painting)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                painting = []
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    activeColor = i[1]
            for i in shape:
                if i[0].collidepoint(event.pos):
                    activeShape = i[1]
    pygame.display.flip() 
pygame.quit()