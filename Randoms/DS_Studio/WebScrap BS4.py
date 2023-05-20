import pygame
from pygame import mixer

pygame.init()

# Setting up the base Canvas for the app
WIDTH = 1280
HEIGHT = 720

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Dop Snaker Studio')
label_font = pygame.font.Font('Fonts/Orbitron-Medium.ttf', 30)

# FPS Counter
fps = 60
timer = pygame.time.Clock()


def draw_grid():
    left_box = pygame.draw.rect(screen, [0, 128, 128], [0, 0, 225, HEIGHT - 150], 5)
    bottom_box = pygame.draw.rect(screen, [0, 128, 128], [0, HEIGHT - 150, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    Hi_Hats_txt = label_font.render('Hi Hat', True, white)
    screen.blit(Hi_Hats_txt, (50, 25))
    Snare_txt = label_font.render('Snare', True, white)
    screen.blit(Snare_txt, (50, 120))
    Kick_txt = label_font.render('Kick', True, white)
    screen.blit(Kick_txt, (50, 215))
    Crash_txt = label_font.render('Crash', True, white)
    screen.blit(Crash_txt, (50, 310))
    Clap_txt = label_font.render('Clap', True, white)
    screen.blit(Clap_txt, (50, 405))
    Floor_Tom_txt = label_font.render('Floor Tom', True, white)
    screen.blit(Floor_Tom_txt, (30, 500))

    for i in range(6):
        pygame.draw.line(screen, [0, 128, 128], (0, (i * 100) + 100), (225, (i * 100) + 100), 5)


# FPS Counter Display
run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
