import pygame
import time
import random

pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set display dimensions
DIS_WIDTH = 800
DIS_HEIGHT = 600

# Set the size of the blocks
BLOCK_SIZE = 20

# Set the speed of the snake
SPEED = 20

# Initialize the screen
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control the game speed
clock = pygame.time.Clock()

# Font settings
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    DIS.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            DIS.fill(BLACK)
            message("You lost! Press Q to Quit or C to play again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Check for boundaries
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True

        # Update position
        x1 += x1_change
        y1 += y1_change
        DIS.fill(BLACK)

        # Draw the food
        pygame.draw.rect(DIS, BLUE, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])

        # Draw the snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        # Draw the snake
        for x in snake_List:
            pygame.draw.rect(DIS, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        # Check if snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            Length_of_snake += 1

        # Control the speed
        clock.tick(SPEED)

    pygame.quit()
    quit()

gameLoop()
