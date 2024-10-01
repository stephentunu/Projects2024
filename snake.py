import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up clock
clock = pygame.time.Clock()
SNAKE_SIZE = 10
SNAKE_SPEED = 15

# Define snake and food
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE,
            random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE]
food_spawn = True
direction = 'RIGHT'
change_to = direction

# Game Over function
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    GO_surface = font.render('Your Score is: ' + str(len(snake_body) - 3), True, RED)
    GO_rect = GO_surface.get_rect()
    GO_rect.midtop = (WIDTH / 2, HEIGHT / 4)
    win.fill(BLACK)
    win.blit(GO_surface, GO_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main Function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 'DOWN':
                    change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                if direction != 'UP':
                    change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                if direction != 'RIGHT':
                    change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                if direction != 'LEFT':
                    change_to = 'RIGHT'

    # If snake is moving in the opposite direction, ignore the key press
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= SNAKE_SIZE
    if direction == 'DOWN':
        snake_pos[1] += SNAKE_SIZE
    if direction == 'LEFT':
        snake_pos[0] -= SNAKE_SIZE
    if direction == 'RIGHT':
        snake_pos[0] += SNAKE_SIZE

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE,
                    random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE]
    food_spawn = True

    # Background
    win.fill(BLACK)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw food
    pygame.draw.rect(win, WHITE, pygame.Rect(food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-SNAKE_SIZE:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-SNAKE_SIZE:
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    pygame.display.update()
    clock.tick(SNAKE_SPEED)
