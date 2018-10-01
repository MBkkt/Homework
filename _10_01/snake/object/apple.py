import random
import pygame


class Apple:
    def __init__(self, apple_color, width, height):
        self.apple_color = apple_color
        self.apple_size = 20
        self.apple_pos = [random.randrange(2, width // 20 - 1) * 20,
                          random.randrange(2, height // 20 - 1) * 20]

    def draw_apple(self, surface):
        pygame.draw.rect(surface, self.apple_color,
                         pygame.Rect(self.apple_pos[0], self.apple_pos[1], self.apple_size, self.apple_size))
