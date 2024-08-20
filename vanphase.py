import pygame

# pygame setup
pygame.init()
clock = pygame.time.Clock()
# game setups
set_display_x = 1200
set_display_y = 700
screen = pygame.display.set_mode((set_display_x, set_display_y))

# game loop
running = True
while running:
    screen.fill ("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
pygame.quit()