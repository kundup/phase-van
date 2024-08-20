import pygame

# pygame setup
pygame.init()

# game setups
set_display_x = 1200
set_display_y = 700
pygame.display.set_mode((set_display_x, set_display_y))

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()

pygame.quit()