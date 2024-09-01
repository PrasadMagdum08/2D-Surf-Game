import pygame,sys

pygame.init()

screen_width, screen_height = 1080, 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Surf 2D Game')

clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 50)

# size & color of surface
surface = pygame.Surface((screen_width, screen_height))
surface.fill('skyblue')

cloud_image = pygame.image.load('icons/cloud.png')


text_surface = test_font.render("Surf Game", False, 'black')


# Main Loop where frames are running
while True:

    # exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # setting coordinates(x, y) of surface on screen
    screen.blit(surface, (0, 0))

    screen.blit(text_surface, (450, 30))

    screen.blit(cloud_image, (500, 100))

    # refreshing frame to add new features
    pygame.display.update()

    # frame-rate -> 60
    clock.tick(60)