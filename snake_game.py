import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display dimensions
WIDTH, HEIGHT = 800, 600

# Set colors
BROWN = (139, 69, 19)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set snake and food sizes
snake_block = 10

# Set fonts
font_style = pygame.font.SysFont(None, 50)


# Function to display message
def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=pos)
    screen.blit(mesg, mesg_rect)


# Function to draw snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])


# Function to create a menu
def main_menu():
    menu = True
    while menu:
        screen.fill(BROWN)
        message("Welcome to Snake Game", WHITE, (WIDTH / 2, HEIGHT / 4))
        message("Press S to Start Game", WHITE, (WIDTH / 2, HEIGHT / 2))
        message("Press Q to Quit", WHITE, (WIDTH / 2, HEIGHT * 3 / 4))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gameLoop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


# Function to run the game
def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Set initial food position
    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    # Level variables
    level = 1
    snake_speed = 15

    # Score variable
    score = 0

    # Adding texture
    def draw_dirt():
        pass

    while not game_over:

        while game_close:
            screen.fill(BROWN)
            message("You Lost! Press C-Play Again or Q-Quit", WHITE, (WIDTH / 2, HEIGHT / 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    snake_speed -= 2
                elif event.key == pygame.K_p:
                    snake_speed += 2

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BROWN)
        draw_dirt()  # Draw texture
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            length_of_snake += 1

            # Increase level and speed every 5 foods eaten
            if length_of_snake % 5 == 0:
                level += 1
                snake_speed += 2

            # Increment score
            score += 10

            # Check if the player won
            if score >= 100:  # Assuming 10 foods eaten equal a win
                game_over = True
                win_screen(score)

        # Display score
        message("Score: " + str(score), WHITE, (WIDTH / 2, 20))

        pygame.display.update()

        clock.tick(snake_speed)


# Function for win screen
def win_screen(score):
    screen.fill(BROWN)
    message("Congratulations! You won!", GREEN, (WIDTH / 2, HEIGHT / 2))
    message("Score: " + str(score), WHITE, (WIDTH / 2, HEIGHT / 2 + 50))
    pygame.display.update()
    time.sleep(2)


# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the game clock
clock = pygame.time.Clock()

# Run the menu
main_menu()
