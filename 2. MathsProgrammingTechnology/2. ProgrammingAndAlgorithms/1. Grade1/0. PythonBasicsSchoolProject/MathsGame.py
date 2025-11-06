import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Running Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Load Mario image (replace 'mario.png' with your actual image file)
mario_img = pygame.image.load('mario.png')
mario_img = pygame.transform.scale(mario_img, (50, 50))
mario_x, mario_y = 50, 550
mario_width = 50
mario_height = 50
mario_velocity_y = 0
mario_velocity_x = 0
gravity = 0.8
jump_strength = 15

# Background
background_img = pygame.Surface((width, height))
background_img.fill(white)
background_x = 0
background_velocity = 0.8  # Slightly slower background (and obstacle) movement

# Obstacles
obstacles = []
def generate_obstacles():
    global obstacles
    obstacles = []
    for i in range(5):
        obstacle_x = random.randint(800 + i * 200, 800 + (i+1) * 200)
        obstacle_y = random.choice([450, 550])
        obstacles.append({"x": obstacle_x, "y": obstacle_y, "width": 50, "height": 50})

generate_obstacles()

# Math problems & Time Limit
math_problems = [
    {"question": "15 + 7 = ?", "answer": 22},
    {"question": "23 - 9 = ?", "answer": 14},
    {"question": "6 x 4 = ?", "answer": 24},
    {"question": "32 / 4 = ?", "answer": 8}
]
current_problem = random.choice(math_problems)
level = 1
time_limit = 10
answering_question = False
start_time = 0
input_text = ""
font = pygame.font.Font(None, 36)
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and mario_y == 550:
                mario_velocity_y = -jump_strength
            elif event.key == pygame.K_RETURN and answering_question:
                end_time = time.time()
                if end_time - start_time > time_limit:
                    print("Time's up! Game Over.")
                    running = False
                else:
                    answer = input_text.strip()
                    try:
                        answer = int(answer)
                        if answer == current_problem['answer']:
                            level += 1
                            answering_question = False
                            input_text = ""
                            score += 10
                        else:
                            print("Wrong answer! Game Over.")
                            running = False
                    except ValueError:
                        print("Invalid input! Game Over.")
                        running = False
            elif answering_question:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Mario movement
    mario_velocity_y += gravity
    mario_y += mario_velocity_y
    mario_x += mario_velocity_x

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_x -= 5
        background_x += background_velocity
    if keys[pygame.K_RIGHT]:
        mario_x += 5
        background_x -= background_velocity

    mario_x = max(0, mario_x)
    mario_x = min(width - mario_width, mario_x)

    if mario_y > 550:
        mario_y = 550
        mario_velocity_y = 0

    # Background movement (looping)
    background_x %= background_img.get_width()

    # Obstacle movement (now they are stationary, but regenerate when off-screen)
    for obstacle in obstacles:
        obstacle['x'] -= background_velocity
        if obstacle['x'] < -obstacle['width']:
            obstacle['x'] = width + random.randint(200, 400)
            obstacle['y'] = random.choice([450, 550])

    # Collision detection & Math Problem Display
    collided = False
    for obstacle in obstacles:
        if mario_x < obstacle['x'] + obstacle['width'] and \
           mario_x + mario_width > obstacle['x'] and \
           mario_y < obstacle['y'] + obstacle['height'] and \
           mario_y + mario_height > obstacle['y']:
            collided = True
            if not answering_question:
                answering_question = True
                start_time = time.time()
                current_problem = random.choice(math_problems)
            break

    # Prevent Mario from moving through obstacles
    if collided:
        if keys[pygame.K_LEFT]:
            mario_x += 5
        if keys[pygame.K_RIGHT]:
            mario_x -= 5

    # Add points for jumping over obstacles
    if not collided and mario_y < 550:
        score += 1

    # Draw
    screen.fill(white)
    screen.blit(background_img, (background_x, 0))
    screen.blit(background_img, (background_x + background_img.get_width(), 0))
    screen.blit(mario_img, (mario_x, mario_y))

    for obstacle in obstacles:
        pygame.draw.rect(screen, black, (obstacle['x'], obstacle['y'], obstacle['width'], obstacle['height']))

    level_text = font.render(f"Level: {level}", True, black)
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(level_text, (10, 10))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

    if answering_question:
        question_text = font.render(current_problem['question'], True, black)
        answer_text = font.render(input_text, True, black)
        time_left = max(0, int(time_limit - (time.time() - start_time)))
        time_text = font.render(f"Time: {time_left}", True, red)
        screen.blit(question_text, (width // 2 - 50, height // 2 - 50))
        screen.blit(answer_text, (width // 2 - 50, height // 2))
        screen.blit(time_text, (width // 2 - 50, height // 2 + 50))

    pygame.display.update()

pygame.quit()