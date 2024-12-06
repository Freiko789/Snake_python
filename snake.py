import pygame

move_delay = 100

class Snake:
    def __init__(self, x, y, ecran):
        self.x = x
        self.y = y
        self.ecran = ecran
        self.width = 20
        self.height = 20
        self.snake_body = [(x, y)]
        self.move = 5
        self.direction = 'RIGHT'
        self.last_direction_change_time = 0

    def drawSnake(self):
        for segment in self.snake_body:
            pygame.draw.rect(self.ecran, (0, 0, 128), pygame.Rect(segment[0], segment[1], self.width, self.height))
    
    def moveSnake(self):
        save = self.snake_body[0]
        head_x, head_y = self.snake_body[0]

        if self.direction == 'DOWN':
            head_y += 20
        elif self.direction == 'UP':
            head_y -= 20
        elif self.direction == 'LEFT':
            head_x -= 20
        elif self.direction == 'RIGHT':
            head_x += 20

        self.snake_body[0] = (head_x, head_y)

        for i in range(1, len(self.snake_body)):
            tmp = self.snake_body[i]
            self.snake_body[i] = save
            save = tmp

    def changeDirection(self, keypressed, current_time):
        if current_time - self.last_direction_change_time >= move_delay:
            if keypressed == pygame.K_DOWN and self.direction != 'UP':
                self.direction = 'DOWN'
                self.last_direction_change_time = current_time
            elif keypressed == pygame.K_UP and self.direction != 'DOWN':
                self.direction = 'UP'
                self.last_direction_change_time = current_time
            elif keypressed == pygame.K_LEFT and self.direction != 'RIGHT':
                self.direction = 'LEFT'
                self.last_direction_change_time = current_time
            elif keypressed == pygame.K_RIGHT and self.direction != 'LEFT':
                self.direction = 'RIGHT'
                self.last_direction_change_time = current_time
    
    def checkBorderAndBodySnake(self):
        head_x, head_y = self.snake_body[0]
        if head_x + self.width > 600 or head_x < 0 or head_y + self.height > 400 or head_y < 0:
            return True
        for segment in self.snake_body[1:]:
            if head_x == segment[0] and head_y == segment[1]:
                return True
        return False
    
    def checkEat(self, appleX, appleY):
        head_x, head_y = self.snake_body[0]
        if head_x < appleX + self.width and head_x + self.width > appleX and head_y < appleY + self.height and head_y + self.height > appleY:
            tail_x, tail_y = self.snake_body[-1]
            
            if self.direction == 'DOWN':
                new_tail = (tail_x, tail_y - self.width)
            elif self.direction == 'UP':
                new_tail = (tail_x, tail_y + self.width)
            elif self.direction == 'RIGHT':
                new_tail = (tail_x - self.width, tail_y)
            elif self.direction == 'LEFT':
                new_tail = (tail_x + self.width, tail_y)

            self.snake_body.append(new_tail)
            return True
        return False