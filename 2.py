import pygame
import os
import time

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
playing = True
running = True
last_press_time = 0
key_delay_time = 0.3 


def play():
    pygame.mixer.music.load(os.path.join(folder, tracks[current]))
    pygame.mixer.music.play()
    print(f"Playing: {tracks[current]}")

def stop():
    pygame.mixer.music.stop()
    print("Music stopped")

def next_track():
    global current, playing
    current = (current + 1) % len(tracks)
    play()
    playing = True

def prev_track():
    global current, playing
    current = (current - 1) % len(tracks)
    play()
    playing = True


def key_delay():
    global last_press_time
    if time.time() - last_press_time > key_delay_time:
        last_press_time = time.time()
        return True
    return False

play()

clock = pygame.time.Clock()

while running:
    screen.blit(img, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and key_delay():
        if playing:
            pygame.mixer.music.pause()
            playing = False
            print("Paused")
        else:
            pygame.mixer.music.unpause()
            playing = True
            print("Resumed")

    if keys[pygame.K_LEFT] and key_delay():
        prev_track()

    if keys[pygame.K_RIGHT] and key_delay():
        next_track()

    clock.tick(60)

pygame.quit()
