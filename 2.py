import pygame
import os

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Music Player")

img = pygame.image.load("/Users/ranid/OneDrive/Desktop/pp2/photo.jpg").convert_alpha()
img = pygame.transform.scale(img, (300, 200))

folder = "/Users/ranid/OneDrive/Desktop/pp2/music"
tracks = []
for f in os.listdir(folder): 
    if f.endswith(".mp3"):
        tracks.append(f)
if not tracks:
    print("No music found!")
    exit()

current = 0
paused = False  

def play():
    pygame.mixer.music.load(os.path.join(folder, tracks[current]))
    pygame.mixer.music.play()
    print(f"Playing: {tracks[current]}")

def stop():
    pygame.mixer.music.stop()
    print("Music stopped")

def next_track():
    global current, paused
    current = current + 1
    play()
    paused = False

def prev_track():
    global current, paused
    current = current - 1 
    play()
    paused = False

play()


while True:
    screen.blit(img, (0, 0))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("Resumed")
                else:
                    pygame.mixer.music.pause()
                    paused = True
                    print("Paused")
            
            elif event.key == pygame.K_s:
                stop()
                paused = False
            
            elif event.key == pygame.K_d:
                next_track()
            
            elif event.key == pygame.K_a:
                prev_track()

pygame.quit()

