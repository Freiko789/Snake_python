import pygame
import random

class Apple:
    def __init__(self, ecran):
        self.x = random.randint(1, 29) * 20
        self.y = random.randint(1, 19) * 20
        self.ecran = ecran
        self.visible = False

    def regenerate(self, snake_body):
        while True:
            self.x = random.randint(1, 29) * 20
            self.y = random.randint(1, 19) * 20
            if not any(self.x == segment[0] and self.y == segment[1] for segment in snake_body):
                break

    def drawApple(self):
            self.visible = True
            pygame.draw.rect(self.ecran,(255,0,0), pygame.Rect(self.x, self.y, 20, 20))
