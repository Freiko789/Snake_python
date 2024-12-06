import pygame
from snake import Snake
from apple import Apple

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Snake Game")
    return screen

def display_start_screen(screen, background, font):
    text = font.render("PRESS SPACE TO PLAY", True, (0, 0, 0))
    text_rect = text.get_rect(center=(300, 200))
    
    start = False
    while not start:
        screen.blit(background, (0, 0))
        screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start = True
        pygame.display.flip()
    if (game_loop(screen, background, font) == True):
        display_start_screen(screen, background, font)
    else:
        pygame.quit()

def game_loop(screen, background, font):
    snake = Snake(100, 100, screen)
    score = 0
    apple = Apple(screen)
    last_move_time = 0
    move_delay = 100

    running = True
    while running:
        score_text = font.render(f"SCORE : {score}", True, (0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(score_text, (10,10))
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    snake.changeDirection(event.key, current_time)
        if current_time - last_move_time >= move_delay:
            snake.moveSnake()
            if snake.checkEat(apple.x, apple.y):
                apple.regenerate(snake.snake_body)
                score += 1
            last_move_time = current_time


        snake.drawSnake()
        if (snake.checkBorderAndBodySnake() == True):
            running = False
            return True
        apple.drawApple()
        pygame.display.flip()

    return True

def main():
    screen = init_game()
    background = pygame.image.load("herbe.jpg")
    font = pygame.font.Font(None, 36)
    display_start_screen(screen, background, font)

if __name__ == "__main__":
    main()
