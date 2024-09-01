from settings import *
from obstacles import *
from Surfer import *

def check_collision(player, obstacles):
    for obstacle in obstacles:
        if player.rect.colliderect(obstacle.rect):
            return True
    return False

# Main Game Loop
def main():
    running = True
    surfer = Surfer()
    waves = [Wave() for _ in range(10)]
    obstacles = [Obstacle() for _ in range(5)]
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            surfer.move(-1)
        if keys[pygame.K_RIGHT]:
            surfer.move(1)

        # Move and draw waves and obstacles
        screen.fill("skyblue")
        for wave in waves:
            wave.move()
            wave.draw()
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw()

        # Draw the surfer
        surfer.draw()

        # Check for collisions
        if check_collision(surfer, obstacles):
            print("Game Over!")
            running = False

        pygame.display.flip() 
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

